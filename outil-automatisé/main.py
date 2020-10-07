#!/usr/bin/python3
import random
import math
import sys
import time
import csv
import csv
import numpy as np

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
Fonction qui va permettre de lire le data de csv
'''
def read_data(file):
    brutefore_array100 = []
    brutefore_array1k = []
    brutefore_array10k = []
    brutefore_array30k = []
    brutefore_array50k = []
    brutefore_array100k = []

    DPR_array100 = []
    DPR_array1k = []
    DPR_array10k = []
    DPR_array30k = []
    DPR_array50k = []
    DPR_array100k = []

    seuil_array100 = []
    seuil_array1k = []
    seuil_array10k = []
    seuil_array30k = []
    seuil_array50k = []
    seuil_array100k = []

    with open(file, 'r') as file:
        next(file)
        reader = csv.reader(file)
        for row in reader:
            if "BF" in row[0]:
                if "100_" in row[0]:
                    brutefore_array100.append(float(row[0].split("|")[2]))
                elif "1k" in row[0]:
                    brutefore_array1k.append(float(row[0].split("|")[2]))
                elif "10k" in row[0]:
                    brutefore_array10k.append(float(row[0].split("|")[2]))
                elif "30k" in row[0]:
                    brutefore_array30k.append(float(row[0].split("|")[2]))
                elif "50k" in row[0]:
                    brutefore_array50k.append(float(row[0].split("|")[2]))                    
                elif "100k" in row[0]:
                    brutefore_array100k.append(float(row[0].split("|")[2]))
            elif "DPR" in row[0]:
                if "100_" in row[0]:
                    DPR_array100.append(float(row[0].split("|")[2]))
                elif "1k" in row[0]:
                    DPR_array1k.append(float(row[0].split("|")[2]))
                elif "10k" in row[0]:
                    DPR_array10k.append(float(row[0].split("|")[2]))
                elif "30k" in row[0]:
                    DPR_array30k.append(float(row[0].split("|")[2]))
                elif "50k" in row[0]:
                    DPR_array50k.append(float(row[0].split("|")[2]))                    
                elif "100k" in row[0]:
                    DPR_array100k.append(float(row[0].split("|")[2]))
            elif "seuil" in row[0]:
                if "100_" in row[0]:
                    seuil_array100.append(float(row[0].split("|")[2]))
                elif "1k" in row[0]:
                    seuil_array1k.append(float(row[0].split("|")[2]))
                elif "10k" in row[0]:
                    seuil_array10k.append(float(row[0].split("|")[2]))
                elif "30k" in row[0]:
                    seuil_array30k.append(float(row[0].split("|")[2]))
                elif "50k" in row[0]:
                    seuil_array50k.append(float(row[0].split("|")[2]))                    
                elif "100k" in row[0]:
                    seuil_array100k.append(float(row[0].split("|")[2]))                    

    method = ["brute","DPR","seuil"]
    lengthOfdata = ["100","1k","10k","30k","50k","100k"]
    average_brute = [sum(brutefore_array100) / len(brutefore_array100), sum(brutefore_array1k) / len(brutefore_array1k), sum(brutefore_array10k) / len(brutefore_array10k), sum(brutefore_array30k) / len(brutefore_array30k), sum(brutefore_array50k) / len(brutefore_array50k), sum(brutefore_array100k) / len(brutefore_array100k)]
    average_DPR = [sum(DPR_array100) / len(DPR_array100), sum(DPR_array1k) / len(DPR_array1k), sum(DPR_array10k) / len(DPR_array10k), sum(DPR_array30k) / len(DPR_array30k), sum(DPR_array50k) / len(DPR_array50k), sum(DPR_array100k) / len(DPR_array100k)]
    average_seuil = [sum(seuil_array100) / len(seuil_array100), sum(seuil_array1k) / len(seuil_array1k), sum(seuil_array10k) / len(seuil_array10k), sum(seuil_array30k) / len(seuil_array30k), sum(seuil_array50k) / len(seuil_array50k), sum(seuil_array100k) / len(seuil_array100k)]
    table = []
    for i in range(18):
        if i < 6:
            table.append([method[0], lengthOfdata[i], average_brute[i]])
        elif i < 12:
            table.append([method[1], lengthOfdata[i-6], average_DPR[i-6]])
        elif i < 18:
            table.append([method[2], lengthOfdata[i-12], average_DPR[i-12]])            
    
    with open("table.csv", "w") as f:
        f.write("methode" + "," + "taille" + "," + "temps" + "\n")
        for i in range(len(table)):
            f.write(table[i][0] + "," + table[i][1] + "," + str(table[i][2]) + "\n")



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
    if argv[0].lower() == "bf":
        #Exécuter l'algorithme force brute
        time_BF, min_DistanceBF = execute_brute_force(sorted_points_x)
        if '-t' in argv:
            print("Temps : ", time_BF)
        if '-p' in argv:
            print("Plus petite distance: ", min_DistanceBF)
        row=["BF",argv[1],time_BF,min_DistanceBF]
    
    elif argv[0].lower() == "dpr":
        #Exécuter l'algorithme Diviser pour régner
        SEUIL_DPR = 3
        time_DPR, min_DistanceDPR = execute_DpR(sorted_points_x, sorted_points_y, SEUIL_DPR)
        if '-t' in argv:
            print("Temps : ", time_DPR)
        if '-p' in argv:
            print("Plus petite distance: ", min_DistanceDPR)
        row=["DPR",argv[1],time_DPR,min_DistanceDPR]
        
    elif argv[0].lower() == "seuil":
        SEUIL_seuil = 4
        time_seuil, min_Distanceseuil = execute_DpR(sorted_points_x, sorted_points_y, SEUIL_seuil)
        if '-t' in argv:
            print("Temps : ", time_seuil)
        if '-p' in argv:
            print("Plus petite distance: ", min_Distanceseuil)
        row=["seuil",argv[1],time_seuil,min_Distanceseuil]
    
    with open('result.csv', 'a', newline='') as file:
        writer = csv.writer(file, delimiter='|')
        writer.writerow(row)

if __name__ == "__main__":

    samples=["ex100_","ex1k_","ex10k_","ex30k_","ex50k_","ex100k_"]
    first_row=["method","file name", "time", "result"]

    
##    with open('result.csv', 'w', newline='') as file:
##        writer = csv.writer(file, delimiter='|')
##        writer.writerow(first_row)
    # for sample in samples:
    #     for x in range(10):
    #         i=x+1
    #         filename=sample + str(i) + ".txt"
    #         main(["BF",filename,'-t','-p'])
    # for sample in samples:
    #     for x in range(10):
    #         i=x+1
    #         filename=sample + str(i) + ".txt"
    #         main(["DPR",filename,'-t','-p'])
##    for sample in samples:
##        for x in range(10):
##            i=x+1
##            filename=sample + str(i) + ".txt"
##            main(["seuil",filename,'-t','-p'])
                
    read_data("../outil-automatisé/result.csv")
    print("end")
