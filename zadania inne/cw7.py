liczba = int(input("podaj liczbe "))
a = 0
while True:
    if 2**a > liczba:
        break
    a+=1
print("najwyższa potęga liczby 2 nie większa od podanej liczby to:",a-1)