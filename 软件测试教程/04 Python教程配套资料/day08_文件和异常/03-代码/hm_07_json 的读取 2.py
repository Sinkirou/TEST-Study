# import json
#
# with open('info2.json', encoding='utf-8') as f:
#     info_list = json.load(f)
#     for info in info_list:
#         print(info.get('name'), info.get('age'), info.get('address').get('city'))
#
#

import random
import json

my_list = []
for i in range(10):
    num = random.randint(1, 20)
    my_list.append(num)

# 写文件
with open('data.json', 'w', encoding='utf-8') as f:
    f.write(str(my_list))

# 读文件
with open('data.json', encoding='utf-8') as f:
    data_list = json.load(f)   # 直接得到列表, 列表中的数据也是 int
    # 排序
    data_list.sort(reverse=True)
    print(data_list)
    print(data_list[:5])
