# 返回函数
def lazy_sum(*args):
    def inner_sum():
        ax = 0
        for x in args:
            ax += x
        return ax
    return inner_sum

print(lazy_sum(1,2,3,4,5))

print(lazy_sum(1,2,3,4,5)())