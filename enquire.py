"""A program to read in city and number from a file and display a
   GUI that lets users select a city by city name and see their number
"""
from tkinter import *  
from tkinter.ttk import *
import csv

class IndustryLookupGui:

    def __init__(self, parent, industry):
        self.industry = industry
        self.header = Label(parent, text="Correlation of city and number", font=("Arial", 18))
        self.header.grid(row=0, column=0, columnspan=3, pady=10)
        self.username_label = Label(parent, text="City:")
        self.username_label.grid(row=1, column=0, padx=10)
        number = list(industry.keys())
        self.selector = Combobox(parent,
                                 values=number,
                                 width=12)
        self.selector.grid(row=1, column=1, padx=10)
        self.selector.bind('<<ComboboxSelected>>', self.update_name)
        self.selector.current(0)
        self.name_label = Label(parent)
        self.name_label.grid(row=1, column=2)
        parent.columnconfigure(0, minsize=100, weight=1)
        parent.columnconfigure(1, minsize=100, weight=1)
        parent.columnconfigure(2, minsize=200, weight=1)
        parent.rowconfigure(1, minsize=50)
        self.update_name(None)    # Load the fields with starting values

    def update_name(self, event):  # Called when combo selection changes
        username = self.selector.get()# Read the combobox
        self.name_label['text'] = self.industry[username]
        self.selector.selection_clear()  # Turn off horrible highlighting

def main():
    window = Tk()
    window.wm_title('Enquire')
    csv_file = open('number_city_relationship.csv')
    rdr = csv.reader(csv_file)
    industry = {}
    for number, city in rdr:
        industry[city] = number
    gui = IndustryLookupGui(window, industry)
    csv_file.close()
    window.mainloop()

main()

