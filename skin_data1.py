import tkinter as tk
from tkinter.filedialog import askopenfilename
import pandas as pd

def import_csv_data():
    """click File Path and choose the csv doucument File Path 
    and click close, the data would print"""
    global v, label
    file_path = askopenfilename()
    print(file_path)
    v.set(file_path)
    df = pd.read_table(file_path)
    print(df)
def main():
    global v, label
    root = tk.Tk()
    tk.Label(root, text='File Path').grid(row=0, column=0)
    v = tk.StringVar()
    entry = tk.Entry(root, textvariable=v).grid(row=0, column=1)
    tk.Button(root, text='Click CSV File',command=import_csv_data).grid(row=1, column=0)
    tk.Button(root, text='Close',command=root.destroy).grid(row=1, column=1)
    root.mainloop()
main()
