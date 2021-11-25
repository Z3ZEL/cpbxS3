from bibgraphes import *

def estParfait(n):
    '''Un nombre n est parfait s'il est égal à la moitié de la somme de ses divisieurs. Par exemple 6 est parfait car : 1+2+3+6 = 2*6.
    28 est aussi un nombre parfait. Cette fonction retourne True si n est parfait, False sinon.'''
    L = []
    for i in range(1,n):
        if(not(n%i)):
            L.append(i)
    sum = 0
    for l in L:
        sum += l
    return n == sum

print(estParfait(6))
print(estParfait(28))
print(estParfait(40))
print(estParfait(496))
print(estParfait(8128))

def degreMoyen(G):
    ''' Ecrire une fonction qui retourne le degré moyen du graphe (la moyenne des degrés des sommets)'''
    sommets = listeSommets(G)
    sumDeg = 0
    for s in sommets :
        sumDeg += degre(s)
    return sumDeg/len(sommets)


G = ouvrirGraphe("europe.dot")
print(degreMoyen(G))
G= ouvrirGraphe("tgv2005.dot")
print(degreMoyen(G))

def effacerCouleurs(G):
    sommets = listeSommets(G)
    for s in sommets:
        colorierSommet(s,"white")

def sommetColoriable(G):
    sommets = listeSommets(G)
    for s in sommets:
        if(couleurSommet(s) == "white"):
            continue
        voisins = listeVoisins(s)
        for v in voisins:
            if(couleurSommet(v) == "white"):
                return v
    return None

def monoCouleurVoisins(s):
    voisins = listeVoisins(s)
    color = "none"
    for v in voisins:
        vColor = couleurSommet(v)
        if(vColor != "white"):
            if(color == "none"):
                color = vColor
            elif(color != vColor):
                return None
    #ne devrait pas arriver dans le cas de la fonction deuxColoration mais dans le cas général cela peut arriver
    if(color != "none"):
        return color
    else:
        return None

def deuxColoration(G,c1,c2):
    effacerCouleurs(G)
    sommets = listeSommets(G)
    sInit = sommets[0]
    colorierSommet(sInit,c1)
    t = sommets[0]
    while(t != None):
        t = sommetColoriable(G)
        if(t == None):
            break
        color = monoCouleurVoisins(t)
        if(color == c1):
            colorierSommet(t,c2)
        else: 
            colorierSommet(t,c1)
        
    return G

def bienColorier(G):
    ''' On dit qu'un graphe est bien colorier si pour chaque arête (u,v) la
    la couleur du sommet u est différente de celle du sommet v. C'est
    le cas du fichier tgvBC.dot ci-dessus
    Cette fonction retourne True si le graphe est bien colorié, '''
    sommets = listeSommets(G)
    for s in sommets:
        c = couleurSommet(s)
        voisins = listeVoisins(s)
        for v in voisins:
            cv = couleurSommet(v)
            if(cv == c):
                return False
    return True

G = ouvrirGraphe("cube.dot")
print(bienColorier(deuxColoration(G,"red","blue")))
G = ouvrirGraphe("petersen.dot")
print(bienColorier(deuxColoration(G,"red","blue")))

def intersection(L1,L2):
    """retourne l'intersection des listes L1 et L2 """
    I = []
    for l1 in L1:
        for l2 in L2:
            if l1 == l2:
                I.append(l1)
    return I

print(intersection([4,5,6,1,2,3],[4,5,6,7,8,9]))
print(intersection([1,2,3],[4,5,6]))