# coding = UTF-8
'''
@File : test_talentReview_list.py
@Time : 2020/11/17 5:46 PM 
@Author : Cc
'''

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import os
import unittest
import requests
from jsonpath import jsonpath
from unittestreport import ddt,list_data
# from test_unittest_git.common import myddt
from test_unittest_git.common.ready_config import conf
from test_unittest_git.common.ready_path import data_path
from test_unittest_git.common.ready_excel import Read_excel
from test_unittest_git.common.ready_log import log
from test_unittest_git.common.read_ssh_db import db

@ddt
class Test_relist(unittest.TestCase):

    # 给Read_excel类创建实例对象
    excel = Read_excel(os.path.join(data_path,'cases.xlsx'),'review_list')
    cases = excel.read_excel()

    @list_data(cases)
    def test_list(self,casedata):
        # 获取用例中的数据
        method = casedata['method']
        parmas = eval(casedata['parmas'])
        expected = eval(casedata["expected"])
        case_row = casedata["case_id"] + 1
        sql = casedata['check_sql']
        # 创建字典cookie(cookies传参需要以字典形式)
        cookie = {conf.get('cookies', 'token_key'): conf.get('cookies', 'token_value')}

        # 请求接口数据
        reqs = requests.request(method=method,url=conf.get('env', 'review_list'),cookies=cookie,json=parmas)
        res = reqs.json()
        # print('预期结果:', expected)
        print('返回结果:', res)

        # 获取task_id
        evaluation_task_id = jsonpath(res,'$..evaluation_task_id')[0]

        # 判断是否有sql
        if sql:
            execute_sql = db.ssh_db(sql.format(evaluation_task_id))
            print('sql:', sql.format(evaluation_task_id))
            print('sql结果:',execute_sql)

        try:
            self.assertIsNotNone(jsonpath(res, '$..data'))
            if sql:
                self.assertTrue(execute_sql)

        except AssertionError as e:
            self.excel.write_excel(row=case_row, column=6, value='失败')
            log.error("用例-{}，执行失败".format(casedata['title']))
            log.exception(e)
            raise e

        else:
            log.info("用例-{}，执行成功".format(casedata['title']))
            self.excel.write_excel(row=case_row, column=6, value='通过')
