import json


def read_data():
    new_list = []
    with open('info3.json', encoding='utf-8') as f:
        data = json.load(f)  # 列表
        # print(data)
        for i in data:  # i 字典
            # print((i.get('username'), i.get('password'), i.get('expect')))
            new_list.append((i.get('username'), i.get('password'), i.get('expect')))

        # print(new_list)
    return new_list
