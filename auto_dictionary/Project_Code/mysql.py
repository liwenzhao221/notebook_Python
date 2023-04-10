'''
数据库操作模块
思路：
将数据库操作封装一个类，将dict_server需要数据库操作功能分别协程方法，
在dict_server中实例化对象，需要什么方法直接调用
'''
import pymysql

class Database:
    def __init__(self,host = 'localhost' ,
                 port = 3306,
                 user = 'root',
                 passwd = 'li1994221',
                 charset = 'utf8',
                 database = None):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.charset = charset
        self.database = database
        self.connect_database() # 连接数据库

    def connect_database(self):
        self.db = pymysql.connect(host=self.host,
                                  port=self.port,
                                  user=self.user,
                                  passwd=self.passwd,
                                  database=self.database,
                                  charset=self.charset)
    def close(self):
        self.db.close()
    def create_cursor(self):
        self.cur = self.db.cursor()
