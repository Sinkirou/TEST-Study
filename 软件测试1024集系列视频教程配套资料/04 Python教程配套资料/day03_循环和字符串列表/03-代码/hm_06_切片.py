# 切片会得到一个字符串, 即可以获取字符串中的多个字符

str1 = 'abcdefg'

# 1. 获取 abc 字符
print(str1[0:3:1])   # abc
# 1.1 如果步长是 1 可以不写, 最后一个冒号也不写
print(str1[0:3])  # abc
# 1.2 如果开始位置为 0 ,可以不写, 但是冒号必须有
print(str1[:3])  # abc

# 2. 获取 efg 字符
print(str1[4:7])  # efg
print(str1[-3:7])  # efg
# 2.1 如果最后一个字符也要取, 可以不写, 但是冒号必须有
print(str1[4:])  # efg
# 2.2 如果开始和结束都不写, 获取全部内容, 但是冒号必须有
print(str1[:])  # abcdefg

# 3. 获取 aceg  # 0 2 4 6, 所以步长为 2
print(str1[0:7:2])  # aceg
print(str1[::2])  # aceg


# 4. 特殊应用, 步长为负数, 开始和结束不写,意思全变, 一般不用管,只有一种使用场景
# 反转(逆置) 字符串  字符串[::-1]
print(str1[::-1])  # gfedcba




