import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz

race = np.linspace(1, 10, 100)

white_membership = fuzz.gaussmf(race, 1.75, 1)
moderate_membership = fuzz.gaussmf(race, 4.75, 1)
black_membership = fuzz.gaussmf(race, 7.75, 1)

plt.plot(race, white_membership, label='White')
plt.plot(race, moderate_membership, label='Moderate')
plt.plot(race, black_membership, label='Black')

plt.legend()

plt.show()
