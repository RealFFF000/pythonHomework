#Znajdź jak największą liczbę mniejszą od 2 000 000 000, która jest iloczynem dwóch liczb pierwszych.
def skladnikiPierwsze(n):
    i = 2
    skladniki = []
    while i**2 <= n:
        if n%i:
            i+=1
        else:
            n = n//i
            skladniki.append(i)
    if n > 1:
        skladniki.append(n)
    return skladniki

liczba = 2000000000
while True:
    for a in range(liczba, 0, -1):
        skladniki = skladnikiPierwsze(a)
        if skladniki.__len__() == 2:
            print(skladniki[0]*skladniki[1],"=",skladniki[0],"*",skladniki[1])
            czekator = input("wciśnij enter aby poznać kolejną liczbę")
