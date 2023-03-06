
for liczba in range (100,1000):
    pierwsza = True
    for a in range(2,liczba):
        if liczba%a == 0:
            pierwsza = False
            break
        
    if pierwsza:
        print(liczba)
