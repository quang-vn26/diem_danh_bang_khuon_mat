import tkinter
import csv

# open file
def hien_thi(filename):
	# root = tkinter.Tk()
	root = tkinter.Tk()
	root.title('Xem danh sach')
	with open(filename, newline = "") as file:
	   reader = csv.reader(file)

	   # r and c tell us where to grid the labels
	   r = 0
	   for col in reader:
	      c = 0
	      for row in col:
	         # i've added some styling
	         label = tkinter.Label(root, width = 10, height = 2, \
	                               text = row, relief = tkinter.RIDGE)
	         label.grid(row = r, column = c)
	         c += 1
	      r += 1

	root.mainloop()