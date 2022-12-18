a = int(input("podaj mniejszą liczbe "))
b = int(input("podaj większą liczbe "))

for c in range(a,b+1):
    print(c,end=" ")
for c in range(b,a-1,-1):
    print(c,end=" ")