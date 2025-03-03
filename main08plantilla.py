#from services import service08_oracle_plantilla as service
#from services import service08_sqlserver_plantilla as service
from services import service08_mysql_plantilla as service
from models.plantilla import Plantilla

print("probando serviciossss varios de BBDD")
servicio = service.ServicePlantilla()


print ("Lista de todos los empleados de la plantilla")
print("=============================================================")
empleados = servicio.getPlantilla()
for emp in empleados:
    print(f"Hospital: {emp.hospital},   Salario: {emp.salario}, Apellido: {emp.apellido},   Oficio: {emp.funcion}")

print("=============================================================")


print("Cambio de Salario:")
hospnum=int(input())
print("Número de Hospital:")
incremento=input()

hospupdate = servicio.updatePlantilla(incremento, hospnum)
print(f"Hospitaleses Modificados: {hospupdate}")