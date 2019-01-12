import requests
import base64
import re
def get_point_by_index(indexs):
    """
    根据图片的序号快速获取坐标
    :param insexs:1,2
    :return:111,111,222,222
    """
    map = {
        '1':'39,43',
        '2':'109,43',
        '3':'185,43',
        '4':'253,43',
        '5':'39,121',
        '6':'109,121',
        '7':'185,121',
        '8':'253,121',
    }
    indexs = indexs.split(',')
    temp = []
    for index in indexs:
        temp.append(map[index])
    return ','.join(temp)
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
session = requests.Session()
#添加请求头
session.headers.update(headers)
#1.访问首页面
login_page_url = 'https://kyfw.12306.cn/otn/resources/login.html'
response = session.get(login_page_url)
# print(response.cookies)
#2.下载图片 验证码
captcha_url = 'https://kyfw.12306.cn/passport/captcha/captcha-image64?login_site=E&module=login&rand=sjrand&1547303075115&callback=jQuery19106706322143238805_1547303062080&_=154730'
captcha_response = session.get(captcha_url)
# print(captcha_response.text)
#获取图片信息
img_data = re.findall(b'"image":"(.*?)"',captcha_response.content)[0]
# print(img_data)
res = base64.b64decode(img_data)
with open('captcha.jpg','wb') as f:
    f.write(base64.b64decode(img_data)) #解码后的验证码图片信息
cookies = captcha_response.cookies
#3.验证验证码
check_captcha_api = 'https://kyfw.12306.cn/passport/captcha/captcha-check'
args = {
    'callback':'jQuery191032014987830377206_1547304492627',
    'answer':get_point_by_index(input("请输入正确的图片坐标：")),
    'rand':'sjrand',
    'login_site':'E',
    '_':'1547304492633',    #只是为了防止浏览器的缓存，爬虫可以不管
}
# print(args)
check_response = session.get(check_captcha_api,params=args)
print(check_response.text)