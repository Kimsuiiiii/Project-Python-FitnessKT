from calendar import month
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import sqlite3
import datetime
import time

global timeend
conn=sqlite3.connect('projectfitness.db')
c = conn.cursor()

#date = datetime.datetime.now()
date = datetime.datetime(2024,2,9)

root = Tk()
root.title("💪 KT Fitness 💪")
root.geometry("500x350+500+200")
canvas = Canvas(root, width=500, height=400,bg='blue')
canvas.pack()
photo = PhotoImage(file='C:\\Users\\uta_s\\OneDrive\\Pictures\\Saved Pictures\\fit-removebg-preview.png')
canvas.create_image(0, 0, image=photo, anchor=NW)
myLabel1 = Label(root,text='\n\t💪 KT Fitness 💪\t\t\n',fg='white',font=20,bg='black').place(x=75,y=50)
#myLabel1 = Label(root,text='\nหน้าหลัก\n',font=20).pack()

def tohome() :
    global date
    preend = date
    name = txt.get()
    Addrss = txt1.get()
    tel1 = txt2.get()
    email = txt3.get()
    password = txt4.get()
    promotion = promo.get()
    datestr = date.strftime('%d-%m-%Y')
    datef = datetime.datetime.strptime(datestr, '%d-%m-%Y')
    if promotion == ('รายวัน 40 บาท') :
        preend = date + datetime.timedelta(days=1)
    if promotion == ('รายเดือน 650 บาท') :
        preend = date + datetime.timedelta(days=30)
    if promotion == ('ราย 3 เดือน 1800 บาท') :
        preend = date + datetime.timedelta(days=90)
    if promotion == ('ราย 6 เดือน 3300 บาท') :
        preend = date + datetime.timedelta(days=180)
    if promotion == ('รายปี 5800 บาท') :
        preend = date + datetime.timedelta(days=365)
    end1 = preend.strftime('%d-%m-%Y')
    if name.isalpha() == False :
        tkinter.messagebox.showinfo('แจ้งเตือน','กรอกชื่อด้วยตัวอักษร')
        txt.set('')
    else :
        if tel1.isnumeric() == False and len(tel1) != 10 :
            tkinter.messagebox.showinfo('แจ้งเตือน','เบอร์โทรศัพท์ไม่ถูกต้อง')
            txt2.set('')
        else :
            data = (name,Addrss,tel1,email,password,promotion,datestr,end1)
            c.execute ('INSERT INTO FitnessKT(Name,Address,Tel,Email,Password,Promotion,วันที่สมัคร,สิ้นสุดการเป็นสมาชิก)VALUES(?,?,?,?,?,?,?,?)',data)
            conn.commit()
            tkinter.messagebox.showinfo('แจ้งเตือน','บันทึกข้อมูลแล้ว ทำการเข้าสู่ระบบได้')
            mywind.destroy()

def login2() :
    global tel,timeend
    tel = telll.get()
    password = passs.get()
    b=c.execute("""SELECT Tel FROM FitnessKT""")
    resulttel = b.fetchall()
    tellist = []
    for i in range(len(resulttel)):
        tellist.append(resulttel[i][0])
    a=c.execute("""SELECT Password FROM FitnessKT WHERE Tel = ?""", (tel,))
    if tel not in tellist :
        tkinter.messagebox.showinfo('แจ้งเตือน','ไม่พบผู้ใช้')
        telll.set('')
    else :
        result = a.fetchall()
        realpassword = result[0][0]
        if password != realpassword :
            tkinter.messagebox.showinfo('แจ้งเตือน','รหัสผ่านไม่ถูกต้อง')
            passs.set('')
        else :
            windw = Toplevel()
            windw.title('💪 KT Fitness 💪')
            windw.geometry("500x350+500+200")
            canvas2 = Canvas(windw, width=500, height=400,bg='blue')
            canvas2.pack()
            photo2 = PhotoImage(file='C:\\Users\\uta_s\\OneDrive\\Pictures\\Saved Pictures\\fit-removebg-preview.png')
            canvas2.create_image(0, 0, image=photo, anchor=NW)
            myLabel1 = Label(windw,text='\n\t💪 KT Fitness 💪\t\t\n',fg='black',font=20,bg='grey').place(x=75,y=40)
            d=c.execute("""SELECT Name,Promotion,สิ้นสุดการเป็นสมาชิก FROM FitnessKT WHERE Tel = ?""",(tel,))
            z = d.fetchall()
            names = z[0][0]
            promo = z[0][1]
            tobeend = z[0][2]
            datestr = date.strftime('%d-%m-%Y')
            datef = datetime.datetime.strptime(datestr, '%d-%m-%Y')
            end = datetime.datetime.strptime(tobeend,'%d-%m-%Y')
            endleft = str(end - datef)
            endlefts = endleft.split(' ')
            timeend = int(endlefts[0])
            text = 'คุณ {} เข้าใช้งานใน FitnessKT แล้ว \nในโปรโมชั่น {}'.format(names, promo)
            myLabel2 = Label(windw,text=text,fg='black',font=20,bg='white').place(x=98,y=120)
            def ending() :
                promotion = promo1.get()
                if promotion == ('รายวัน 40 บาท') :
                    preend = end + datetime.timedelta(days=1)
                if promotion == ('รายเดือน 650 บาท') :
                    preend = end + datetime.timedelta(days=30)
                if promotion == ('ราย 3 เดือน 1800 บาท') :
                    preend = end + datetime.timedelta(days=90)
                if promotion == ('ราย 6 เดือน 3300 บาท') :
                    preend = end + datetime.timedelta(days=180)
                if promotion == ('รายปี 5800 บาท') :
                    preend = end + datetime.timedelta(days=365)
                endf = preend.strftime('%d-%m-%Y')
                ends = datetime.datetime.strptime(endf,'%d-%m-%Y')
                data = (promotion,endf,tel)
                c.execute('update FitnessKT set Promotion = ?,สิ้นสุดการเป็นสมาชิก = ? where Tel = ?',data)
                conn.commit()
                tkinter.messagebox.showinfo('แจ้งเตือน','ต่ออายุการใช้งานเรียบร้อยแล้ว')
                windw.destroy()
                mywind1.destroy()

            def pageend() :
                global promo1
                label = Label(windw,text = 'promotion',fg='black').place(x=225,y=260)
                promo1 = StringVar(windw)
                drop = ttk.Combobox(windw,textvariable=promo1)
                drop["values"] = [
                    "รายวัน 40 บาท",
                    "รายเดือน 650 บาท",
                    "ราย 3 เดือน 1800 บาท",
                    "ราย 6 เดือน 3300 บาท",
                    "รายปี 5800 บาท"
                ]
                drop.place(x=181,y=280)
                bt5 = Button(windw,text='ยืนยัน',fg='white',bg='green',command = ending).place(x=240,y=300)
            if timeend <= 5 :
                textend = 'เหลือเวลาใช้งานอีก {} วัน\nต้องการต่ออายุหรือไม่'.format(timeend)
                myLabel3 = Label(windw,text=textend,bg='red',fg='white').place(x=198,y=185)
                bt4 = Button(windw,text='ต่ออายุการใช้งาน',fg='white',font=8,bg='blue',command = pageend).place(x=181,y=220)

