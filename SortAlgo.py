from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title('Sorting Algorithm Visualization')
root.maxsize(900,600)
root.config(bg = 'black')

# Variables
selected_algo = StringVar()

def draw(data):
    c_height = 300
    c_width = 600

def Generate():
    print("Algorithm Selected: " + selected_algo.get())

# Frame / Base Layout
UI_frame = Frame(root, width = 600, height=200, bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width = 600, height=300, bg='white')
canvas.grid(row=1, column=0, padx = 10, pady=5)

# UI
# Row: 0
Label(UI_frame, text="Alogrithm: ", bg = 'grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algomenu = ttk.Combobox(UI_frame, textvariable = selected_algo, values=['Bubble Sort', 'Merge Sort'])
algomenu.grid(row=0, column=1, padx=5, pady=5)
algomenu.current(0)
Button(UI_frame, text="Generate", command=Generate, bg='red').grid(row = 0, column=2, padx=5, pady=5)

# Row: 1
Label(UI_frame, text="Size: ", bg = 'grey').grid(row=1, column=0, padx=5, pady=5, sticky=W)
sizeEntry = Entry(UI_frame)
sizeEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

Label(UI_frame, text="Min Value: ", bg = 'grey').grid(row=1, column=2, padx=5, pady=5, sticky=W)
minEntry = Entry(UI_frame)
minEntry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

Label(UI_frame, text="Max Value: ", bg = 'grey').grid(row=1, column=4, padx=5, pady=5, sticky=W)
maxEntry = Entry(UI_frame)
maxEntry.grid(row=1, column=5, padx=5, pady=5, sticky=W)






root.mainloop()