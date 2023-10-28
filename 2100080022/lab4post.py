!pip install -U scikit-fuzzy
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
x = np.arange(0, 10, 0.1)
mf = fuzz.gaussmf(x, 5, 2)
plt.plot(x, mf)
plt.show()
z = fuzz.interp_membership(x, mf, 6.5)
print(z)
y = fuzz.defuzz(x, mf, 'centroid')
print(y)
