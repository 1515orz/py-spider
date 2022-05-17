import urllib.request
import urllib.parse
import json
# inputtext: Yes I need I need my samurai type: AUTO
# encode 是编码. decode是解码
url = 'https://m.youdao.com/translate'
data = {}
data['type'] = 'AUTO'
data['inputtext'] = 'fuck you'

data = urllib.parse.urlencode(data).encode('utf-8')  # 编码data

response = urllib.request.urlopen(url,data)  # openurl操作
html = response.read().decode('utf-8')  # 解码读取

print(html)
# target = json.loads(html)

