import urllib.request
myURl = urllib.request.urlopen('https://www.runoob.com')
print(myURl.getcode()) # 可以使用getcode()获取网页状态,200说明正常,404说明不存在

