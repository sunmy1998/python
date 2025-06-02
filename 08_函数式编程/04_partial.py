# 便函数
import functools

int2 = functools.partial(int, base=2)
print(int2('100'))

max2 = functools.partial(max, 100)
print(max2(1,2,3))