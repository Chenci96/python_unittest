# coding = UTF-8
'''
@File : read_ssh_db.py 
@Time : 2020/11/20 1:42 PM 
@Author : Cc
'''

import os
import paramiko
import pymysql
from sshtunnel import SSHTunnelForwarder
from test_unittest_git.common.ready_config import conf
from test_unittest_git.common.ready_path import config_path

class SSH_DB():
    def __init__(self):
        # 配置跳板机
        self.ssh_host = conf.get('ssh', 'ssh_host')
        self.ssh_port = int(conf.get('ssh', 'ssh_port'))
        self.ssh_keyfile = conf.get('ssh', 'ssh_keyfile')
        self.ssh_keypw = conf.get('ssh', 'ssh_keypw')
        self.ssh_name = conf.get('ssh', 'ssh_name')

        # 配置数据库
        self.host = conf.get('mysql', 'host')
        self.port = int(conf.get('mysql', 'port'))
        self.user = conf.get('mysql', 'user')
        self.password = conf.get('mysql', 'password')

    # 链接跳板机
    def ssh_db(self,sql):
        # 获取密钥   (秘钥地址,密码短语)
        key_path = os.path.join(config_path, self.ssh_keyfile)
        private_key = paramiko.RSAKey.from_private_key_file(key_path, self.ssh_keypw)

        with SSHTunnelForwarder(
                # 指定ssh登录的跳转机的host,port
                ssh_address_or_host=(self.ssh_host, self.ssh_port),
                # 跳板机密钥
                ssh_pkey=private_key,

                # 跳板机账户密码
                ssh_username=self.ssh_name,
                # 如果是通过密码访问，可以把下面注释打开，将密钥注释即可。
                # ssh_password = "XXX",

                # 设置A机器的数据库服务地址及端口
                remote_bind_address=(self.host, self.port)
                ) as server:

            db = pymysql.connect(host='127.0.0.1',  # 此处必须是必须是127.0.0.1，代表C机器
                                 port=server.local_bind_port,
                                 user=self.user,
                                 passwd=self.password,
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor  # 以字典形式返回操作结果,默认为元组形式
                                 )

            cur = db.cursor()  # 使用cursor()获取游标

            cur.execute(sql)  # 使用execute()方法执行sql语句
            data = cur.fetchall()  # 获取所有记录列表
            # data1 = cur.fetchone()       # 使用 fetchone() 方法获取一条数据

            # 关闭数据库/游标
            db.close()
            cur.close()

            return data

db = SSH_DB()

if __name__ == '__main__':
    # print(db.ssh_db("select * from dsp_business_pool.dsp_talent_review limit 1;"))
    print(db.ssh_db("SELECT * FROM `dsp_business_pool`.`dsp_talent_review` where evaluation_task_id = 7330678935255831448;"))