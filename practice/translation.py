import requests
from parsel import Selector


class Translator():
    def __init__(self, word):
        self.method = "POST"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
        }
        self.url = "https://smartisandict.youdao.com/translate"
        self.data = {
            "inputtext": word,
            "type": "AUTO"
        }

    # 用requests库输出响应内容，这里的响应内容是个html，所以使用text
    def get_data(self):
        resp = requests.request(self.method ,self.url, data=self.data, headers=self.headers, timeout=10)
        return resp.text

    # 使用parsel库的Selector方法，实例话html，然后通过xpath找到找到的内容
    def parse_text(self, html):
        selector = Selector(text=html)
        # 通过xpath找到具体位置后，如果想输出文案，需要添加text()
        result = selector.xpath("//*[@id='translateResult']/li/text()").get()
        print(result)

    # 执行方法命令
    def run(self):
        resp = self.get_data()
        self.parse_text(resp)

# 区分脚本的 “运行方式”
if __name__ == '__main__':
    print("===== 有道翻译工具 =====")
    print("输入「退出」或者「quit」可终止程序\n")
    # 无限循环，直到输入「退出」或者「quit」
    while True:
        # 获取用户输入（去除首尾空格，避免误判）
        word = input("请输入想翻译的内容：").strip()
        # 判断是否退出
        if word in ("退出", "quit"):
            print("程序已终止，感谢使用！")
            break
        # 判空：避免输入空内容时请求接口
        if not word:
            print("输入内容不能为空，请重新输入！")
            continue
        # 执行翻译
        trans = Translator(word)
        trans.run()
        print("-" * 50)  # 分隔线，优化输出体验
