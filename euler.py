from bibgraphes import *
from bibgraphes import __c_node

#Je n'était pas au td donc ya des trucs c'est un peu flou j'ai pas forcément utiliser toutes les fonctions 
#demandée donc a prendre avec des pincettes.

def nombreAretes(G):
    A=[]
    toutDemarquer(G)
    for s in listeSommets(G):
        for a in listeAretesIncidentes(s):
            if(not(estMarqueeArete(a))):
                marquerArete(a)
                A.append(a)
    toutDemarquer(G)
    return len(A)
def nombreAreteCycle(C):
    i=0
    for item in C:
        if(not(isinstance(item,__c_node))):
            i+=1
    return i

def visualSommetListe(S):

    for i,s in enumerate(S):
        print(f'Element {i}  : { nomSommet(s) if isinstance(s,__c_node) else print(s)}')
def toutDemarquer(G):
    sommets = listeSommets(G)
    for s in sommets:
        demarquerSommet(s)
        for a in listeAretesIncidentes(s):
            demarquerArete(a)

def areteIncidenteNonMarquee(s):
    for a in listeAretesIncidentes(s):
        if(not(estMarqueeArete(a))):
            return a
    return None

def areteIncidenteNonMarquee_melange(s):
    for a in melange(listeAretesIncidentes(s)):
        if(not(estMarqueeArete(a))):
            return a
    return None

def sommetAvecAretesIncidentesMarqueeEtNonMarquee(G):
    for s in listeSommets(G):
        hasMarked = False
        hasUnMarked = False
        for a in listeAretesIncidentes(s):
            if not(hasMarked):
                hasMarked = estMarqueeArete(a)
            if not(hasUnMarked):
                hasUnMarked = not(estMarqueeArete(a))
        if(hasUnMarked and hasMarked):
            return s
    return None



def cycleSansIssue(s):
    L = [s]
    while areteIncidenteNonMarquee(L[len(L)-1]) != None:
        tempS = L[len(L)-1]
        a = areteIncidenteNonMarquee(tempS)
        marquerArete(a)
        voisin = sommetVoisin(tempS,a)
        L.append(a)
        L.append(voisin)
    return L

def cycleEuler(G):
    nbArete = nombreAretes(G)
    print(f"Nombre d'aretes {nbArete}")
    for i,s in  enumerate(listeSommets(G)):
        toutDemarquer(G)
        sPrime = s
        C = cycleSansIssue(sPrime)
        while(nombreAreteCycle(C) != nbArete):
            for _s in listeSommets(G):
                a = areteIncidenteNonMarquee(_s)
                if(a != None):
                    sPrime = sommetVoisin(_s,a)
                    C += cycleSansIssue(sPrime)
        print( f"Cycle Euler, sommet départ : {i}" if nombreAreteCycle(C) == nbArete else f"Pas Cycle Euler, sommet départ : {i}")

def cycleEuler_random(G):
    nbArete = nombreAretes(G)
    print(f"Nombre d'aretes {nbArete}")
    toutDemarquer(G)
    s = elementAleatoireListe(listeSommets(G))
    C = cycleSansIssue(s)
    while(nombreAreteCycle(C) != nbArete):
        for _s in listeSommets(G):
                a = areteIncidenteNonMarquee(_s)
                if(a != None):
                    sPrime = sommetVoisin(_s,a)
                    C += cycleSansIssue(sPrime)
    print( f"Cycle Euler, sommet départ : {nomSommet(s)}" if nombreAreteCycle(C) == nbArete else f"Pas Cycle Euler, sommet départ : {nomSommet(s)}")

def listeCyclesSansIssue(G):
    L = []
    nbArete = nombreAretes(G)
    toutDemarquer(G)
    s = elementAleatoireListe(listeSommets(G))
    C = cycleSansIssue(s)
    L.append(C)
    while(nombreAreteCycle(C) != nbArete):
        for _s in listeSommets(G):
                a = areteIncidenteNonMarquee(_s)
                if(a != None):
                    sPrime = sommetVoisin(_s,a)
                    CPrime = cycleSansIssue(sPrime)
                    L.append(CPrime)
                    C += CPrime
    return L

#Calcul CycleEulerien on calcul juste si elle possède une chaine et on verifie que le premier est égal au dernier


def calculeCycleEulerienOuChaineEulerienne(G):
    nbArete = nombreAretes(G)
    for i,s in  enumerate(listeSommets(G)):
        toutDemarquer(G)
        sPrime = s
        C = cycleSansIssue(sPrime)
        if(nombreAreteCycle(C) == nbArete):
            return C
    return None

G = ouvrirGraphe("resources/euler.dot")
calculeCycleEulerienOuChaineEulerienne(G)
dessiner(G)
# cycleEuler(construireTriangle(5))