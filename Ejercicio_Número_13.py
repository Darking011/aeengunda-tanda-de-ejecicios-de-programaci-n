numeros=[[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12],
         [13,14,15,16]]
cont=0
suma=0
cont2=3
suma2=0
for x in range(0,4):
    suma2=numeros[x][cont2]+suma2
    cont2=cont2-1
    suma=numeros[x][cont]+suma
    cont=cont+1
    print(cont2,suma2)
print("la suma de la contradiagonal es: ", suma2)
print("la suma de la diagonal principal es: ", suma)
