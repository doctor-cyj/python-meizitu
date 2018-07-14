"""
__author__ = 'Doctor-CYJ'
__mtime__ = '2018/5/3'
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import  requests,os,time
from  meizituDemo import getURL
url = "http://mm.chinasareview.com/wp-content/uploads/"
#返回年份列表
year_dir = getURL.getYear()
dir = "g:/picture/"
headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
                     "*/*;q=0.8", "Accept-Encoding": "gzip, deflate",
           "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
           "Connection": "keep-alive", "Host": "mm.chinasareview.com", "Upgrade-Insecure-Requests": "1",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0"}
currentTime = time.time()
#判断目录是否存在
for year in year_dir:
    #根据年份创建不同的目录
    dir_path = dir+year
    #判断目录是否存在
    if not os.path.exists(dir_path):
        print("目录不存在")
        os.mkdir(dir_path)
    #返回月份开始的图片地址
    list = getURL.getMeiZiTuUrl()
    for month_jgp_path in list:
        picture_url= url + year + month_jgp_path
        # print(picture_url)
        response = requests.get(picture_url, headers=headers)
        if response.status_code != 200:
            # print("路径错误了")
            print(response.status_code)
            continue


        #当请求路径错误则不执行下列代码
        file_name = year + month_jgp_path
        #响应成功则为图片命名
        file_name = file_name.replace("/","-")
        with open(dir_path+"/"+file_name,"wb") as file:
            file.write(response.content)
            print("一")
        file.close()
afterTime = time.time()
print("项目跑完了")
print(afterTime-currentTime)