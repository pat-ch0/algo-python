import graphviz

def action(x, top):
    op, pos, lettre = top
    if op == 'd':
        return x[:pos] + x[pos+1:]
    elif op == 'i':
        return x[:pos] + lettre + x[pos:]
    elif op == 's':
        return x[:pos] + lettre + x[pos+1:]
    else:
        return "ERREUR"

def visualisation(Lop, x, y):
    dot = graphviz.Digraph("g1")
    arrivee = x
    for op, pos, lettre in Lop:
        depart = arrivee
        arrivee = action(depart, (op, pos, lettre))
        dot.edge(depart, arrivee, label = op + " " + str(pos) + " " + lettre)
    display(dot)


#Solution avec meilleure complexité : ajouter dico en entrée, vide par défaut
#clef = paramètres utiles de la fonction
#si clef pas dans dico : faire le travail usuel, stocker le résultat dans dico[clef]; renvoyer dico[clef]
#Cela évite la redondance des appels récursifs
def d(M, P, cts, G, dico = dict()):
    clef = (M, P)
    if clef not in dico:
        cs, cd, ci = cts
        if len(M) == 0: #M vide doit devenir P
            out = ci * len(P)
            out2 = [('i', 0, c) for c in P[::-1]] #Insertion en tête, donc toujours en position 0
        elif len(P) == 0: #P vide, on efface M
            out = cd * len(M)
            out2 = [('d', 0, c) for c in M] #Suppression de M par la tête
        
        else:
            u = M[:-1]
            x = M[-1]
            v = P[:-1]
            y = P[-1]
            depart = M + ' / ' + P

            if x == y: #Derniers caractères égaux
                arrivee = u + ' / ' + v
                G.edge(depart, arrivee)
                out, out2 = d(u, v, cts, G)
            
            else:
                n = len(M)

                arrivee = u + ' / ' + v
                G.edge(depart, arrivee)
                s, ops = d(u, v, cts, G)
                s += cs
                ops = [('s', n-1, y)] + ops

                arrivee = M + ' / ' + v
                G.edge(depart, arrivee)
                i, opi = d(M, v, cts, G)
                i += ci
                opi = [('i', n, y)] + opi

                arrivee = u + ' / ' + P
                G.edge(depart, arrivee)
                e, ope = d(u, P, cts, G)
                e += cd
                ope = [('d', n-1, x)] + ope

                #comparaison des coûts
                out = s
                out2 = ops
                for c, op in zip([i, e], [opi, ope]):
                    if c < out:
                        out = c
                        out2 = op
        dico[clef] = (out, out2)
    return dico[clef]

M = "hello"
P = "halof"
cts = (1, 1, 1)
Gappels = graphviz.Digraph()
cout, Lop = d(M, P, cts, Gappels)
display(Gappels)
visualisation(Lop, M, P)