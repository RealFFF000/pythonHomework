#Znajdź jak największą liczbę mniejszą od 2 000 000 000, która jest iloczynem dwóch liczb pierwszych.
def czypierwsza(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False 
    return True
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
        if skladnikiPierwsze(a).__len__() == 2:
            print(a,skladnikiPierwsze(a))
