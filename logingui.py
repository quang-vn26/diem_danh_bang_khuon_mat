import tkinter 
from PIL import ImageTk, Image
from tkinter.messagebox import showinfo,showerror
import sqlite3

master = tkinter.Tk()
master.geometry("390x350")
# print('chay di')

master.title("HỆ THỐNG ĐIỂM DANH BẰNG KHUÔN MẶT")
width = 515
height = 300

screen_width = master.winfo_screenwidth()
screen_height = master.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
master.geometry("%dx%d+%d+%d" % (width, height, x, y))
master.resizable(0, 0)

def login():
	# Connect to database
	db = sqlite3.connect('login.db')
	c = db.cursor()
	username = lblusername.get()
	password = lblpassword.get()
	
	c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
	
	if c.fetchall():
		# showinfo(title = "success", message = "Username and password correct")
		master.destroy()
		# goi ham giao dien chinh
		import bang_dieu_khien
	else:
		showerror(title = "warning", message = "incorrect username or password")
		
	c.close()


bg_color = "#263D42"
fg_color = "white"
master.configure(background= bg_color)

#---heading image
photo = ImageTk.PhotoImage(Image.open("logo.png"))
tkinter.Label(master, image=photo).grid(rowspan = 3, columnspan = 5, row =0,column = 0)
# -------username
tkinter.Label(master,  text="Username:", fg=fg_color, bg=bg_color, font=("Helvetica", 15)).grid(row=8, padx=(50, 0), pady=(20, 10))
lblusername = tkinter.Entry(master)
lblusername.grid(row=8, column=1, padx=(10, 10), pady=(20, 10))

# ----password
tkinter.Label(master,  text="Password:", fg=fg_color, bg=bg_color, font=("Helvetica", 15)).grid(row=9, padx=(50, 0), pady=(20, 10))
lblpassword = tkinter.Entry(master)
lblpassword.config(show="*");
lblpassword.grid(row=9, column=1, padx=(10, 10),pady=(20, 10))

# --------button
tkinter.Button(master, text="Login",borderwidth=3, relief='ridge', fg=fg_color, bg=bg_color, width = 15, command = login).grid(row = 10,  padx=(50, 0), pady=(20, 10))

master.mainloop()