str1 = "and itcast and itheima and Python"

# 在字符串中查找 and
num = str1.find('and')
print(num)  # 0

# 在字符串中查找 第二个 and 出现的下标, 从第一次出现的后一位开始找
num1 = str1.find('and', num+1)
print(num1)  # 11

# 在字符串中查找 第三个 and 出现的下标, 从第二次出现的后一位开始找
num2 = str1.find('and', num1+1)
print(num2)  # 23

# 在字符串中查找 第四个 and 出现的下标, 从第三次出现的后一位开始找
num3 = str1.find('and', num2+1)
print(num3)  # -1
