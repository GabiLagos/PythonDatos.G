import oracledb
from models import doctor as model

class ServiceOracleDoctores:
    def __init__(self): #LO PRIMERO, CREAMOS UN OBJETO CONNECTION
        self.connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
        
    
    def getAllDoctors(self):
        sql ="select * from doctor order by 3"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        datos = [] #creamos una lista para almacenar los departamentos
    
        for row in cursor: #recorremos el cursor de datos
            doc=model.Doctor()
            doc.hospital=row[0]
            doc.numero=row[1]
            doc.apellido=row[2]  
            doc.especialidad=row[3]
            doc.salario=row[4]
            datos.append(doc) 
        cursor.close()
        return datos
    
    def createDoctors(self, hospital, numero, apellido, especialidad, salario):
        sql = "insert into doctor values (:p1, :p2, :p3, :p4, :p5)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (hospital, numero, apellido, especialidad, salario))
        registros = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registros
    
    def updateDoctor(self, hospital, apellido, especialidad, salario, numero):
        sql = "update doctor set hospital_cod=:p1, apellido=:p2, especialidad=:p3, salario=:p4 where doctor_no=:p5"
        cursor = self.connection.cursor()
        cursor.execute(sql, (hospital, apellido, especialidad, salario, numero))
        registros= cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registros 
    
    def deleteDoctor(self, numero):
        sql = "delete from doctor where doctor_no=:p1"
        cursor = self.connection.cursor()
        cursor.execute(sql, (numero,) )
        registros= cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registros