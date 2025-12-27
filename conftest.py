import os
import time
from datetime import datetime

import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

from commons.yaml_util import clean_yaml


# 设置fixture的作用域为session
# 基础fixture，浏览器初始化
@pytest.fixture(scope='session')
def browser(request):
    driver = webdriver.Safari()
    # 最大化窗口
    driver.maximize_window()
    yield driver
    driver.quit()


# 打开百度
"""扩展 fixture：依赖 browser"""


@pytest.fixture()
def driver(browser):
    browser.get('https://www.baidu.com')
    # 隐式等待
    browser.implicitly_wait(10)
    yield browser


# 登录测试
@pytest.fixture()
def driver_login(browser):
    browser.get('https://bahuyun.com/bda/login')
    # 隐式等待
    browser.implicitly_wait(10)
    yield browser
    # 登出
    browser.find_element(By.XPATH, '/html/body/ul/li[5]').click()


def pytest_runtest_makereport(item, call):
    """
    修复：通过report对象判断用例状态，替代无效的item.is_skipped()
    记录所有用例的执行结果（成功/失败/跳过/错误）到logs/pytest_result.log
    """
    # 生成完整的report对象（包含状态、跳过原因等）
    report = item.reportinfo()
    # 计算用例执行耗时
    duration = call.duration if hasattr(call, "duration") else 0.0

    # ========== 核心修复：正确判断用例状态 ==========
    # 1. 先判断是否为跳过状态（通过call.excinfo是否为Skipped异常）
    is_skipped = False
    skip_reason = ""
    if call.excinfo is not None and isinstance(call.excinfo.value, pytest.skip.Exception):
        is_skipped = True
        skip_reason = str(call.excinfo.value) or "无跳过原因"

    # 2. 定义用例最终状态
    if is_skipped:
        status = "SKIPPED"
    elif call.excinfo is not None:
        if call.when == "setup":
            status = "ERROR"  # 前置步骤失败
        else:
            status = "FAILED"  # 用例执行失败
    else:
        status = "PASSED"  # 用例执行成功

    # 提取异常信息（非跳过的异常）
    exc_info = ""
    if call.excinfo is not None and not is_skipped:
        exc_info = f"异常类型：{call.excinfo.type.__name__} | 异常信息：{str(call.excinfo.value)}"

    # 提取用例标记（可选扩展）
    # marks = [marker.name for marker in item.iter_markers()]
    # mark_info = " | ".join(marks) if marks else "无标记"
    # 提取运行环境（可选扩展）
    # env = item.config.getoption("--env")
    # 运行环境：{env}
    # 用例标记：{mark_info}
    # ========== 写入结果日志 ==========
    with open("logs/pytest_result.log", "a", encoding="utf-8") as f:
        f.write(f"""
======================================================================
执行时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
用例名称：{item.name}
用例路径：{item.nodeid}
执行阶段：{call.when}（setup/teardown/call）
执行状态：{status}
执行耗时：{duration:.4f} 秒
跳过原因：{skip_reason}
异常信息：{exc_info}
======================================================================
""")


# 通过fixture前置条件，清除temp.yaml数据
@pytest.fixture(scope='session', autouse=True)
def clean_datas():
    clean_yaml()
    yield
    # clean_yaml()

