import requests
import json
import re
from docx import Document

def get_document(url):
    # 文库url
    sess = requests.session()
    res = sess.get(url).content
    print(res)
    html = res.decode("gbk")
    # 抓取到文档标题
    title = re.search('id="doc-tittle-0">(.*?)</span>', html).group(1)
    print(title)
    # 使用正则提取 文档内容的url
    res = re.search("WkInfo.htmlUrls = '(.*)'", html).group(1)
    # \\x22是linux中的引号，替换成Python中的引号
    res = res.replace("\\x22", "\"")
    # 转成字典
    data = json.loads(res)
    # 新建一个文档
    document = Document()
    string = ""
    for i in data["json"]:
        url = i["pageLoadUrl"]  # 获取到url
        url = url.replace("\\", "")  # url中有转义符\去掉
        # 请求文档内容
        data = requests.get(url).content.decode("utf-8")
        # 提取文本数据
        res = re.search(r"wenku_\d*\((.*)\)", data, re.S).group(1)
        # 将json对象数据转成Python对象
        data = json.loads(res)
        for i in data['body']:
            # 判断数据是什么类型
            if i["t"] == "word":
                # 获取到文本
                string += str(i["c"])
                # ps中不为空并且_enter==1的时候是换行也就是一段内容
                if i["ps"] and i["ps"].get("_enter") == 1:
                    document.add_paragraph(string)  # 将一段内容写入到word
                    #print(string)
                    string = ""  # 重新复制 "" 表示新的一段文本
    # 保存word
    document.save(title + ".docx")
#get_document("https://wenku.baidu.com/view/96aa5f28fad6195f312ba695")
get_document("https://wenku.baidu.com/view/5003f11dc081e53a580216fc700abb68a982ad02.html")
