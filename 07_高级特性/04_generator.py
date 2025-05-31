# 生成器
g = (x*x for x in range(1,10))
print(next(g))
for x in g:
    print(x)

# 斐波那契散列
def fib(count):
    n, a, b = 0, 0, 1
    while n < count:
        yield b
        a, b = b, a + b
        n = n + 1
    print('done')

for x in fib(6):
    print(x)

def odd():
    print('step1')
    yield 1
    print('step2')
    yield 3
    print('step3')
    yield 5

for x in odd():
    print(x)

