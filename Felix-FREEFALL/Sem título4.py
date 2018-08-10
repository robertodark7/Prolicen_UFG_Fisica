# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 13:58:19 2017

@author: Robertof
"""

import numpy as np
import matplotlib.pyplot as plt
import math

vetor1=[]
vetor2=[]
vetor3=[]
vetor4=[]
vetor5=[]
arq = open('DadosGR1.txt','r')

for linha in arq:
    a,b,c,d,e = linha.split(';')
    vetor1.append (float(a))
    vetor2.append (float(b))
    vetor3.append (float(c))
    vetor4.append (float(d))
    vetor5.append (float(e))

altitude    = np.array(vetor1)
temperatura = np.array(vetor2)
pressao     = np.array(vetor3)
densidade   = np.array(vetor4)
vsom        = np.array(vetor5)

#!constantes
G = 6.67E-11 #unidades
m = 118 # kg
Me = 5.98E24 #kg verifique
R_terra = 6356.8E3 # metros
const_gas = 8.314 #mol-1 K-1
Ma = 0.029 #kg mol-1
gamma = 1.4
Cda = 0.18
g = G*Me/(R_terra+altitude[780])**2        
#!constantes



for i in range (len(altitude)): 
    a= g-(1/2*m*Cda*densidade[i]*V[i-1])
    V=(np.sqrt(V[i-1]**22*a[i]*(range(0,39000,50))))




print (V)

#Fg=G*m*Me/(R_terra + altitude)**2
#          
#plt.plot(Fg,altitude,'ob')
#plt.title('Forca Gravitacional''//dados analisados='+str(len(altitude)))
#plt.xlabel('Forca G(N)', fontsize = 16) 
#plt.ylabel('Altitude (m)', fontsize = 16)
#plt.savefig('grafico_Fg.png')
#plt.grid(True)
#plt.show()
#plt.close()
#
#plt.plot(vsom,altitude,'-r')
#plt.title('Velocidade do Som''//dados analisados='+str(len(altitude)))
#plt.xlabel('Velocidade do Som (m/s)', fontsize = 16) 
#plt.ylabel('Altitude (m)', fontsize = 16)
#plt.savefig('grafico_vsom.png')
#plt.grid(True)
#plt.show()
#plt.close()

