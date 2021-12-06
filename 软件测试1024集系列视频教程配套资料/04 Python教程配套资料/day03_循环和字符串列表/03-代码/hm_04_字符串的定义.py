# 1. 使用单引号定义
my_str1 = 'hello'
print(my_str1, type(my_str1))
# 2, 使用双引号定义
my_str2 = "hello"
print(my_str2, type(my_str2))

# 3. 使用三引号定义
my_str3 = """hello"""
print(my_str3, type(my_str3))
my_str4 = '''hello'''
print(my_str4, type(my_str4))

# 4. 字符串本身包含引号 I'm 小明
# 4.1 字符串本身包含单引号, 则在定义的时候不能使用单引号
# 4.2 字符串本身包含双引号, 则在定义的时候不能使用双引号
my_str5 = "I'm 小明"
print(my_str5)

# 5. 字符串本身包含单引号,在定义的时候,我就是想使用单引号
# 5.1 使用 \ 转义字符,将字符串本身的引号进行转义 \' --> '  \" --> "
my_str6 = 'I\'m 小明'
print(my_str6)
# 5.2 字符串  I\'m 小明  \\ --> \
my_str7 = 'I\\\'m 小明'
print(my_str7)

# 5.3 字字符串前边加上 r""  原生字符串, 字符串中 的\不会作为转义字符, 文件操作会用一下
my_str8 = r'I\'m 小明'
print(my_str8)
my_str9 = r'I\\\'m 小明'
print(my_str9)
