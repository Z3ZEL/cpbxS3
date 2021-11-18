from bibgraphes import *
def pim_pam(n):
    valueToReturn=""
    if(not(n%3)):
        valueToReturn+="pim"
    if(not(n%5)):
        valueToReturn+="pam"
    if(valueToReturn == ""):
        return n
    return valueToReturn


# print(pim_pam(2))
# print(pim_pam(3))
# print(pim_pam(5))
# print(pim_pam(15))
# print(pim_pam(0))


def renverse(L):
    for i in range(len(L)//2):
        L[i],L[len(L)-1-i] = L[len(L)-1-i],L[i]

    
# L1 =[30,12,4,3]
# L2 = [5,12,3,1,20]
# renverse(L1)
# renverse(L2)
# print(L1)
# print(L2)


def nbDegMax(G):
    #Cherche le degré max
    sommets = listeSommets(G)
    degreMax = degre(sommets[0])
    for i in range(1,len(sommets)):
        tempDegre = degre(sommets[i])
        if(tempDegre > degreMax):
            degreMax = tempDegre
    
    #Compte le nombre de sommet ayant le degré max
    degreMaxCount = 0
    for s in sommets:
        if(degre(s) == degreMax):
            degreMaxCount += 1
    return degreMaxCount


# G = ouvrirGraphe("tgv2005.dot")
# print(nbDegMax(G))