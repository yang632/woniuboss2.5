# -*- encoding: utf-8 -*-
# File    : utility
# Author  : yang
# Email   : yang@163.com
# Software: PyCharm
# Time    : 2020/5/14 13:09
class Utility:
    @classmethod
    def get_json(cls, path):
        import json
        with open(path, encoding='utf8') as file:
            contents = json.load(file)
        return contents

    #读Excel文件,提取测试数据
    @classmethod
    def get_testinfo(cls,conf):
        import xlrd
        # 获取Excel表的路径
        workbook=xlrd.open_workbook(conf['TESTINFO_PATH'])
        # 获取工作表的对象
        contents=workbook.sheet_by_name(conf['SHEETNAME'])
        testinfo = []
        # 通过sheet页对象读取其内容
        for i in range(conf['START_ROW'], conf['END_ROW']):
            testdata = contents.cell(i, conf['TESTDATA_COL']).value
            expect = contents.cell(i, conf['EXPECT_COL']).value
            # 使用换行符作为分隔符
            temp = testdata.split('\n')
            # 定义字典用于存放每一项测试数据
            tup = {}
            for t in temp:
                # 给字典添加元素
                tup[t.split('=')[0]] = t.split('=')[1]
            # 在字典中添加期望结果的元素
            tup['expect'] = expect
            testinfo.append(tup)
        # 返回测试的数据
        return testinfo
    # 判断封装
    @classmethod
    def assert_equals(cls, expect, actual):
        if expect == actual:
            return True
        else:
            return False

    # 生成随机数
    @classmethod
    def get_random_num(cls, start, end):
        import random
        return random.randint(start, end)

    # 创建数据库连接
    @classmethod
    def getConn(cls):
        import pymysql
        contents = cls.get_json('../conf/base.conf')
        return pymysql.connect(contents['HOSTNAME'],
                               contents['DBUSER'], contents['DBPASS'],
                               contents['DBNAME'], charset='utf8')

    # 查询一条记录
    @classmethod
    def query_one(cls, sql):
        conn = cls.getConn()
        cur = conn.cursor()
        try:
            cur.execute(sql)
            result = cur.fetchone()
        except Exception as e:
            result = None
        finally:
            cur.close()
            conn.close()
        return result

    # 查询多条记录
    @classmethod
    def query_all(cls, sql):
        conn = cls.getConn()
        cur = conn.cursor()
        try:
            cur.execute(sql)
            result = cur.fetchall()
        except Exception as e:
            result = None
        finally:
            cur.close()
            conn.close()
        return result

    # 增删改操作
    @classmethod
    def update_data(cls, sql):
        flag = False
        conn = cls.getConn()
        cur = conn.cursor()
        try:
            cur.execute(sql)
            conn.commit()
            flag = True
        finally:
            cur.close()
            conn.close()
            return flag

