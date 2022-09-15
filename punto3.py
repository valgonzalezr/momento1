#Construir un programa para ir de compras en un supermercado que permita la construcción del siguiente 
print("")
print("*****************************     MENU    **************************************")
print("")
print("Digitar 1 para recibir {código, nombre, precio} de un producto")
print("Digitar 2 para mostrar todos los productos registrados")
print("Digitar 3 para permitir buscar por código un producto y editar el precio de este")
print("Digitar 4 para permitir buscar por código un producto y eliminar el producto")
print("Digitar 0 para SALIR")
print("")

productos=[]

opcion=1

while(opcion != 0):
    opcion=int(input("Digite una opcion: "))
    print("")

    if (opcion == 0):
        print("SALI DEL PROGRAMA")

    elif(opcion == 1):
        diccionarioProducto={}
        diccionarioProducto['codigo']=int(input('Ingresar codigo del producto: '))
        diccionarioProducto['nombre']=(input('Ingresar nombre del producto : '))
        diccionarioProducto['precio']=float(input('Ingresar el precio del producto: $'))
        productos.append(diccionarioProducto)
        print("")

    elif(opcion == 2):
        for i in productos:
            print(f"codigo: {i['codigo']}")
            print(f"nombre: {i['nombre']}")
            print(f"precio: ${i['precio']}")
            print("")

    elif(opcion == 3):
            buscarCodigo= int(input("Ingrese el codigo del Producto a buscar: "))  
            localizado=False 
            for i in productos:
                if i['codigo']==buscarCodigo:
                    precio=float(input(f"Digitar el precio nuevo del {i['nombre']} : $"))
                    i['precio']=precio
                    print(f"Precio modificado")
                    print(f"codigo: {i['codigo']}")
                    print(f"nombre: {i['nombre']}")
                    print(f"precio: ${i['precio']}")
                    print("")
                    localizado=True
            if not localizado:                    
                print(f'El código {buscarCodigo} NO existe')

    elif(opcion == 4):
            buscarCodigo= int(input("Ingrese el codigo del Producto que se va a eliminar : ")) 
            localizado=False
            for i in productos:
                if i['codigo'] == buscarCodigo:
                    print(f"codigo: {i['codigo']}")
                    print(f"nombre: {i['nombre']}")
                    print(f"precio: ${i['precio']}")
                    print("")
                    eliminado=i['nombre']
                    productos.pop(productos.index(i))
                    print(f"Se elimina el producto {eliminado}") 
                                    
            if not eliminado:
                    print(f'El código {buscarCodigo} NO existe')



    else:
        print("Digite un numero entre 0 y 4") 