# 函数定义
def my_abs(x):
    if x < 0:
        return -x
    else:
        return x

print(my_abs(-100))

# 空函数
def nop():
    pass

# 返回多个值（元组）
import math

def move(x, y, step, angle=0.0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

print(move(100, 100, 60, math.pi / 6))