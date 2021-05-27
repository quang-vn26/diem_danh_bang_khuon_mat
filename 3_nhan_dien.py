import tkinter 
from PIL import ImageTk, Image
from tkinter.messagebox import showinfo,showerror
import sqlite3
import numpy as np
import os
import pickle
import cv2
# import giaodien

# Các chức năng chính
def nhan_dien():
    face_cascade = cv2.CascadeClassifier('khuonMat.xml')
    #recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    #recognizer.read("huanluyen/huanluyen.yml")
    recognizer.read("trainer/face-trainner.yml")

    def getProfile(Id,mon_hoc=''):
        conn=sqlite3.connect("mydata.db")
        query="SELECT * FROM sinh_vien WHERE masv="+str(Id)
        cursor=conn.execute(query)
        profile=None
        for row in cursor:
            profile=row
        conn.close()
        return profile

    #cap = cv2.VideoCapture("rtsp://admin:admin@172.16.1.45:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif")
    cap = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_COMPLEX
    while True:
        #comment the next line and make sure the image being read is names img when using imread
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]

            nbr_predicted, conf = recognizer.predict(gray[y:y+h, x:x+w])
            if conf < 70:   
                profile=getProfile(nbr_predicted)
                if profile != None:
                    cv2.putText(img, ""+str(profile[1]), (x+10, y), font, 1, (0,255,0), 1);
            else:
                cv2.putText(img, "Unknown", (x, y + h + 30), font, 0.4, (0, 255, 0), 1);


        cv2.imshow('img', img)
        if(cv2.waitKey(1) == ord('q')):
            break
    cap.release()
    cv2.destroyAllWindows()

# Hàm nút
def lay_du_lieu():
   # goi ham lay du lieu, tranning data
   return True
def diem_danh():
   # doi gio dien diem danh va close giao dien cu
   return True
def danh_sach_sinh_vien():
   # danh sach sih vien
   return True
def gui_email():   
   return True
def login():
   return True   



# Code giao dien
master = tkinter.Tk()
master.geometry("390x350")
# print('chay di')

master.title("ĐIỂM DANH THEO MÔN HỌC")
width = 515
height = 390

screen_width = master.winfo_screenwidth()
screen_height = master.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
master.geometry("%dx%d+%d+%d" % (width, height, x, y))
master.resizable(0, 0)


bg_color = "#263D42"
fg_color = "white"
master.configure(background= bg_color)

#---heading image
photo = ImageTk.PhotoImage(Image.open("logo.png"))
tkinter.Label(master, image=photo).grid(rowspan = 3, columnspan = 5, row =0,column = 0)
# --------button
tkinter.Button(master, text="Đồ án 5",borderwidth=3, relief='ridge', fg=fg_color, bg=bg_color, width = 45, command = login).grid(row = 8,  padx=(50, 0), pady=(20, 10))
tkinter.Button(master, text="Xử lý ảnh",borderwidth=3, relief='ridge', fg=fg_color, bg=bg_color, width = 45, command = login).grid(row = 9,  padx=(50, 0), pady=(20, 10))
tkinter.Button(master, text="Trình biên dịch",borderwidth=3, relief='ridge', fg=fg_color, bg=bg_color, width = 45, command = login).grid(row = 10,  padx=(50, 0), pady=(20, 10))
tkinter.Button(master, text="Xử lý tín hiệu số",borderwidth=3, relief='ridge', fg=fg_color, bg=bg_color, width = 45, command = login).grid(row = 11,  padx=(50, 0), pady=(20, 10))
tkinter.Button(master, text="Bảo mật",borderwidth=3, relief='ridge', fg=fg_color, bg=bg_color, width = 45, command = login).grid(row = 12,  padx=(50, 0), pady=(20, 10))
master.mainloop()