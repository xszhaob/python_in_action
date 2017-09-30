import pymysql

conn = pymysql.connect(host = '', port = 8080, user = 'caocao', password = '', db = '', charset = 'utf8')

sql = 'select * from order_system.os_order where order_no = %d'
cur = conn.cursor()
try:
	cur.execute(sql % 1969)
	print(cur.fetchone())
	conn.commit()
except Exception as e:
 	conn.rollback()
finally:
	cur.close()
	conn.close()
