import requests
login_url = 'https://www.douban.com/accounts/login'
headers = {
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
form_data = {
    'source': 'index_nav',
    'form_email': '*******',
    'form_password': '*********'
}
response = requests.post(login_url,data=form_data,headers=headers)
print(response.text)
print(response.url)
