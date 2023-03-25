import tkinter as tk
from tkinter import *

root = Tk()
root.geometry("100x100")
btn = Button(root, text = "Click me !", bd = '6', command = root.destroy)
btn.pack(side = "top")
root.mainloop()


a = input("digite qual valor deseja soma: ")
b = input("digite qual valor deseja soma: ")
soma = int(a) + int(b)
print("A soma de ",a," e de ",b,": ",soma)