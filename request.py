import time
import requests
import urllib.parse
from lxml import etree
import re
headers = {
'Host': 'sso.wyschina.com',
'Connection': 'keep-alive',
'Cache-Control': 'max-age=0',
'Origin': 'http://sso.wyschina.com',
'Upgrade-Insecure-Requests': '1',
'Content-Type': 'application/x-www-form-urlencoded',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
'Accept': 'textml,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}
url = 'http://sso.wyschina.com/login.jsp'
s = requests.Session()
response = s.get(url,headers=headers)
html = response.text
print(html)

# r= s.get('http://www.wyschina.com/include/getArticle.jsp?amid=340&callback=jsonp{}'.format(int(time.time()*1000)))
# print('-'*100)
# print(r.text)

photourl = 'http://sso.wyschina.com/createimage?Rgb=255|0|0&r=8212'
response = s.get(photourl)
with open('./photo.jpg', 'ab') as f:
    f.write(response.content)

loginurl = 'http://sso.wyschina.com/SSOAuth'
headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Content-Length': '170',
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'sso.wyschina.com',
'Origin': 'http://sso.wyschina.com',
'Referer': 'http://sso.wyschina.com/login.jsp',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3510.2 Safari/537.36'
}
postdata = {
'username': 'd18123003156',
'password': '18123003156',
'url': 'http://w.wyschina.com/custom/login.action?action=http%3A%2F%2Fw.wyschina.com%2Findex.html',
}
postdata['random'] = input('验证码:')
html = s.post(loginurl, headers=headers, data=postdata)

print(html.text)