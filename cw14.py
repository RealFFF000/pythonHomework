liczba1 = input("podaj liczbe 1\n")
liczba2 = input("podaj liczbe 2\n")
liczba3 = input("podaj liczbe 3\n")

if liczba1 == liczba2:
    czy = True
elif liczba1 == liczba3:
    czy = True
elif liczba2 == liczba3:
    czy = True
else:
    czy = False
print(czy)