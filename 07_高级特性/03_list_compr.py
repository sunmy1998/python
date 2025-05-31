
# 列表生成式
import os

print([x * x for x in range(1, 10)])

print([x * x for x in range(1, 10) if x % 2 == 0])

print([m + n for m in 'ABC' for n in 'XYZ'])

print([d for d in os.listdir('.')])

print([x if x % 2 == 0 else -x for x in range(1, 10)])