#Funcion para listar productos
def listarProducts(products):
    print("\nProductos: \n")
    contador = 1
    for cur in products:
        datos="{0}. idProducts: {1} | nameProduct: {2} ({3} price)"
        print(datos.format(contador, cur[0], cur[1], cur[2]))
        contador = contador + 1
    print(" ")

#Funcion para ver Clientes. ( FALTA ARREGLAR )
def listarClients(clients):
    print("\nClientes: \n")
    contador = 1
    for cur in clients:
        datos="{0}. ID: {1} | Nombre: {2} {3} | DNI: {4}"
        print(datos.format(contador, cur[0], cur[1], cur[2], cur[3], cur[4]))
        contador = contador + 1
    print(" ")

#Funcion para ver Empleados ( FALTA ARREGLAR )
def verEmployees(employees):
    print("\nEmpleados: \n")
    contador = 1
    for cur in employees:
        datos="{0}. ID: {1} | Nombre: {2} {3} | DNI {4}"
        print(datos.format(contador, cur[0], cur[1], cur[2], cur[3], cur[4]))
        contador = contador + 1
    print(" ")

#Funcion para crear cliente
def colocarDatosClientes():
    names = input("Ingrese Nombres: ")
    surnames = input("Ingrese Apellidos: ")

    dniCorrecto = False
    while(not dniCorrecto):
        dni = input("Ingrese DNI sin puntos: ")
        if len(dni) < 8 or dni.isnumeric():
            dniCorrecto = True
            dni = int(dni)
        else:
            print("DNI debe tener como maximo 8 digitos y sin puntos.")

    direction = input("Ingrese Direccion: ")
    
    phone = input("Ingrese Telefono (SIN SEPARACIONES, NI(-,.,+,#)): ")
    if len(phone) > 8 or len(phone) < 12: 
        if phone.isnumeric():
            phone = int(phone)
        else:
            print('Telefono incorrecto: Debe ser solamente numerico.')
    else:
        print("El numero de telefono no es valido")
    
    email = input("Ingrese E-mail: ")

    clients = (names, surnames, dni, direction, phone, email)
    return clients

#Funcion para crear empleado
def agregarEmpleado():
    nameEmployee = input("Ingrese Nombre Empleado: ")
    surnameEmployee = input("Ingrese Apellidos Empleado: ")

    dniEmpleado = False
    while(not dniEmpleado):
        dniEmployee = input("Ingrese DNI sin puntos: ")
        if len(dniEmployee) < 8 or dniEmployee.isnumeric():
            dniEmpleado = True
            dniEmployee = int(dniEmployee)
        else:
            print("DNI debe tener como maximo 8 digitos y sin puntos.")
    
    phoneEmployee = input("Ingrese Telefono (SIN SEPARACIONES, NI(-,.,+,#)): ")
    if len(phoneEmployee) > 8 or len(phoneEmployee) < 12: 
            if phoneEmployee.isnumeric():
                phoneEmployee = int(phoneEmployee)
            else:
                print('Telefono incorrecto: Debe ser solamente numerico.')
    else:
        print("El numero de telefono no es valido")
    
    employees = (nameEmployee, surnameEmployee, dniEmployee, phoneEmployee)
    return employees

#Funcion para agregar Producto.
def agregarProducto():

    idProducts = input("Ingrese codigo del Producto ")

    nameProduct = input("Ingrese Nombre Producto ")
    
    stockProducto = False
    while(not stockProducto):
        stock = input("Ingrese cantidad de productos agregados: ")
        if stock.isnumeric():
            stockProducto = True
            stock = int(stock)
        else:
            print("Ingrese la cantidad en numeros.")
    
    precioProducto = False
    while(not precioProducto):
        price = input("Ingrese el precio del producto agregados: ")
        if price.isnumeric():
            precioProducto = True
            price = int(price)
        else:
            print("Ingrese el precio en numeros.")
    
    products = (idProducts, nameProduct, stock, price)
    return products

#Funcion para eliminar productos
def datosEliminarProducto(products):
    listarProducts(products)
    
    existeId = False
    eliminarProducto = input("Ingrese el ID del producto a eliminar: ")
    for cur in products:
        if cur[0] == int(eliminarProducto):
            existeId = True
            break
    if not existeId:
        existeId = ""
    
    return int(eliminarProducto)

#Funcion para eliminar cliente
def datosEliminarCliente(clients):
    listarClients(clients)
    
    existeDni = False
    eliminarCLiente = input("Ingrese el DNI del cliente a eliminar: ")
    for cur in clients:
        if cur[3] == int(eliminarCLiente):
            existeDni = True
            break
    if not existeDni:
        existeDni = ""
    
    return int(eliminarCLiente)

    #Funcion para eliminar empleado
def datosEliminarEmpleado(employees):
    verEmployees(employees)
    
    existeDniEmpleado = False
    eliminarEmpleado = input("Ingrese el DNI del empleado a eliminar: ")
    for cur in employees:
        print(cur)
        if cur[3] == int(eliminarEmpleado):
            existeDniEmpleado = True
            break
    if not existeDniEmpleado:
        existeDniEmpleado = ""
    
    return int(eliminarEmpleado)