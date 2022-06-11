print('Hello World')

## CAGR 
import numpy as np
import random
import matplotlib.pyplot as plt
import csv

import pandas as pd

x=np.random.uniform(100000,990000,10)
y=np.random.uniform(1000000,9900000,10)
Year=list(range(2001,2011))
def CAGR(ini,fin,n):
    return ((fin/ini) ** (1/n)-1)*100
for i,j in zip(x,y):
    CAG=CAGR(x,y,10)

f = open("CAGR.txt", "w")
f.write("Intial\t"+"Final\t"+"Year\t"+"CAGR\n")
for i,j,k,l in zip(x,y,Year,CAG):
    f.write(str(i)+"\t"+str(j)+"\t"+str(k)+"\t"+str(l)+"\n")

f.close()

f1=pd.read_table("CAGR.txt")
plt.plot(f1.Year,f1.CAGR)
plt.show()


