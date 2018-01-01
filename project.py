from tkinter import *
import tkinter.messagebox
import sqlite3
con=sqlite3.Connection('newhrdb')
cur=con.cursor()
cur.execute("create table if not exists flights(id number primary key,flight_name varchar(20),source varchar(50),destination varchar(60))")
cur.execute("create table if not exists passenger(id number primary key,flight_name varchar(20),last_name varchar(20),age date,sex varchar(10),phone_no number(20),source varchar(50),destination varchar(60),id_p number(20))")
root1=Tk()
def enter():
    root1.destroy()
    root=Tk()
    root.geometry('1500x300')
    root.configure(bg='light blue')
    root.title("FLIGHT")
    Label(root,text='FLIGHT_DETAILS',font="Arial 30 bold",bg='red').grid(row=0,column=4)
    Label(root,text='FLIGHT_ID',font="Arial 10 bold",bg='light blue').grid(row=1,column=0)
    i=Entry(root)
    i.grid(row=1,column=1)
    Label(root,text='FLIGHT_NAME',font="Arial 10 bold",bg='light blue').grid(row=2,column=0)
    i1=Entry(root)
    i1.grid(row=2,column=1)
    Label(root,text='SOURCE:-',font="Arial 10 bold",bg='light blue').grid(row=3,column=0)
    v=IntVar(root)
    Radiobutton(root,text='NEW DELHI',font="Arial 9 bold",bg='light blue',variable=v,value=1).grid(row=3,column=1)
    Radiobutton(root,text='MUMBAI',font="Arial 9 bold",bg='light blue',variable=v,value=2).grid(row=3,column=2)
    Radiobutton(root,text='BANGLURU',font="Arial 9 bold",bg='light blue',variable=v,value=3).grid(row=3,column=3)
    Radiobutton(root,text='CHENNAI',font="Arial 9 bold",bg='light blue',variable=v,value=4).grid(row=3,column=4)
    Label(root,text='DESTINATION:-',font="Arial 10 bold",bg='light blue').grid(row=3,column=6)
    v1=IntVar(root)
    Radiobutton(root,text='CHICAGO',font="Arial 9 bold",bg='light blue',variable=v1,value=1).grid(row=3,column=7)
    Radiobutton(root,text='LONDON',font="Arial 9 bold",bg='light blue',variable=v1,value=2).grid(row=3,column=8)
    Radiobutton(root,text='NEW YORK',font="Arial 9 bold",bg='light blue',variable=v1,value=3).grid(row=3,column=9)
    Radiobutton(root,text='GOA',font="Arial 9 bold",bg='light blue',variable=v1,value=4).grid(row=3,column=10)
    Label(root,text='ENTER THE ID TO SEARCH',font="Arial 10 bold",bg='light blue').grid(row=4,column=0)
    i2=Entry(root)
    i2.grid(row=4,column=1)
    def show_all():
        cur.execute("select * from flights")
        m=cur.fetchall()
        s=''
        for x in m:
            y=str(x[0])+' '+x[1]+' '+x[2]+' '+x[3]+'\n'
            s=s+y
        tkinter.messagebox.showinfo('show',s)
    Button(root,text='SEARCH ALL',font="Arial 10 bold",bg='light blue',command=show_all).grid(row=20,column=3)
    def add_flight():
        q=i.get()
        w=i1.get()
        a1=''
        a2=''
        if v.get()==1:
            a1='NEW DELHI'
        elif v.get()==2:
            a1='MUMBAI'
        elif v.get()==3:
            a1='BANGLURU'
        elif v.get()==4:
            a1='CHENNAI'
        if v1.get()==1:
            a2='CHICAGO'
        elif v1.get()==2:
            a2='LONDON'
        elif v1.get()==3:
            a2='NEW YORK'
        elif v1.get()==4:
            a2='GOA'
        cur.execute("insert into flights (id,flight_name,source,destination)values(?,?,?,?)",(q,w,a1,a2))
        con.commit()
        tkinter.messagebox.showinfo('insert','Added')
        i.delete(0,END)
        i1.delete(0,END)
        v.delete(0,END)
        v1.delete(0,END)
    Button(root,text='ADD FLIGHT',font="Arial 10 bold",bg='light blue',command=add_flight).grid(row=20,column=4)
    def search():
        e=i2.get()
        cur.execute("select * from flights where id=?",(int(e),))
        n=cur.fetchone()
        if n==None:
            tkinter.messagebox.showwarning('error','not available')
            return
        x=str(n[0])+' '+n[1]+' '+n[2]+' '+n[3]+'\n'
        tkinter.messagebox.showinfo('found',x)
    Button(root,text='SEARCH',font="Arial 10 bold",bg='light blue',command=search).grid(row=20,column=5)
    Label(root,text='FOR BOOKING TICKET CLICK HERE',font="Arial 10 bold",bg='light blue').grid(row=30,column=0)
    def proceed():
        root.destroy()
        r1=Tk()
        r1.geometry('2000x300')
        r1.configure(bg='light blue')
        Label(r1,text='PASSENGER DETAILES',font="Arial 25 bold",bg='red',justify=CENTER).grid(row=0,column=4)
        Label(r1,text='FLIGHT ID',font="Arial 10 bold",bg='light blue').grid(row=2,column=0)
        a=Entry(r1)
        a.grid(row=2,column=1)
        Label(r1,text='FIRST NAME',font="Arial 10 bold",bg='light blue').grid(row=4,column=0)
        a1=Entry(r1)
        a1.grid(row=4,column=1)
        Label(r1,text='LAST NAME',font="Arial 10 bold",bg='light blue').grid(row=4,column=7)
        a2=Entry(r1)
        a2.grid(row=4,column=9)
        Label(r1,text='DOB(DD/MM/YYYY',font="Arial 10 bold",bg='light blue').grid(row=5,column=0)
        a3=Entry(r1)
        a3.grid(row=5,column=1)
        Label(r1,text='SEX',font="Arial 10 bold",bg='light blue').grid(row=6,column=0)
        v=IntVar(r1)
        Radiobutton(r1,text='MALE',font="Arial 9 bold",bg='light blue',variable=v,value=1).grid(row=6,column=1)
        Radiobutton(r1,text='FEMALE',font="Arial 9 bold",bg='light blue',variable=v,value=2).grid(row=6,column=2)
        Label(r1,text='PHONE NUMBER',font="Arial 10 bold",bg='light blue').grid(row=7,column=0)
        a4=Entry(r1)
        a4.grid(row=7,column=1)
        Label(r1,text='SOURCE:-',font="Arial 10 bold",bg='light blue').grid(row=8,column=0)
        v1=IntVar(r1)
        Radiobutton(r1,text='NEW DELHI',font="Arial 9 bold",bg='light blue',variable=v1,value=1).grid(row=8,column=1)
        Radiobutton(r1,text='MUMBAI',font="Arial 9 bold",bg='light blue',variable=v1,value=2).grid(row=8,column=2)
        Radiobutton(r1,text='BANGLURU',font="Arial 9 bold",bg='light blue',variable=v1,value=3).grid(row=8,column=3)
        Radiobutton(r1,text='CHENNAI',font="Arial 9 bold",bg='light blue',variable=v1,value=4).grid(row=8,column=4)
        Label(r1,text='DESTINATION:-',font="Arial 10 bold",bg='light blue').grid(row=8,column=6)
        v2=IntVar(r1)
        Radiobutton(r1,text='CHICAGO',font="Arial 9 bold",bg='light blue',variable=v2,value=1).grid(row=8,column=7)
        Radiobutton(r1,text='LONDON',font="Arial 9 bold",bg='light blue',variable=v2,value=2).grid(row=8,column=8)
        Radiobutton(r1,text='NEW YORK',font="Arial 9 bold",bg='light blue',variable=v2,value=3).grid(row=8,column=9)
        Radiobutton(r1,text='GOA',font="Arial 9 bold",bg='light blue',variable=v2,value=4).grid(row=8,column=10)
        Label(r1,text='ID PROOF(VOTER/PAN NO./ADHAR NO.)',font="Arial 10 bold",bg='light blue').grid(row=9,column=0)
        a5=Entry(r1)
        a5.grid(row=9,column=1)
        def confirm():
            q1=a.get()
            w1=a1.get()
            q2=a2.get()
            w2=a3.get()
            p=a4.get()
            m1=a5.get()
            b=''
            b1=''
            b2=''
            if v1.get()==1:
                b1='NEW DELHI'
            elif v1.get()==2:
                b1='MUMBAI'
            elif v1.get()==3:
                b1='BANGLURU'
            elif v1.get()==4:
                b1='CHENNAI'
            if v2.get()==1:
                b2='CHICAGO'
            elif v2.get()==2:
                b2='LONDON'
            elif v2.get()==3:
                b2='NEW YORK'
            elif v2.get()==4:
                b2='GOA'
            if v.get()==1:
                b='MALE'
            elif v.get()==2:
                b='FEMALE'
            cur.execute("insert into passenger (id,flight_name,last_name,age,sex,phone_no,source,destination,id_p)values(?,?,?,?,?,?,?,?,?)",(q1,w1,q2,w2,p,m1,b,b1,b2))
            con.commit()
            tkMessageBox.showinfo('insert','TICKET CONFIRM')
            a.delete(0,END)
            a1.delete(0,END)
            a2.delete(0,END)
            a3.delete(0,END)
            a4.delete(0,END)
            a5.delete(0,END)
        Button(r1,text='CONFIRM',font="Arial 10 bold",bg='light blue',padx=20,command=confirm).grid(row=14,column=2)
        def show_t():
            cur.execute("select * from passenger")
            m=cur.fetchall()
            s=''
            for x in m:
                y=str(x[0])+' '+x[1]+' '+x[2]+' '+x[3]+' '+x[4]+' '+str (x[5])+' '+x[6]+' '+x[7]+' '+str (x[8])+'\n'
                s=s+y
            tkinter.messagebox.showinfo('show_t',s)
        Button(r1,text='SHOW TICKET',font="Arial 10 bold",bg='light blue',padx=20,command=show_t).grid(row=14,column=6)
        def Ticket():
            if v1.get()==1 and v2.get()==1:
                tkMessageBox.showinfo('ticket','150000')
            if v1.get()==1 and v2.get()==2:
                tkMessageBox.showinfo('ticket','560000')
            if v1.get()==1 and v2.get()==3:
                tkMessageBox.showinfo('ticket','675600')
            if v1.get()==1 and v2.get()==4:
                tkMessageBox.showinfo('ticket','458213')
            if v1.get()==2 and v2.get()==1:
                tkMessageBox.showinfo('ticket','365214')
            if v1.get()==2 and v2.get()==2:
                tkMessageBox.showinfo('ticket','785462')
            if v1.get()==2 and v2.get()==3:
                tkMessageBox.showinfo('ticket','655241')
            if v1.get()==2 and v2.get()==4:
                tkMessageBox.showinfo('ticket','452152')
            if v1.get()==3 and v2.get()==1:
                tkMessageBox.showinfo('ticket','578655')
            if v1.get()==3 and v2.get()==2:
                tkMessageBox.showinfo('ticket','658975')
            if v1.get()==3 and v2.get()==3:
                tkMessageBox.showinfo('ticket','985644')
            if v1.get()==3 and v2.get()==4:
                tkMessageBox.showinfo('ticket','256636')
            if v1.get()==4 and v2.get()==1:
                tkMessageBox.showinfo('ticket','458799')
            if v1.get()==4 and v2.get()==2:
                tkMessageBox.showinfo('ticket','255000')
            if v1.get()==4 and v2.get()==3:
                tkMessageBox.showinfo('ticket','500369')
            if v1.get()==4 and v2.get()==4:
                tkMessageBox.showinfo('ticket','300000')
        Button(r1,text='TOTAL AMOUNT',font="Arial 10 bold",bg='light blue',padx=20,command=Ticket).grid(row=14,column=4)
        r1.mainloop()
    Button(root,text='PROCEED>>',font="Arial 10 bold",bg='light blue',justify=RIGHT,command=proceed).grid(row=31,column=0)
    root.mainloop()
