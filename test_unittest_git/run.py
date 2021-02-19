# coding = UTF-8
'''
@File : run.py 
@Time : 2020/11/17 4:41 PM 
@Author : Cc
'''

import sys
import os
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import unittest
import time
from unittestreport import TestRunner
from test_unittest_git.common.ready_path import case_path, report_path
from test_unittest_git.common.ready_config import conf

# 加载套件
suite = unittest.defaultTestLoader.discover(case_path)


# 执行用例

runner = TestRunner(suite,
                    # filename=time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time())) + conf.get('reports', "report_name"),
                    filename=conf.get('reports', "report_name"),
                    report_dir=report_path,
                    title='测试报告',
                    tester='Cc',
                    desc="test测试报告",
                    templates=1)
runner.run()

# 发送测试报告到邮箱
runner.send_email(host='smtp.qq.com',
                  port=465,
                  user='164592267@qq.com',
                  password='fkufihkleszobicd',
                  to_addrs=['ci.chen@ifchange.com'])

