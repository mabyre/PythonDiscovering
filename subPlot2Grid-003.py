""" Understand subplot2grid

    work on your graph here before adapting it to the final graph
    It's hard tuff to make it work cause it depends on the function you ask 
    and the order in which you call them
    
    play with subplot2grid
"""
import matplotlib.pyplot as plt
import numpy as np

# -------------------------------------------------------------------------

def annotate_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)

# -----------------
# User's parameters
# -----------------

COMPAGNY_NAME = 'My Company'

PARAM_ONE = 50

PARAM_TWO = 50

# ----------------
# Create data test
# ----------------
#
x = np.linspace( 0, 10, 100 )
y1 = 1.18 * np.sin( 0.95 * x )
y2 = 1.89 * np.cos( 1.753 * x )

#-----
# Plot
#-----

# Specify Figure's size
fig = plt.figure( figsize = (8, 6) )
fig_shape = (8, 1)

# Plot ax1
ax1 = plt.subplot2grid( fig_shape, (0, 0), rowspan = 6 )
ax1.set_title( f"{COMPAGNY_NAME} days in past: {PARAM_ONE} EPOCHS: {PARAM_TWO}" )
ax1.set_ylabel( f'Label in y of Signal 1' )
ax1.plot( x, y1, label='Signal 1', color='blue' )
ax1.legend()

# Plot ax2
ax2 = plt.subplot2grid( fig_shape, (6, 0), rowspan = 2, sharex=ax1 )
ax2.set_title( f"Title of signal 2" )
ax2.set_ylabel( f'Label in y of Signal 2' )
ax2.plot( x, y2, label='Signal 2', color='green' ) 
ax2.legend()

# annotate_axes(fig) # It makes the axis labels disappear !!!

plt.legend()
plt.tight_layout()
plt.subplots_adjust( left=0.1, bottom=0.1, right=0.95, top=0.90, wspace=0 ) # hspace=0.4
plt.show()
