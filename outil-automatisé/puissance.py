import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os


data = pd.read_csv("table.csv")

sortingNames = ["BF", "DPR", "seuil"]
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
    ax.plot(x, np.poly1d(np.polyfit(x, y, 1))(x),c= colors[i])
    print(np.polyfit(x, y, 1))
    
ax.legend(loc="lower right")
plt.show()
fig.savefig("Puissance")

