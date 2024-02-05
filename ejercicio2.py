empleados = []
i = 1
def agregar_empleado(i):
    nombreEmpleado = input('Ingrese el nombre del empleado: ')
    cargoEmpleado = input("Ingrese el cargo del empleado: ")
    salarioEmpleado=input("Ingrese el salario del empleado")
    empleados.append([i, nombreEmpleado, cargoEmpleado, salarioEmpleado])
    return  1

def ver_empleados():
    for empleado in empleados:
        print(f'Id: {empleado[0]}, Nombre: {empleado[1]}, Cargo: {empleado[2]}')

def eliminar_empleado():
    idEliminado = int(input("Elige el id del empleado que deseas eliminar: "))
    for j in range(len(empleados)):
        if empleados[j][0] == idEliminado:
            del empleados[j]
            break

def mostrar_menu():
    print("""
1. Agregar Empleado
2. Ver Empleado
3. Despedir Empleado
4. Salir""")

while True:
    mostrar_menu()
    opcion = int(input("Elige una Opcion: "))

    if opcion == 1:
        i += agregar_empleado(i)
    elif opcion == 2:
        ver_empleados()
    elif opcion == 3:
        eliminar_empleado()
    elif opcion == 4:
        break
    else:
        pass