str1 = 'good good study'

# 1, 将 str1 中 所有的 g 改为 G
str2 = str1.replace('g', 'G')
print('str1:', str1)   # str1: good good study
print('str2:', str2)   # str2: Good Good study

# 2. 将 str1 中第一个 good 改为 GOOD
str3 = str1.replace('good', 'GOOD', 1)
print('str3:', str3)   # str3: GOOD good study

# 3. 将 str1 中第二个 good 改为 GOOD
# 3.1 先将全部的 good  --> GOOD
str4 = str1.replace('good', "GOOD")
# 3.2 再将第一个 GOOD --> good
str4 = str4.replace('GOOD', 'good', 1)
print('str4:', str4)  # str4: good GOOD study
