

exit = True
print("Bienvenue sur les résolutions d'équation")
print("Pour quitter ce menu, tapez exit")
print("Veuillez espacez tous vos calculs  : "
          "2x * ( 4 + 2 ) + 2y / 2")

while exit:
    choix = int(input("""Selectionnez le type:
    1. Système
    2. Polynomiale
    3. Degré 1
     """))
    if choix == 1:
        import degre_1
    elif choix == 2:
        choix_poly = int(input("""Selectionnez le type de polynome:
        2
        3
        4
        5
        6"""))
        if choix_poly == 2:
            import polynome_2
    elif choix == 3:
        pass