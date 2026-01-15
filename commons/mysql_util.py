'''
封装数据库连接、查询、关闭等操作
'''

# commons/mysql_util.py
import pymysql
from pymysql.cursors import DictCursor
from typing import List, Dict


class MySQLUtil:
    def __init__(self, host, port, user, password, db, charset="utf8mb4"):
        # 初始化数据库连接
        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            db=db,
            charset=charset,
            cursorclass=DictCursor  # 查询结果以字典格式返回
        )
        self.cursor = self.conn.cursor()

    def query(self, sql: str, params: tuple = None) -> List[Dict]:
        """执行SQL查询，返回结果列表（字典格式）"""
        self.cursor.execute(sql, params)
        return self.cursor.fetchall()

    def close(self):
        """关闭游标和连接"""
        self.cursor.close()
        self.conn.close()
