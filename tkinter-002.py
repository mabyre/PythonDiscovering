from datetime import datetime
import math
import sys
import tkinter as tk


def save():
    print(tbe_dia.get())
    stdoutOrigin = sys.stdout
    sys.stdout = open(nc_get.get()+".txt", 'w')
    now = datetime.now()
    now_str = now.strftime("%H:%M")
    #now_day = now.strftime("%Y.%m.%d")
    #now_str = now.strftime("%H:%M:%S")
    doy = datetime.now().timetuple().tm_yday
    if doy < 100:
        now_doy = str(doy)
        now_doy = str("0"+(now_doy))
    else:
        now_doy = str(doy)
    print("%")
    print()
    print("O"+(nc_get.get()))
    print()
    print("(PROVEN "+(now_str)+":"+(now_doy)+")")
    print()
    sys.stdout.close()
    sys.stdout = stdoutOrigin


gui = tk.Tk()

os_wdh = gui.winfo_screenwidth()
os_hgt = gui.winfo_screenheight()
tk_wdh = 500
tk_hgt = 500
xn_cnt = (os_wdh/2)-(tk_wdh/2)
yn_cnt = (os_hgt/2)-(tk_hgt/2)

gui.title('PRJ_ARC')
gui.geometry('%dx%d+%d+%d' % (tk_wdh, tk_hgt, xn_cnt, yn_cnt))
gui.resizable(width=False, height=False)

nc_get = tk.Entry(gui, width=10)
# nc_get.pack#(fill=tk.NONE)
nc_get.place(x=360, y=25)

nc_run = tk.Button(gui, text='!', width=5, command=save)
# nc_run.pack()
nc_run.place(x=438, y=22)

tbe_dia = tk.Entry(gui, width=5)
# tbe_dia.pack#(fill=tk.NONE)
tbe_dia.place(x=25, y=30)

tbe_lbl = tk.Label(gui, text="TBE_DIA")
# tbe_lbl.pack#(fill=tk.NONE)
tbe_lbl.place(x=65, y=30)


def psn_01():
    print('psn_01 :', chk_v01.get())


chk_v01 = tk.IntVar()

btn_01 = tk.Checkbutton(gui, text="PSN_01",
                        variable=chk_v01,
                        command=psn_01)
btn_01.pack()

dia_01 = tk.Entry(gui, width=10)
dia_01.place(x=100, y=55)

lbl_01 = tk.Label(gui, text="DIA")
lbl_01.place(x=170, y=55)

xpn_01 = tk.Entry(gui, width=10)
xpn_01.place(x=200, y=55)

lbl_01 = tk.Label(gui, text="XPN")
lbl_01.place(x=270, y=55)

apn_01 = tk.Entry(gui, width=10)
apn_01.place(x=300, y=55)

lbl_01 = tk.Label(gui, text="APN")
lbl_01.place(x=370, y=55)

drl_lbl = tk.Label(gui, text="DRL")
drl_lbl.place(x=50, y=90)

drl_01 = tk.Entry(gui, width=10)
drl_01.place(x=100, y=90)

drl_dia = tk.Label(gui, text="DIA")
drl_dia.place(x=170, y=90)

gui.mainloop()
