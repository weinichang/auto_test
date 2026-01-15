import os
import time

import pytest

if __name__ == '__main__':
    pytest.main()
    time.sleep(1)
    # 构建、输入allure测试报告
    os.system("/opt/homebrew/bin/allure generate ./report/allure_result_temp -o ./report/allure_report --clean")
    # 自动打开测试报告，并且生成局域网地址
    # os.system("allure open ./report/allure_report")