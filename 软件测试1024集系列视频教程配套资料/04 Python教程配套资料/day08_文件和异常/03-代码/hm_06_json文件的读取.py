# 1, 导入 json
import json

# 2, 读打开文件
with open('info.json', encoding='utf-8') as f:
    # 3. 读取文件
    # buf = f.read()
    # print(type(buf), buf)
    result = json.load(f)
    print(type(result))  # <class 'dict'>
    # 姓名
    print(result.get('name'))
    # 年龄
    print(result.get('age'))
    # 城市
    print(result.get('address').get('city'))

