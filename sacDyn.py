def sac(W, L):
    n = len(L)
    #table pour stocker la valeur maximum obtenable pour chaque poids et chaque valeur d'objets
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    #table pour mémoriser les objets sélectionnés
    selected = [[False] * (W + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            #vérifier si l'objet actuel peut aller dans le sac
            if L[i - 1][1] <= w:
                #si oui, calculer la valeur max obtenable en l'incluant ou l'excluant
                include = L[i - 1][0] + dp[i - 1][w - L[i - 1][1]]
                exclude = dp[i - 1][w]
                #choisir la meilleure option
                dp[i][w] = max(include, exclude)
                selected[i][w] = include > exclude
            else:
                #sinon, prendre la valeur max obtenable sans l'objet
                dp[i][w] = dp[i - 1][w]
    
    #récupérer la liste des objets sélectionnés
    i, w = n, W
    selected_items = []
    while i > 0 and w > 0:
        if selected[i][w]:
            selected_items.append(L[i - 1])
            w -= L[i - 1][1]
        i -= 1
    #valeur totale max, liste des objets dans le sac
    return dp[n][W], selected_items[::-1]

if __name__ == "__main__":
    L = [(1, 10), (2, 6), (1, 5)]
    print(sac(16, L))