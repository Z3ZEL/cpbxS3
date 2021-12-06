#2013-2014    """""Correction avec de gros guillemet"""""
#Exercice 1
#1 Appliquer Master Theoreme

#2
def U(n):
  if(n==0):
    return 0
  elif(n==1):
    return U(0) + 1
  else:
    return n**2 + 2*U(n//2) + U(n//4)

#print(U(4))

#3 Flemme

#Exercice 2

#1
def Mystere(n,k):
    if(k==0):
        z=1
    else:
        v=Mystere(n-1,k-1)
        w=v*n
        z=w/k
    return z

#print(Mystere(6,4))  RETOURNE 15

#2
def MysterePasOpti(n,k):
    z = 1
    for i in range(1,k+1):
        w = (n-k+i) * z
        z = w/i
    return z

#print(MysterePasOpti(6,4)) RETOURNE 15


#Exercice 3 

L= [2,9,3,1,6,4,1,5,1,6,87,45]

#1
def EstMedian(L,i):
  sup = []
  inf = []
  if not(len(L) % 2):
    for nb in L:
      if(nb == L[i]):
        continue
      if nb > L[i]:
        sup.append(nb)
      else:
        inf.append(nb)
    return (len(sup) == (len(L)-2)/2 and len(inf)==(len(L)-2)/2 + 1) or (len(inf) == (len(L)-2)/2 and len(sup)==(len(L)-2)/2 + 1)
  else:
    for nb in L:
      if(nb == L[i]):
        continue
      if nb > L[i]:
        sup.append(nb)
      else:
        inf.append(nb)
    return len(sup) == len(inf) == (len(L)-1)/2

#print(EstMedian(L,2))

#2
def TrouveMedian(L):
  for i in range(len(L)):
    if(EstMedian(L,i)): #Attention ici on veut l'index et non le nombre en lui meme
      return L[i]

#print(TrouveMedian(L))

#3 Si la liste est dans l'ordre croissant on peut le retrouver au milieu de la liste donc à l'index n-1/2 pour une liste impaire
# et n-2/2 et n-2/2 +1 pour les deux median de la liste paire. On aurait pu utiliser le tri fusion ou quicksort qui sont de #complexité n log (n) et nous aurons ensuite directement retourner l'élement du milieu puisqu'elle seront triée
