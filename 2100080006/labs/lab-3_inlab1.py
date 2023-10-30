import matplotlib.pyplot as plt
import skfuzzy as fuzz
import numpy as np



height=np.linspace(3,6.5,35)

tall_mf=fuzz.trimf(height,[5,5.75,6.4])
verytall_mf=fuzz.trimf(height,[6,6.25,6.4])
normal_mf=fuzz.trimf(height,[5,5.5,5.9])
veryshort_mf=fuzz.trimf(height,[3,3.75,4.5])
short_mf=fuzz.trimf(height,[4.5,4.75,5.5])

plt.plot(height,normal_mf, label='Normal')
plt.plot(height,tall_mf ,label='Tall')
plt.plot(height,verytall_mf ,label='Very Tall')
plt.plot(height,veryshort_mf, label='Very Short')
plt.plot(height,short_mf, label='Short')


plt.legend()
plt.show()