from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox
import numpy as np
import os
import cv2
import sqlite3

# data
class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS sinh_vien (id INTEGER PRIMARY KEY, masv text, ten text, lop text, email text)")
        self.conn.commit()

    def fetch(self, ten=''):
        self.cur.execute(
            "SELECT * FROM sinh_vien WHERE ten LIKE ?", ('%'+ten+'%',))
        rows = self.cur.fetchall()
        return rows

    def fetch2(self, query):
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows

    def insert(self, masv,ten,lop,email):
        self.cur.execute("INSERT INTO sinh_vien VALUES (NULL, ?, ?, ?, ?)",
                         (masv,ten, lop,email))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM sinh_vien WHERE id=?", (id,))
        self.conn.commit()
    def remove2(self, masv):
        self.cur.execute("DELETE FROM sinh_vien WHERE masv=?", (masv,))
        self.conn.commit()    
    def update(self, id, masv,ten,lop,email):
        self.cur.execute("UPDATE sinh_vien SET masv = ?, ten = ?, lop = ?, email = ? WHERE id = ?",
                         (masv,ten,lop,email, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


db = Database("mydata.db")

# ham data
def populate_list(hostname=''):
    for i in router_tree_view.get_children():
        router_tree_view.delete(i)
    for row in db.fetch(hostname):
        router_tree_view.insert('', 'end', values=row)

def populate_list2(query='select * from sinh_vien'):
    for i in router_tree_view.get_children():
        router_tree_view.delete(i)
    for row in db.fetch2(query):
        router_tree_view.insert('', 'end', values=row)

def add_sinh_vien():
    if ten_text.get() == '' or masv_text.get() == '' or lop_text.get() == '' or email_text.get() == '':
        messagebox.showerror('Lỗi', 'Hãy nhập đầy đủ thông tin')
        return

    db.remove2(masv_text.get())

    db.insert(masv_text.get(), ten_text.get(),
              lop_text.get(), email_text.get())
    
    # chup hinh
    # print
    face_cascade = cv2.CascadeClassifier('khuonMat.xml')
    cap = cv2.VideoCapture(0)
    sample_number = 0

    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            sample_number += 1

            if not os.path.exists('data_face'):
                os.makedirs('data_face')

            cv2.imwrite('data_face/User.'+str(masv_entry.get())+"."+str(sample_number)+".jpg",  img[y:y+h,x:x+w])
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

        cv2.imshow('img', img)
        cv2.waitKey(1);
        if(sample_number>100):
            cap.release()
            cv2.destroyAllWindows()
            break;
    clear_text()
    populate_list()        


def select_router(event):
    try:
        global selected_item
        index = router_tree_view.selection()[0]
        selected_item = router_tree_view.item(index)['values']
        masv_entry.delete(0, END)
        masv_entry.insert(END, selected_item[1])
        ten_entry.delete(0, END)
        ten_entry.insert(END, selected_item[2])
        lop_entry.delete(0, END)
        lop_entry.insert(END, selected_item[3])
        email_entry.delete(0, END)
        email_entry.insert(END, selected_item[4])
    except IndexError:
        pass
def remove_sinh_vien():
    db.remove(selected_item[0])
    clear_text()
    populate_list()

def update_sinh_vien():
    db.update(selected_item[0], masv_text.get(), ten_text.get(),
              lop_text.get(), email_text.get())
    populate_list()

def clear_text():
    ten_entry.delete(0, END)
    masv_entry.delete(0, END)
    lop_entry.delete(0, END)
    email_entry.delete(0, END)

def search_ma_sinh_vien():
    hostname = masv_search.get()
    populate_list(hostname)


def execute_query():
    query = query_search.get()
    populate_list2(query)
def bang_dieu_khien():
    app.destroy()
    import bang_dieu_khien
    return True
# giao dien
app = Tk()
frame_search = Frame(app)
frame_search.grid(row=0,column=0)

lbl_search = Label(frame_search,text="Tìm kiếm theo Tên sinh viên",font=('bold',12),pady=20)
lbl_search.grid(row=0, column=0, sticky=W)
masv_search = StringVar()
masv_search_entry = Entry(frame_search, textvariable=masv_search)
masv_search_entry.grid(row=0, column=1)

lbl_search = Label(frame_search, text='Tìm kiếm bằng câu lệnh',font=('bold', 12), pady=20)
lbl_search.grid(row=1, column=0, sticky=W)
query_search = StringVar()
query_search.set("Select * from sinh_vien where masv='18IT348'")
query_search_entry = Entry(frame_search, textvariable=query_search, width=40)
query_search_entry.grid(row=1, column=1)


frame_fields = Frame(app)
frame_fields.grid(row=1, column=0)
# masv
masv_text = IntVar()
masv_label = Label(frame_fields, text='Mã sinh viên', font=('bold', 12))
masv_label.grid(row=0, column=0, sticky=E)
masv_entry = Entry(frame_fields, textvariable=masv_text)
masv_entry.grid(row=0, column=1, sticky=W)
# ten
ten_text = StringVar()
ten_label = Label(frame_fields, text='Tên', font=('bold', 12))
ten_label.grid(row=0, column=2, sticky=E)
ten_entry = Entry(frame_fields, textvariable=ten_text)
ten_entry.grid(row=0, column=3, sticky=W)
# lop
lop_text = StringVar()
lop_label = Label(frame_fields, text='Lớp', font=('bold', 12))
lop_label.grid(row=1, column=0, sticky=E)
lop_entry = Entry(frame_fields, textvariable=lop_text)
lop_entry.grid(row=1, column=1, sticky=W)
# ngaysinh
email_text = StringVar()
email_label = Label(frame_fields, text='Email', font=('bold', 12), pady=20)
email_label.grid(row=1, column=2, sticky=E)
email_entry = Entry(frame_fields, textvariable=email_text)
email_entry.grid(row=1, column=3, sticky=W)





frame_router = Frame(app)
frame_router.grid(row=4, column=0, columnspan=4, rowspan=6, pady=20, padx=20)

columns = ['id', 'Mã SV', 'Tên', 'Lớp', 'Email']
router_tree_view = Treeview(frame_router, columns=columns, show="headings")
router_tree_view.column("id", width=30)
for col in columns[1:]:
    router_tree_view.column(col, width=120)
    router_tree_view.heading(col, text=col)
router_tree_view.bind('<<TreeviewSelect>>', select_router)
router_tree_view.pack(side="left", fill="y")
scrollbar = Scrollbar(frame_router, orient='vertical')
scrollbar.configure(command=router_tree_view.yview)
scrollbar.pack(side="right", fill="y")
router_tree_view.config(yscrollcommand=scrollbar.set)




frame_btns = Frame(app)
frame_btns.grid(row=3, column=0)

add_btn = Button(frame_btns, text='Thêm', width=12, command=add_sinh_vien)
add_btn.grid(row=0, column=0, pady=20)

remove_btn = Button(frame_btns, text='Xóa',
                    width=12, command=remove_sinh_vien)
remove_btn.grid(row=0, column=1)

update_btn = Button(frame_btns, text='Cập nhập',
                    width=12, command=update_sinh_vien)
update_btn.grid(row=0, column=2)

clear_btn = Button(frame_btns, text='Nhập mới',
                   width=12, command=clear_text)
clear_btn.grid(row=0, column=3)

home_btn = Button(frame_btns, text='Về trang chủ',width=12, command=bang_dieu_khien)
home_btn.grid(row=0, column=4)


search_btn = Button(frame_search, text='Tìm kiếm',
                    width=12, command=search_ma_sinh_vien)
search_btn.grid(row=0, column=2)

search_query_btn = Button(frame_search, text='Tìm kiếm',
                          width=12, command=execute_query)
search_query_btn.grid(row=1, column=2)


# frame_home = Frame(app)
# frame_home.grid(row=3, column=0)

# home_btn = Button(frame_home, text='Về trang chủ',width=12, command=bang_dieu_khien)
# home_btn.grid(row=0, column=5)



app.title('Dữ liệu sinh viên')
app.geometry('800x660')

# Populate data
populate_list()

# Start program
app.mainloop()




