"""
审题：
    1. 目标网站：百度音乐
    2. 指定歌手：---key=薛之谦
    3.获取的是MP3文件
分析；
    1.网站分析：网页源代码    ---songid
    2.抓包分析：
        1.json文件   url  里面存放MP3
思路；
    1.指定歌手：---key=薛之谦
    2.从网页源代码里获取歌曲id
    3.制作json文件   url
    4.从json文件里提取MP3文件链接
http://music.taihe.com/search?key=%E8%96%9B%E4%B9%8B%E8%B0%A6
解
"""
import re
import requests
import json
# from bs4 import BeautifulSoup
"""
爬虫流程
1.url
2.模拟浏览器请求资源
3.解析网页
4.
"""
url = "http://music.taihe.com/search"
data = {
    "key":"薛之谦"
}
response = requests.get(url,params=data)    #网页源代码
html = response.text    #返回网页源代码的文本形式
# print(html)
# 歌曲id
sids = re.findall(r'data-playdata="(.+?)"',html)
# print(sids)
da1 = re.findall(r'\d+',sids[0])
# print(da1)

# http://111.40.195.236/cache/zhangmenshiting.qianqian.com/data2/music/03f079f62f693c045ec78416f8ae3515/596832469/596832469.mp3?xcode=6653d0f7f3ccebd32b8f63f9ac723f36&ich_args2=620-05222603023203_f198eeaae57c3890b00c73e84bd2d467_10575301_9c89602ad1caf9d5973b518939a83798_aa825625c0f5ccb7fd1f063103892bc8
for i in da1:
    api = 'http://111.40.195.236/cache/zhangmenshiting.qianqian.com/data2/music/03f079f62f693c045ec78416f8ae3515/596832469/596832469.mp3?xcode=%sd0f7f3ccebd32b8f63f9ac723f36&ich_args2=620-05222603023203_f198eeaae57c3890b00c73e84bd2d467_10575301_9c89602ad1caf9d5973b518939a83798_aa825625c0f5ccb7fd1f063103892bc8
'%i
    # print(api)

    response = requests.get(api)
    data = response.text
    print(data)
    #提取
    data1 = re.findall(r'\((.*)\)',data)



# 答题步骤