import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile
import pandas as pd
import numpy as np

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140)#, window=entry1)

def random_entry():  
    filename = askopenfilename()
    global df
    df = pd.read_csv(filename, encoding = "ISO-8859-1")
    df = df[['Name','Recipient Primary Major','Personal Email',
            'Response Status','Knowledge Source','Outcome',
            'How likely would you recommend using the services and resources available through your Career Development office to a future student?']]
    df = df[(df['Knowledge Source'] == 'Survey Response')&
            (df['Outcome'] != 'Still Looking')].dropna(how='any').sample(1)
    df_name = df.Name.item()
    label1 = tk.Label(root, text=df_name)
    canvas1.create_window(200, 160, window=label1)
    canvas1.create_window(200, 100, window=button2)

def save_df():
    filename = asksaveasfile(defaultextension=".csv", 
                             filetypes=(("Comma-separated values file", "*.csv"),
                                        ("All Files", "*.*") ))
    df.to_csv(filename)
    label2 = tk.Label(root, text='Saved to File')
    canvas1.create_window(200, 190, window=label2)
    

button1 = tk.Button(text='Select .CSV File To Get Random Winner', command=random_entry)
button2 = tk.Button(text='Save Winner\'s info to File', command = save_df)
canvas1.create_window(200, 50, window=button1)



root.mainloop()