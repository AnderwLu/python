from pathlib import Path


# dir_path：目录路径，可以是绝对路径或相对路径（相对当前工作目录 CWD）
# show_hidden：布尔类型，表示是否显示隐藏文件/目录
def show_tree(dir_path: str, show_hidden: bool = False):
    """
    以树形结构打印目录内容。

    Args:
        dir_path: 要遍历的目录路径 (字符串)
        show_hidden: 是否显示隐藏文件/目录 (布尔值)
    """
    path = Path(dir_path).resolve()  # 转换为绝对路径

    if not path.exists():
        raise FileNotFoundError(f"路径不存在: {path}")

    def _is_hidden(entry: Path) -> bool:
        """判断文件或文件夹是否隐藏"""
        return entry.name.startswith(".")

    def _print_tree(current_path: Path, prefix: str = ""):
        """递归打印目录树"""
        entries = sorted(current_path.iterdir(), key=lambda e: e.name)

        if not show_hidden:
            entries = [e for e in entries if not _is_hidden(e)]

        for index, entry in enumerate(entries):
            is_last = index == len(entries) - 1
            connector = "└── " if is_last else "├── "
            print(f"{prefix}{connector}{entry.name}{'/' if entry.is_dir() else ''}")

            if entry.is_dir():
                extension = "    " if is_last else "│   "
                _print_tree(entry, prefix + extension)

    # 打印根目录名称
    print(path.name)
    _print_tree(path)
