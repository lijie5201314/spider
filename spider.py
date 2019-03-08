import requests


url = 'http://sso.wyschina.com/login.jsp'
url1 = 'http://sso.wyschina.com/createimage?Rgb=255|0|0'
url2 = 'http://sso.wyschina.com/SSOAuth'
url3 = 'http://w.wyschina.com/home/home.action'

headers1 = {
'Host': 'sso.wyschina.com',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}
response1 = requests.get(url,headers=headers1)
cookies = requests.utils.dict_from_cookiejar(response1.cookies)
cookie = ''
for (key,value) in cookies.items():
    a = key + '=' + value
    cookie = a + cookie

headers2 = {
'Host': 'sso.wyschina.com',
'Connection': 'keep-alive',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
'Referer': 'http://sso.wyschina.com/login.jsp',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
'Cookie':cookie
}
response2 = requests.get(url1,headers=headers2)
with open('code.jpg','wb')as f:
    f.write(response2.content)

code = input()

body = {
'username':'lijiecxq',
'password':'123456789',
'random':code,
'url':'http://w.wyschina.com/custom/login.action?action=http%3A%2F%2Fw.wyschina.com%2Findex.html'
}


headers5 = {
'Host': 'w.wyschina.com',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Referer': 'http://w.wyschina.com/index.html',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
'Cookie': cookie
}

session = requests.session()
response3 = session.post(url2,data=body,headers=headers5)
respon = session.get(url3)
print(respon.content)
