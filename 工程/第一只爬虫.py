import urllib.request

response = urllib.request.urlopen('http://www.baidu.com')  # 打开url传入response
html = response.read()  # 如果不解码,结果是二进制难以查看(b开头说明是二进制)
# 使用utf-8解码操作
html = html.decode('utf-8')
print(html)  # 获取网页信息