#MARTA ENRICH GARCIA

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd
from numpy.fft import fft
import os

T= 0.025                               
data, fm =sf.read('meg_part4.wav')       
L = int(fm * T)                     
Tm=1/fm                            
t=Tm*np.arange(L)                  

print('Frecuencia de muestreo:',fm)

print('Numero de muestras:',L)

plt.figure(0)                          
plt.plot(t[0:L],data[0:L])              
plt.xlabel('t en segons')               
plt.title('Senyal 25ms')  
plt.show()                             


N=5000 
X=fft(data[0:L],N) 
k=np.arange(N)  
X_dB = 20*np.log10(np.abs(X)/max(np.abs(X)))
fk = k[0:N//2+1]*fm/N         #Calcul de la fk, pels valors de l'eix d'abscisses
plt.figure(1)
plt.subplot(211)   
plt.plot(fk,X_dB[0:N//2+1])  # Representació del mòdul de la transformada en dB y de 0 a FK/2
plt.title(f'Transformada del senyal de Ls={L} mostres amb DFT de N={N}')   
plt.ylabel('Mòdul en dB')                  
plt.subplot(212)                      
plt.plot(fk,np.unwrap(np.angle(X[0:N//2+1])) )   
plt.xlabel('f en Hz')                
plt.ylabel('$\phi_x[k]$')              
plt.show() 