def login() :
    global mywind1,telll,passs
    mywind1 = Tk()
    mywind1.title('เข้าสู่ระบบ')
    mywind1.geometry('400x300+550+220')
    loginlabel = Label(mywind1,text = '\tเข้าสู่ระบบ\t\t',bg='blue',font=20,fg='white').pack()
    label = Label(mywind1,text = 'เบอร์โทรศัพท์',fg='black').pack()
    telll=StringVar(mywind1)
    mytext = Entry(mywind1,textvariable=telll).pack()
    label = Label(mywind1,text = 'password',fg='black').pack()
    passs=StringVar(mywind1)
    mytext1 = Entry(mywind1,textvariable=passs,show='*').pack()
    bt4=Button(mywind1,text='ยืนยัน',fg='white',font=10,bg='green',command = login2).pack()

def page2() :
    global txt,txt1,txt2,txt3,txt4,mywind,promo
    mywind = Tk()
    mywind.title('สมัครสมาชิก')
    mywind.geometry('400x300+550+220')
    label = Label(mywind,text = 'ชื่อ-นามสกุล',fg='black').pack()
    txt=StringVar(mywind)
    mytext = Entry(mywind,textvariable=txt).pack()
    label = Label(mywind,text = 'ที่อยู่',fg='black').pack()
    txt1=StringVar(mywind)
    mytext1 = Entry(mywind,textvariable=txt1,width=40).pack()
    label = Label(mywind,text = 'เบอร์โทรศัพท์',fg='black').pack()
    txt2=StringVar(mywind)
    mytext2 = Entry(mywind,textvariable=txt2).pack()
    label = Label(mywind,text = 'Email',fg='black').pack()
    txt3=StringVar(mywind)
    mytext3 = Entry(mywind,textvariable=txt3).pack()
    label = Label(mywind,text = 'password',fg='black').pack()
    txt4=StringVar(mywind)
    mytext4 = Entry(mywind,textvariable=txt4).pack()
    label = Label(mywind,text = 'promotion',fg='black').pack()
    promo = StringVar(mywind)
    drop = ttk.Combobox(mywind,textvariable=promo)
    drop["values"] = [
        "รายวัน 40 บาท",
        "รายเดือน 650 บาท",
        "ราย 3 เดือน 1800 บาท",
        "ราย 6 เดือน 3300 บาท",
        "รายปี 5800 บาท"
    ]
    drop.pack()
    bt3 = Button(mywind,text='ลงทะเบียน',fg='white',font=15,bg='green',command = tohome).pack()

bt1 = Button(root,text='เข้าสู่ระบบ',fg='white',font=15,bg='blue',command = login).place(x=200,y=150)
bt2 = Button(root,text='สมัครสมาชิก',fg='white',font=15,bg='green',command = page2).place(x=189,y=200)

root.mainloop()

for i in range(30) :
    c.execute('SELECT Tel FROM FitnessKT')
    k = c.fetchall()
    alltel = []
    for i in range(len(k)):
        alltel.append(k[i][0])
    for i in alltel:
        enddb =c.execute("""SELECT สิ้นสุดการเป็นสมาชิก FROM FitnessKT WHERE Tel = ?""",(i,))
        e = enddb.fetchall()
        tobeend = e[0][0]
        datestr = date.strftime('%d-%m-%Y')
        datef = datetime.datetime.strptime(datestr, '%d-%m-%Y')
        end = datetime.datetime.strptime(tobeend,'%d-%m-%Y')
        endleft = str(end - datef)
        endlefts = endleft.split(' ') 
        timeend = int(endlefts[0])
        if timeend <= 0 :
            c.execute('delete from FitnessKT where Tel = ?',(i,))
            conn.commit()
            time.sleep(86400)
