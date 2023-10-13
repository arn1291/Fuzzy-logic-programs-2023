import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

x = np.linspace(0,190,190)

very_tall = fuzz.trimf(x, [170,180,190])
tall= fuzz.trimf(x, [150,160,170])
normal = fuzz.trimf(x, [150,160,170])
short = fuzz.trimf(x, [130,140,150])
very_short = fuzz.trimf(x, [110,120,130])


plt.plot(x,very_tall)
plt.plot(x,tall)
plt.plot(x,normal)
plt.plot(x,short)
plt.plot(x,very_short)
plt.show()
