from ast import Break
import funtions
from src.conexion_mysql import DAO

#SE CREA FUNCION PARA MENU PRINCIPAL#
def menuPrincipal():

    print("========== MENU PRINCIPAL ==========")
    print("1 - Productos")
    print("2 - Clientes")
    print("3 - Empleados")
    print("4 - Facturas")
    print("5 - Salir")
    print("====================================")
    opcion = int(input("Selecione una opcion: "))

    if opcion == 1:
        print("1 - Lista Productos")
        print("2 - Agregar Producto")
        print("3 - Borrar Producto")
        print("4 - Buscar Producto")
        print("5 - Regresar menu principal")
        print("====================================")
        
        def ejecutarOpcion(opcionProducto):
            opcionProducto = int(input("Selecione una opcion: "))
            dao = DAO()
            
            if opcionProducto == 1:
                try:
                    products = dao.listarProducts()
                    if len(products) > 0:
                        funtions.listarProducts(products)
                    else:
                        print("No se encontraron productos...")
                except:
                    print("Ocurrio un error...")
            
            elif opcionProducto == 2:
                print("Nuevo Producto")
                products = funtions.agregarProducto()
                try:
                    dao.nuevoProducto(products)
                except:
                    print("Ocurrio un error...")

            elif opcionProducto == 3:
                
                try:
                    products = dao.listarProducts()
                    if len(products) > 0:
                        funtions.listarProducts(products)
                        eliminarProducto = funtions.datosEliminarProducto(products)
                        if (eliminarProducto == ""):
                            dao.deleteProducto(eliminarProducto)
                        else:
                            print("Producto no encontrado...")
                    else:
                        print("No se encontraron productos...\n")

                except:
                    print("Ocurrio un error...")

            elif opcionProducto == 4:
                pass
            elif opcionProducto == 5:
                return menuPrincipal
                
            elif opcionProducto < 1 or opcionProducto > 5:
                print(" ")
                print("Opcion incorrecta, ingrese nuevamente...")
                print(" ")

    elif opcion == 2:
        print("1 - Lista Clientes")
        print("2 - Agregar Cliente")
        print("3 - Borrar Cliente")
        print("4 - Buscar Cliente")
        print("5 - Regresar menu principal")
        print("====================================")

        def ejecutarOpcion(opcionCliente):
            opcionCliente = int(input("Selecione una opcion: "))
            dao = DAO()
            if opcionCliente == 1:
                try:
                    clients = dao.listarClients()
                    if len(clients) > 0:
                        funtions.listarClients(clients)
                    else:
                        print("No se encontraron clientes...")
                except:
                    print("Ocurrio un error...")
            
            elif opcionCliente == 2:
                print("Nuevo Cliente")
                clients = funtions.colocarDatosClientes()
                try:
                    dao.nuevoCliente(clients)
                except:
                    print("Ocurrio un error...")
            
            elif opcionCliente == 3:
                try:
                    clients = dao.listarClients()
                    if len(clients) > 0:
                        funtions.listarProducts(clients)
                        eliminarCliente = funtions.datosEliminarCliente(clients)
                        if (eliminarCliente == ""):
                            dao.deleteCliente(eliminarCliente)
                        else:
                            print("Producto no encontrado...")
                    else:
                        print("No se encontraron productos...\n")

                except:
                    print("Ocurrio un error...")
            elif opcionCliente == 4:
                pass
            elif opcionCliente == 5:
                return menuPrincipal
                
            elif opcionCliente < 1 or opcionCliente > 5:
                print(" ")
                print("Opcion incorrecta, ingrese nuevamente...")
                print(" ")

    elif opcion == 3:
        print("1 - Lista Empleados")
        print("2 - Agregar Empleado")
        print("3 - Borrar Empleado")
        print("4 - Buscar Empleado")
        print("5 - Regresar menu principal")
        print("====================================")
        
        def ejecutarOpcion(opcionEmpleado):
            opcionEmpleado = int(input("Selecione una opcion: "))
            dao = DAO()
            
            if opcionEmpleado == 1:
                try:
                    employees = dao.listarEmployees()
                    if len(employees) > 0:
                        funtions.verEmployees(employees)
                    else:
                        print("No se encontraron empleados...")
                except:
                    print("Ocurrio un error...")
            
            elif opcionEmpleado == 2:
                print("Nuevo Empleado")
                employees = funtions.agregarEmpleado()
                try:
                    dao.nuevoEmpleado(employees)
                except:
                    print("Ocurrio un error...")

            elif opcionEmpleado == 3:
                pass
            elif opcionEmpleado == 4:
                pass
            elif opcionEmpleado == 5:
                return menuPrincipal
                
            elif opcionEmpleado < 1 or opcionEmpleado > 5:
                print(" ")
                print("Opcion incorrecta, ingrese nuevamente...")
                print(" ")

    elif opcion == 4:
        print("1 - Lista Facturas")
        print("2 - Nueva Factura")
        print("3 - Borrar Factura")
        print("4 - Buscar Factura")
        print("5 - Regresar menu principal")
        print("====================================")
        opcionFactura = int(input("Selecione una opcion: "))
        
        if opcionFactura == 1:
            pass
        elif opcionFactura == 2:
            pass
        elif opcionFactura == 3:
            pass
        elif opcionFactura == 4:
            pass
        elif opcionFactura == 5:
            return menuPrincipal
                
        elif opcionFactura < 1 or opcionFactura > 5:
            print(" ")
            print("Opcion incorrecta, ingrese nuevamente...")
            print(" ")
        
    elif opcion == 5:
        print(" ")
        print("¡Gracias por usar este Sistema!")
        print(" ")
        

    elif opcion < 1 or opcion > 5:
        print(" ")
        print("Opcion incorrecta, ingrese nuevamente...")
        print(" ")

    else: 
        opcionCorrecta = True
        ejecutarOpcion(opcion)

menuPrincipal()
