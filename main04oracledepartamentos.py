from services import service04oracledepartamentos as service
from models import departamento

print("----SERVICIO ORACLE DEPARTAMENTOS")
#NECESITAMOS UNA OBJETO DE TIPO SERVICIO PARA TRABAJAR
servicio = service.ServiceOracleDepartamentos()
print("1.- Insertar departamento")
print("2.- Buscar departamento")
print("3.- Eliminar departamento")
print("4.- Modificar departamento")
print("5.- Mostrar departamentos")
print("Seleccione una opción")
opcion = int(input())
if (opcion == 1):
    print("Insertar departamento")
    print("Id del departamento")
    numero = int(input())
    print("Nombre del departamento")
    nombre = input()
    print("Localidad")
    localidad = input()
    afectados = servicio.insertarDepartamento(numero,nombre, localidad)
    print(f"Departamentos insertados: {afectados}")
elif (opcion == 2):
    print("Buscador de departamentos por ID")
    print("Introduzca el id del departamento")
    iddept = int(input())
    #DECLARAMOS UNA VARIABLE PARA GUARDAR EL DEPARTAMENTO
    dept = servicio.buscarDepartamentoId(iddept)
    print(f"{dept.numero}, {dept.nombre}, {dept.localidad}")
elif (opcion == 3):
    print("Buscador de departamentos por ID")
    print("Introduzca el numero del departamento que desea eliminar")
    numero = int(input())
    registros = servicio.borrarDepartamento(numero)
    print(f"Departamento elimindado: {registros}")
elif (opcion == 4):
    print("Buscador de departamentos por ID")
    print("Introduzca el número del departamento que desea modificar")
    numero = int(input())
    print("Introduzca el nombre del nuevo departamento")
    nombre = input()
    print("Introduzca el nombre de la nueva localidad")
    localidad = input()
    registros = servicio.modificarDepartamento(numero, nombre, localidad)
    print(f"Ha sido modificado {registros} departamento")
elif (opcion == 5):
    datos = servicio.getAllDept()
    print("Aqui la lista de departamentos:")
    print("============================================")
    for dept in datos:
        print(f"{dept.numero}, {dept.nombre}, {dept.localidad}")
    
print("Fin de programa")