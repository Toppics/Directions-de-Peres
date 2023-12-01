# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 13:20:01 2023

@author: yan-s
"""

# On récupère la liste des 33 directions de Peres déterminées précédemment
directionsPeres = [[1.0, 0.0, 1.0],
                   [1.0, 1.0, 0.0],
                   [1.0, -0.7071067811865476, -0.7071067811865476],
                   [1.0, 0.7071067811865476, -0.7071067811865476],
                   [1.0, -0.7071067811865476, 0.7071067811865476],
                   [1.0, 0.7071067811865476, 0.7071067811865476],
                   [1.0, -0.7071067811865475, 0.0],
                   [1.0, 0.7071067811865475, 0.0],
                   [1.0, 0.0, 0.0],
                   [1.0, 0.0, -0.7071067811865475],
                   [1.0, 0.0, 0.7071067811865475],
                   [-1.0, 0.0, 1.0],
                   [0.0, -1.0, 1.0],
                   [0.0, 1.0, 1.0],
                   [-0.7071067811865475, 0.0, 1.0],
                   [0.7071067811865475, 0.0, 1.0],
                   [0.0, 0.0, 1.0],
                   [0.0, -0.7071067811865475, 1.0],
                   [0.0, 0.7071067811865475, 1.0],
                   [-0.7071067811865476, -0.7071067811865476, 1.0],
                   [0.7071067811865476, -0.7071067811865476, 1.0],
                   [-0.7071067811865476, 0.7071067811865476, 1.0],
                   [0.7071067811865476, 0.7071067811865476, 1.0],
                   [-1.0, 1.0, 0.0],
                   [-0.7071067811865475, 1.0, 0.0],
                   [0.7071067811865475, 1.0, 0.0],
                   [0.0, 1.0, 0.0],
                   [-0.7071067811865476, 1.0, 0.7071067811865476],
                   [-0.7071067811865476, 1.0, -0.7071067811865476],
                   [0.7071067811865476, 1.0, 0.7071067811865476],
                   [0.7071067811865476, 1.0, -0.7071067811865476],
                   [0.0, 1.0, -0.7071067811865475],
                   [0.0, 1.0, 0.7071067811865475]]

# On récupère la liste des 16 triplets déterminées précédemment
triplets = [[[1.0, 0.0, 1.0], [-1.0, 0.0, 1.0], [0.0, 1.0, 0.0]],
            [[1.0, 0.0, 1.0], [-0.7071067811865476, 1.0, 0.7071067811865476], [0.7071067811865476, 1.0, -0.7071067811865476]],
            [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [-1.0, 1.0, 0.0]],
            [[1.0, 1.0, 0.0], [0.7071067811865476, -0.7071067811865476, 1.0], [-0.7071067811865476, 0.7071067811865476, 1.0]],
            [[1.0, -0.7071067811865476, -0.7071067811865476], [1.0, 0.7071067811865476, 0.7071067811865476], [0.0, -1.0, 1.0]],
            [[1.0, 0.7071067811865476, -0.7071067811865476], [1.0, -0.7071067811865476, 0.7071067811865476], [0.0, 1.0, 1.0]],
            [[1.0, -0.7071067811865475, 0.0], [0.0, 0.0, 1.0], [0.7071067811865475, 1.0, 0.0]],
            [[1.0, 0.7071067811865475, 0.0], [0.0, 0.0, 1.0], [-0.7071067811865475, 1.0, 0.0]],
            [[1.0, 0.0, 0.0], [0.0, -1.0, 1.0], [0.0, 1.0, 1.0]],
            [[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]],
            [[1.0, 0.0, 0.0], [0.0, -0.7071067811865475, 1.0], [0.0, 1.0, 0.7071067811865475]],
            [[1.0, 0.0, 0.0], [0.0, 0.7071067811865475, 1.0], [0.0, 1.0, -0.7071067811865475]],
            [[1.0, 0.0, -0.7071067811865475], [0.7071067811865475, 0.0, 1.0], [0.0, 1.0, 0.0]],
            [[1.0, 0.0, 0.7071067811865475], [-0.7071067811865475, 0.0, 1.0], [0.0, 1.0, 0.0]],
            [[-1.0, 0.0, 1.0], [-0.7071067811865476, 1.0, -0.7071067811865476], [0.7071067811865476, 1.0, 0.7071067811865476]],
            [[-0.7071067811865476, -0.7071067811865476, 1.0], [0.7071067811865476, 0.7071067811865476, 1.0], [-1.0, 1.0, 0.0]]]

# On récupère la liste des 24 paires non déjà présentes dans triplets déterminées précédemment
paires = [[[1.0, -0.7071067811865476, -0.7071067811865476], [0.7071067811865475, 0.0, 1.0]],
          [[1.0, -0.7071067811865476, -0.7071067811865476], [0.7071067811865475, 1.0, 0.0]],
          [[1.0, 0.7071067811865476, -0.7071067811865476], [0.7071067811865475, 0.0, 1.0]],
          [[1.0, 0.7071067811865476, -0.7071067811865476], [-0.7071067811865475, 1.0, 0.0]],
          [[1.0, -0.7071067811865476, 0.7071067811865476], [-0.7071067811865475, 0.0, 1.0]],
          [[1.0, -0.7071067811865476, 0.7071067811865476], [0.7071067811865475, 1.0, 0.0]],
          [[1.0, 0.7071067811865476, 0.7071067811865476], [-0.7071067811865475, 0.0, 1.0]],
          [[1.0, 0.7071067811865476, 0.7071067811865476], [-0.7071067811865475, 1.0, 0.0]],
          [[1.0, -0.7071067811865475, 0.0], [0.7071067811865476, 1.0, 0.7071067811865476]],
          [[1.0, -0.7071067811865475, 0.0], [0.7071067811865476, 1.0, -0.7071067811865476]],
          [[1.0, 0.7071067811865475, 0.0], [-0.7071067811865476, 1.0, 0.7071067811865476]],
          [[1.0, 0.7071067811865475, 0.0], [-0.7071067811865476, 1.0, -0.7071067811865476]],
          [[1.0, 0.0, -0.7071067811865475], [0.7071067811865476, -0.7071067811865476, 1.0]],
          [[1.0, 0.0, -0.7071067811865475], [0.7071067811865476, 0.7071067811865476, 1.0]],
          [[1.0, 0.0, 0.7071067811865475], [-0.7071067811865476, -0.7071067811865476, 1.0]],
          [[1.0, 0.0, 0.7071067811865475], [-0.7071067811865476, 0.7071067811865476, 1.0]],
          [[0.0, -0.7071067811865475, 1.0], [-0.7071067811865476, 1.0, 0.7071067811865476]],
          [[0.0, -0.7071067811865475, 1.0], [0.7071067811865476, 1.0, 0.7071067811865476]],
          [[0.0, 0.7071067811865475, 1.0], [-0.7071067811865476, 1.0, -0.7071067811865476]],
          [[0.0, 0.7071067811865475, 1.0], [0.7071067811865476, 1.0, -0.7071067811865476]],
          [[-0.7071067811865476, -0.7071067811865476, 1.0], [0.0, 1.0, 0.7071067811865475]],
          [[0.7071067811865476, -0.7071067811865476, 1.0], [0.0, 1.0, 0.7071067811865475]],
          [[-0.7071067811865476, 0.7071067811865476, 1.0], [0.0, 1.0, -0.7071067811865475]],
          [[0.7071067811865476, 0.7071067811865476, 1.0], [0.0, 1.0, -0.7071067811865475]]]
from copy import deepcopy

def listAposition(lst, position):
    """Transforme liste coordonnées en liste position dans Peres"""
    l = deepcopy(lst)
    
    for idx, i in enumerate(lst):
        for iidx, ii in enumerate(i):
            for iiidx, iii in enumerate(position):
                if ii == iii:
                    l[idx][iidx] = iiidx
                    break
    return l

def binInt(n):
    """ """
    return [int(x) for x in bin(n)[2:]]

def add33Bits(l, n):
    """ """
    for i in range(n):
        if len(l) < n:
            l.insert(0,0)
    return l

## Créer liste triplets correspondant position dans direction
tripletsPosition = listAposition(triplets, directionsPeres)
pairesPosition = listAposition(paires, directionsPeres)

# Boucle tant que somme != 2
somme = 0
itr = 0
while somme != 2:
    itr +=1
    lst33Bin = add33Bits(binInt(itr), 33)
    
    for idx, i in enumerate(tripletsPosition):
        if (lst33Bin[int(i[0])] + lst33Bin[int(i[1])] + lst33Bin[int(i[2])]) >=2:
           print(f'{itr} est le premier nombre avec les vecteurs : {triplets[idx]}')
           somme = 2

# Nota Bene: 14.25it/s
