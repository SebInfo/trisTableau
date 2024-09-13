def tri_insertion(tableau):
    # Parcourir chaque élément du tableau à partir du deuxième
    for i in range(1, len(tableau)):
        clé = tableau[i]
        j = i - 1

        # Déplacer les éléments plus grands que la clé vers la droite
        while j >= 0 and tableau[j] > clé:
            tableau[j + 1] = tableau[j]
            j -= 1

        # Insérer la clé à sa place correcte
        tableau[j + 1] = clé


# Exemple d'utilisation
tableau = [29, 10, 14, 37, 13]
print("Tableau avant tri :", tableau)
tri_insertion(tableau)
print("Tableau après tri :", tableau)
