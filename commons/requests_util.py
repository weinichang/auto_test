'''
整合requests库的session(),实现自动关联cookie，维持会话的持久化
'''

import requests


class RequestsUtil:
    # 同一个session，关联cookie
    sess = requests.Session()

    def all_requests(self, **kwargs):
        # 设置公共参数
        total_headers = {
            "Content-Type": "application/json",
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
        }
        # 统一处理参数
        for key, value in kwargs.items():
            # 针对headers的统一处理
            if key == "headers":
                kwargs["headers"].update(total_headers)
            # 针对上传文件的统一处理（用例只需要写地址）
            elif key == "files":
                for file_key, file_value in value.items():
                    value[file_key] = open(file_value, "rb")

        resp = RequestsUtil.sess.request(**kwargs)
        return resp
