import matplotlib.pyplot as plt
import pandas
from collections import Counter

def read() :
    lista = []
    with open('GEH.txt','r') as f:
        lines = f.read().split('\n')
        for i in lines:
            for j in i.split(' '):
                lista.append(j.lower())
        print(lista)
        f.close()
        return lista

plt.hist(read(),orientation="horizontal",edgecolor="black") #gives you a histogram of your array 'a'
#plt.hist(orientation="horizonta")
plt.show() #finishes out the plot