import socket
import asyncio
import run


# 网络请求future，接受host和端口返回一个future
def async_connect(host: str, port: int) -> asyncio.Future:
    # 获取当前运行的事件循环
    loop = asyncio.get_running_loop()  # 获取当前的事件循环
    # 创建一个socketc对象持有文件操作符
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)  # 设置为非阻塞模式
    try:
        # socket连接，这一步是触发连接，上面是非阻塞模式，所以触发完成后会异常退出
        # 那这里是怎么连接成功的，这里其实是触发了操作系统的socket连接，只要触发成功了操作系统就会去连接
        # 非阻塞模式就不用等连接结果，前面的sock对象里有这个socket的文件操作符可以监听这个文件操作符如果连接操作系统连接成功可以正常监听到
        sock.connect((host, port))
    except BlockingIOError:
        pass
    # 创建一个future
    fut = asyncio.Future()

    def on_writable() -> None:
        # 获取系统socket连接的错误吗，这里为啥要获取
        # 因为前面是非阻塞模式下连接的，这里可能连接失败也可能连接成功所以这里是通过文件操作符获取前面socket是否连接成功
        err = sock.getsockopt(socket.SOL_SOCKET, socket.SO_ERROR)
        # 移除 sock 写入监听
        # 为啥要移除，这里因为事件监听里io列表里其实放的不是回调函数，而是注册文件描述符及其监听事件
        # 监听事件满足监听条件才会讲回调函数加到ready队列让事件循环去处置。完成后这个监听是不会移除的
        # 下一轮循环继续判断这个文件描述符是否可写如果可写会继续调用回调
        # 直到调用remove_writer，就不再监听
        # 这里之所以注册可写事件就是用来判断socket连接的状态是否可写
        # 因为socket连接成功，连接失败时候就会变成可写状态，连接中是不会的
        # 执行了on_writable说明socket已经有连接结果了，我们这里的目的也是拿到socket的连接结果
        # 而不是真正的写入，所以这里要删除这个可写监听
        loop.remove_writer(sock)
        if err == 0:
            # 返回socket成功连接
            fut.set_result(sock)
        else:
            # 返回socket连接异常
            fut.set_exception(ConnectionError(f"Connect failed: {err}"))

    # 监听文件描述符的可写事件，当socket连接成功时，文件描述符会变为可写
    loop.add_writer(sock, on_writable)
    return fut


# 异步读取socket函数，接受sock对象，host，端口，地址返回future
def async_read(sock: socket.socket, host: str, port: int, path: str) -> asyncio.Future:
    # 获取当前真正运行的事件循环对象
    loop = asyncio.get_running_loop()
    # 创建一个future
    fut = asyncio.Future()
    # 多行字符串准备http请求报文
    req = f"""GET {path} HTTP/1.1
Host: {host}:{port}
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7,ru;q=0.6
Cache-Control: no-cache
Connection: close
Pragma: no-cache
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36

""".replace("\n", "\r\n")  # 体换换行符号为\r\n
    # 设置sock为非阻塞模式，这里其实无需再次设置，连接时候已经设置后面都是非阻塞模式，除非有地方改动
    sock.setblocking(False)
    # 发送tcp数据，这里只是写到操作系统缓冲区，所以send是同步的
    # 如果连接仍然打开或只（收到 FIN），缓冲区可以写入正常写入，注意这里写入数据大于缓冲区，只写能写入的部分其余部分会被丢弃，所以这里要监听写入，本案例写入内容很小所以简化
    # 如果连接仍然打开或只（收到 FIN），缓冲区满了写入会抛出异常BlockingIOError
    # 如果本地断开或收到（RST），写入会报其他异常
    sock.send(req.encode())
    data = b""

    # 总结这里的读取逻辑，读取时候读的是缓冲区的数据，
    # 如果连接仍然打开，如果缓冲区有数据正常读取
    # 如果连接仍然打开，缓冲区没有数据会抛出异常BlockingIOError
    # 如果连接正常关闭（收到 FIN），缓冲区为空，返回b""说明读取完了
    # 如果连接异常关闭，抛出ConnectionResetError异常
    def on_readable() -> None:
        nonlocal data
        try:
            # 每次读取4096个byte，这里是从缓冲区读取所以也是同步的
            chunk = sock.recv(4096)
            if chunk:
                data += chunk
            else:
                # 对端正常关闭发送方向，且缓冲区剩余数据已读完，sock会返回返回 b""所以到了这里说明已经读取完了
                loop.remove_reader(sock)
                # 返回读取到的数据
                fut.set_result(data.decode())
        # 缓冲区暂时没有数据，连接仍然打开。读取数据的情况
        # 这是因为多线程时候会有这个问题
        except BlockingIOError:
            pass

    # 注册可读监听到事件循环
    loop.add_reader(sock, on_readable)
    return fut


# 接受URL，端口，路径，返回一个future
def async_request(host: str, port: int, path: str) -> asyncio.Future:
    # 创建一个future
    fut = asyncio.Future()

    # 创建一个回调函数，，接受一个future，返回None
    def on_connected(f: asyncio.Future) -> None:
        try:
            # 获取成功返回
            sock = f.result()
            # 获取读取future
            read_fut = async_read(sock, host, port, path)
            # 添加一个回调函数到，读取future的回调列表，读取回调的结果赋值给网络future的状态
            read_fut.add_done_callback(lambda rf: fut.set_result(rf.result()))
        except Exception as e:
            # 异常将网络future状态设置为异常
            fut.set_exception(e)

    # 获取connect的future
    connect_fut = async_connect(host, port)
    # connect的future添加回调函数
    connect_fut.add_done_callback(on_connected)
    return fut


def main() -> None:
    # 回调函数，接受一个future
    def on_response(f: asyncio.Future) -> None:
        try:
            # 获取future的成功结果
            response = f.result()
            print(response)
        except Exception as e:
            print(f"Request failed: {e}")
        finally:
            # 获取当前运行的事件循环停止它
            asyncio.get_running_loop().stop()

    async_request("shae-learn.yuanjin.tech", 80, "/").add_done_callback(on_response)


run.run(main)
