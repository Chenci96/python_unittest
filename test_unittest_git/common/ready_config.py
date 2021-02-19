# coding = UTF-8
'''
@File : ready_config.py
@Time : 2020/11/17 10:48 AM 
@Author : Cc
'''
import os
from configparser import ConfigParser
from test_unittest_git.common.ready_path import config_path

class Config(ConfigParser):
    def __init__(self,filename, encoding='utf-8'):
        super().__init__()
        self.read(filename, encoding=encoding)
        self.filename = filename
        self.encoding = encoding

    def write_data(self, section, option, value):
        self.set(section, option, value)
        self.write(fp=open(self.filename, 'w', encoding=self.encoding))

# 创建一个配置文件解析器
conf = Config(os.path.join(config_path, 'config.ini'))

if __name__ == '__main__':
    # 测试获取接口地址
    # print(conf.get('env','Review_list'))

    # 测试写入数据到配置文件中
    conf.write_data('env','Cookie','11112')