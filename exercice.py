#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
import sys
sys.path.insert(0, 'C:\\Users\Tianna\Documents\GitHub\H2021\\2021h-ch6-1-exercices-VincentHuaa')
from _exercice_version_prof import frequence
from turtle import *




# TODO: Définissez vos fonction ici

def fct_ellipsoide (a=5, b=4, c=7, masse_vol=0.8):

    volume = 4/3 * math.pi * a * b * c
    masse = masse_vol * volume

    return volume, masse


def draw_branch(branch_len, pen_size, angle):
    if branch_len > 0 and pen_size > 0:
        pensize(pen_size)
        forward(branch_len)
        right(angle)
        draw_branch(branch_len - 10 , pen_size - 1, angle - 5)
        left(angle * 2)
        draw_branch(branch_len - 10, pen_size - 1, angle - 5)
        right(angle)
        backward(branch_len)


def draw_tree():
    setheading(90)
    color("green")
    draw_branch(70, 7, 35)

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(fct_ellipsoide())
    print((lambda sentence: sorted(frequence(sentence), key=frequence(sentence).__getitem__)[-1])("test test test test"))
    draw_tree()

