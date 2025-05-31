# 切片
L = list(range(100))

# 取前三个
print(L[0:3])

# 从第一个开始，取两个
print(L[1:3])

# 取倒数两个
print(L[-2:])

# 前十个，每2个取1个
print(L[0:10:2])

# 元组切片
print((1,2,3)[:2])

# 字符串切片
print('abcd'[:2])

# trim
def trim(x):
    left = 0
    right = len(x) - 1;
    while x[left] == ' ':
        left += 1
    while x[right] == ' ':
        right -= 1
    print('left => %s, right => %s' % (left, right))
    return x[left:right+1]

print(trim(' abcd  '))