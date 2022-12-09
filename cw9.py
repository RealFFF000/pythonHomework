h = int(input("podaj godzinę startu: "))
m = int(input("podaj minutę startu: "))
d = int(input("podaj czas trwania w minutach: "))

h = h + (m + d) // 60
m = (m + d) % 60
h = h % 24

print("godzina to ", h, ":", m, sep="")