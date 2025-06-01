# 高阶函数
from functools import reduce


def f_add(a, b, f):
    return f(a) + f(b)


print(f_add(-1, 2, abs))


# map
def f(x):
    return x * x


print(list(map(f, [1, 2, 3, 4, 5])))

print(list(map(str, [1, 2, 3, 4, 5])))


# reduce
def add(a, b):
    return a + b


print(reduce(add, [1, 2, 3, 4, 5]))


# char2num
DIGITS = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

print(reduce(lambda x, y: x * 10 + y, map(char2num, '12345')))

# 按姓名格式修改（首字母大写、其余小写）
print(list(map(lambda name: name[0].upper() + name[1:].lower(), ['adam', 'LISA', 'barT'])))

# filter
print(list(filter(lambda x: x % 2 == 0, [1,2,3,4,5,6,7,8,9])))

# sorted
print(sorted([1,-2,3,-4]))

print(sorted([1,-2,3,-4], key=abs))

print(sorted([1,-2,3,-4], key=abs, reverse=True))



