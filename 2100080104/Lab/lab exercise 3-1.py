import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
x=np.linspace(5,10,10)
very_tall = fuzz.trimf(x,[6.3,6.5,6.8])
tall=fuzz.trimf(x,[5.9,6.0,6.2])
normal=fuzz.trimf(x,[5.6,5.7,5.8])
short=fuzz.trimf(x,[5.3,5.4,5.5])
very_short=fuzz.trimf(x,[4.8,4.9,5.0])
heights_memberFunction={
    'very_tall':very_tall,
    'tall':tall,
    'normal':normal,
    'short':short,
    'very_short':very_short
 }
plt.figure(figsize=(8,6))
for a,b in heights_memberFunction.items():
    plt.plot(x,b)
plt.xlabel('Height')
plt.ylabel('membership')
plt.grid('True')
plt.show()
obj = fuzz.defuzz(x,tall,'centroid')
print(obj)
