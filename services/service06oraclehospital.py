import oracledb
from models import hospital as model

class ServiceOracleHospitales:
    def __init__(self): 
        self.connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
        
    def listaHospitales(self):
        sql = "select * from hospital order by 2"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        datos=[]
        
        for row in cursor:
            hosp=model.Hospital()
            hosp.numero=row[0]
            hosp.nombre=row[1]
            hosp.direccion[2]
            hosp.telefono[3]
            hosp.camas[4]
            datos.append(hosp)
        cursor.close()
        return datos