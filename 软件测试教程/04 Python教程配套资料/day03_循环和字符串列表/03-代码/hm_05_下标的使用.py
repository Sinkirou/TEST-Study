str1 = 'abcdefg'

# 1. 打印字符串中最开始位置的字符
print(str1[0])  # a

# 2. 打印最后一个位置的数据
print(str1[-1])  # g

# 3. 打印倒数第二个位置的字符
print(str1[-2])  # f

# 打印下标为 2 的数据
print(str1[2])  # c

# 获取字符串中字符的个数(获取字符串的长度)
# len(字符串)   # length(长度)
num = len(str1)
print(num)
# 长度-1 的下标位置是最后一个字符
print(str1[num-1])  # g 最后一个字符,倒数第一个

print(str1[len(str1)-1])  # g 最后一个字符,倒数第一个
