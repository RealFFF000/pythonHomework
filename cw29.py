def pole(a,b,c):
    if (a+b>c) and (c+b>a) and (a+c>b):
        p = (a + b + c)/2
        S = float((p*(p-a)*(p-b)*(p-c))**0.5)
        print("Pole trójkąta to: "+str(S))
    else:
        print("ten trojkat nie istnieje")

pole(input(),input(),input())