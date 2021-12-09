#Correction 2018-2019 Trichotomique
def trichotomiqueFusion(L1,L2,L3):
    L=[]
    while(len(L1)>0 or len(L2)>0 or len(L3)>0):
        L.append(popMin(L1,L2,L3))
    return L

def popMin(L1,L2,L3):
    T = []

    #Creating 2-D List to simplify
    L=[L1,L2,L3]
    for LX in L:
        if(len(LX) > 0):
            T.append(LX[0])
    
    #Find the min
    min = T[0]
    for nb in T:
        if nb < min:
            min = nb
    
    for LX in L:
        if(len(LX) > 0 and LX[0] == min):
            return LX.pop(0)
    
L = [1,3,5,8,10,11,12]
G = [2,30,31,40]
F= [9,10,14,18,20]

print(trichotomiqueFusion(L,G,F))