'''
# 9x9
for i in range(1,10):
    for j in range(1, i+1):
        print(f"{j}x{i}={i*j}", end=" ")
    print("\n")


# 冒泡排序
def bubble_sort(arr):
    l = len(arr)
    for i in range(l):
        for j in range(l - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# 选择排序
def selection_sort(arr):
    l = len(arr)
    for i in range(l - 1):
        min_index = i
        for j in range(i + 1, l):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr



# 递归（1. 斐波那契数列（F (n) = F (n-1) + F (n-2)）, 2. 阶乘）
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)



# 栈的概念（有效匹配括号）

def isValid(self, s: str) -> bool:
    bracket_map = {')': '(', ']': '[', '}': '{'}
    stack = []

    for i in s:
        if i in bracket_map.values():  # 左括号，入栈
            stack.append(i)
        elif i in bracket_map.keys():  # 右括号，检查匹配
            # 栈空 或 栈顶不匹配，返回false
            if not stack or stack.pop() != bracket_map[i]:
                return False

    # 遍历结束后栈必须为空（所有左括号都匹配完成）
    return len(stack) == 0





DRR
Red

第 1 轮时，第一个来自 Dark 阵营的参议员可以使用第一项权利禁止第二个参议员的权利
第 2 轮时，第三个来自 Red 阵营的参议员可以使用他的第一项权利禁止第一个参议员的权利
这样在第 3 轮只剩下第三个参议员拥有投票的权利，于是他可以宣布胜利。


def read_yaml(path):
    with open(path, 'r', encoding="utf-8") as f:
        return yaml.safe_load(f)

def write_yaml(path):
    with open(path, 'w', encoding="utf-8") as f:
        data = {"name": "玉龙", "age": 30, "information": [{"color": 'red'}, {"hobby": "football"}]}
        yaml.safe_dump(data, f, allow_unicode=True)

def clean_yaml(path):
    with open(path, 'w', encoding="utf-8") as f:
        pass

clean_yaml("./practice.yaml")
# print(read_yaml("./practice.yaml"))
'''

value = {
    "file": "/Users/changyilong/PycharmProjects/pytest/material/sc1.jpg"
}

MIME_TYPE_MAP = {
                    "jpg": "image/jpeg",
                    "jpeg": "image/jpeg",
                    "png": "image/png",
                    "txt": "text/plain",
                    "pdf": "application/pdf",
                    "doc": "application/msword",
                    "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    "xls": "application/vnd.ms-excel",
                    "xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            }
for file_key, file_value in value.items():
     with open(file_value, "rb") as f:
          file_content = f.read()
     file_name = file_value.split("/")[-1]
     file_mine = MIME_TYPE_MAP.get(file_name.split(".")[-1].lower())
     # value[file_key] = (file_name, file_content,file_mine)
     print(file_name, file_content,file_mine)