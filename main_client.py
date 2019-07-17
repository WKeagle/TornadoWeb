import sys
import tornado.ioloop
from tornado.httpclient import HTTPClient,AsyncHTTPClient

# 定义函数: 处理html内容
def handle_response(response):
	if response.error:
		print("Error")
	else:
		print("called")

if __name__ == '__main__':
    # 调用函数asynchronous_fetch时,仅执行asynchronous_fetch函数里面的代码(默认不会帮你执行callback的代码)
    # 只有启动tornado的事件环回机制后<tornado.ioloop.IOLoop.instance().start()>
    # 才会执行callback中的内容.
    http_client = AsyncHTTPClient()
    http_client.fetch("https://localhost:7089", handle_response)
    tornado.ioloop.IOLoop.instance().start()