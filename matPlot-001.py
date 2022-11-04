#
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html
# https://matplotlib.org/stable/gallery/index.html
#
import matplotlib.pyplot as plt
import numpy as np

plt.title('Sinusoïde')
plt.ylabel('axe Y')
plt.xlabel('axe X')

# Create a list of evenly-spaced numbers over the range
x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))           # Plot the sine of each x point
plt.plot(x, np.sin(x + 3.14/8))  # Plot the sine of each x point
plt.show()                       # Display the plot
