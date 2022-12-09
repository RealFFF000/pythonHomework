strzałka = (["    *    ", "   * *   ", "  *   *  ", " *     * ", "***   ***", "  *   *  ", "  *   *  ", "  *****  "])
#for i in range(strzałka.__len__()):
#    print(strzałka[i])

def printart(x,thicc,copies):
    
    for i in range(x.__len__()):
        x[i]=(x[i]+" ")*copies
        for thiccx in range(thicc):
            for a in range(x[i].__len__()):
                    for thiccy in range(thicc):
                        print(x[i][a], end="")
            print("")
        
printart(strzałka,2,1)

# ad 4,5,6,7
# no interpreter głupieje bo dostaje nieznane mu komendy