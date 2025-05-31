# 函数的参数
def power(x, n=2):
    s = 1
    while n > 0:
        s *= x
        n -= 1
    return s
print(power(2))
print(power(2,3))

def enroll(name, gender, age=6, city='北京'):
    print(name, gender, age, city)

enroll('张三', '男')
enroll('李四', '女', city='东百')

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end())
print(add_end())

# 可变参数
def my_max(*numbers):
    res = numbers[0]
    for n in numbers:
        if n > res:
            res = n
    return res

print(my_max(1,2,3,4))

# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Bob', 35, city='Beijing')

# 限制关键字参数的名字
def person2(name, age, *, city):
    print('name:', name, 'age:', age, 'city:', city)
person2('Michael', 30, city='Beijing')
