import urllib.request
try:  # 在不报错的情况下返回网页是否是404的信息`
    myURL2 = urllib.request.urlopen("https://www.runoob.com/no.html")
except urllib.error.HTTPError as e:
    if e.code == 404:
        print(404)   # 404
