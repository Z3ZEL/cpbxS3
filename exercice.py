#/usr/bin/python3
# -*-coding:utf-8 -*
from bibgraphes import *


def nbDegPair(G):
    nb = 0
    for s in listeSommets(G):
        if(degre(s) % 2 == 0):
            nb += 1
    return nb

def listeSommetsDegPair(G):
    Even = []
    for s in listeSommets(G):
        if(degre(s) % 2 == 0):
            Even.append(s)
    return Even


G = ouvrirGraphe("tgv2005.dot")
print(nbDegPair(G))
print(len(listeSommetsDegPair(G)))
print(listeSommetsDegPair(G))
# dessiner(G)

def decal(L, d, a):
    for i in range(d,a,-1):
        L[i],L[i-1] = L[i-1],L[i]

L=[8,1,0,5,2,4,9,7,6,3]


def evenNb(L):
    nb = 0
    for n in L:
        if(n%2==0):
            nb+=1
    return nb

def pairs_impairs(L):
    nbEven = evenNb(L)
    i = len(L)-1
    while(i>nbEven):
        #Décale tout les nombres paires de la partie droite jusqu'a que nbEven on été déplacé donc il ya derrière nbEven de nombre à gauche
        i-=1
        if(L[i] % 2 == 0):
            decal(L,i,0)
            i+=1
    #Et on résoud le problème de l'indice du milieu
    if(L[nbEven-1] % 2 == 0):
            decal(L,nbEven-1,0)






pairs_impairs(L)
print(L)


def toutDemarquer(G):
    sommets = listeSommets(G)
    for s in sommets:
        demarquerSommet(s)
        for a in listeAretesIncidentes(s):
            demarquerArete(a)

def sommetNonCouvert(G):
    for s in listeSommets(G):
        if(estMarqueSommet(s)):
            continue
        hasMarkedOne = False
        for v in listeVoisins(s):
            if(estMarqueSommet(v)):
                hasMarkedOne = True
                break
        if(not(hasMarkedOne)):
            return s
    return None


def calculESM(G):
    ESM = []
    t = sommetNonCouvert(G)
    while(t != None):
        marquerSommet(t)
        ESM.append(t)
        t = sommetNonCouvert(G)
    return ESM


G = ouvrirGraphe("europe.dot")
calculESM(G)
# dessiner(G)

