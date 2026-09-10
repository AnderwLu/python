'''
请实现一个单链表类 LinkedList，支持以下操作：

需要实现的方法：

方法	说明
__init__(data=None)	初始化空链表；data 可以是列表、元组或集合，其中的值会被初始化为链表的节点
traverse(callback)	遍历链表，对每个节点值调用 callback(index, value)
__str__()	返回链表的字符串表示，如 "1 -> 2 -> 3"
to_list()	将链表转换为 Python 列表并返回
append(value)	在链表尾部添加一个新节点
prepend(value)	在链表头部添加一个新节点
insert(index, value)	在指定索引位置插入新节点，索引从 0 开始
delete_by_value(value)	删除第一个值等于 value 的节点，返回是否删除成功
delete_by_index(index)	删除指定索引位置的节点，返回被删除的值，索引越界时返回 None
find(value)	查找值等于 value 的节点，返回其索引，不存在返回 -1
get(index)	获取指定索引位置的值，索引越界时返回 None
get_length()	返回链表长度
is_empty()	判断链表是否为空
提示： 你可能需要先定义一个 Node 类来表示链表节点。
'''
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,data=None):
        self.data = LinkedList.link(data)

    def traverse(self,callback):
        data = self.data
        index = 0
        while data is not None :
            callback(index,data)
            data = data.next
            index += 1
        
    def __str__(self):
        values = []
        self.traverse(lambda k,v : values.append(f"index {k} , value {v.value if v is not None else None} , next {v.next if v is not None else None}"))
        return " -> ".join(value for value in values)

    def to_list(self):
        str = []
        self.traverse(lambda k,v : str.append(v))
        return str
    def append(self,value):
        data = self.data
        while True :
            if None is data.next:
                data.next = value
                break
            data = data.next

    def prepend(self,value):
        value.next = self.data
        self.data = value
        
    def insert(self,index, value):
        def ins(i,v):
            if index == i:
                value.next = v.next
                v.next = value
        self.traverse(ins)

    def delete_by_value(self,value):
        data = self.data
        while data is not None:
            if data.value == value.value:
                data.next = data.next.next
                return True
            if data.next is not None and data.next.value == value.value:
                data.next = data.next.next
                return True
            data = data.next
        return False

    def find(self,value):
        index = -1
        def fin(i,v):
            if v.value == value.value:
                nonlocal index
                index = i
        self.traverse(fin)
        return index
    def get(self, index):
        value = None
        def fin(i,v):
            if i == index:
                nonlocal value
                value = v
        self.traverse(fin)
        return value
    def delete_by_index(self,index):
        node = None
        pnode = None
        if index == 0 :
            node = self.data
            self.data = self.data.next
            return node
        def sel(i,v) :
            if i == index -1:
                nonlocal pnode
                pnode = v
        self.traverse(sel)
        print (pnode.value)
        if pnode is None or pnode.next is None:
            return node
        node = pnode.next
        pnode.next = pnode.next.next
        return node

    def get_length(self):
        return len(self.to_list())

    def is_empty(self):
        return False if self.to_list() else True

    @staticmethod
    def link (data):
        if not data:
            return None
        data = list(data)
        h = Node(data[0])
        c = h
        for item in data[1:]:
            c.next = Node(item)
            c = c.next
        return h

link = LinkedList({10,20,30})
print(link.__str__())
link.traverse(lambda k,v : print(f"value {k} , next {v}"))
print(link.to_list())
link.append(Node(40))
print(link.__str__())
link.prepend(Node(50))
print(link.__str__())
link.insert(3,Node(60))
print(link.__str__())
print("删除指定节点")
# link.delete_by_value(Node(60))
node =  link.delete_by_index(0)
print(node)
print(link.__str__())
print("find指定节点")
print(link.find(Node(90)))

print("get index")
print(link.get(9))

print("get len")
print(link.get_length())

print("is_empty")
link1 = LinkedList({})
print(link1.is_empty())