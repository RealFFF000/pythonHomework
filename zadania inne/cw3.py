liczba = str(input("podaj liczbę w systemie binarnym "))
suma = 0
iteracja = 1
for a in liczba:
    suma += int(a)*(2**(liczba.__len__()-iteracja))
    iteracja+=1
print(suma)