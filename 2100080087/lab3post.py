import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz

temp = np.linspace(-10, 50, 100)


warm_membership = fuzz.trapmf(temp, [20, 25, 30, 35])
moderate_membership = fuzz.trapmf(temp, [10, 15, 20, 25])
cold_membership = fuzz.trapmf(temp, [-5, 0, 5, 10])
hot_membership = fuzz.trapmf(temp, [30, 35, 40, 45])

plt.plot(temp, warm_membership, label='Warm')
plt.plot(temp, moderate_membership, label='Moderate')
plt.plot(temp, cold_membership, label='Cold')
plt.plot(temp, hot_membership, label='Hot')


plt.legend()
plt.show()
