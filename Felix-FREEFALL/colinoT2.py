"""

@author: Robertof
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

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

#plt.plot(altitude,vsom, '-r')
#plt.plot(altitude,pressao, '-b')

#!constantes
G = 6.67E-11 #unidades
m = 118 # kg
Me = 5.98E24 #kg verifique
R_terra = 6356.8E3 # metros
const_gas = 8.314 #mol-1 K-1
Ma = 0.029 #kg mol-1
gamma = 1.4
g=9.71
CDA = 0.18
#!constantes

Ace=np.zeros(len(altitude))
Vel=np.zeros(len(altitude))
Fd= np.zeros(len(altitude))

Ace[0] = 9.71
Vel[0]=0.0
Fd[0]=0.0


Fg=G*m*Me/(R_terra + altitude)**2
tempo=np.arange(50,len(altitude),1)


for t in tempo:
    Vel[t]=np.sqrt((Vel[t-1])**2+2*Ace[t-1]*altitude[t])
    Ace[t]=g - 0.5*CDA*pressao[t]*Vel[t-1]**2
    Fd[t]= -0.5*CDA*densidade[t]*Vel[t-1]**2


plt.plot(densidade,altitude,'b',lw=2)
plt.title('Pressao Atmosferica''//dados analisados='+str(len(altitude)))
plt.xlabel('Pressao(Pa)', fontsize = 16) 
plt.ylabel('Altitude (m)', fontsize = 16)
plt.grid(True)
plt.savefig('grafico_PRESSAO.JPG',dpi = 800,bbox_inches='tight')
plt.show()
plt.close()

plt.plot(temperatura,altitude,'b',lw=2)
plt.title('Temperatura''//dados analisados='+str(len(altitude)))
plt.xlabel('Temperatura(k)', fontsize = 16) 
plt.ylabel('Altitude (m)', fontsize = 16)
plt.grid(True)
plt.savefig('grafico_Temperatura.JPG',dpi = 800,bbox_inches='tight')
plt.show()
plt.close()

plt.plot(densidade,altitude,'b',lw=2)
plt.title('Densidade Atmosferica''//dados analisados='+str(len(altitude)))
plt.xlabel('Densidade(Kg/m3)', fontsize = 16) 
plt.ylabel('Altitude (m)', fontsize = 16)
plt.grid(True)
plt.savefig('grafico_DensidadeV.JPG',dpi = 800,bbox_inches='tight')
plt.show()
plt.close()

plt.plot(vsom,altitude,'-r')
plt.title('Velocidade do Som''//dados analisados='+str(len(altitude)))
plt.xlabel('Velocidade do Som (m/s)', fontsize = 16) 
plt.ylabel('Altitude (m)', fontsize = 16)
plt.grid(True)
plt.savefig('grafico_vsom.jpg',dpi = 800,bbox_inches='tight')
plt.show()
plt.close()

plt.plot(Fg,altitude,'k',lw=2)
plt.title('Forca Gravitacional''//dados analisados='+str(len(altitude)))
plt.xlabel('G Force (N)', fontsize = 16) 
plt.ylabel('Altitude (m)', fontsize = 16)
plt.grid(True)
plt.savefig('grafico_Fg.JPG',dpi = 800,bbox_inches='tight')
plt.show()
plt.close()
