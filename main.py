####from math import sqrt

#### Fonction secondaire

"""
author: marie-emilienne.gnamien@edu.esiee.fr

"""


def isprime(p):

    """
    Determine si p est premier

    Args:
        p: valeur entiere positive
    
    Returns:
        isprime(p) : True, False
    """

    premier = True
    if p == 1:
        return False
    for i in range(2,p):
        if p%i == 0:
            premier = False
            break
    return premier

#### Fonction principale


def main():
    """
    Appelle la fonction secondaire et affiche 
    les nombres premiers entre 0 et 99

    """
    # vos appels à la fonction secondaire ici
    print(isprime(2))
    print(isprime(4))
    print(isprime(20))
    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
