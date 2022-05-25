from tkinter import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

root = Tk()
root.geometry('600x660')
root.title("Giữi Email cho sinh viên")

Label_0 = Label(root, text="Đăng nhập tài khoản", width=20, fg="green", font=("bold", 20))
Label_0.place(x=90, y=33)
#######################################
# nhập đầu vào
Rmail = StringVar()
Rpswrd = StringVar()
Rsender = StringVar()
Rsubject = StringVar()
#######################################

Label_1 = Label(root, text="Tài khoản Email :", width=20, font=("bold", 10))
Label_1.place(x=40, y=110)

emailE = Entry(root, width=40, textvariable=Rmail)
emailE.insert(0,'nttam.18it5@sict.udn.vn')
emailE.place(x=200, y=110)

Label_2 = Label(root, text="Mật khẩu:", width=20, font=("bold", 10))
Label_2.place(x=40, y=160)

passwordE = Entry(root, width=40, show="*", textvariable=Rpswrd)
passwordE.insert(0,'nguyentrongtam2468')
passwordE.place(x=200, y=160)

compose = Label(root, text="Người nhận ", width=20, font=("bold", 15))
compose.place(x=180, y=210)

Label_3 = Label(root, text="Email người nhận:", width=20, font=("bold", 10))
Label_3.place(x=40, y=260)

senderE = Entry(root, width=40, textvariable=Rsender)
senderE.place(x=200, y=260)

Label_4 = Label(root, text="Chủ để:", width=20, font=("bold", 10))
Label_4.place(x=40, y=310)

subjectE = Entry(root, width=40, textvariable=Rsubject)
subjectE.insert(0,'Hệ thống điểm danh khuôn mặt')
subjectE.place(x=200, y=310)

Label_5 = Label(root, text="Nội dung:", width=20, font=("bold", 10))
Label_5.place(x=40, y=360)

msgbodyE = Text(root, width=30, height=10)
msgbodyE.place(x=200, y=360)




def sendemail():
    # email: nttam.18it5@sict.udn.vn
    # pass='nguyentrongtam2468'
    try:
        mymsg = MIMEMultipart()
        mymsg['From'] = str(Rmail.get())
        mymsg['To'] = str(Rsender.get())
        mymsg['Subject'] = str(Rsubject.get())

        mymsg.attach(MIMEText(msgbodyE.get(1.0, 'end'), 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(str(Rmail.get()), str(Rpswrd.get())+".")
        text = mymsg.as_string()
        server.sendmail(str(Rmail.get()), str(Rsender.get()), text)

        Label_6 = Label(root, text="Hoàn thành!", width=20, fg='green', font=("bold", 15))
        Label_6.place(x=140, y=550)

        server.quit()
    except:
        Label_6 = Label(root, text="Có lỗi xãy ra ! ", width=20, fg='red', font=("bold", 15))
        Label_6.place(x=140, y=550)


Button(root, text="Giữi", width=20, bg='brown', fg="white", command=sendemail).place(x=180, y=590)

root.mainloop()
