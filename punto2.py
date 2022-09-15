#Leer el nombre de 10 frutas para preparar un salpicón; el programa debe permitir mostrar las 10 frutas ingresadas al mismo tiempo en sentido inverso al ingresado
frutas=[]

for i in range(0,10,1):
    fruta=input("Ingrese una fruta:")

    frutas.append(fruta)
print(f'Imprima frutas en orden de Lista {frutas}')
frutas.reverse()
print(f'Imprima frutas en sentido inverso a la Lista {frutas}')