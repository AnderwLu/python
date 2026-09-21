# 编写一个函数 merge_markdown(files: list[str], output: str) -> None，接收两个参数：


# files：Markdown 文件路径列表
# output：合并后保存的目标文件路径
# 函数的作用是将多个 Markdown 文件合并为一个文件保存到目标路径。合并规则如下："""
def merge_markdown(files: list[str], output: str) -> None:
    with open(output, "w", encoding="utf-8") as destination:
        for index, file in enumerate(files):
            with open(file, "r", encoding="utf-8") as source:
                lines = []
                in_code_block = False
                for line in source:
                    line_without_newline = line.rstrip("\n")
                    stripped = line_without_newline.lstrip()
                    if stripped.startswith(("```", "~~~")):
                        in_code_block = not in_code_block
                        lines.append(line)
                        continue
                    if not in_code_block:
                        level = len(stripped) - len(stripped.lstrip("#"))
                        if 1 <= level <= 6 and stripped[level : level + 1] in (" ", ""):
                            title = stripped[level:].strip()
                            indent = line_without_newline[
                                : len(line_without_newline) - len(stripped)
                            ]
                            if level == 6:
                                line_without_newline = f"{indent}**{title}**"
                            else:
                                line_without_newline = (
                                    f"{indent}{'#' * (level + 1)} {title}"
                                )
                            line = line_without_newline + (
                                "\n" if line.endswith("\n") else ""
                            )
                    lines.append(line)
                content = "".join(lines).rstrip()
            if index:
                destination.write("\n\n")
            destination.write(content)
        destination.write("\n")
