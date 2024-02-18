def sac(W, L):
    if not(L):
        return 0, []
    v, l = sac(W, L[:-1])
    price, weight = L[-1]
    if weight <= W:
        v2, l2 = sac(W-weight, L[:-1])
        v3 = price + v2
        if v3 > v:
            return v3, l2 + [L[-1]]
    return v, l

def sac(W, L, dico = dict()): #Mémoïsation
    clef = (str(W), str(L))
    if clef not in dico:
        out, out2 = (0, [])
        if L:
            v, l = sac(W, L[:-1])
            out, out2 = (v, l)
            price, weight = L[-1]
            if weight <= W:
                v2, l2 = sac(W-weight, L[:-1])
                v3 = price + v2
                if v3 > v:
                    out, out2 = (v3, l2 + [L[-1]])
        dico[clef] = (out, out2)    
    return dico[clef]

if __name__ == "__main__":
    L = [(1, 10), (2, 6), (1, 5)]
    print(sac(16, L))