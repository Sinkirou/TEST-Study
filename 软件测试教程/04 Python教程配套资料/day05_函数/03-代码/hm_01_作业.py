# my_list = []
#
# for i in range(3):
#     my_dict = {}  # 每循环一次创建一个字典
#     name = input('请输入姓名:')
#     age = input('请输入年龄:')
#     my_dict['name'] = name
#     my_dict['age'] = age
#     my_list.append(my_dict)
#
# # 遍历列表, 列表中存的都是字典, 所以 item 是字典
# for item in my_list:   # item  是字典
#     print(item['name'], item['age'])  # 根据字典的 key 获取 value

#
# my_list = [{'id': 1,'money': 10}, {'id': 2, 'money': 20},
#            {'id': 3, 'money': 30}, {'id': 4, 'money': 40}]
#
# def func():
#     for i in my_list:  # i 变量, 字典类型
#         # 1. 如果字典中 ID 的值为奇数,则对 money 的值加 20
#         if i.get('id') % 2 == 1:
#             i['money'] = i.get('money') + 20
#         #     2. 如果字典中 ID 的值为偶数, 则对 money 的值加 10
#         else:
#             i['money'] = i.get('money') + 10
#
#     #     3. 打印输出列表,查看最终的结果
#     print(my_list)
#
# func()


my_dict = {'登录': [{'desc': '正确的用户名密码', 'username': 'admin', 'password': '123456', 'expect': '登录成功'}, {'desc': '错误的用户名', 'username': 'root', 'password': '123456', 'expect': '登录失败'}, {'desc': '错误的密码', 'username': 'admin', 'password': '123123', 'expect': '登录失败'}, {'desc': '错误的用户名和密码', 'username': 'aaaa', 'password': '123123', 'expect': '登录失败'}],
           '注册': [{'desc': '注册1', 'username': 'abcd', 'password': '123456'}, {'desc': '注册1', 'username': 'xyz', 'password': '123456'}]}

# 1. 自定义以程序, 实现如下要求
# 2. 能够获取测试人员输入的信息(登录/测试)
opt = input('请输入要获取的数据(登录/注册) :')
info_list = []
if opt == '登录':
    print('获取登录数据')
    for d in my_dict.get('登录'):  # d 字典类型
        # 需要将数据组成元组类型(定义元组)
        my_tuple = (d.get('username'), d.get('password'), d.get('expect'))
        # 需要将元组添加到列表中  append()
        info_list.append(my_tuple)
elif opt == '注册':
    print('获取注册数据')
    for d in my_dict.get('注册'):
        my_tuple = (d.get('username'), d.get('password'))
        info_list.append(my_tuple)
else:
    print('输入错误')

print(info_list)

