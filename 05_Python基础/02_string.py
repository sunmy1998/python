# 格式化
print('hello, %s' % 'world')
print('Hi %s, you have $%d' % ('张三', 100))
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

# format()
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

# f-string
r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')

# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
s1 = 72
s2 = 85
r = (s2 - s1) / s1
print('%.1f' % r)
