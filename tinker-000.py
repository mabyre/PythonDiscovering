from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x200")

w = Label(root, text='GeeksForGeeks', font="50")
w.pack()

messagebox.showinfo("showinfo", "Information")
messagebox.showwarning("showwarning", "Warning")
messagebox.showerror("showerror", "Error")

result = messagebox.askquestion("askquestion", "Are you sure?")
print(result)

result = messagebox.askokcancel("askokcancel", "Want to continue?")
print(result)
if result == False:
    print('Program ended...')
    exit()

print('Program continue')

result = messagebox.askyesno("askyesno", "Find the value?")
print(result)
