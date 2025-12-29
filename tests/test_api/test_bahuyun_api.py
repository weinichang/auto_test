import allure
import pytest

from commons.requests_util import RequestsUtil
from commons.yaml_util import write_yaml, read_yaml, read_yaml_cases


# ---------------------- 接口脚本 ----------------------
@allure.epic("项目名称：接口测试练习项目")
@allure.feature("模块名称：用户中心模块")
class Test_Bahuyun:

    @allure.story("接口名称：登录接口")
    @pytest.mark.parametrize("case", read_yaml_cases("./case/test_login.yaml"),
                             ids=[case["title"] for case in read_yaml_cases("./case/test_login.yaml")])
    def test_login(self, case):
        '''
        登录接口；
        3条用例；
        登录成功的用例中提取“body”令牌
        接口关联方案：通过yaml存储临时数据形式被其他接口调用，实现接口关联（12.26）；
        此次接口关联方案不再使用全局变量
        '''
        headers = case["request"]["headers"]
        # 使用封装的RequestsUtil().all_requests，自动关联cookie，实现持久化
        response = RequestsUtil().all_requests(method=case["request"]["method"], url=case["request"]["url"],
                                               headers=headers,
                                               json=case["request"]["json"])
        if case["case_id"] == "login_001":
            # 取值后以字典类型写入，方便yaml文件写入和读取
            data = {"auth": response.json().get("body")}
            write_yaml(data)
        assert response.json()["status"] == case["expected"]["response"]["status"]
        assert response.json()["message"] == case["expected"]["response"]["message"]

    @allure.story("接口名称：我的")
    @pytest.mark.parametrize("case", read_yaml_cases("./case/test_me.yaml"),
                             ids=[case["title"] for case in read_yaml_cases("./case/test_me.yaml")])
    def test_me(self, case):
        '''
        我的接口，在登录成功后的页面；
        1条用例；
        加载yaml存储的临时数据，加入到header中；
        放弃全局变量
        '''
        headers = case["request"]["headers"]
        headers["authorization"] = f"Bearer {read_yaml("auth")}"
        response = RequestsUtil().all_requests(method=case["request"]["method"], url=case["request"]["url"],
                                               headers=headers)

        assert response.json()["status"] == case["expected"]["response"]["status"]
        assert response.json()["body"]["nickname"] == case["expected"]["response"]["body"]["nickname"]
        assert response.json()["body"]["mobile"] == case["expected"]["response"]["body"]["mobile"]
        assert response.json()["body"]["isWxBound"] == case["expected"]["response"]["body"]["isWxBound"]
        assert response.json()["body"]["id"] == case["expected"]["response"]["body"]["id"]

    @allure.story("接口名称：创建联系人接口")
    @pytest.mark.skipif(1 == 2, reason="测试有条件跳过用例标签")
    @pytest.mark.parametrize("case", read_yaml_cases("./case/test_create_contact.yaml"),
                             ids=[case["title"] for case in read_yaml_cases("./case/test_create_contact.yaml")])
    def test_create_contact(self, case):
        '''
        创建联系人接口；
        2条用例；
        加载yaml中的auth数据，加入到header中；
        创建成功的用例中提取“body”联系人id；
        接口关联方案：通过yaml存储临时数据形式被其他接口调用，实现接口关联（12.26）；
        此次接口关联方案不再使用全局变量
        '''
        headers = case["request"]["headers"]
        headers["authorization"] = f"Bearer {read_yaml("auth")}"
        response = RequestsUtil().all_requests(method=case["request"]["method"], url=case["request"]["url"],
                                               headers=headers, json=case["request"]["json"])
        if case["case_id"] == "contact_001":
            # 字典类型保存数据
            data = {"contact_id": response.json().get("body")}
            write_yaml(data)

        assert response.status_code == case["expected"]["status_code"]
        assert response.json()["status"] == case["expected"]["response"]["status"]
        assert response.json()["message"] == case["expected"]["response"]["message"]
        if case["case_id"] == "contact_002":
            assert response.json()["body"][0]["message"] == case["expected"]["response"]["body"][0]["message"]

    @allure.story("接口名称：联系人列表接口")
    @pytest.mark.parametrize("case", read_yaml_cases("./case/test_contact_list.yaml"),
                             ids=[case["title"] for case in read_yaml_cases("./case/test_contact_list.yaml")])
    def test_contact_list(self, case):
        '''
        联系人列表，展示创建的我的联系人；
        1条用例；
        '''
        headers = case["request"]["headers"]
        headers["authorization"] = f"Bearer {read_yaml("auth")}"
        response = RequestsUtil().all_requests(method=case["request"]["method"], url=case["request"]["url"],
                                               headers=headers, params=case["request"]["params"])

        assert response.status_code == case["expected"]["status_code"]
        assert response.json()["status"] == case["expected"]["response"]["status"]
        assert response.json()["message"] == case["expected"]["response"]["message"]
        assert response.json()["body"]["items"][0]["id"] == read_yaml("contact_id")

    @allure.story("接口名称：删除联系人接口")
    @pytest.mark.parametrize("case", read_yaml_cases("./case/test_del_contact.yaml"),
                             ids=[case["title"] for case in read_yaml_cases("./case/test_del_contact.yaml")])
    def test_del_contact(self, case):
        '''
        删除联系人接口；
        2条用例；
        '''
        headers = case["request"]["headers"]
        headers["authorization"] = f"Bearer {read_yaml("auth")}"
        if case["case_id"] in ("contact_del_001", "contact_del_003"):
            url = case["request"]["url"] + str(read_yaml("contact_id"))
        else:
            url = case["request"]["url"]
        response = RequestsUtil().all_requests(method=case["request"]["method"], url=url, headers=headers)

        assert response.status_code == case["expected"]["status_code"]
        assert response.json()["status"] == case["expected"]["response"]["status"]
        assert response.json()["message"] == case["expected"]["response"]["message"]
        if case["case_id"] in ("contact_del_002", "contact_del_003", "contact_del_004"):
            assert response.json()["name"] == case["expected"]["response"]["name"]

    @allure.story("接口名称：注册接口")
    @pytest.mark.parametrize("case", read_yaml_cases("./case/test_register.yaml"),
                             ids=[case["title"] for case in read_yaml_cases("./case/test_register.yaml")])
    def test_register(self, case):
        '''
        注册接口；
        3条用例；
        登录成功的用例中提取“body”令牌
        接口关联方案：通过yaml存储临时数据形式被其他接口调用，实现接口关联（12.26）；
        此次接口关联方案不再使用全局变量
        '''
        headers = case["request"]["headers"]
        response = RequestsUtil().all_requests(method=case["request"]["method"], url=case["request"]["url"],
                                               headers=headers, params=case["request"]["params"],
                                               json=case["request"]["json"])
        assert response.json()["status"] == case["expected"]["response"]["status"]
        assert response.json()["message"] == case["expected"]["response"]["message"]
        assert response.json()["body"][0]["message"] == case["expected"]["response"]["body"][0]["message"]

    @allure.story("接口名称：我的素材")
    @pytest.mark.parametrize("case", read_yaml_cases("./case/test_my_file.yaml"),
                             ids=[case["title"] for case in read_yaml_cases("./case/test_my_file.yaml")])
    def test_my_file(self, case):
        '''
        我的素材接口；
        1条用例；
        登录成功的用例中提取“body”令牌
        '''
        headers = case["request"]["headers"]
        headers["authorization"] = f"Bearer {read_yaml("auth")}"
        response = RequestsUtil().all_requests(method=case["request"]["method"], url=case["request"]["url"],
                                               headers=headers, params=case["request"]["params"])
        assert response.json()["status"] == case["expected"]["response"]["status"]
        assert response.json()["message"] == case["expected"]["response"]["message"]

    @allure.story("接口名称：上传素材接口")
    @pytest.mark.parametrize("case", read_yaml_cases("./case/test_upload_my_file.yaml"),
                             ids=[case["title"] for case in read_yaml_cases("./case/test_upload_my_file.yaml")])
    def test_upload_my_file(self, case):
        '''
        上传素材接口；
        4条用例；
        登录成功的用例中提取“body”令牌
        '''
        headers = case["request"]["headers"]
        headers["authorization"] = f"Bearer {read_yaml("auth")}"

        response = RequestsUtil().all_requests(method=case["request"]["method"], url=case["request"]["url"],
                                               headers=headers, params=case["request"]["params"],
                                               files=case["request"]["datas"])

        assert response.json()["status"] == case["expected"]["response"]["status"]
        assert response.json()["message"] == case["expected"]["response"]["message"]
        assert response.json()["code"] == case["expected"]["response"]["code"]
        if case["case_id"] == "upload_my_file_001":
            assert response.json()["body"]["code"] == case["expected"]["response"]["body"]["code"]
        elif case["case_id"] != "upload_my_file_001":
            assert response.json()["name"] == case["expected"]["response"]["name"]
