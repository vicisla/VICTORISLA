listaProductos = []
dinero = 0


while True:
    opcion = int(input('Eliga una opcion: '))
    print(opcion)
    if opcion == 1:
        cantidadProductos = int(input('Ingrese la cantidad de productos'))
        while cantidadProductos < 0:
            cantidadProductos = int(input('Ingrese la cantidad de productos'))

        for i in range(cantidadProductos):
            producto = input(f'Nombre del producto {i+1}: ')

            precio = int(input(f'Precio del producto {i+1}: '))
            while precio < 0:
                precio = input("El precio debe ser un valor positivo: ")

            stock = int(input('Cuanto de ese producto ingresa: '))
            while stock < 0:
                stock = input("El stock debe ser un valor positivo: ")

            producto = [producto, stock,precio]

            listaProductos.append((producto))  
    elif opcion == 2:
        for i in range(len(listaProductos)):
            print(f'{i + 1}) {listaProductos[i][0]}')

        eleccion = int(input("Ingrese el numero del producto que quiere comprar: ")) - 1
        while True:
            try:
                eleccion = producto[eleccion]
                break
            except:
                eleccion = int(input("Ingrese el numero del producto que quiere comprar: ")) - 1


        cantidad = int(input("Cuanto va a comprar de ese producto: "))
        while cantidad < 0:
            cantidad = int(input("Cuanto va a comprar de ese producto: "))
            while cantidad > eleccion[1]:
                cantidad = int(input("Cuanto va a comprar de ese producto: "))
        
        dinero += eleccion[2] * cantidad
        eleccion[1] += -cantidad

        print("Gracias por su compra")

    elif opcion == 3:
        print(f"s/{dinero}")
    else:
        break