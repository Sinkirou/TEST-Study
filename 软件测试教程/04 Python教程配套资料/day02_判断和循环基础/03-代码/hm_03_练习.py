# 1. 获取用户输入的用户名信息
name = input('请输入你的用户名:')
# 2. 如果用户名信息是 admin, 就在控制台输出出来
if name == 'admin':
    print('欢迎 admin')
# 3. 如果用户名信息不是 admin, 就在控制台输出"用户名错误!"
else:
    print('用户名错误!')
