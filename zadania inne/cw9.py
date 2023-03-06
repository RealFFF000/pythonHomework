liczba = str(input("podaj liczbe do odwrocenia "))

lista = []
for a in liczba:
    lista.append(a)

for b in range(1,lista.__len__()+1):
    print(lista[lista.__len__()-b],end="")
