lis = [x ** 2 for x in range(4)]
print(lis)

lis = [x ** 2 for x in range(4) if x % 2 == 0]
print(lis)

lis = [x if x % 2 == 0 else x for x in range(10)]
print(lis)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for m in matrix for x in m]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 只保留偶数
result = [x for row in matrix for x in row if x % 2 == 0] 
print(result)  # [2, 4, 6, 8]


def flatten(nested_list):
    # 你的代码
    for i in nested_list:
        try:
            iter(i)
            yield from flatten(i)
        except Exception:
            yield i



nested = [1, [2, [3, 4], 5], 6, [7, 8]]
print(list(flatten(nested)))
# [1, 2, 3, 4, 5, 6, 7, 8]