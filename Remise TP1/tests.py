#!/usr/bin/python3
import random
import math
import sys
import time
import csv
import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import sys

from brute_force import execute_brute_force
from DpR import execute_DpR
from utils import GRID_SIZE

'''
Fonction qui calcule le test de puissance
'''
def test_puissance(tablePath):
    data = pd.read_csv(tablePath)
    AlgoNames = ["BF", "DPR", "seuil"]
    colors = ["b", "r", "g"]
    plt.clf()
    fig = plt.figure()   
    ax = fig.add_subplot(1,1,1)
    ax.set_xlabel('log n')
    ax.set_ylabel('log (temps)')
    #Tests de puissances
    for i in range(3):
        x = np.array(np.log(data["taille"][(6*i):(6*i)+6]))
        y = np.array(np.log(data["temps"][(6*i):(6*i)+6]))
        ax.scatter(x, y, c = colors[i], label = data["methode"][(6*i)])
        print(np.poly1d(np.polyfit(x, y, 1))(x))
        ax.plot(x, np.poly1d(np.polyfit(x, y, 1))(x),c= colors[i])
        print(np.polyfit(x, y, 1))
        
        ax.legend(loc="lower right")
        plt.show()
        fig.savefig("Puissance" + AlgoNames[i])

'''
Fonction qui calcule le test de rapport
'''
def test_rapport(tablePath):
    data = pd.read_csv(tablePath)
##        On change fx n**2 pour brute et nlog(n) pour recursif et seuil
    data["temps"] = data["temps"]/(data["taille"]**2)
    AlgoNames = ["BF", "DPR", "seuil"]
    colors = ["b", "r", "g"]
    for i in range(3):
        plt.clf()
        fig = plt.figure()   
        ax = fig.add_subplot(1,1,1)
        x = np.array(data["taille"][(6*i):(6*i)+6])
        y = np.array(data["temps"][(6*i):(6*i)+6])
        ax.scatter(x, y, c = colors[i], label = data["methode"][(6*i)])
        print(np.polyfit(x, y, 1))
    
        ax.legend(loc="lower right")
        plt.show()
        fig.savefig("Rapport" + AlgoNames[i])

'''
Fonction qui va calculer le test de constante
'''
def test_constante(tablePath):
    data = pd.read_csv(tablePath)
    AlgoNames = ["BF", "DPR", "seuil"]
    colors = ["b", "r", "g"]

    for i in range(3):
        plt.clf()
        fig = plt.figure()   
        ax = fig.add_subplot(1,1,1)
##        On change fx n**2 pour brute et nlog(n) pour recursif et seuil
        fx=(data["taille"][(6*i):(6*i)+6])**2
        x = np.array(fx)
        y = np.array(data["temps"][(6*i):(6*i)+6])
        ax.scatter(x, y, c = colors[i], label = data["methode"][(6*i)])
        ax.plot(x, np.poly1d(np.polyfit(x, y, 1))(x),c= colors[i])
        print(np.poly1d(np.polyfit(x, y, 1))(x))
    
        ax.legend(loc="lower right")
        plt.show()
        fig.savefig("constante" + AlgoNames[i])
