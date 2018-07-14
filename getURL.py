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

import  time
def getYear():
    # 年数'2011a','2012a','2013a' , '2014a', '2015a', '2016a','2017a'
    year = ['2013a']
    return year


def getMeiZiTuUrl():
    # 年数
    # year = ['2011a', '2012a', '2013a', '2014a', '2015a', '2016a', '2017a']
    # 月数
    month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    # 天数
    day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18',
           '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
    # 图片数
    pictureNum = ['01.jpg', '02.jpg', '03.jpg', '04.jpg', '05.jpg', '06.jpg', '07.jpg', '08.jpg', '09.jpg', '10.jpg']
    list = []
    # print(yearPath)
    # for yearP in year:
    #     yearPath = yearP +"/"
    for monthP in month:
        monPath = "/" + monthP + "/"
        # print(monPath)
        for dayP in day:
            dayPath = monPath + dayP + "/"
            # print(dayPath)
            for picture in pictureNum:
                picturePath = dayPath + picture
                # print(picturePath)
                list.append(picturePath)

    return list


