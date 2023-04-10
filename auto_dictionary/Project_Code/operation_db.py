import pymysql
import re

f = open('dict.txt')

db = pymysql.connect(port=3306,host='localhost',user='root',password='li1994221',database='auto_dictionary',charset='utf8')
cur = db.cursor()

sql = 'insert into words (word,mean) values (%s,%s)'
for line in f:
    tup = re.findall(r'(\S+)\s+(.*)',line)[0] # 返回的整体是一个元组,元祖中的内容是两个捕获组
    try:
        cur.execute(sql,tup)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()

cur.close()
db.close()