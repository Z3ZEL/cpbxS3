from math import *

def estPremier(n):
    i = 2
    while i*i <= n:
        if(not(n%i)):
            return False
        i += 1
    return True

# print(estPremier(999999929))
print(estPremier(25))
print(estPremier(1_000_000_000_000_091))

def estMultipleDe3(n):
    return not(n%3)

# print(estMultipleDe3(22))