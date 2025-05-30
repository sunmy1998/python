# 递归
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

# 尾递归
def fact_new(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
