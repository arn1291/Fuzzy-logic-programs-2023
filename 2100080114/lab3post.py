import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
t = np.linspace(-10, 50, 100)


warm = fuzz.trapmf(t, [20, 25, 30, 35])
moderate = fuzz.trapmf(t ,[10, 15, 20, 25])
cold = fuzz.trapmf(t, [-5, 0, 5, 10])
hot = fuzz.trapmf(t, [30, 35, 40, 45])
plt.plot(t, warm, label='Warm')
plt.plot(t, moderate, label='Moderate')
plt.plot(t, cold, label='Cold')
plt.plot(t, hot, label='Hot')
plt.show()
