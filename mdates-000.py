#
# https://stacklima.com/matplotlib-dates-datestr2num-en-python/
#
#
# PAY ATTENTION :
# A very important thing is to remark that in datestr2num function
# strptime mask is different from strftime mask
#
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

days = [
    '30/01/2019',
    '31/01/2019',
    '01/02/2019',
    '02/02/2019',
    '03/02/2019',
    '04/02/2019'
]
data1 = [2, 5, 13, 6, 11, 7]
data2 = [6, 3, 10, 3, 6, 5]

z = mdates.datestr2num([
    datetime.strptime(day, '%d/%m/%Y').strftime('%m/%d/%Y')
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
    mdates.AutoDateLocator(minticks=3, interval_multiples=False))

axes.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m/%y"))

plt.show()
