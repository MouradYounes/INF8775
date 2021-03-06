#!/usr/bin/python3
import random
import math
import sys
import time
import csv

from brute_force import execute_brute_force
from DpR import execute_DpR
from utils import GRID_SIZE

PATH = "../Echantillons/"

'''
Un point est représenté par un tuple (position_x, position_y)
La fonction generate_points génère une liste de N points.
'''
def generate_points(FILE):
    with open(PATH+FILE) as f:
        #Skip first line
        next(f)
        mylist = [tuple(map(float, i.split(' '))) for i in f]
    return mylist


'''
--------------------------------------------------------------------
ATTENTION : Dans votre code vous devez utiliser le générateur gen.py
pour générer des points. Vous devez donc modifier ce code pour importer
les points depuis les fichiers générés.
De plus, vous devez faire en sorte que l'interface du tp.sh soit
compatible avec ce code (par exemple l'utilisation de flag -e, -a, (p et -t)).
--------------------------------------------------------------------
 '''

def main(argv):

    POINTS = generate_points(argv[1])
    sorted_points_x = sorted(POINTS, key=lambda x: x[0])
    sorted_points_y = sorted(POINTS, key=lambda x: x[1])
    
    if argv[0] == "BF":
        #Exécuter l'algorithme force brute
        time_BF, min_DistanceBF = execute_brute_force(sorted_points_x)
        if '-t' in argv:
            print("Temps : ", time_BF)
        if '-p' in argv:
            print("Plus petite distance: ", min_DistanceBF)
    
    elif argv[0] == "DPR":
        #Exécuter l'algorithme Diviser pour régner
        SEUIL_DPR = 3
        time_DPR, min_DistanceDPR = execute_DpR(sorted_points_x, sorted_points_y, SEUIL_DPR)
        if '-t' in argv:
            print("Temps : ", time_DPR)
        if '-p' in argv:
            print("Plus petite distance: ", min_DistanceDPR)
    
    elif argv[0] == "seuil":
        SEUIL_DPR = 4
        time_DPR, min_DistanceDPR = execute_DpR(sorted_points_x, sorted_points_y, SEUIL_DPR)
        if '-t' in argv:
            print("Temps : ", time_DPR)
        if '-p' in argv:
            print("Plus petite distance: ", min_DistanceDPR)

if __name__ == "__main__":
    main(sys.argv[1:])