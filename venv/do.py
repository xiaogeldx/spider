# import requests
# ---------------
# login_url = ''      #豆瓣
# response = requests.post(login_url)
# headers = {
#     'User-Agent':''
# }
# form_data = {
#     'source':'index_nav',
#     'form_email':'',
#
# }
# response = requests.post(login_url,data=form_data,headers=headers)
# print(response.text)
# print(response.url)
#1.访问首页面 cookie
#2.验证用户名和密码携带上一次的cookie
# 3.权限验证，携带上一次的cookie
# 123当做一个会话
# -------------
# 1.访问首页面
# import base64
# import re
# def get_point_by_index(index):
#     """
#     根据图片的序号快读获取坐标
#     :param index: 1,2
#     :return: 111,111,222,222
#     """
#     map = {
#         '1':'39,43',
#         '2':'109,43',
#         '3':'185,43',
#         '4':'253,43',
#         '5':'39,121',
#         '6':'109,121',
#         '7':'185,121',
#         '8':'253,121',
#     }
#     indexs = index.split(',')
#     temp = []
#     for index in indexs:
#         temp.append(map[index])
#     return ','.join(temp)
# cookies = None
# login_page_url = ''
# headers = {
#     'User':
# }
# response = requests.get(login_page_url,headers=headers)
# cookies = response.cookies
# # 2.下载 图片验证码
# captcha_url = ''
# captcha_response = requests.get(captcha_url,headers=headers)
# # print(captcha_response.text)
# # print(captcha_response.content)
# img_data = re.findall(b'image":"(.*?)"',captcha_response.content)[0]
# # print(img_data)
# # res = base64.b64decode(img_data)
# # print(res)
# with open('captcha','wb') ad f:
#     f.write(base64.b64decode(img_data)) #解码后的验证码图片信息
# cookies = captcha_response.cookies
# #验证验证码
# check_captcha_api = ''
# args = {
#     'callback':'',
#     'answer':get_point_by_index(input('请输入正确的图片坐标：')),
#     'rand':'sjrand',
#     'login_site':'E',
#     '_':'1547128748677',    #为了防止浏览器的缓存
# }
# # print(args)
# check_response =



# 就是说协议定义好后，protobuf可以生成不同系统的反序列化代码，stub就可以被异构系统读取
# print(parse.parse_qs('wd=%E6%B5%8B%E8%AF%95&code=1&height=188'))


