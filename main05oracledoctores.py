from services import service05oracledoctores as service
from models import doctor as model

print("----CRUD DOCTORES-------")
#NECESITAMOS UNA OBJETO DE TIPO SERVICIO PARA TRABAJAR
servicio = service.ServiceOracleDoctores()
print("Seleccione una opción")
print("1.- Mostrar Doctores")
print("2.- Insertar un nuevo Doctor")
print("3.- Modificar Doctor")
print("4.- Eliminar Doctor")
opcion = int(input())
if (opcion==1):
    doctores= servicio.getAllDoctors()
    for doc in doctores:
        print (f"Dr. {doc.apellido}, Especialidad: {doc.especialidad}")
        
elif (opcion==2):
    print ("Introduzca el número de hospital del nuevo doctor")
    hosp = int(input())
    print ("Introduzca el número  del nuevo doctor")
    doc = int(input())
    print ("Introduzca el apellido")
    apell = input()
    print ("Introduzca la especialidad")
    espe = input()
    print ("Introduzca el salario")
    sal = int(input())
    nuevodoc = servicio.createDoctors(hosp, doc, apell, espe, sal)
    print(f"Doctores insertados: {nuevodoc}")
    
elif (opcion==3):
    print ("Introduzca el número del doctor que desea mofificar")
    num = int(input())
    print ("Introduzca el número  del hospital")
    hosp = int(input())
    print ("Introduzca el apellido")
    apell = input()
    print ("Introduzca la especialidad")
    espe = input()
    print ("Introduzca el salario")
    sal = int(input())
    docmod = servicio.updateDoctor(hosp, apell, espe, sal, num)
    print(f"Doctores Modificados: {docmod}")
    
elif (opcion==4):
    print ("Introduzca el número del doctor que desea borrar")
    num = int(input())
    docborrado = servicio.deleteDoctor(num)
    print(f"Doctores Borrados: {docborrado}")