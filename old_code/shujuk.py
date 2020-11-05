import pymysql


db = pymysql.connect(host='localhost', user='me', password='abcd445566', port=3306, db='spider')
cursor = db.cursor()
'''
sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
cursor.execute(sql)
'''

id_ = '20190831'
user = 'edu'
age = '22'
sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s) '
try:
    cursor.execute(sql, (id_, user, age))
    db.commit()
except:
    db.rollback()
db.close()

