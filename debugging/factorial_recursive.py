#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calcule le factoriel d'un nombre entier n de manière récursive.
    Le factoriel de n (noté n!) est le produit de tous les entiers de 1 à n.
    Par convention, 0! = 1.
    """
    if n == 0:
        return 1  # Cas de base : 0! = 1
    else:
        return n * factorial(n - 1)  # Appel récursif pour n * (n-1)!

# Récupère l'argument passé en ligne de commande et le convertit en entier
number = int(sys.argv[1])

# Calcule le factoriel et l'affiche
result = factorial(number)
print(result)
