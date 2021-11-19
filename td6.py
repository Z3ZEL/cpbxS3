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
