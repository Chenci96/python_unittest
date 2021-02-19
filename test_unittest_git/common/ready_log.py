# coding = UTF-8
'''
@File : ready_log.py 
@Time : 2020/11/18 4:52 PM 
@Author : Cc
'''

import os
import logging
from test_unittest_git.common.ready_path import log_path
from test_unittest_git.common.ready_config import conf
from logging.handlers import TimedRotatingFileHandler


log_file_path = os.path.join(log_path, conf.get('logging', 'log_name'))


def logs():
    # 判断是否有日志文件

    # 创建日志收集器
    logger = logging.getLogger('logs')
    # 设置日志收集器等级
    logging.root.setLevel(logging.NOTSET)
    # 最多存放日志的数量
    backup_count = conf.get('logging', 'backup_count')

    # 日志输出级别
    console_output_level = conf.get('logging', 'console_output_level')  # 控制台输出级别
    file_output_level = conf.get('logging', 'file_output_level')  # 文件输出级别

    # 日志输出格式
    formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s')

    """在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回"""
    if not logger.handlers:  # 避免重复日志
        # 创建输出到控制台的输出渠道
        console_handler = logging.StreamHandler()
        # 获取控制台输出格式
        console_handler.setFormatter(formatter)
        # 设置控制台收集器等级
        console_handler.setLevel(console_output_level)
        # 添加到收集器中
        logger.addHandler(console_handler)

        # 每天重新创建一个日志文件，最多保留backup_count份
        file_handler = TimedRotatingFileHandler(filename=log_file_path,
                                                when='D',
                                                interval=1,
                                                backupCount=backup_count,
                                                delay=True,
                                                encoding='UTF-8')
        # 获取文件输出格式
        file_handler.setFormatter(formatter)
        # 获取文件输出等级
        file_handler.setLevel(file_output_level)
        logger.addHandler(file_handler)

    return logger


log = logs()

if __name__ == '__main__':
    log.info('测试日志')
