import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from numpy.fft import fft
import sounddevice as sd

x_r, fm = sf.read('AUDIO_Ex4.wav')

#Seleccio de la finestra (25ms)
T = 0.025                                                                                          
L = int(fm * T)                      
Tm=1/fm                              
t=Tm*np.arange(L)                          
sf.write('AUDIO_Ex4.wav', x_r, fm)   

plt.figure(3)                             # Nova figura
plt.plot(t[0:L], x_r[0:L])                # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('25ms de audio')                # Títol del gràfic
plt.show()  

N=5000                        
X=fft(x_r[0 : L], N) 

k=np.arange(N)
plt.figure(4)
plt.plot(k,X)
plt.title('Transformada del senyal')  
plt.show()

# Exercici 3
Xdb = 20*np.log10(1.e-1 + np.abs(X)/(max(np.abs(X))))
fk = (k/N)*(fm/2)

plt.figure(5)
plt.plot(fk,Xdb)
plt.title('Modul Transformada del senyal')  
plt.show()