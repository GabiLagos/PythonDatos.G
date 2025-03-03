import pymysql

connection = pymysql.connect(host='localhost', port=3306
, user='root', password='123456', database='classicmodels')
print("funciona la conexion mysql-python????")