import urllib.request
import urllib.parse
import re

url = 'http://sso.wyschina.com/login.jsp'

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

headers = {
'Host': 'sso.wyschina.com',
'Connection': 'keep-alive',
'Cache-Control': 'max-age=0',
'Origin': 'http://sso.wyschina.com',
'Upgrade-Insecure-Requests': 1,
'Content-Type': 'application/x-www-form-urlencoded',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',

'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
'Cookie': 'UM_distinctid=16956ece7a0b0-09d6cdf321718e-9333061-100200-16956ece7a225f; ectrip_5db92b025cc14214afb23ad984ef2235=lijiecxq; ectrip_558be96cc59542b7aa0a7a0d89c12689=lijiecxq; EctripSSOID=ectrip_8693f342a98447ba9a1ebc3b4a8d8c06; ectrip_8693f342a98447ba9a1ebc3b4a8d8c06=lijiecxq; JSESSIONID=0000T-cSvnVFvGF-6KuElIQGrPn:1bkekdau0; CNZZDATA1263271798=1399443820-1551941560-http%253A%252F%252Fw.wyschina.com%252F%7C1551951251'
}
loginurl = 'http://sso.wyschina.com/SSOAuth'


pat = re.compile('src="/create.*? ')
imgurl = pat.findall(html)
imgurl = imgurl[0].strip()
imgurl = 'http://sso.wyschina.com/'+imgurl.replace('"','')
imgurl = imgurl.replace('src=/','')
print(imgurl)

urllib.request.urlretrieve(imgurl,filename='random.jpg')
random = int(input('请输入验证码'))
formdata = {
    "username":"lijiecxq",
    "password":"123456789",
    'random':random,
    'url':'http://w.wyschina.com/custom/login.action?action=http%3A%2F%2Fwww.wyschina.com%2Findex.html',
}

data = bytes(urllib.parse.urlencode(formdata), encoding='utf8')
request = urllib.request.Request(loginurl,data=data,headers=headers)
resp = urllib.request.urlopen(request)
print(resp.read().decode('utf8'))