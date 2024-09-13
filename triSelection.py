def tri_selection(tableau):
    # Parcourt tout le tableau
    for i in range(len(tableau)-1):
        # Trouve l'indice du plus petit élément dans la portion non triée
        min_index = i
        for j in range(i + 1, len(tableau)):
            if tableau[j] < tableau[min_index]:
                min_index = j
        if (min_index != i):
            # Échange l'élément minimum trouvé avec le premier élément de la portion non triée
            tableau[i], tableau[min_index] = tableau[min_index], tableau[i]


# Exemple d'utilisation
notes = [4, 13, 12, 12, 11]
print("Tableau avant tri :", notes)
tri_selection(notes)
print("Tableau après tri :", notes)
