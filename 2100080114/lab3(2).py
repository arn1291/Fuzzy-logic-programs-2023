import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

x = np.linspace(1,10,120)

white = fuzz.gaussmf(x,1.54,1)
moderate= fuzz.gaussmf(x,5.8,1)
black = fuzz.gaussmf(x,8.4,1)
plt.plot(x,white,label='white')
plt.plot(x,moderate,label='white')
plt.plot(x,black,label='white')
plt.show()
