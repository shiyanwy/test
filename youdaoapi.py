import requests
import json

class Youdao():
    def __init__(self,word):
        self.url='http://fanyi.youdao.com/openapi.do'    #url、key、keyfrom都是固定的值，所以采用这种方式赋值
        self.key='929705525'
        self.keyfrom='pythonxiaodeng'
        self.word=word
        
    def getTranslation(self):
        data={'keyfrom':self.keyfrom,
            'key':self.key,
            'type':'data',
            'doctype':'json',
            'version':'1.1',
            'q':self.word}
        #encode
        data=requests.get(data)
        #print data
        #keyfrom=pythonxiaodeng&doctype=json&q=student&version=1.1&key=929705525&type=data
        url=self.url+'?'+data               #链接url和参数dict
        html=requests.get(url).read()
        html=json.loads(html)
        return html

#调用
youdao=Youdao('student')
result=youdao.getTranslation()
for key in result:
    print(key)