from math import *
from test_dichot import *



def Dicho(range):
    (min,max) = range
    while(min+1<max):
        middle = (max+min)//2
        if est_plus_grand_que(middle):
            min=middle
        else:
            max=middle
    #test_final(max)

def Dicho2():
    reinit_V2()
    min=0
    max=1000
    gap=1000
    hasFound=False
    while not(hasFound):
        if est_plus_grand_que(max):
            min=max
            max=min+gap
            gap *= 2
        else:
            hasFound=True
    Dicho((min,max))
    return C[0]

# mean = 0
# for i in range(1000):
#     mean += Dicho2()

# print(mean/1000)

#La fonction a une complexité fluctuante entre 29 coups pour un intervalles non fixé. L'algorithme est donc assez
#efficace car l'algorithme calcule pour un nombre sans intervalle (même si techniquement il est quand même borné)
#L'ordre de grandeur est donc inférieur à 100 est reste donc logarithmique en ajoutant malgré tout de nouvelles opérations

def TriPasOuf(L):
    T = []
    while(len(L)>1):
        temp = MinList(L)
        T.append(temp)
        L.remove(temp)
    T.append(L[0])
    print(T)

def MinList(L):
    min = L[0]
    for i in L:
        if i<min:
            min = i
    return min

def TriInsertionPasOuf(L):
    T=[L.pop()]
    while(len(L)>0):
        temp = L.pop()
        for i in range(len(T)):
            if(temp<T[i]):
                T.insert(i,temp)
                break
        if(temp >= T[len(T)-1]):
            T.append(temp)
    print(T)



#TriPasOuf(genere_liste(10))
#TriInsertionPasOuf(genere_liste(10))


def DichoSort(L):
    T = [L.pop()]
    while(len(L)>1):
        temp = L.pop()
        T.insert(SearchList(temp,T),temp)
    return T

def SearchList(x,L):
    min = 0
    max = len(L) - 1
    if(L[0]>x):
        return 0

    while(min<=max):
        #print(str(min) + "   " + str(max))
        middle = (max+min+1)//2
        if x >= L[middle]:
            min=middle
            if min==max:
                return min+1
        elif min+1==max:  #gère le problème d'indice consécutif qui bloque le programme pas très élégant mais ça marc
            print(str(L[min])+" "+str(x)+"  "+str(L[max]))

            if x >= L[min] and x<=L[max]:
                return max
        else:
            max=middle
            if min==max:
                return min

# DichoSort(genere_liste(10))

#La version tri par insertion dichotomique est plus efficace car à chaque valeur de la
#premiere liste à trier parcouru un effort de locatisation via dichotomie est demandé de
# complexité logarithmique. Disons k complexe. On va l'effectuer nk fois avec n la longueur de la liste.
# à l'inverse la version naïve on parcours la première liste une fois et à chaque fois on parcour la deuxième entierement
# pour chaque élément de la première liste. la complexité est donc quadratrique.



