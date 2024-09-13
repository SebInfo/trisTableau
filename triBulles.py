def tri_bulle(tableau):
    permutation = True
    passage = 0
    while permutation:
        permutation = False
        passage += 1
        # Parcourt les éléments non triés du tableau
        for en_cours in range(0, len(tableau) - passage):
            if tableau[en_cours] > tableau[en_cours + 1]:
                # Échange les éléments si le premier est plus grand que le suivant
                tableau[en_cours], tableau[en_cours + 1] = tableau[en_cours + 1], tableau[en_cours]
                permutation = True  # Indique qu'une permutation a eu lieu
    return tableau


# Exemple d'utilisation
notes = [4, 14, 5, 2, 12, 17, 9]
print("Tableau avant tri :", notes)
tableau_trie = tri_bulle(notes)
print("Tableau après tri :", tableau_trie)
