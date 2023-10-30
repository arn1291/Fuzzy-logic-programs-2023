import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz

x = np.arange(0, 5.05, 0.1)
mfx = fuzz.trapmf(x, [2, 2.5, 3, 4.5])

defuzz_bisector = fuzz.defuzz(x, mfx, 'bisector')
defuzz_mom = fuzz.defuzz(x, mfx, 'mom')

print('Bisector defuzzification result:', defuzz_bisector)
print('mean of maximum defuzzification result:', defuzz_mom)

plt.plot(x, mfx, 'k')
plt.vlines(defuzz_bisector, 0, fuzz.interp_membership(x, mfx, defuzz_bisector),
             label='Bisector', color='b')
plt.vlines(defuzz_mom, 0, fuzz.interp_membership(x, mfx, defuzz_mom),
             label='mean of maximum', color='g')
plt.show()
