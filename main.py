import tkinter as tk
import pandas as pd
import numpy
from tkinter import ttk, filedialog, messagebox

def update_name(excel, entry, tree):
    if entry.get():
        excel.loc[len(excel)] = entry.get()
        update_tree(excel, tree)
    print(excel)
    pd.DataFrame.to_excel(excel, 'employees.xlsx', index=False)
def delete_name(excel, entry, tree):
    value = tree.item(tree.focus())['values'][0]
    for i in range(len(excel['name'])):
        if excel['name'][i]==value:
            excel = excel.drop(excel.index[i])
            print(value)
            print(i)
    pd.DataFrame.to_excel(excel, 'employees.xlsx', index=False)
    update_tree(excel, tree)
excel = pd.read_excel('employees.xlsx')
window = tk.Tk()
name = tk.Label(text='enter employee name')
entry = tk.Entry()
submit_button = tk.Button(text='submit', command=lambda: update_name(excel, entry, tree))
delete_button = tk.Button(text='delete', command=lambda: delete_name(excel, entry, tree))
tree = ttk.Treeview(window)
def update_tree(excel, tree):
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
update_tree(excel, tree)
#pack everything
name.pack()
entry.pack()
submit_button.pack()
delete_button.pack()
tree.pack()


window.mainloop()