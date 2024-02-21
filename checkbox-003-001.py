""" matPlotLib - CheckButtons

    + sur une deuxième ax ...

    https://matplotlib.org/stable/gallery/widgets/check_buttons.html
"""
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.widgets import CheckButtons

t = np.arange(0.0, 2.0, 0.01)
s0 = np.sin(2*np.pi*t)
s1 = np.sin(4*np.pi*t)
s2 = np.sin(6*np.pi*t)

fig, (ax1, ax2) = plt.subplots( 2, 1 )
line0, = ax1.plot(t, s0, visible=False, lw=2, color='black', label='1 Hz')
line1, = ax1.plot(t, s1, lw=2, color='red', label='2 Hz')
line2, = ax2.plot(t, s2, lw=2, color='green', label='3 Hz')

lines_by_label = {l.get_label(): l for l in [line0, line1, line2]}
line_colors = [l.get_color() for l in lines_by_label.values()]

# Make checkbuttons with all plotted lines with correct visibility
#rax = ax1.inset_axes([0.0, 0.0, 0.12, 0.2])
rax = ax1.inset_axes([0.85, 0.0, 0.15, 0.5]) # (left, bottom, width, height)
check = CheckButtons(
    ax=rax,
    labels=lines_by_label.keys(),
    actives=[l.get_visible() for l in lines_by_label.values()],
    label_props={'color': line_colors},
    frame_props={'edgecolor': line_colors},
    check_props={'facecolor': line_colors},
)

def callback(label):
    ln = lines_by_label[label]
    ln.set_visible(not ln.get_visible())
    ln.figure.canvas.draw_idle()

check.on_clicked(callback)

plt.show()