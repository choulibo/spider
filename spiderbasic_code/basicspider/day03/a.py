# coding=utf-8
import json
# json.dumps 实现python类型转化为json字符串
# indent实现换行和空格
# ensure_ascii=False实现让中文写入的时候保持为中文
json_str = json.dumps(my_dict, indent=2, ensure_ascii=False)

# json.loads 实现json字符串转化为python类型
my_dict = json.loads(json_str)

# json.dump 实现把python类型写入类文件对象
with open("temp.txt", "w") as f:
    json.dump(my_dict, f, ensure_ascii=False, indent=2)

# json.load 实现类文件对象中的json字符串转化为python类型
with open("temp.txt", "r") as f:
    my_dict = json.load(f)
