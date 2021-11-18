from test_dichot import *
import time

def fusion(L1,L2):
    i = 0
    j = 0
    T = []
    #Ajoute à la nouvelle liste un des deux élément en fonction de celui qui est le plus inférieur
    #jusqu'à ce qu'un des deux index soit nul
    while(j < len(L2) and i < len(L1)):
        if(L1[i] < L2[j]):
            T.append(L1[i])
            i += 1
        else:
            T.append(L2[j])
            j += 1
    #ajoute tout les restes des éléments de la dernière liste afin de compléter la list fusionnée
    while(j < len(L2) or i < len(L1)):
        if(i < len(L1)):
            T.append(L1[i])
            i += 1
        else:
            T.append(L2[j])
            j += 1
    return T
    #Nous aurions pu directement travailler avec les éléments des listes et les supprimer au fur et à mesure et ajouter les listes à la fin
    #cela nous aurai évité la dernière boucle while cependant dans la consigne nous devions travailler avec des index.

# test1 = DichoSort(genere_liste(5))
# test2 = DichoSort(genere_liste(5))  # DichoSort mon algo de tri implémenté au dernier td afin d'avoir une liste triée pour tester la fusion
# fusion(test1,test2)


def fusionSort(L):
    T = []
    #Creation d'une 2-D liste composée d'un seul élément de chaque élément de L
    while(len(L)>0):
        T.append([L.pop()])
    #Fusionne deux à deux en partant de la fin les éléments de la liste T et place la nouvelle liste à la fin et ainsi de suite
    #jusqu'à ce que la longueur de la liste soit égale à 1
    while(len(T) > 1):
        T.append(fusion(T.pop(),T.pop()))
    return T[0]

# fusionSort(genere_liste(10))


def quickSort(L, start=0,end=None):
    if(end == None):
        end = len(L)
    if(end - start <= 1):
        return L
    index = random.randint(start,end-1 )
    pivot = L[index]
    seuil = part(L,start,end-1,pivot)
    quickSort(L,start,seuil)
    quickSort(L,seuil,end)


# def part(L,start,end,pivot,pivot_index):
#     i= start
#     j= end
#     #balaye à chaque fois les éléments à gauche et à droite du pivot jusqu'à ce que l'on trouve une valeur plus grand ou plus petite respectivement à droite
#     #ou à gauche du pivot et on inverse avec le pivot. Répétons cela jusqu'à que les deux index balais start-end sans aucun soucis 
#     #de comparaison.
#     while(i < pivot_index or j > pivot_index):
#         if(i < pivot_index and L[i] > pivot):
#             L[i],L[pivot_index] = L[pivot_index],L[i]
#             pivot_index = i
#             i=start
#             j=end
#             continue
#         if(j > pivot_index and L[j] < pivot):
#             L[j],L[pivot_index] = L[pivot_index],L[j]
#             pivot_index = j
#             i=start
#             j=end
#             continue
#         i+=1
#         j-=1
#     return pivot_index



def part(L,start,end,pivot):
    i = start
    j = end
    samePivotNb = 0
    while(i<j):
        if(L[j] < L[i]):
            L[j],L[i] = L[i],L[j]
        if(L[i] < pivot):
            i+=1
        if(L[j] > pivot):
            j-=1
        if(L[j] == pivot and L[i] == pivot and j != i):
            L.remove(L[i])
            samePivotNb += 1
    for k  in range(samePivotNb):
        L.insert(i,pivot)            
        

    return i

L = genere_liste(20)
quickSort(L)
print(L)
# U = [10,2,26,30,40,80,5,40,10,12,30,12,2]
# print(part(U,0,12,30))
# print(U)


def meanTimeGap(sampleNb,listLength):
    totalTimeFusion = 0
    totalTimeQuickSort = 0
    for i in range(sampleNb):
        gap=0
        L = genere_liste(listLength)
        startTime = time.time()
        fusionSort(L)
        totalTimeFusion+=time.time()-startTime
        L = genere_liste(listLength)
        startTime = time.time()
        quickSort(L)
        totalTimeQuickSort += time.time()-startTime
        print(totalTimeFusion,totalTimeQuickSort)
    return (totalTimeFusion/sampleNb,totalTimeQuickSort/sampleNb)

#RETURN THE MEAN OF THE TIME OF FUSION AND QUICKSORT
# print(meanTimeGap(1000,1000))
# Pour un échantillions de 1000 tests de tri d'une liste de 1000 élément nous trouvons :
# QuickSort = 0.0420534200668335
# FusionSort = 0.12241889214515686
# Nous pouvons conclure que le quicksort est donc environs 3 fois plus rapide en moyenne ce qui est vraiment efficace.

