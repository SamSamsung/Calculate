def repere_ortho_i(i, n):
    if i == n // 2:
        i = 0
    elif i < (n // 2):
        i = 0 - (n // 2 - i)

    elif i > n // 2:
        i = i - n // 2
    return i


def repere_ortho_j(j, n):
    if j == n // 2:
        j = 0
    elif j < n // 2:
        j = 0 - (n // 2 - j)

    elif j > n // 2:
        j = j - n // 2
    return j


def dessiner_repere(i, j, L, x, y):
    if x == 0:
        L[i][j] = 1
    elif y == 0:
        L[i][j] = 2
    else:
        L[i][j] = 0
    return L


def dessiner_fonction(i, j, L, x, y, equation):
    if x == -(eval(equation)):
        if L[i][j] == 1:
            L[i][j] = 1
        elif L[i][j] == 2:
            L[i][j] = 2
        else:
            L[i][j] = 3
    return L


def carre(n, equation):
    L = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        x = repere_ortho_i(i, n)
        for j in range(n):
            y = repere_ortho_j(j, n)
            L = dessiner_repere(i, j, L, x, y)
            L = dessiner_fonction(i, j, L, x, y, equation)
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
    equa = equa.replace("x", "y")
    affichage(carre(40, equa))