shortcutbar = Frame(root1, height=60, bg='orange')
toolbar = Label(shortcutbar, text='PYTHON PROJECT',bg='blue',fg='black',height=2,font='Arial 12 bold')
toolbar.pack(side=TOP,fill=X,expand=YES)
shortcutbar.pack(expand=NO, fill=X)
shortcutbar2 = Frame(root1, height=60, bg="orange")
toolbar = Label(shortcutbar2, text="Welcome To Flight Ticket Management System ",bg='green',fg='black',height=2,font='Arial 12 bold')
toolbar.pack(side=TOP,fill=X,expand=YES)
shortcutbar2.pack(expand=NO, fill=X)
toolbar = Label(shortcutbar, text='',bg='green',fg='black',height=2,font='Arial 12 bold')
toolbar.pack(side=TOP,fill=X,expand=YES)
shortcutbar.pack(expand=NO, fill=X)
shortcutbar2 = Frame(root1, height=60, bg='orange')
toolbar = Label(shortcutbar2, text="",bg='light green',fg='black',height=2,font='Arial 12 bold')
toolbar.pack(side=TOP,fill=X,expand=YES)
shortcutbar2.pack(expand=NO, fill=X)
def aboutus():
    master=Tk()
    shortcutbar = Frame(master, height=30, bg='light blue')
    toolbar = Label(shortcutbar, text='PYTHON PROJECT',bg='light blue',fg='purple',height=2,font='Arial 12 bold')
    toolbar.pack(side=TOP,fill=X,expand=YES)
    shortcutbar.pack(expand=NO, fill=X)
    Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(master, text='\n\n\nFlight Ticket Management System\n\n\nThe project is designed by',fg='red',font='Times 18').pack(side=TOP,anchor=CENTER)
    Label(master, text='Ayush Dayal',fg='black',font='Times 20 bold').pack(side=TOP,anchor=CENTER)
    Label(master, text='Enroll-(151264)',fg='black',font='Times 20 bold').pack(side=TOP,anchor=CENTER)
    Label(master, text='Batch-B2',fg='black',font='Times 20 bold').pack(side=TOP,anchor=CENTER)
    Label(master, text='Email-id=ayush.dayal22@gmail.com',fg='black',font='Times 20 bold').pack(side=TOP,anchor=CENTER)
    Label(master, text='Mobile NO=9630693058',fg='black',font='Times 20 bold').pack(side=TOP,anchor=CENTER)
    Label(master, text='\nSubmitted To',fg='black',font='Times 18').pack(side=TOP,anchor=CENTER)
    Label(master, text='Dr. Mahesh Kumar',fg='black',font='Times 20 bold').pack(side=TOP,anchor=CENTER)
    def sbmt():
        master.destroy()
        page2()
    s = Frame(master, height=30, bg='light green')
    Button(s, text='EXIT',width=16,height=1,bg='light blue',fg='black',font='Times 12 bold',command=master.destroy).pack(side=BOTTOM,fill=X,anchor=SW)
    s.pack(side=BOTTOM,expand=NO, fill=X)
def submit():    
    root1.destroy()
    page2()
s = Frame(root1, height=30, bg='light green')
Button(s, text='Exit',width=16,height=1,bg='light blue',fg='black',font='Times 14 bold',command=root1.destroy).pack(side=BOTTOM,fill=X,anchor=SW)
s.pack(side=BOTTOM,expand=YES, fill=X)    
Button(padx=16,pady=1,bd=4,fg="black",font=("arial",14,"bold"),background="powder blue",width=4,
           text="STUDENT INFORMATION",command=aboutus).pack(side=BOTTOM,fill=X,anchor=SW)
Button(padx=16,pady=1,bd=4,fg="black",font=("arial",14,"bold"),background="powder blue",width=4,
           text="Enter",command=enter).pack(side=BOTTOM,fill=X,anchor=SW)
root1.mainloop()

