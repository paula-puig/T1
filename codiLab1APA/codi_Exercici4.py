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

plt.figure(0)                             # Nova figura
plt.plot(t[0:L], x_r[0:L])                # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('25ms de audio')                # Títol del gràfic
plt.show()  