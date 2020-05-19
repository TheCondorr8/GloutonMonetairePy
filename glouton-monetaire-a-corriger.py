# Algorithme glouton de résolution de monnaie à rendre
# A CORRIGER
# NF.NSI

# montant de la monnaie donnée
montant = float(input())

# valeur des pieces disponibles en euro trié dans l'ordre décroissant
pieces = [ 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01 ]
billets = [500, 200, 100, 50, 20, 10, 5]

## exemple de cas non optimal
## montant = 21
## pieces = [ 18, 7, 1 ]

def Monnaie(somme, ListeMontantPiece, ListeMontantBillet) :

    # tableau de nombre de piece max a rendre selon le tableau de pieces
    ListeNbPieces = [-1 for k in ListeMontantPiece]
    ListeNbBillets = [-1 for k in ListeMontantBillet]

    for k in range(len(ListeMontantBillet)) :

        ListeNbBillets[k] = somme // ListeMontantBillet[k]

        somme = round(somme % ListeMontantBillet[k], 2)

    # parcours de la liste des pieces
    for k in range(len(ListeMontantPiece)) :

        # recupere le nombre de piece selon le quotient (entier //)
        ListeNbPieces[k] = somme // ListeMontantPiece[k]

        # somme restante a deduire du montant
        somme = round(somme % ListeMontantPiece[k], 2)

    return somme, ListeNbBillets, ListeNbPieces

print(montant, Monnaie(montant, pieces, billets))
