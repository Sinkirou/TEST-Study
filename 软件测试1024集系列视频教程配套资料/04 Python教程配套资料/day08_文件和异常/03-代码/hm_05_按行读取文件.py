# with open('b.txt', encoding='utf-8') as f:
#     buf = f.readline()  # 111
#     print(buf)
#     print(f.readline())  # 222


# with open('b.txt', encoding='utf-8') as f:
#     for i in f:  # 按行读取, 读到文件末尾结束
#         print(i, end='')


# read() 和 readline() 读到文件末尾, 返回一个空字符串

with open('b.txt', encoding='utf-8') as f:
    while True:
        buf = f.readline()
        if len(buf) == 0:
            break
        else:
            print(buf, end='')


# 在容器中 , 容器为空,即容器中的数据的个数为 0 ,表示 False, 其余情况都是 True
with open('b.txt', encoding='utf-8') as f:
    while True:
        buf = f.readline()
        if buf:  # if len(buf) != 0
            print(buf)
        else:
            break

