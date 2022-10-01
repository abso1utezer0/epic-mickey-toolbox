from tkinter import *;
import tkinter as tk;
from tkinter import filedialog as fd

r=tk.Tk()
# add widgets here
filename = fd.askopenfilename();

r.title('Epic Mickey Toolbox')
r.geometry("500x800")
r.mainloop()