lista_productos = []

opcion = ""
while True:
    print("Menú de opciones")
    print("1. Alta de producto")
    print("2. Listar producto")
    print("3. Salir")
    opcion = input("Ingrese la opción que desee: ").lower()


    if opcion == "1":
        """Alta"""
        nuevo_producto = []
        nombre_producto = input("Nombre del producto: ")
        cantidad_producto = int(input("Cantidad: "))
        
        nuevo_producto = [nombre_producto, cantidad_producto]

        lista_productos.append(nuevo_producto)

    elif opcion == "2":
        # Listar productos
        if len(lista_productos) == 0:
            print("No hay productos en la lista.")
        else:
            for producto in lista_productos:
                print(f"Producto: {producto[0]} - Cantidad: {producto[1]}")

    elif opcion == "3":
        break
    else:
        print("Opción no válida. Ingrese 1, 2 o 3")