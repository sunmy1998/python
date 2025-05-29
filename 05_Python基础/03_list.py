# 集合
classmates = ['A', 'B', 'C', 'D', 'E', 'F']

# 打印
print(classmates)

# 长度
print(len(classmates))

# 获取元素
print(classmates[0])
print(classmates[-1])

# 添加元素
classmates.append('G')
print(classmates)

# 插入元素
classmates.insert(1, 'AA')
print(classmates)

# 移除元素
classmates.pop(1)
print(classmates)

# 多维数组
arr = ['A', 'B', ['C', 'D']]
print(arr[2][1])