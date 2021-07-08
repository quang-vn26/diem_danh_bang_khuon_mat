import tkinter 
from PIL import ImageTk, Image
from tkinter.messagebox import showinfo,showerror
import sqlite3
import numpy as np
import os
import pickle
import cv2
from datetime import datetime
import csv

# Các chức năng chính
vang =0
def nhan_dien(monhoc=''):
    face_cascade = cv2.CascadeClassifier('haar.xml')
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    recognizer.read("HuanLuyen/huanluyen.yml")

    def getProfile(Id):
        conn=sqlite3.connect("mydata.db")
        query="SELECT * FROM sinh_vien WHERE masv="+str(Id)

        if vang==1:
            query = "SELECT * FROM sinh_vien WHERE masv NOT LIKE"+str(Id)

        cursor=conn.execute(query)
        profile=None

        for row in cursor:
            profile=row
        conn.close()
        return profile
    # Tao thu muc luu file
    thu_muc_mon_hoc = "Mon_Hoc/"+str(monhoc)
    if not os.path.exists(thu_muc_mon_hoc):
        os.makedirs(thu_muc_mon_hoc)
    
    # tao file
    now = datetime.now()
    ten_file =now.strftime('%d_%m_%Y') 
    # ghi header
    try:
        with open(thu_muc_mon_hoc+"/"+ten_file+".csv", "x") as f:
            f.writelines(f'\nma_sv,ten,email,time')
    except Exception as e:
        print(e)
        
    # doc file va ghi danh sach sinh vien co mat
    def ghi_file_diem_danh(masv,name,email,vang=0):
        open_file = thu_muc_mon_hoc+"/"+ten_file+".csv"
        if vang == 1:
            open_file = thu_muc_mon_hoc+"/"+ten_file+"_vang.csv"
        # xu ly ghi file
        with open(open_file,'r+') as f:
            myDataList = f.readlines()
            masvList = []
            for line in myDataList[1:]:
                entry = line.split(',')
                masvList.append(entry[0])
            if masv not in masvList:
                now = datetime.now()
                dtString = now.strftime('%H:%M:%S')
                f.writelines(f'\n{masv},{name},{email},{dtString}')

    def danh_sach_vang():
        conn=sqlite3.connect("mydata.db")
        query="SELECT * FROM sinh_vien"
        cursor=conn.execute(query)
        profile=None
        for row in cursor:
            profile=row
            with open(thu_muc_mon_hoc+"/"+ten_file+".csv") as f:
                reader = csv.DictReader(f, delimiter=',')
                for row2 in reader:
                    print(row2)
                    masv1 = row2[1]
                    name1 = row2[2]
                    email1 = row2[4]
                    if masv1 != profile[1]:
                        vang = 1
                        ghi_file_diem_danh(masv1,name1,email1,vang)

        conn.close()
                      
 
    # Ham insert csdl mon hoc
    cap = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_COMPLEX
    while True:
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
                    masv_string = str(profile[1])
                    ten_string = str(profile[2])
                    email_string = str(profile[4])
                    cv2.putText(img, "MSV:"+masv_string+",Name: "+ten_string, (x+10, y), font, 1, (0,255,0), 1);
                    ghi_file_diem_danh(masv_string,ten_string,email_string)
            else:
                cv2.putText(img, "Unknown", (x, y + h + 30), font, 0.4, (255,0, 0), 1);
        cv2.imshow('img', img)
        if(cv2.waitKey(1) == ord('q')):
            break
    # danh_sach_vang()            
    cap.release()
    cv2.destroyAllWindows()

# Hàm nút
def do_an():
   nhan_dien("do_an")
   return True
def xu_ly_anh():
   nhan_dien("xu_ly_anh")
   return True
def trinh_bien_dich():
   nhan_dien("trinh_bien_dich")
   return True
def tin_hieu_so():   
   nhan_dien("tin_hieu_so")
def bao_mat():
   nhan_dien("bao_mat")
   return True   
def bang_dieu_khien():
   master.destroy()
   import bang_dieu_khien
   return True   


# Code giao dien
master = tkinter.Tk()
master.geometry("390x350")

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

photo = ImageTk.PhotoImage(Image.open("logo.png"))
tkinter.Label(master, image=photo).grid(rowspan = 3, columnspan = 5, row =0,column = 0)

tkinter.Button(master, text="Đồ án",borderwidth=3, relief='ridge', fg=fg_color, bg=bg_color, width = 45, command = do_an).grid(row = 8,  padx=(50, 0), pady=(20, 10))
tkinter.Button(master, text="Xử lý ảnh",borderwidth=3, relief='ridge', fg=fg_color, bg=bg_color, width = 45, command = xu_ly_anh).grid(row = 9,  padx=(50, 0), pady=(20, 10))
tkinter.Button(master, text="Trình biên dịch",borderwidth=3, relief='ridge', fg=fg_color, bg=bg_color, width = 45, command = trinh_bien_dich).grid(row = 10,  padx=(50, 0), pady=(20, 10))
tkinter.Button(master, text="Xử lý tín hiệu số",borderwidth=3, relief='ridge', fg=fg_color, bg=bg_color, width = 45, command = tin_hieu_so).grid(row = 11,  padx=(50, 0), pady=(20, 10))
tkinter.Button(master, text="Quay về bảng điều khiển",borderwidth=3, relief='ridge', fg=fg_color, bg=bg_color, width = 45, command = bang_dieu_khien).grid(row = 12,  padx=(50, 0), pady=(20, 10))
master.mainloop()