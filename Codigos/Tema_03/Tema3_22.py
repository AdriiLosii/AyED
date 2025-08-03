# Tema3_22
def vueltasRecB(listValMonedas, vueltas, resultconoc):
    #print(vueltas)
    minMonedas = vueltas
    if vueltas in listValMonedas:
        resultconoc[vueltas] = 1
        return 1
    elif resultconoc[vueltas] > 0:
        return resultconoc[vueltas]
    else:
        for i in [m for m in listValMonedas if m <= vueltas]:
            numeroMonedas = 1 + \
                vueltasRecB(listValMonedas, vueltas-i, resultconoc)
            if numeroMonedas < minMonedas:
                minMonedas = numeroMonedas
                resultconoc[vueltas] = minMonedas
    return minMonedas


print(vueltasRecB([1, 5, 10, 25, 50], 63, [0]*64))
#print(vueltasRecB([1, 5, 10, 21, 50], 63, [0]*64))
