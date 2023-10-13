import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
height=np.linspace(3,7.5,35)
verytall=fuzz.trapmf(height,[6.1,6.6,6.8,7.5 ])
tall=fuzz.trapmf(height, [5.0, 5.5, 6.0, 6.4])
normal=fuzz.trapmf(height,[4.9, 5.3, 5.5, 5.7])
short=fuzz.trapmf(height,[4.1, 4.6, 5.1, 5.5])
veryshort=fuzz.trapmf(height,[3.0, 3.6, 4.1, 4.3])
o=fuzz.defuzz(height,verytall,"centroid")
o2=fuzz.defuzz(height,tall,"centroid")

g=[6.1,6.6,6.8,7.5]
g2=[5.0, 5.5, 6.0, 6.4]
plt.plot(height,verytall,label='Very Tall')
plt.plot(height,tall,label='Tall')
plt.plot(height,normal,label='Normal')
plt.plot(height,short, label='Short')
plt.plot(height,veryshort, label='Very Short')
plt.show()
print(o,o2)
print(np.mean(g))
print(np.mean(g2))
