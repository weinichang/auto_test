import allure
import pytest

data = [(1, 1, 2), ("hello", "world", "helloworld"), ([1, 2], [3, 4], [1, 2, 3, 4])]

# ddt数据驱动测试，数据参数化
@allure.epic("项目名称：测试项目")
@allure.story("接口名称：测试ddt参数化")
@pytest.mark.parametrize("a,b,c", data, ids=["int", "string", "list"])
def test_add(a, b, c):
    result = add(a, b)
    assert c == result

def add(a, b):
    return a + b
