# https://stacklima.com/matplotlib-dates-datestr2num-en-python/
#
# usualy mdates is declared like this
# import matplotlib.dates as mdates
#
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import (
    DateFormatter,
    AutoDateLocator,
    AutoDateFormatter,
    datestr2num
)


days = [
    '30/01/2019 00:00',
    '31/01/2019 00:00',
    '01/02/2019 00:00',
    '02/02/2019 00:00',
    '03/02/2019 00:00',
    '04/02/2019 00:00'
]
data1 = [2, 5, 13, 6, 11, 7]
data2 = [6, 3, 10, 3, 6, 5]

z = datestr2num([
    datetime.strptime(day, '%d/%m/%Y %H:%M').strftime('%m/%d/%Y %H:%M')
    for day in days
])

r = 0.25

figure = plt.figure(figsize=(8, 4))
axes = figure.add_subplot(111)

axes.bar(z - r, data1, width=2 * r,
         color='g', align='center',
         tick_label='day')

axes.bar(z + r, data2, width=2 * r,
         color='y', align='center',
         tick_label='day')

axes.xaxis_date()
axes.xaxis.set_major_locator(
    AutoDateLocator(minticks=3, interval_multiples=False))

axes.xaxis.set_major_formatter(DateFormatter("%d/%m/%y"))

plt.show()
