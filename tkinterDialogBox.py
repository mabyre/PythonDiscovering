#
# https://www.python-course.eu/tkinter_dialogs.php
#

import tkinter
from tkinter import filedialog

fileName = 'essai'


def callback():
    name = filedialog.askopenfilename()
    fileName = name
    print(name)


print("===>fileName: " + fileName)

errmsg = 'Error!'
tkinter.Button(text='File Open', command=callback).pack(fill=tkinter.X)
tkinter.mainloop()

print("===>choix du fichier: " + fileName)
