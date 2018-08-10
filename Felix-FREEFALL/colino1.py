# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 03:54:53 2017

@author: Robertof
"""
import matplotlib.pyplot as plt
import numpy as np
import math


#import csv
#arq = open('C:/Users/Robertof/Desktop/reprolicen/COLINO/teste/COLINODADOS.txt','r')
#for linha in arq:
#    a, b, c, d = linha.split()
#    altitude.append(float(a))
#    valor2.append(int(b))
#
#vetor1 = np.array(valor1)

#arq1 = open('C:/Users/Robertof/Desktop/reprolicen/COLINO/teste/temperatura.txt','r')
#
#texto = arq.read()
#texto1 = arq1.read()
##arq.writelines(texto)
#T = len(texto)
#print(texto,texto1)
#print(T)
#print(type(variavel))
#arq.close
G = 6.67E-11 #unidades
m = 118 # kg
Me = 5.98E24 #kg verifique
R_terra = 6356.8E3 # metros
const_gas = 8.314 #mol-1 K-1
Ma = 0.029 #kg mol-1
gamma = 1.4


z=altitude = [1 , 1000 , 2000 , 3000 , 4000 , 5000 , 6000 , 7000 , 8000]
altitude += [9000 , 10000 , 12000 , 15000 , 20000 , 25000 , 30000 , 35000 , 40000] 
temperatura =(288.15,281.65,275.15,268.65,262.15,255.65,249.15,242.65,236.15,229.65,223.15,216.65,216.65,216.65,221.65,226.65,237.05,251.05)
pressao = (10132500000,8987460000,7949520000,7010850000,6164020000,5401990000,4718100000,4106070000,3559980000,3074250000,2643630000,1933040000,1204460000,547489000,251102000,117187000,55892400,27752200)
Nz = len(altitude)
Fg = np.empty(Nz, dtype = float)
gravidade = np.empty(Nz, dtype = float)

vsom = np.empty(Nz, dtype = float)

for i in range(Nz):
    Fg[i] = G*m*Me/(R_terra+altitude[i])**2
    gravidade[i] = G*Me/(R_terra+altitude[i])**2
    vsom[i] = math.sqrt(gamma * const_gas * temperatura[i] / Ma)

plt.plot(z,Fg,'ob')
plt.savefig('grafico_Fg.png')
plt.show()
plt.close()

plt.plot(z,vsom,'-r')
plt.show()
plt.savefig('grafico_vsom.png')
plt.close()

