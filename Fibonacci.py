
#--------------------------------------------------|
#--- Application that calculates the number     ---|
#--- that is located in the selected position.  ---|
#--------------------------------------------------|

#----- Import of the Tkinter library -----#
import tkinter as tk
from tkinter import *

#----- Tkinter Settings -----#
root = tk.Tk()
root.geometry("800x360")
root.configure(background="#3DC1AC")
root.resizable(False, False)
tk.Wm.wm_title(root, "Fibonacci Sequence")
entr = tk.StringVar(root)
output = tk.StringVar(root)
inpt = tk.StringVar(root)


#----- Function that calculates the number found in the selected position -----#
def calc():
    result = [1]
    num = int(inpt.get()) - 1
    if num > -1 and num < 112:
        for i in range(num):
            if len(result) < 2:
                result.append(result[i-1])
            else:
                result.append(result[len(result)-1]+result[len(result)-2])
        output.set(result[-1])
    else:
        output.set("Only from 1 to 112")

#----- Function that removes the content of the output and input -----#
def delet():
    output.set("")
    inpt.set("")


#----- Send Button -----#
tk.Button(
    root,
    text="SEND",
    font=("Courier", 20, "bold"),
    bg="#50C878",
    command=calc,
).place(x=410,y=100)

#----- Delete Button -----#
tk.Button(
    root,
    text="DELETE",
    font=("Courier", 20, "bold"),
    bg="#E41B17",
    command=delet,
).place(x=600,y=100)

#----- TEXT LABELS -----#
tk.Label(
    root,
    text="POSITION:",
    font=("Courier", 40, "bold"),
    bg="#3DC1AC",
).place(x=40,y=30)

tk.Label(
    root,
    text="RESULT:",
    font=("Courier", 40, "bold"),
    bg="#3DC1AC",
).place(x=40,y=150)


#----- Information entry -----#
entr = tk.Entry(
    bg="#008B8B",
    font=("Courier", 30, "bold"),
    width=16,
    border=2,
    relief="solid",
    justify="center",
    textvariable=inpt,
).place(x=370,y=30,height=60)

#----- Information output -----#
out = tk.Label(
    bg="#99ff66",
    fg="Black",
    font=("Courier", 36, "bold"),
    textvariable=output,
    bd=2,
    relief="solid",
    width=24,
).place(x=40, y=230, height=70)


root.mainloop()