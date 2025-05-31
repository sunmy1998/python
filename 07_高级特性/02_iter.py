# 迭代
from collections.abc import Iterable

# dict
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
for k in d:
    print(k, d[k])

print('----------%s----------' % '分隔符')

for v in d.values():
    print(v)

print('----------%s----------' % '分隔符')

for k,v in d.items():
    print(k, v)

print('----------%s----------' % '分隔符')

# 判断是否可以迭代
print(isinstance(d, Iterable))
print(isinstance('abc', Iterable))

print('----------%s----------' % '分隔符')

# 获取索引迭代
for i, name in enumerate(['张三','李四','王五']):
    print(i, name)

# 查找一个list中的最大值与最小值
def find_min_and_max(L):
    if len(L) == 0:
        return None, None
    min_num = L[0]
    max_num = L[0]
    for x in L:
        if x < min_num:
            min_num = x
        if x > max_num:
            max_num = x
    return min_num, max_num

# 测试
if find_min_and_max([]) != (None, None):
    print('测试失败!')
elif find_min_and_max([7]) != (7, 7):
    print('测试失败!')
elif find_min_and_max([7, 1]) != (1, 7):
    print('测试失败!')
elif find_min_and_max([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
