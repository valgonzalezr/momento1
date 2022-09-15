#Construir un programa que permita ingresar N (cantidad digitada por elusuario) números enteros y cuente cuantos múltiplos de 2 y de 3 fueron ingresados

numeros=[]
multiplosDe2=[]
multiplosDe3=[]

longitudLista=int(input("Digite cantidad de numeros a ingresar: "))
for i in range(longitudLista):
    numero=int(input('Ingrese un numero: '))
    numeros.append(numero)

for numero in numeros:
    if(numero%2==0):
        multiplosDe2.append(numero)
print(f'La cantidad de Multiplos de 2 ingresados son: {len(multiplosDe2)}')
for numero in numeros:
    if(numero%3==0):
        multiplosDe3.append(numero)
print(f'La cantidad de Multiplos de 3 ingresados son: {len(multiplosDe3)}')
#print(len(multiplosDe2yDe3))

