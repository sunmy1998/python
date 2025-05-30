# 循环

sum = 0
for x in [1,2,3,4,5]:
    sum += x
print('sum = %s' % sum)

sum = 0
for x in (range(1,6)):
    sum += x
print('sum = %s' % sum)

sum = 0
x = 1
while x <= 5:
    sum += x
    x += 1
print('sum = %s' % sum)

n = 1
while n <= 100:
    n +=1
    if n % 2 == 0:
        continue
    if n > 10:
        break
    print('n = %d' % n)
