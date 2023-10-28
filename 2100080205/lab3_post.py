import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

categories = ['Warm', 'Moderate', 'Cold', 'Hot']
category_params = {
    'Warm': {'mean': 25, 'std_dev': 3},
    'Moderate': {'mean': 15, 'std_dev': 4},
    'Cold': {'mean': 5, 'std_dev': 3},
    'Hot': {'mean': 35, 'std_dev': 5}
}
x = np.linspace(0, 50, 100)

plt.figure(figsize=(12, 6))

for category in categories:
    params = category_params[category]
    pdf = norm.pdf(x, params['mean'], params['std_dev'])

    plt.plot(x, pdf, label=category)

plt.title('Gaussian Membership Functions for Temperature Categories')
plt.xlabel('Temperature')
plt.ylabel('Membership')
plt.legend()
plt.grid(True)
plt.show()
