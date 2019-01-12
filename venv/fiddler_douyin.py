import requests

url = 'http://v5-dy.ixigua.com/d61ad9da7f06806b31083c39a572a292/5c398986/video/m/2203697acf8ee1149f8ba1e8d470beb4252116130d440000b5eaeebe30dc/?rc=anN4aWo7OXVuajMzO2kzM0ApQHRAbzg3Njo0OzgzNDQzNjU0PDNAKXUpQGczdylAZmh1eXExZnNoaGRmOzRAbmYyLW9lNTBwXy0tYi0vc3MtbyNvIzY0NDE1LS4tLS8wLi4tLi9pOmItbyM6YC1vI3BiZnJoXitqdDojLy5e'  # 在fiddler上复制
headers = {  # 在fiddler上复制
'User-Agent': 'Lavf/57.71.100',
'Accept': '*/*' ,
'Icy-MetaData': '1',
'Vpwp-Type': 'proxy',
'Vpwp-Key': '0D0F192CFB460AF69F316AC3AD2137F8',
'Vpwp-Raw-Key': 'v0200f080000bgsjbfb3ft9sjdrpkr3g_h264_540p_893347',
'Vpwp-Mp-Range': 'bytes=0-',
'Vpwp-Flag': '0',
'Accept-Encoding': 'identity',
'Host': 'v5-dy.ixigua.com',
'Connection': 'Keep-Alive'

}
response = requests.get(url, headers=headers)
with open('douyin.mp4', 'wb') as f:
    f.write(response.content)
