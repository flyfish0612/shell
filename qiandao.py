#encoding:UTF-8
import urllib.request  
import urllib  
import gzip  
import http.cookiejar  
  
  
def getOpener(head):  
    # deal with the Cookies  
    cj = http.cookiejar.CookieJar()  
    pro = urllib.request.HTTPCookieProcessor(cj)  
    opener = urllib.request.build_opener(pro)  
    header = []  
    for key, value in head.items():  
        elem = (key, value)  
        header.append(elem)  
    opener.addheaders = header  
    return opener  
  
def ungzip(data):  
    try:        # try extract  
        print('extracting file .....')  
        data = gzip.decompress(data)  
        print('finished!')  
    except:  
        print('it is ok,do not need to extract.')  
    return data  
  
  
header = {  
    'Connection': 'Keep-Alive',  
    'Accept-Language': 'zh-CN,zh;q=0.8', 
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',  
    'User-Agent':' Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',  
    'Accept-Encoding': 'gzip, deflate',  
    'Host': '123.206.92.65',  
}  
  
  
url = 'http://123.206.92.65/web/useraction.php?a=dologin'  
opener = getOpener(header)  
  
id = 'xxxxxxx'  
password = 'xxxxxx'  
postDict = {  
        'qq': id,  
        'pass': password,  
}  
  
postData = urllib.parse.urlencode(postDict).encode()  
op = opener.open(url, postData)  
data = op.read()  
data = ungzip(data)  
  
print(data)  
  
  
url = 'http://123.206.92.65/web/action.php?a=qiandao' 
  
op = opener.open(url)  
  
data = op.read()  
data = ungzip(data)  
  
print(data)  