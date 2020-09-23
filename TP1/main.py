import random
import math
import sys
import time
import csv

from brute_force import execute_brute_force
from DpR import execute_DpR
from utils import GRID_SIZE

ALGO = "BF" #sys.argv[1] # Algo à utiliser DPR ou BF
FILE = "ex1000.txt" #sys.arg[2] #Nom du fichier ou on va extraire les points
#NB_POINTS = int(sys.argv[2]) # Nombre de points à générer
PATH = "../tp1-A20/"

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

def main(algo, file):
    POINTS = generate_points(file)
    sorted_points_x = sorted(POINTS, key=lambda x: x[0])
    sorted_points_y = sorted(POINTS, key=lambda x: x[1])
    
    if algo == "BF":
        #Exécuter l'algorithme force brute
        time_BF = execute_brute_force(sorted_points_x)
        print("Temps : ", time_BF)
    
    elif algo == "DPR":
        #Exécuter l'algorithme Diviser pour régner
        SEUIL_DPR = 3
        time_DPR = execute_DpR(sorted_points_x, sorted_points_y, SEUIL_DPR)
        print("Temps : ", time_DPR)

main(ALGO, FILE)