import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

x = np.arange(0, 11, 0.1)

# Define fuzzy sets
low = fuzz.trimf(x, [0, 0, 5])
medium = fuzz.trimf(x, [0, 5, 10])
high = fuzz.trimf(x, [5, 10, 10])

# Plot
plt.figure()
plt.plot(x, low, 'b', label='Low')
plt.plot(x, medium, 'g', label='Medium')
plt.plot(x, high, 'r', label='High')
plt.title('Fuzzy Membership Functions')
plt.legend()
plt.show()
