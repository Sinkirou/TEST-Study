my_list = [3, 2, 4, 1, 2, 3, 3, 2, 1, 2, 3, 1]
# print(list(set(my_list)))
#
# new_list = list(set(my_list))
# print(new_list)

new_list = []
# for i in my_list:
#     # 判断新列表中是否存在 i
#     if i in new_list:
#         # 存在
#         pass  # continue
#     else:
#         new_list.append(i)

for i in my_list:
    if i not in new_list:
        new_list.append(i)

print(new_list)
