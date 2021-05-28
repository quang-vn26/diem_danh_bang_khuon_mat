import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import csv
import demo_file
# create the root window
root = tk.Tk()
root.title('Xem danh sach')
root.resizable(False, False)
root.geometry('300x150')


def select_file():
    filetypes = (
        ('text files', '*.csv'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        # initialdir='/',
        filetypes=filetypes)
    if(filename):
        # open file
        root.destroy()

        demo_file.hien_thi(filename)


    # showinfo(
    #     title='Selected File',
    #     message=filename
    # )


# open button
open_button = ttk.Button(
    root,
    text='Open a File',
    command=select_file
)

open_button.pack(expand=True)


# run the application
root.mainloop()
