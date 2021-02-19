# coding = UTF-8
'''
@File : ready_path.py
@Time : 2020/11/17 10:45 AM 
@Author : Cc
'''

import os

# 获取项目的根路径
base_path = os.path.dirname(os.path.dirname(__file__))

# 测试用例路径
case_path = os.path.join(base_path, 'testcase')

# 测试报告路径
report_path = os.path.join(base_path, 'report')

# 用例数据的路径
data_path = os.path.join(base_path, 'data')

# 日志路径
log_path = os.path.join(base_path, 'logs')

# 配置文件路径
config_path = os.path.join(base_path, 'config')