import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("TODO")
root.geometry('400x500')
root.resizable(False, False)
root.iconbitmap('ICON.ico')


def addtask( event):
    task = taskEntry.get()
    taskEntry.delete(0, tk.END)
    if task:
        ListEntry.insert(tk.END, task)


def deletetask():
    task2 = ListEntry.get(tk.ANCHOR)
    ListEntry.delete(tk.ANCHOR)


heading = ttk.Label(root, text="Your Tasks", font='arial 20 bold')
heading.pack(pady=20)

frame = ttk.Frame(root, width=400, height=50)
frame.pack()

taskEntry = ttk.Entry(frame, width=25, font='arial 18')
taskEntry.pack(pady=20)

taskEntry.bind("<Return>", addtask)

frame1 = ttk.Frame(root, width=300, height=250)
frame1.pack()

ListEntry = tk.Listbox(frame1, width=50, height=16)
ListEntry.pack(pady=20)

ttk.Style().configure('TButton', font='arial 12 bold')

deleteButton = ttk.Button(root, text='Delete', style='TButton', command=deletetask)
deleteButton.pack()

root.mainloop()
