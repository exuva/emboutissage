import math
def calc(D, fD,nbP):
    print('Pass nb: ', nbP)
    pC = round(pB(fD, nbP), 2)
    dP = round(D * pC, 2)
    print('Coefredu: ', pC)
    print("Dia-poin / passe:", dP)
    sFlan = round(math.pi * (fD / 2) ** 2, 2)
    sPoin = round(math.pi * (dP / 2) ** 2, 2)
    sLat = round(sFlan - sPoin, 2)
    pdP = round(math.pi * dP, 2)
    hdP = round(sLat / pdP, 2)
    print('s-f:', sFlan)
    print('s-p:', sPoin)
    print('s-l:', sLat)
    print('perim-poincon:', pdP)
    print('h-passe:', hdP)
    print('---------')
    return dP

def recur(d, objectif):
    inc = 1
    nextD = calc(d, d, inc)
    while nextD > objectif:
        inc = inc + 1
        nextD = calc(nextD, d, inc)
    return

def pB(a, nbP):
    b = ((1 / a) * (100 / a))
    if nbP == 1:
        return pB1(b)
    if nbP == 2:
        return pB2(b)
    if nbP == 3:
        return pB3(b)
    if nbP == 4:
        return pB4(b)
    return pB5(b)

def pB1(b):
    if b < 0.115:
        return 0.63
    if b < 0.275:
        return 0.6
    if b < 0.45:
        return 0.58
    if b < 0.8:
        return 0.55
    if b < 1.25:
        return 0.53
    if b < 1.75:
        return 0.5
    return 0.48

def pB2(b):
    if b < 0.115:
        return 0.82
    if b < 0.275:
        return 0.80
    if b < 0.45:
        return 0.79
    if b < 0.8:
        return 0.78
    if b < 1.25:
        return 0.76
    if b < 1.75:
        return 0.75
    return 0.73

def pB3(b):
    if b < 0.115:
        return 0.84
    if b < 0.275:
        return 0.82
    if b < 0.45:
        return 0.81
    if b < 0.8:
        return 0.80
    if b < 1.25:
        return 0.79
    if b < 1.75:
        return 0.78
    return 0.76

def pB4(b):
    if b < 0.115:
        return 0.86
    if b < 0.275:
        return 0.85
    if b < 0.45:
        return 0.83
    if b < 0.8:
        return 0.82
    if b < 1.25:
        return 0.81
    if b < 1.75:
        return 0.80
    return 0.78

def pB5(b):
    if b < 0.115:
        return 0.88
    if b < 0.275:
        return 0.87
    if b < 0.45:
        return 0.86
    if b < 0.8:
        return 0.85
    if b < 1.25:
        return 0.84
    if b < 1.75:
        return 0.82
    return 0.80

def main():
    print('Calcul flan poincon(D)')
    print ('rappel: formule Developper :')
    print (' math.sqrt(dTotal ** 2 + 4 * dTotal * hTotal)')
    d = float(input("dia. inter:"))
    h = float(input("Haut. exter:"))
    e = float(input("ep. mat. :"))
    dTotal = d + e
    hTotal = h - (0.5 * e)
    D = round(math.sqrt(dTotal ** 2 + 4 * dTotal * hTotal), 2)
    print('D: ', D, '%')
    print('------')
    recur(D, d)
    return

main()