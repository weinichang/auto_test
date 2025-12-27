import time
import json

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import service
# 导入鼠标事件包
from selenium.webdriver.common.action_chains import ActionChains
# 导入键盘事件包
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


@allure.epic("项目名称：webui自动化测试练习")
class Test_WebUI:

    # 使用fixture 作为前置和后置条件
    @allure.story("接口名称：百度标题")
    @allure.title("用例标题：测试百度首页title")
    def test_baidu_title(self, driver):
        # 检查title
        # 使用fixture 的前置返回值
        web_title = driver.title
        assert web_title == "百度一下，你就知道"

    @allure.story("接口名称：百度搜索")
    @allure.title("测试百度搜索")
    def test_baidu_search(self, driver):
        # 输入框输入"China"
        baidu_str = driver.find_element(By.ID, "chat-textarea")
        baidu_str.send_keys("China", Keys.ENTER)
        # 查询关键文案
        res = driver.find_element(By.CLASS_NAME, "content-text_5T5yg").text.strip()
        assert res == "用文心助手回答：China"

    @allure.story("接口名称：百度搜索页标题")
    @allure.title("测试百度搜索页title")
    def test_baidu_search_title(self, driver):
        driver.find_element(By.ID, "chat-textarea").send_keys("China", Keys.ENTER)
        time.sleep(2)
        title = driver.title
        assert title == "China_百度搜索"

    # 测试iframe，使用标签添加fixture（这里也是引用browser，和方法中直接引用browser一样）
    @pytest.mark.usefixtures("browser")
    # 通过标签添加fixture，如果需要获取返回值，需要再用例参数中加入request
    @allure.story("接口名称：iframe")
    @allure.title("测试网页中有iframe时的跳转")
    def test_iframe_switch(self, request):
        # 获取fixture的返回值
        browser = request.getfixturevalue("browser")
        # 打开有iframe的测试网站
        browser.get("https://sahitest.com/demo/iframesTest.htm")
        # 隐式等待
        browser.implicitly_wait(10)
        # 定位iframe模块
        iframe_module = browser.find_element(By.XPATH, '/html/body/iframe')
        # 进入iframe模块中
        browser.switch_to.frame(iframe_module)
        # 定位元素并点击
        browser.find_element(By.XPATH, '/html/body/table/tbody/tr/td[1]/a[1]').click()
        time.sleep(1)
        # 跳出iframe模块
        browser.switch_to.default_content()
        # 重新定位元素，确认是否跳出成功
        browser.find_element(By.XPATH, '/html/body/input[2]').click()

    @allure.story("接口名称：测试网站登录")
    @allure.title("测试登录")
    def test_login(self, driver_login):
        time.sleep(1)
        driver_login.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div[1]/div[2]').click()
        time.sleep(2)
        driver_login.find_element(By.XPATH,
                                  '//*[@id="app"]/div/div[2]/div/div[1]/div[3]/form/div[1]/div/div/input').send_keys(
            "13811491621")
        time.sleep(2)
        driver_login.find_element(By.XPATH,
                                  '//*[@id="app"]/div/div[2]/div/div[1]/div[3]/form/div[2]/div/div/input').send_keys(
            "chang1long")
        time.sleep(2)
        driver_login.find_element(By.XPATH,
                                  '//*[@id="app"]/div/div[2]/div/div[1]/div[3]/form/div[3]/div/div[1]/button').click()
        time.sleep(2)
        driver_login.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[1]/div[9]/div/div').click()
        time.sleep(2)
        login_name = driver_login.find_element(By.XPATH, '/html/body/ul/div[1]').text
        login_title = driver_login.title
        assert login_title == "我的工作区 - 八狐表单"
        assert login_name == "维尼常"

    # 网页后退
    # driver.back()
    # time.sleep(1)
    # 网页前进
    # driver.forward()
    # 获取tilte
    # print(driver.title)
    # print(driver.find_element(By.XPATH, '/html/head/title').is_displayed())
    # 获取标题
    # print(driver.find_element(By.XPATH, '/html/body/h2').text)

    # 定位按钮元素
    # driver.find_element(By.XPATH, '/html/body/form/input[1]').click()
    # time.sleep(2)
    # 获取弹窗信息
    # print(driver.switch_to.alert.text)
    # 输入信息
    # driver.switch_to.alert.send_keys("heheheh")
    # time.sleep(1)
    # 切换到弹窗并点击确认
    # driver.switch_to.alert.accept()
    # 切换到弹窗并点击取消
    # driver.switch_to.alert.dismiss()

    # for i in range(2):
    #
    #     driver.find_element(By.XPATH, value='//*[@id="my-node"]/div[3]/div/div[2]/div/div/div[1]/span').click()
    #
    #     driver.find_element(By.XPATH, value='//*[@id="my-node"]/div[4]/div/div[2]/div/div/div[1]').click()
    #     driver.find_element(By.XPATH, value='//*[@id="my-node"]/div[4]/div/div[2]/div/div/div[2]').click()
    #     driver.find_element(By.XPATH, value='//*[@id="my-node"]/div[4]/div/div[2]/div/div/div[3]').click()
    #
    #     driver.find_element(By.XPATH, value='//*[@id="my-node"]/div[5]/div/div[2]/div/div/div/select/option[2]').click()
    #
    #     driver.find_element(By.XPATH, value='//*[@id="input-1klwTGCKpCKKy3zpX8yzG"]').send_keys('0020250202')
    #
    #     driver.find_element(By.XPATH, '//*[@id="my-node"]/div[7]/div/div[2]/div/div[1]/div[2]/div[5]/i').click()
    #     driver.find_element(By.XPATH, '//*[@id="my-node"]/div[7]/div/div[2]/div/div[2]/div[2]/div[5]/i').click()
    #
    #     driver.find_element(By.XPATH, value='//*[@id="my-node"]/div[8]/div/div[2]/div/div/div/div/div/input').send_keys('/Users/changyilong/Downloads/1.jpg')
    #     time.sleep(1)
    #     driver.find_element(By.XPATH, '//*[@id="submit-button"]').click()
    #     time.sleep(1)
    #     driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/div[2]/div[3]/button').click()
    #     # 浏览器所有的标签页列表
    #     new_driver = driver.window_handles
    #     # 确认当前标签页
    #     print(driver.current_window_handle)
    #     driver.close()
    #     # 切换到新开的列表
    #     driver.switch_to.window(new_driver[1])
    #     # 确认更新后的标签页
    #     print(driver.current_window_handle)

    # 定位搜索框，发送"China"
    # driver.find_element(By.XPATH, value='//*[@id="chat-textarea"]').send_keys("China")
    # driver.find_element(By.ID, value="chat-textarea").send_keys("China")
    # driver.find_element(By.CLASS_NAME, 'chat-input-textarea.chat-input-scroll-style').send_keys("China")
    # driver.find_element(By.CSS_SELECTOR, value='#chat-textarea').send_keys('China')
    # driver.find_elements(By.TAG_NAME, value='textarea')[2].send_keys('Japan')
    # 定位链接,并点击
    # driver.find_element(By.LINK_TEXT, value='地图').click()
    # driver.find_element(By.PARTIAL_LINK_TEXT, value='图').click()
    # 清除输入内容
    # driver.find_element(By.ID, value="chat-textarea").clear()
    # 点击搜索
    # driver.find_element(By.ID, value='chat-submit-button').click()
    # 最大化窗口
    # driver.maximize_window()
    # 最小化窗口
    # driver.minimize_window()
    # 打开窗口的位置
    # driver.set_window_position(0, 0)
    # 设置窗口大小
    # driver.set_window_size(320, 740)
    # 刷新网页
    # driver.refresh()
    # 截屏（浏览器区域）
    # driver.get_screenshot_as_file("1.png")
    # 关闭当前标签
    # driver.close()
    # 关闭浏览器（所有标签页）并释放驱动
    # driver.quit()

    # 类的方案
    # class TestOpenbaidu():
    #     def setup_method(self, method):
    #         self.driver = webdriver.Firefox()
    #         self.vars = {}
    #
    #     def teardown_method(self, method):
    #         self.driver.quit()
    #
    #     def test_openbaidu(self):
    #         # Test name: open_baidu
    #         # Step # | name | target | value
    #         # 1 | open | / |
    #         self.driver.get("https://www.baidu.com/")
    #         # 2 | setWindowSize | 1512x850 |
    #         self.driver.set_window_size(1512, 850)
    #         # 3 | click | id=chat-textarea |
    #         self.driver.find_element(By.ID, "chat-textarea").click()
    #         # 4 | type | id=chat-textarea | china
    #         self.driver.find_element(By.ID, "chat-textarea").send_keys("china")
    #         # 5 | click | id=head_wrapper |
    #         self.driver.find_element(By.ID, "head_wrapper").click()
    #         # 6 | click | id=chat-submit-button |
    #         self.driver.find_element(By.ID, "chat-submit-button").click()
    #         # 7 | storeWindowHandle | root |
    #         self.vars["root"] = self.driver.current_window_handle
    #         # 8 | close |  |
    #         self.driver.close()

    # 前置条件设置成函数形式，后优化到conftest中
    # def setting_open_browser():
    #     # 创建"设置浏览器"对象
    #     q1 = Options()
    #     # 禁用沙盒模式（增加兼容性，有可能浏览器闪退）
    #     q1.add_argument('--no-sandbox')
    #     # 保持在结束后浏览器打开状态
    #     q1.add_experimental_option('detach', True)
    #     q1.add_argument('--ignore-certificate-errors')
    #     # 打开"Chrome"浏览器
    #     driver = webdriver.Chrome(options=q1)
    #     # 设置隐形等待，即在设定时间内返回则开始执行下一步操作，全局有效
    #     driver.implicitly_wait(10)
    #     driver.maximize_window()
    #     return driver
