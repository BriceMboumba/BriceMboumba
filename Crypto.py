import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
from math import*

def PhiN():
    p = int(input('Entrez p : p = '))
    q = int(input('Entrez q : q = '))
    m = int(input("Entrez le message (m etant un chiffre) : m = "))

    # clé publique
    N = p * q
    e = int(input('Entrer clé e : e = '))

    # phi(N)
    phiN = (p - 1) * (q - 1)
    print("phiN = ", phiN)


# fonction bezout pour trouver d
def bezout_fct(a, b):
    a = e
    b = phiN
    if b == 0:
        return 1, 0
    else:
        u, v = bezout_fct(b, a % b)
        print("d =", u)
       # return v, u - (a // b) * v


def resoud_equation(a, b, c):
    u, v = bezout_fct(a, b)
    return "Les solutions de l'équation {}x + {}y = {} sont:\n({} + {}k , {} - {}k)".format(a, b, c, u, b, v, a)


def Ciphertext():
    c = pow(m, e) % N
    print("Ciphertext = ", c)


def pgcd(a, b):

    a = p
    b = q
    if b == 0:
        return a
    else:
        r = a % b
        return pgcd(b, r)


# print ("pgcd = ",pgcd(e,phiN))
def Bezout(a, b):
     if b == 0 :
         #while(b==0):
            # b= int(input("Choisissez b>0"))
         print("Choisissez b>0")
         return 1
     elif a<b :
         a = b
         ech = a
         b = ech
     else :
         y, r = a//b, a%b
         a_prim = b*y + r
         if (a_prim == a):
             b = r*(b//r)+(b%r)
             u, v = (b//r), b%r
             Bezout(u,v)
             if r == 1 | b%r == 1:
                 print("les nombres choisis",a,"et",b,"ne sont premiers entre eux")
             else :
                 print("les nombres choisis",a,"et",b,"sont premiers")



if __name__ == '__main__':
    Bezout(368,13)


