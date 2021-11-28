from bibgraphes import *
from palettes import *
def toutDemarquer(G):
    sommets = listeSommets(G)
    for s in sommets:
        demarquerSommet(s)
        for a in listeAretesIncidentes(s):
            demarquerArete(a)
def effacerCouleurs(G):
    sommets = listeSommets(G)
    for s in sommets:
        colorierSommet(s,"white")
def Visual(G,s):
    c1 = '\033[92m'
    c2 = '\033[0m'
    c3 = '\033[91m'
    (peres,distance) = parcoursEnLargeur(G,s)
    for sommet in peres:
        pere = None
        if(peres[sommet] == 'NIL'):
            pere = 'NIL'
        else:
            pere = nomSommet(peres[sommet])
        print(f"{c1}{nomSommet(sommet)} : {c2} \n Père : {c3}{pere}{c2} \n Distance : {c3}{distance[sommet]}{c2}")



def parcoursEnLargeur(G,s):
    peres =  {}
    distances = {}
    F = [s]
    sommets = listeSommets(G)
    for sommet in sommets:
        if(sommet == s):
            peres[s] = "NIL"
            distances[s] = 0
            colorierSommet(s,"grey")
            continue
        peres[sommet] = "NIL"
        distances[sommet] = -1
        colorierSommet(sommet,"white")
    while(len(F) != 0):
        target = F.pop(0)
        for v in listeVoisins(target):
            if(couleurSommet(v) == "white"):
                colorierSommet(v,"grey")
                distances[v] = distances[target] + 1
                peres[v] = target
                F.append(v)
        colorierSommet(target,"black")
    return (peres,distances)
def parcoursEnLargeur_marquage(G,s):
    toutDemarquer(G)
    peres =  {}
    distances = {}
    F = [s]
    sommets = listeSommets(G)
    for sommet in sommets:
        if(sommet == s):
            peres[s] = "NIL"
            distances[s] = 0
            marquerSommet(s)
            continue
        peres[sommet] = "NIL"
        distances[sommet] = -1
    while(len(F) != 0):
        target = F.pop(0)
        for v in listeVoisins(target):
            if(not(estMarqueSommet(v))):
                marquerSommet(v)
                distances[v] = distances[target] + 1
                peres[v] = target
                F.append(v)

    toutDemarquer(G)
    return (peres,distances)
def parcoursEnLargeur_arete(G,s):
    toutDemarquer(G)
    peres =  {}
    distances = {}
    F = [s]
    sommets = listeSommets(G)
    for sommet in sommets:
        if(sommet == s):
            peres[s] = "NIL"
            distances[s] = 0
            marquerSommet(s)
            continue
        peres[sommet] = "NIL"
        distances[sommet] = -1
    while(len(F) != 0):
        target = F.pop(0)
        for a in listeAretesIncidentes(target):
            if(not(estMarqueeArete(a))):
                marquerArete(a)
                v = sommetVoisin(target,a)
                marquerSommet(v)
                distances[v] = distances[target] + 1
                peres[v] = target
                F.append(v)

    toutDemarquer(G)
    return (peres,distances)

def colorierParPalette(G,s,p):
    effacerCouleurs(G)
    (peres,distances) = parcoursEnLargeur_arete(G,s)
    print(distances)
    sommets = listeSommets(G)
    dmax = 0
    for sommet in sommets:
        if(distances[sommet] > dmax):
            dmax = distances[sommet]
    
    for sommet in sommets:
        i = (len(p)*distances[sommet])//dmax
        if(i <0):
            i = 0
        elif(i >= len(p)):
            i = len(p)-1

        color = p[i]
        
        colorierSommet(sommet,color)

    dessiner(G)
        

# G = construireGrille(7,7)
# colorierParPalette(G,listeSommets(G)[24],paletteNumero(2)) 



