from tkinter import *
import tkinter.ttk as ttk
import csv

root = Tk()
root.title("Danh sách sinh viên")
width = 800
height = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)


TableMargin = Frame(root, width=500)
TableMargin.pack(side=TOP)
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("MaSV", "Tên", "Email"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('MaSV', text="MaSV", anchor=W)
tree.heading('Tên', text="Tên", anchor=W)
tree.heading('Email', text="Email", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=200)
tree.column('#2', stretch=NO, minwidth=0, width=200)
tree.column('#3', stretch=NO, minwidth=0, width=300)
tree.pack()

from tkinter import filedialog as fd

filetypes = (
        ('text files', '*.csv'),
        ('All files', '*.*')
  )
file  = fd.askopenfile(filetypes=filetypes)
# print (file)
if file:
	with file as f:
	    reader = csv.DictReader(f, delimiter=',')
	    for row in reader:
	        MaSV = row['masv']
	        Tên = row['ten']
	        Email = row['email']
	        tree.insert("", 0, values=(MaSV, Tên, Email))
else:
	pass
#============================INITIALIZATION==============================
if __name__ == '__main__':
    root.mainloop()