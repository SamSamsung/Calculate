def repere_orthonorme(n, fonction):
    L = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        y = (n//2) - i
        for j in range(n):
            x = (n//2) - j
            try:
                if y == eval(fonction):
                    L[i][j] = 3
            except ZeroDivisionError:
                L[i][j] = 0
            if x == 0:
                L[i][j] = 2
            elif y == 0:
                L[i][j] = 1
    return L


def affichage(L):
    for i in range(len(L)):
        for j in range(len(L[i])):
            if L[i][j] == 0:
                print(" ", end=" ")
            elif L[i][j] == 1:
                print("-", end=" ")
            elif L[i][j] == 2:
                print("|", end=" ")
            elif L[i][j] == 3:
                print("*", end=" ")
        print()





exit = True

print("Bienvenue sur le graphique")
print("Veuillez poser votre equation tout en espaçant les calculs : ")
print("2 * x + 3")


while exit:
    equa = str(input("Veuillez écrire l'équation : "))
    if equa == "exit":
        exit = False
    affichage(repere_orthonorme(40, equa))
