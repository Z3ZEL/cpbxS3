from bibgraphes import *

G = ouvrirGraphe("resources/europe.dot")


def toutDemarquer(G):
    sommets = listeSommets(G)
    for s in sommets:
        demarquerSommet(s)
        for a in listeAretesIncidentes(s):
            demarquerArete(a)
# print(toutDemarquer(G))


def sommetAccessible(G):
    sommets = listeSommets(G)
    for s in sommets:
        voisins = listeVoisins(s)
        for v in voisins:
            if(estMarqueSommet(v)):

                for a in listeAretesIncidentes(v):
                    if(sommetVoisin(v,a) == s):
                        marquerArete(a)
                    return v
    
    
    return None

# print(sommetAccessible(G))

def marquerAccessible(G,s):
    voisins = listeVoisins(s)
    marquerSommet(s)
    for v in voisins:
        if(not(estMarqueSommet(v))):
            marquerSommet(v)
            marquerAccessible(G,v)

#En utlisant la fonction précédente Version : Adrien
def marquerAccessibles2(G,s):
    toutDemarquer(G)
    marquerSommet(s)
    while sommetAccessible(G) != None :
        marquerSommet(sommetAccessible(G))



# s1 = sommetNom(G,"France")
# s2 = sommetNom(G,"Irlande")
# s3 = sommetNom(G,"Norvege")
# s4 = sommetNom(G,"Portugal")
# marquerAccessible(G,s4)

# print(estMarqueSommet(s2))
# print(estMarqueSommet(s3))
# print(estMarqueSommet(s1))

def sommetsTousMarques(G):
    sommets = listeSommets(G)
    for s in sommets:
        if(not(estMarqueSommet(s))):
            return False
    return True


def estConnexe(G):
    s = listeSommets(G)[0]
    marquerAccessible(G,s)
    return sommetsTousMarques(G)




def nbComposantesConnexes(G):
    sommets = listeSommets(G)[:]
    nbComposanteConnexes=0
    while len(sommets) > 0:
        toutDemarquer(G)
        s = sommets[0]
        marquerAccessible(G,s)
        nbSommetMarque = 0
        for sommet in sommets[:]:
            if sommet != s and estMarqueSommet(sommet):
                nbSommetMarque += 1
                sommets.remove(sommet)
        if(nbSommetMarque != 0):
            nbComposanteConnexes += 1
        sommets.remove(s)
        
    return nbComposanteConnexes


# print(nbComposantesConnexes(G))
def estAccessibleDepuis(G,s,t):
    toutDemarquer(G)
    marquerAccessible(G,s)
    return estMarqueSommet(t)


# s1 = sommetNom(G,"France")
# s2 = sommetNom(G,"Irlande")
# s3 = sommetNom(G,"Portugal")
# print(estAccessibleDepuis(G,s1,s2))
# print(estAccessibleDepuis(G,s1,s3))


def chemin(G,s,t):
    if(not(estAccessibleDepuis(G,s,t))):
        return []
    toutDemarquer(G)
    return chemin_aux(G,s,t)

def chemin_aux(G,s,t):
    if(s == t):
        return [s]
    marquerSommet(s)
    voisins = listeVoisins(s)
    for v in voisins:
        if(not(estMarqueSommet(v))):
            L = [s] + chemin_aux(G,v,t)
            if(L[len(L) - 1] == t):
                return L
    return [v] 

# print(chemin(G,sommetNom(G,"France"),sommetNom(G,"Hongrie")))


def bienColorie(G):
    sommets = listeSommets(G)
    for s in sommets:
        c = couleurSommet(s)
        voisins = listeVoisins(s)
        for v in voisins:
            cv = couleurSommet(v)
            if(cv == c):
                return False
    return True

# print(bienColorie(ouvrirGraphe("resources/menthol.dot")))

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
        
    return bienColorie(G)

# L = [construireGrille(4,4),construireArbre(3,3),construireBipartiComplet(2,5),ouvrirGraphe("resources/petersen.dot"),ouvrirGraphe("resources/cube.dot"),ouvrirGraphe("resources/octaedre.dot"),ouvrirGraphe("resources/dodecaedre.dot")]
# for g in L:
#     print(nomGraphe(g) + " : " + str(deuxColoration(g,"red","blue")))
#     # dessiner(g)
