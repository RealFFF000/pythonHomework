a = float(input("podaj liczbe a\n"))
b = float(input("podaj liczbe b\n"))
c = float(input("podaj liczbe c\n"))

if (a+b>c) and (c+b>a) and (a+c>b):
    p = (a + b + c)/2
    S = float((p*(p-a)*(p-b)*(p-c))**0.5)
    print("Pole trójkąta to: "+str(S))
else:
    print("ten trojkat nie istnieje")