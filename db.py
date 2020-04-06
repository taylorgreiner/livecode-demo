import pymysql.cursors

def get_db():
    return pymysql.connect(host='localhost', user='root', password='root', db='gg', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)