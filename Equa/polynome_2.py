import math

a = float(input("Nombre réel non nul, a = "))
b = float(input("Nombre réel, b = "))
c = float(input("Nombre réel, c = "))

Delta = (b * b) - 4 * a * c
print("Δ = " + str(Delta))

if Delta > 0:
    print("Δ > 0 : Il y a deux solutions distinctes : ")
    x1 = (-b - math.sqrt(Delta)) / (2 * a)
    x2 = (-b + math.sqrt(Delta)) / (2 * a)

    if int(math.sqrt(Delta) ** 2) == Delta:
        if x1 > x2:
            print("S = {" + str(x2) + " ; " + str(x1) + "}")
        elif x1 < x2:
            print("S = {" + str(x1) + " ; " + str(x2) + "}")

    else:
        d = 2 * a
        if x1 > x2:
            print("S = {" + str(b) + "+√" + str(Delta) + "/" + str(d) + " ; " + str(b) + "-√" + str(Delta) + "/" + str(
                d) + "}")
        elif x1 < x2:
            print("S = {" + str(b) + "-√" + str(Delta) + "/" + str(d) + " ; " + str(b) + "+√" + str(Delta) + "/" + str(
                d) + "}")

elif Delta == 0:
    print("Δ = 0 : Il y a une unique solution")
    x0 = -b / (2 * a)
    print("S = {" + str(x0) + "}")
elif Delta < 0:
    print("Δ < 0 : Il n'y a pas de solution possible.")
