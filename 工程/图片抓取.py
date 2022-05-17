import urllib.request

res_cat = urllib.request.urlopen('http://www.placekitten.com/g/200/300')  # 返回的是一个内容,可以用read来读取
cat_image = res_cat.read()

with open('cat_500_600.jpg','wb') as f:
    f.write(cat_image)

# 同样可以执行的第二种方法
# req = urllib.request.Request('http://www.placekitten.com/g/200/300')
# response = urllib.request.urlopen(req)
# cat_img = response.read()
# with open('cat_500_600.jpg','wb') as f:
#     f.write(cat_img)

res_cat.get