import urllib.request as ure
import urllib

# res_fishc = ure.urlopen('http://www.fishc.com')  # 打开url传入response
# html = res_fishc.read()  # 如果不解码,结果是二进制难以查看(b开头说明是二进制)
# 使用utf-8解码操作
# html = html.decode('utf-8')
# print(html)  # 获取网页信息
res_runoob = urllib.request.urlopen('https://www.runoob.com')
# print(res_runoob.read().decode('utf-8'))  # read参数可以调整读几行,输出网页信息
# print(res_runoob.readlines())  # 也可以使用readline()读取一行,或者readlines()读取全部内容,并赋值到一个列表变量

myURl = urllib.request.urlopen('https://www.runoob.com')
print(myURl.getcode()) # 可以使用getcode()获取网页状态,200说明正常,404说明不存在
# f = open('runoob_urllib_test.html','wb')  # 创建一个对象为f的文件
# content = myURl.read()  # 读取网页内容
# f.write(content)  # 对文件f进行写入
# print(myURl.geturl())  # geturl()得到的是访问地址
# print(myURl.info())  # info()返回的是服务器属性
# 编码
encode_url = urllib.request.quote('https://www.runoob.com')  # 进行编码操作
print(encode_url)  # 输出编码后的结果
# 解码
unencode_url = urllib.request.unquote('https://www.runoob.com')  # 进行解码操作
print(unencode_url) # 输出解码后的结果
