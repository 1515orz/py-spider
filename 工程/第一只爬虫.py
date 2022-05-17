import urllib.request as ure
import urllib


# res_fishc = ure.urlopen('http://www.fishc.com')  # 打开url传入response
# html = res_fishc.read()  # 如果不解码,结果是二进制难以查看(b开头说明是二进制)
# 使用utf-8解码操作
# html = html.decode('utf-8')
# print(html)  # 获取网页信息
res_runoob = urllib.request.urlopen('https://www.runoob.com')
print(res_runoob.read().decode('utf-8'))  # read参数可以调整读几行
# print(res_runoob.readlines())  # 也可以使用readline()读取一行,或者readlines()读取全部内容,并赋值到一个列表变量
print(dir(urllib))
