def calcul_score_colonne(des):
    scores = [0, 0, 0]

    for j in range(3):  # Parcours des colonnes
        valeurs_colonne = [des[i][j] for i in range(3)]
        valeurs_uniques = set(valeurs_colonne)

        if len(valeurs_uniques) == 1:  # Si toutes les valeurs sont identiques
            n = len(valeurs_colonne)
            v = valeurs_colonne[0]
            scores[j] = n * n * v
        elif len(valeurs_uniques) == 3:  # Si toutes les valeurs sont différentes
            scores[j] = sum(valeurs_colonne)
        else:  # Si deux valeurs sont identiques
            for v in valeurs_uniques:
                if valeurs_colonne.count(v) == 2:
                    valeur_identique = v
                    break
            valeurs_differentes = [x for x in valeurs_uniques if x != valeur_identique]
            valeur_unique = valeurs_differentes[0]
            n = valeurs_colonne.count(valeur_identique)
            scores[j] = n * n * valeur_identique + valeur_unique

    return scores

des1 = [
    [1, 2, 3],
    [2, 2, 2],
    [3, 3, 3]
]
print("Résultat 1:", calcul_score_colonne(des1))  #[6, 11, 14]

des2 = [
    [3, 2, 3],
    [1, 2, 3],
    [5, 3, 3]
]
print("Résultat 2:", calcul_score_colonne(des2))  #[9, 11, 27] 
