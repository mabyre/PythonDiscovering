#
#  Load datas form files then plot in a graph
#
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html
# https://matplotlib.org/stable/gallery/index.html
#
# https://pythonprogramming.net/matplotlib-python-3-basics-tutorial/?completed=/python-3-subprocess-tutorial/
#
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

x, y = np.loadtxt('.\datas\courbe-000.txt',
                  unpack=True,
                  delimiter=',')

x1, y1 = np.loadtxt('.\datas\courbe-001.txt',
                    unpack=True,
                    delimiter=',')

plt.plot(x, y, label='courbe un')
plt.plot(x1, y1, label='courbe deux')

plt.title('MySample')
plt.ylabel('axe Y')
plt.xlabel('axe X')
plt.legend()

plt.show()
