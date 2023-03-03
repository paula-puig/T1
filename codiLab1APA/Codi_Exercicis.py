import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from numpy.fft import fft
import sounddevice as sd

# Exercici 1
T= 2.5                               
fm=8000                              
fx=4000                               
A=4                                  
pi=np.pi                             
L = int(fm * T)                      
Tm=1/fm                              
t=Tm*np.arange(L)                    
x = A * np.cos(2 * pi * fx * t)      
sf.write('so_Lab1APA.wav', x, fm)

# Exercici 2
x_r, fm = sf.read('so_Lab1APA.wav')
Tx=1/fx                                  
Ls=int(fm*5*Tx)                           

plt.figure(0)                             
plt.plot(t[0:Ls], x[0:Ls])                
plt.xlabel('t en segons')                 
plt.title('5 periodes de la sinusoide')   
plt.show()  

sd.play(x, fm)
     
N=5000                        
X=fft(x[0 : Ls], N) 

k=np.arange(N)
plt.figure(1)
plt.plot(k,X)
plt.title('Transformada del senyal')  
plt.show()

# Exercici 3
Xdb = 20*np.log10(1.e-1 + np.abs(X)/(max(np.abs(X))))
fk = (k/N)*(fm/2)

plt.figure(2)
plt.plot(fk,Xdb)
plt.title('Modul Transformada del senyal')  
plt.show()


 

