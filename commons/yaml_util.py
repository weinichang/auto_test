'''
实现对yaml文件的读、写、清除操作
应用在对接口数据的提取和使用，实现接口关联，提取的数据会存放在temp.yaml文件中
'''
import yaml


# 临时文件读
def read_yaml(key):
    with open("/Users/changyilong/PycharmProjects/pytest/temp.yaml", 'r', encoding="utf-8") as f:
        result = yaml.safe_load(f)
        return result[key]


# 临时文件写
def write_yaml(data):
    with open("/Users/changyilong/PycharmProjects/pytest/temp.yaml", 'a', encoding="utf-8") as f:
        yaml.safe_dump(data, f, allow_unicode=True)


# 临时文件清除
def clean_yaml():
    with open("/Users/changyilong/PycharmProjects/pytest/temp.yaml", 'w', encoding="utf-8") as f:
        pass


# 用例文件读
def read_yaml_cases(yaml_path):
    with open(yaml_path, 'r', encoding="utf-8") as f:
        result = yaml.safe_load(f)
        return result["cases"]
