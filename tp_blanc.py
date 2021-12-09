from bibgraphes import *
def contient(L1,L2):
    for i in range(len(L2)):
        same = True
        for j in range(0,len(L1)):
            if(j+i >= len(L2)):
                return False
            if(L2[j+i] != L1[j]):
                same = False
                break
        if(same):
            return True
    return False

L=[1,2,3]
G=[1, 2, 1, 3, 1, 2, 3, 2, 1]
# print(contient(L,G))

def prefixe(L1,L2):
    maxPrefixeLength=0
    maxPrefixeIndex=0
    for i in range(len(L2)):
        prefixeLength = 0
        for j in range (len(L1)):
            if(j+i >= len(L2)):
                break
            if(L2[j+i] == L1[j]):
                prefixeLength +=1
        if prefixeLength > maxPrefixeLength:
            maxPrefixeLength = prefixeLength 
            maxPrefixeIndex = i
    return ((maxPrefixeIndex,maxPrefixeLength) if maxPrefixeLength > 0 else  None)

# print(prefixe(L,G))
        
def toutDemarquer(G):
    sommets = listeSommets(G)
    for s in sommets:
        demarquerSommet(s)
        for a in listeAretesIncidentes(s):
            demarquerArete(a)

def est_domine(G):
    for s in listeSommets(G):
        if(estMarqueSommet(s)):
            continue
        hasMarkedNeighbor = False
        for v in listeVoisins(s):
            if(estMarqueSommet(v)):
                hasMarkedNeighbor = True
                break
        if(not(hasMarkedNeighbor)):
            return False
    return True

G = ouvrirGraphe("resources/tgv2005.dot")
def sommet_non_domine(G):
    for s in listeSommets(G):
        if(estMarqueSommet(s)):
            continue
        hasMarkedNeighbor = False
        for v in listeVoisins(s):
            if(estMarqueSommet(v)):
                hasMarkedNeighbor = True
                break
        if(not(hasMarkedNeighbor)):
            return s
    return None

def dominant_minal(G):
    toutDemarquer(G)
    while(est_domine(G) != True):
        testMinal = sommet_non_domine(G)
        marquerSommet(testMinal)

def est_dominant_minimal(G):
    D = []
    for s in listeSommets(G):
        if(estMarqueSommet(s)):
            D.append(s)
    print(D)
    for i in range(0,len(D)):
        demarquerSommet(D[i])
        if(est_domine(G)):
            return False
        marquerSommet(D[i])
    return True

print(est_domine(G))
dominant_minal(G)
print(est_dominant_minimal(G))
