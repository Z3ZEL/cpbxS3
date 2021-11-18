from bibgraphes import *

testGraph = ouvrirGraphe("resources/europe.dot")


def toutColorier(G,c):
    sommets = listeSommets(G)
    for sommet in sommets:
        colorierSommet(sommet,c)


# toutColorier(testGraph,"red")


def existeCouleur(G,c):
    sommets = listeSommets(G)
    for sommet in sommets:
        cTemp = couleurSommet(sommet)
        if(cTemp == c):
            return True
    return False

# print(existeCouleur(testGraph,"red"))

def toutCouleur(G,c):
    sommets = listeSommets(G)
    for sommet in sommets:
        cTemp = couleurSommet(sommet)
        if(cTemp != c):
            return False
    return True

# colorierSommet(sommetNom(testGraph,"France"),"red")
# print(toutCouleur(testGraph,"red"))

def tousLaMemeCouleur(G):
    sommets = listeSommets(G)
    if(len(sommets) <= 0):
        return False
    c = couleurSommet(sommets[0])
    for sommet in sommets:
        cTemp = couleurSommet(sommet)
        if(cTemp != c):
            return False
    return True
# print(tousLaMemeCouleur(testGraph))

def nbSommetsCouleur(G,c):
    nbSommet = 0
    sommets = listeSommets(G)

    for sommet in sommets:
        cTemp = couleurSommet(sommet)
        if(cTemp == c):
            nbSommet += 1
    return nbSommet


# colorierSommet(sommetNom(testGraph,"France"),"red")
# print(nbSommetsCouleur(testGraph,"red"))

def nbSommetsColores(G):
    nbSommet = 0
    sommets = listeSommets(G)

    for sommet in sommets:
        cTemp = couleurSommet(sommet)
        if(cTemp != "white"):
            nbSommet += 1
    return nbSommet

# colorierSommet(sommetNom(testGraph,"Italie"),"red")
# colorierSommet(sommetNom(testGraph,"France"),"blue")

# print(nbSommetsColores(testGraph))

def sontVoisins(s1,s2):
    voisins = listeVoisins(s1)
    for voisin in voisins:
        if(voisin == s2):
            return True
    return False

# print(sontVoisins(sommetNom(testGraph,"France"),sommetNom(testGraph,"Italie")))
# print(sontVoisins(sommetNom(testGraph,"Irlande"),sommetNom(testGraph,"Italie")))

def listeVoisinsCommuns(s1,s2):
    sommetsCommun = []
    sommets1 = listeVoisins(s1)
    sommets2 = listeVoisins(s2)
    for i in range(len(sommets1)):
        for j in range(len(sommets2)):
            if(sommets1[i] != s2 and sommets2[j]!= s1 and sommets1[i] == sommets2[j]):
                sommetsCommun.append(sommets1[i])
    return sommetsCommun

# s1 = sommetNom(testGraph,"Allemagne")
# s2 = sommetNom(testGraph,"Tchequie")
# print(listeVoisinsCommuns(s1,s2))
        
def degreMax(G):
    sommets = listeSommets(G)
    degreMax = degre(sommets[0])
    for i in range(1,len(sommets)):
        tempDegre = degre(sommets[i])
        if(tempDegre > degreMax):
            degreMax = tempDegre
    return degreMax

# print(degreMax(testGraph))

def degreMin(G):
    sommets = listeSommets(G)
    degreMin = degre(sommets[0])
    for i in range(1,len(sommets)):
        tempDegre = degre(sommets[i])
        if(tempDegre < degreMin):
            degreMin = tempDegre
    return degreMin

def nbSommetsDegre(G,d):
    sommets = listeSommets(G)
    nbSommetsDegre = 0
    for sommet in sommets:
        dTemp = degre(sommet)
        if(dTemp == d):
            nbSommetsDegre += 1
    return nbSommetsDegre


def nbArretes(G):
    sommets = listeSommets(G)
    degreTot = 0
    for sommet in sommets:
        degreTot += degre(sommet)
    return degreTot/2

# print(nbArretes(testGraph))

def existeIsole(G):
    sommets = listeSommets(G)
    for sommet in sommets:
        voisins = listeVoisins(sommet)
        hasVoisin = False
        for voisin in voisins:
            if(voisin != sommet):
                hasVoisin = True
                break
        if(not(hasVoisin)):
            return True
    return False

# print(existeIsole(testGraph))