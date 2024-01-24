""" Using Pandas
    
    for matPlot-005 i use Numpy is it easiest to use Pandas?
"""
import matplotlib.pyplot as plt
import pandas as pd

FILE_NAME = r'.\datas\CARMAT_2024-01-19 (1).txt'

# Read data in DataFrame df
df = pd.read_csv(FILE_NAME, sep='\t', parse_dates=['date'])

# Cool way yo read file's data 
print(df)

# -------------
# Display Graph
# -------------
axe_date = plt.subplot2grid((1, 1), (0, 0), rowspan=1, colspan=1)
for label in axe_date.xaxis.get_ticklabels():
    label.set_rotation(45)
plt.setp(axe_date.get_xticklabels(), visible=True)
plt.plot(df['date'],df['ouv'], color='midnightblue', label=f"ouv")
plt.title(f"PANDAS")
plt.xlabel(f'date')
plt.ylabel(f'price')
plt.grid(True, linestyle='--', linewidth=0.5, color='gray')
plt.legend
# Otherwise dates are ploted out of graph
plt.subplots_adjust(left=0.11, bottom=0.24, right=0.90, top=0.90, wspace=0.2, hspace=0)
plt.show()
