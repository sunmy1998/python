# 条件判断
age = 20
if age < 18:
    print('未成年')
elif age >= 18:
    print('已成年')
else:
    print('年龄有误')

birth = input('请输入生日')
birth = int(birth)
if birth < 2000:
    print('00前')
else:
    print('00后')