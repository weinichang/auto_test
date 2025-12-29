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
                MIME_TYPE_MAP = {
                    "jpg": "image/jpeg",
                    "jpeg": "image/jpeg",
                    "png": "image/png",
                    "txt": "text/plain",
                    "pdf": "application/pdf",
                    "doc": "application/msword",
                    "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    "json": "application/json",
                    "mp4": "video/mp4",
                    "zip": "application/zip",
                    "xls": "application/vnd.ms-excel",
                    "xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                }
                for file_key, file_value in value.items():
                    with open(file_value, "rb") as f:
                        file_content = f.read()
                    file_name = file_value.split("/")[-1]
                    file_mine = MIME_TYPE_MAP.get(file_name.split(".")[-1].lower())
                    # 上传文件的格式
                    value[file_key] = (file_name, file_content, file_mine)
        resp = RequestsUtil.sess.request(**kwargs)
        return resp
