liczba1 = float(input("podaj liczbe 1\n"))
liczba2 = float(input("podaj liczbe 2\n"))
liczba3 = float(input("podaj liczbe 3\n"))

if liczba1<liczba2:
    if liczba2<liczba3:
        print("liczby zostały podane w porządku rosnącym")
    else:
        print("liczby nie zostały podane w porzadku rosnącym")
else:
    print("liczby nie zostaly podane w porzadku rosnacym")

