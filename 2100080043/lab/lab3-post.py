import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
t=np.linspace(-10,50,100)
cold=fuzz.trapmf(t, np.linspace(0,15,4))
moderate=fuzz.trapmf(t ,np.linspace(15,25,4))
warm=fuzz.trapmf(t,np.linspace(25,35,4))
hot=fuzz.trapmf(t,np.linspace(35,50,4))
plt.plot(t,warm,label='Warm')
plt.plot(t,moderate,label='Moderate')
plt.plot(t,cold,label='Cold')
plt.plot(t,hot,label='Hot')
plt.show()
