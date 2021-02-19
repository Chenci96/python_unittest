# coding = UTF-8
'''
@File : ready_excel.py
@Time : 2020/11/17 6:53 PM 
@Author : Cc
'''

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import os
import openpyxl
from test_unittest_git.common.ready_path import data_path

class Read_excel(object):

    def __init__(self,file_name,sheet_name):
        self.file_name = file_name
        self.sheet_name = sheet_name

    def open_workbook(self):
        # 第一步将excel加载至工作簿
        self.wb = openpyxl.load_workbook(self.file_name)

        # 第二步打开单元格
        self.sh = self.wb[self.sheet_name]

    def read_excel(self):
        # 打开用例工作薄
        self.open_workbook()

        # 第三步通过rows批量读取这个sheet内容行数的值(列表格式)
        res = list(self.sh.rows)

        """-------普通循环实现---------"""
        # title = []
        # # 循环遍历第一列单元格数据，并添加到列表中
        # for i in res[0]:
        #     title.append(i.value)

        """-------列表推导式实现---------"""
        # 取出第一行(标题)每列的值，将value以列表形式存储
        title = [i.value for i in res[0]]
        # 分别将每一行每一列的值(除第一行)对应第一行每列的value以字典形式进行存储
        cases_data = []

        # 循环res列表中的值，从下标值1开始(切片)
        for tu in res[1:]:
            # 第一种，常规循环写法
            # data = []
            # for c in tu:
            #     data.append(c.value)

            # 第二种，列表方程式循环写法
            data = [c.value for c in tu]

            case = dict(zip(title, data))
            cases_data.append(case)
        return cases_data

    # 写入excel方法
    def write_excel(self, row, column, value):
        # 调用打开工作簿方法将excel加载至工作簿并打开单元格
        self.open_workbook()
        # 将数据写入指定行列单元格中
        self.sh.cell(row=row, column=column, value=value)
        # 保存数据
        self.wb.save(self.file_name)

if __name__ == '__main__':
    excel_path = os.path.join(data_path,'cases.xlsx')
    excel = Read_excel(excel_path,'review_list')
    data = excel.read_excel()
    print(data)