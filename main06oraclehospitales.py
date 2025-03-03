from services import service06oraclehospital as service
from models import hospital as model
 
print ("------------ CRUD HOSPITALES -----------")
servicio= service.ServiceOracleHospitales()
print("Seleccione una opción")
print("1.- Listar Hospitales")
print("2.- Insertar un Hospital nuevo")
print("3.- Modificar Hospital")
print("4.- Eliminar Hospital")
opcion = int(input())

if (opcion==1):
    hospitales = servicio.listaHospitales()
    for hosp in hospitales:
        print(f"Hospital {}")