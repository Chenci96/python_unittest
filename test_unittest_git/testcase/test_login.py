# coding = UTF-8
'''
@File : test_login.py
@Time : 2020/11/17 10:42 AM 
@Author : Cc
'''

import unittest
import requests
from test_unittest_git.common.ready_config import conf
from test_unittest_git.common.ready_log import log
from unittestreport import ddt,list_data
from jsonpath import jsonpath

@ddt
class Testlogin(unittest.TestCase):
    data = [{"title":"B端登录"}]

    @list_data(data)
    def testlogin(self,case):
        data = {
        "username": conf.get('user_info','username'),
        "password": conf.get('user_info','password')
        }
        reqs = requests.post(url=conf.get('env','Login'),json=data)
        res = reqs.json()
        print('返回结果:',res)
        # 断言
        try:
            self.assertEqual(reqs.status_code, 200)
        except AssertionError as e:
            log.error("用例-{}执行失败".format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info("用例-{}执行成功".format(case['title']))
            # 将token写入配置文件
            token = jsonpath(res, '$..token')[0]
            conf.write_data('cookies','token_value',token)





