import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,  # use operator.div for Python 2
    '%': operator.mod,
    '^': operator.pow,
}

stay = False
print("Bienvenue sur les calculs algébriques")
print("Pour quitter ce menu, tapez exit")
print("Veuillez espacez tous vos calculs  : ")
print("( 4 + 2 ) * 2 + 2 / 2")
print("Lorsque vous factorisez, mettez à gauche, comme ceci :")
print("( 2 + 4 * 2 ) * 4 ")


def priorite(liste):
    cpt = 0
    cpt_parenthese = 0
    for i in range(len(liste)-cpt):
        if liste[i-cpt] == "*" or liste[i-cpt] == "/" or liste[i-cpt] == "%" or liste[i-cpt] == "^":
            if liste[i - cpt - 1] == ")":
                while liste[i - cpt - cpt_parenthese] != "(":
                    cpt_parenthese += 1
                parenthese(i-cpt - cpt_parenthese, cpt_parenthese, liste, cpt)
                cpt += cpt_parenthese - 1
            elif liste[i - cpt + 1] == "(":
                while liste[i - cpt + cpt_parenthese] != ")":
                    cpt_parenthese += 1
                parenthese(i-cpt + 1, cpt_parenthese, liste, cpt)
                cpt += cpt_parenthese - 1
            res = operation(i-1-cpt, i+1-cpt, liste)
            liste.pop(i-cpt)
            liste.pop(i-cpt)
            liste[i-1-cpt] = res
            cpt += 2


def operation(prem, deux, liste):
    L = liste[prem:deux+1]
    if liste[prem+1] == "^":
        print("=", end=" ")
        for i in range(int(liste[deux]) - 1):
            print(liste[prem], "*", end=" ")
        print(liste[prem])
    L[0] = float(L[0])
    L[2] = float(L[2])

    return ops[L[1]](L[0], L[2])


def parenthese(prem, cpt_parenthese, liste, cpt):
    while len(calcul[prem + 1: prem + cpt_parenthese - 1]) > 3:
        res = operation(prem + 1, prem + 3, liste)
        calcul.pop(prem + 2)
        calcul.pop(prem + 2)
        calcul[prem + 1] = res
        cpt += 2
    res2 = operation(prem + 1, prem + 3, liste)
    calcul.pop(prem + 2)
    calcul.pop(prem + 2)
    calcul[prem + 1] = res2
    calcul.pop(prem)
    calcul.pop(prem + 1)



while exit:
    calcul = input("Quelle calcul voulez vous faire : ")

    if calcul == "exit":
        exit = False
    cpt_pat = 0
    for j in range(len(calcul)):
        if calcul[j] == "(" or calcul[j] == ")":
            cpt_pat += 1
    print(calcul)
    calcul = calcul.split(" ")

    L = []
    priorite(calcul)
    cpt_parenthese = 0
    cpt = 0
    for i in range(len(calcul) - cpt_pat):
        if calcul[i-cpt] == "(":
            while calcul[i-cpt + cpt_parenthese] != ")":
                cpt_parenthese += 1
            parenthese(i-cpt, cpt_parenthese, calcul, cpt)
            cpt += cpt_parenthese - 2



        """
            while len(calcul[i-cpt + 1 : i-cpt + cpt_parenthese - 1]) > 3:
                print("")
            res = operation_priorite(i-cpt + 1, i-cpt + cpt_parenthese - 1, calcul)
            del calcul[i-cpt+1:i-cpt + cpt_parenthese + 1]
            calcul[i-cpt] = res
            cpt += cpt_parenthese - 2

            print(calcul)
        """



    """
    while cpt < len(calcul) // 2:
        if calcul[1 + (2 * cpt)] == "*" or calcul[1 + (2 * cpt)] == "/" or calcul[1 + (2 * cpt)] == "%" or calcul[1 + (2 * cpt)] == "^":
            L.append(calcul[(2 * cpt)])
            L.append(calcul[1 + (2 * cpt)])
            L.append(calcul[2 + (2 * cpt)])
            L[0], L[2] = float(L[0]), float(L[2])
            L[0] = ops[L[1]](L[0], L[2])
            calcul[(2 * cpt)] = L[0]
            calcul.pop(1 + (2 * cpt))
            calcul.pop(1 + (2 * cpt))
            L = []
            cpt += 1
        elif calcul[1 + (2 * cpt)] == "+" or calcul[1 + (2 * cpt)] == "-":
    """

    for i in range(len(calcul) // 2):
        try:
            calcul[0] = calcul[0].replace(",", ".")
            calcul[2] = calcul[2].replace(",", ".")
        except:
            pass
        calcul[0], calcul[2] = float(calcul[0]), float(calcul[2])
        calcul[0] = ops[calcul[1]](calcul[0], calcul[2])
        calcul.remove(calcul[1])
        calcul.remove(calcul[1])
    print("= ", calcul[0])


"""
Travail restant :
- Parenthèse a droite du calcul
"""