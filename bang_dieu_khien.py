import tkinter 
from PIL import ImageTk, Image
from tkinter.messagebox import showinfo,showerror
import sqlite3

master = tkinter.Tk()
master.geometry("390x350")

master.title("HỆ THỐNG ĐIỂM DANH BẰNG KHUÔN MẶT")
width = 515
height = 390

screen_width = master.winfo_screenwidth()
screen_height = master.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
master.geometry("%dx%d+%d+%d" % (width, height, x, y))
master.resizable(0, 0)

def lay_du_lieu():
   # goi ham lay du lieu, tranning data
   master.destroy()
   import du_lieu
   return True
def dao_tao():
   import mo_hinh
   return True
def diem_danh():
   master.destroy()
   import diem_danh
   return True
def xem_danh_sach():  
   master.destroy()
   import xem_file 
   return True
def gui_email():
   # master.destroy()
   import send_email
   return True   



bg_color = "#263D42"
fg_color = "white"
master.configure(background= bg_color)

photo = ImageTk.PhotoImage(Image.open("logo.png"))
tkinter.Label(master, image=photo).grid(rowspan = 3, columnspan = 5, row =0,column = 0)
#button
tkinter.Button(master, text="Dữ liệu",borderwidth=3, relief='ridge', fg=fg_color, bg=bg_color, width = 45, command = lay_du_lieu).grid(row = 8,  padx=(50, 0), pady=(20, 10))
tkinter.Button(master, text="Đào tạo mô hình",borderwidth=3, relief='ridge', fg=fg_color, bg=bg_color, width = 45, command = dao_tao).grid(row = 9,  padx=(50, 0), pady=(20, 10))
tkinter.Button(master, text="Điểm danh",borderwidth=3, relief='ridge', fg=fg_color, bg=bg_color, width = 45, command = diem_danh).grid(row = 10,  padx=(50, 0), pady=(20, 10))
tkinter.Button(master, text="Danh sách sinh viên",borderwidth=3, relief='ridge', fg=fg_color, bg=bg_color, width = 45, command = xem_danh_sach).grid(row = 11,  padx=(50, 0), pady=(20, 10))
tkinter.Button(master, text="Gửi email",borderwidth=3, relief='ridge', fg=fg_color, bg=bg_color, width = 45, command = gui_email).grid(row = 12,  padx=(50, 0), pady=(20, 10))
master.mainloop()