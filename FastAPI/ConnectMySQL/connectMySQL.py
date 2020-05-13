'''
@Author: _zone
@Date: 2020-05-13 15:16:55
@LastEditTime: 2020-05-13 17:29:36
@FilePath: /FastAPIDemo/ConnectMySQL/connectMySQL.py
'''

import pymysql


# 链接数据库
db = pymysql.connect(host='地址',
                     port=端口,
                     user='用户名',
                     passwd='密码',
                     db='数据库',
                     charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()


def search_version():

    # 使用 execute() 方法执行 SQL 查询
    sql = "SELECT VERSION()"
    try:
        cursor.execute(sql)
        data = cursor.fetchone()
        print("Database version : %s " % data)
    except(Exception):
        print('Error: unable to fetch data')

    # 关闭数据库链接
    db.close()


def search_data():
    # SQL 查询语句
    sql = "select * from python"  # python 表为小写，若写成大写就挂了
    try:
        cursor.execute(sql)
        results = cursor.fetchall()

        for row in results:
            uid = row[0]
            name = row[1]
            sex = row[2]
            height = row[3]
            weight = row[4]
            area = row[5]
            city = row[6]

            print("uid=%d" % uid)
            print("name=%s" % name)
            print("sex=%s" % sex)
            print("height=%d" % height)
            print("weight=%d" % weight)
            print("area=%s" % area)
            print("city=%s" % city)

    except(Exception):  # Exception 加入防止 PEP8 报错问题
        print('Error: unable to fetch data')

    # 关闭数据库连接
    db.close()


if __name__ == "__main__":
    search_data()
    # search_version()
