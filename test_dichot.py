#/usr/bin/python3
# -*-coding:utf-8 -*

import random

M=[(int(random.uniform(1,1000)))]
C=[0]

def reinit():
   C[0]=0
   M[0]=(int(random.uniform(1,1000)))

def reinit_V2():
   C[0]=0
   M[0]=int(random.expovariate(.000001))

def est_plus_petit_que(i):
    C[0]+=1
    return i> M[0]
        
def est_plus_grand_que(i):
    C[0]+=1
    return i< M[0]
   
def test_final(x):
   if x==M[0]:
      print("Bravo, la valeur est bien ",x)
      print("Cela t'a pris ",C[0]," coups")
      reinit()
   else:
      print("Non, ce n'est pas ",x)


def genere_liste(x):
   L=[]
   for i in range(x):
      L.append(int(random.uniform(1,10000)))
   return L
