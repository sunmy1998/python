def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('参数类型异常')
    if x < 0:
        return -x
    else:
        return x