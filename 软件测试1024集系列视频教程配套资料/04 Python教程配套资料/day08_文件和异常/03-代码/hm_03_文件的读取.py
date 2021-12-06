# 1, 打开文件
f = open('a.txt', 'r', encoding='utf-8')
# 2, 读文件
buf = f.read()
print(buf)  # 目前只是打印读取的内容,可以做其它的事
# 3. 关闭文件
f.close()

# r 方式打开文件 ,如果文件不存在,代码会报错
