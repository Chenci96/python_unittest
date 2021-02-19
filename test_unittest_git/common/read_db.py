# coding = UTF-8
'''
@File : read_db.py
@Time : 2020/11/19 3:00 PM 
@Author : Cc
'''

import pymysql
import paramiko
from sshtunnel import SSHTunnelForwarder
from test_unittest_git.common.ready_config import conf

class DB:

    # 链接数据库     DictCursor - 以字典形式返回操作结果
    def __init__(self,host,port,user,password):
        self.db = pymysql.connect(host = host,
                                  port = port,
                                  user = user,
                                  password = password,
                                  charset = 'utf8',
                                  cursorclass = pymysql.cursors.DictCursor)
        # 使用cursor()获取游标
        self.cur = self.db.cursor()

    def find_data(self,sql):
        # 提交数据库事务
        self.db.commit()

        # 使用execute()方法执行sql语句
        self.cur.execute(sql)
        # 获取所有记录列表
        data = self.cur.fetchall()

        # 关闭数据库/游标
        self.db.close()
        self.cur.close()

        return data



db = DB(host=conf.get('mysql', 'host'),
        port=conf.getint('mysql', 'port'),
        user=conf.get('mysql', 'user'),
        password=conf.get('mysql', 'password')
        )

if __name__ == '__main__':
    print(db.find_data("select * from 'dsp_business_pool'.'dsp_talent_review limit 1'"))
