import tkinter as tk
import pandas as pd
import numpy
from tkinter import ttk, filedialog, messagebox

def update_name(excel, entry):
    if entry.get():
        excel.loc[len(excel)] = entry.get()
    print(excel)
    pd.DataFrame.to_excel('employees.xlsx', excel)

excel = pd.read_excel('employees.xlsx')
window = tk.Tk()
name = tk.Label(text='enter employee name')
entry = tk.Entry()
button = tk.Button(text='submit', command=lambda: update_name(excel, entry))
tree = ttk.Treeview(window)
#clear data
tree.delete(*tree.get_children())
#get headers
tree['column'] = list(excel.columns)
tree['show'] = 'headings'
#show headers
for col in tree['column']:
    tree.heading(col, text=col)
#show data
excel_rows = excel.to_numpy().tolist()
for row in excel_rows:
    tree.insert("", "end", values=row)
#pack everything
name.pack()
entry.pack()
button.pack()
tree.pack()


window.mainloop()