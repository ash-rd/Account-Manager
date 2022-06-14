from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image
from PIL import *
from functools import partial
import backend
import json 

"""===========================================================
                    APPLICATION WINDOW CONFIG
============================================================="""

win = Tk()
win.title('Accoount Manager')
win.resizable(False, False)
win.geometry('650x600')
icon =PhotoImage(file="icon/Account_Manager.png")
win.iconphoto(False, icon)


"""===========================================================
                        APPLICATION INFO
============================================================="""

global version_ID
version_ID = "   Account Manager    v 1.0"
global Titile
Title = "Account Manager"



"""===========================================================
                         FILE HANDLING
============================================================="""


global file
file = 'username.json'
global file2
file2 = 'password.json'

global file_password
file_password = 'password2.json'


"""===========================================================
                         START FUNCTION
============================================================="""

def main():
    try:
        with open(file, 'r') as file_object:
            pass

    except FileNotFoundError:
        reg()

    else:
        login()


"""===========================================================
                         CHECK FUNCTION
============================================================="""

def check():
    with open(file, 'r') as check_object:
        check_data = check_object.read()
        
        if check_data == "":
            messagebox.showwarning("Warning", "Username cannot be blank")
            reg()

    with open(file2, 'r') as check_object2:
        check_data2 = check_object2.read()

        if check_data2 == "":
            messagebox.showwarning("Warning", "Password cannot be blank")
            reg()
        
        else:
            login()

"""===========================================================
                        VALID FUNCTION
============================================================="""

def valid():
    with open(file2, 'r') as valid_object:
        valid = valid_object.read()
        
        with open(file_password, 'r') as fp_object:
            fp = fp_object.read()
            
            if valid == fp:
                dashboard()
                
            else:
                messagebox.showwarning("Warning", "Password is incorrect")
                login()


#DELETE FUNCTION
def delete_function():
    try:
        backend.delete(selected_row[0])
        messagebox.showwarning("Warning", "1 record has been deleted")
        dashboard()
        
    except:
        NameError
        dashboard()
        
"""===========================================================
                     REGISTERATION FORM
============================================================="""


def reg():

    backend.drop_TableAccount()
    backend.drop_TableUser()
    backend.connect()
    
    #frame
    reg = Frame()
    reg.place(x=0, y=0, width=650, height=600)
    
    #IMAGE #ICON
    img1 = Image.open("icon/manager_PNG.png")
    image1 = img1.resize((120, 120))
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test
    label1.place(x=262, y=10)

    
    #Label
    emptySpace =  Label(reg, text=' ', padx=10, pady=25, font=("Century Gothic", 45)).pack()

    textRegister = Label(reg, text='Register', padx=10, pady=2,font=("Verdana", 25)).pack()
    dashLabel = Label(reg, text='______________________', padx=10, pady=2,font=("Verdana", 18)).pack()

    #Label & Button | Username
    empty_space=Label(reg, text='', pady=2,font=("Century Gothic", 12)).pack()
    text=Label(reg, text='Enter Username ', padx=10, pady=2,font=("Century Gothic", 12)).pack()

    #IMAGE #ICON #USERNAME
    img1 = Image.open("icon/user_reg.png")
    image1 = img1.resize((18, 18))
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test
    label1.place(x=160, y=272)

    #USERNAME ENTRY
    username = tk.StringVar()
    e1 = Entry(reg, textvariable=username, width=30, font=("Century Gothic", 12)).pack()
    
    #Label & Button | Password
    empty_space=Label(reg, text='', pady=2,font=("Century Gothic", 6)).pack()
    text=Label(reg, text='Enter Password', padx=10, pady=2,font=("Century Gothic", 12)).pack()

    #IMAGE #ICON #PASSWORD
    img1 = Image.open("icon/padlock.png")
    image1 = img1.resize((18, 18))
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test
    label1.place(x=160, y=346)

    #PASWORD ENTRY
    password = tk.StringVar()
    e2 = Entry(reg, textvariable=password, width=30, font=("Century Gothic", 12), show='*').pack()
    
    empty_space=Label(reg, text='', pady=4,font=("Century Gothic", 10)).pack()

    
    #LOAD FUNCTION FETCHING ENTRY AND STORING IT IN FILE JSON FORMAT
    def load():
        with open(file, 'w') as file_object:
            data1 = (username.get())
            file_object.write(data1)
            file_object.close()
            
        with open(file2, 'w') as file2_object:
            data2 = (password.get())
            file2_object.write(data2)
            file2_object.close()
            
        check()

    #REGISTER BUTTON
    button = Button(reg, text='Register', padx=2, pady=2, width=22, fg='white', bg='#4285F4"',
                  font=('Century Gothic', 12), command=load).pack()

    #APP INFO
    #IMAGE #ICON #USERNAME
    img1 = Image.open("icon/Account_Manager.png")
    image1 = img1.resize((18, 18))
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test
    label1.place(x=476, y=578)


    dashLabel = Label(reg, text='____________________________',padx=1, pady=0,
                   font=("Century Gothic", 10)).place(x=460, y=560)

    #VERSION ID
    AmLabel = Label(reg,text=version_ID, fg='blue', padx=10, pady=2,
                    font = ("Segoe UI Semibold", 8)).place(x=480, y=578)



"""===========================================================
                          LOGIN FORM
============================================================="""


def login():
    #LOGIN FRAME
    login = Frame()
    login.place(x=0, y=0, width=650, height=600)
    
    #IMAGE #ICON
    img1 = Image.open("icon/manager_PNG.png")
    image1 = img1.resize((120, 120))
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test
    label1.place(x=262, y=10)

    #EMPTY PADDING
    emptySpace =  Label(login, text=' ', padx=30, pady=30, font=("Century Gothic", 45)).pack()

    #HEADER LABEL
    text=Label(login, text='Login', padx=10, pady=2,font=("Verdana", 25)).pack()
    text=Label(login, text='______________________', padx=10, pady=2,font=("Verdana", 18)).pack()


   #FILE HANDLING 
    with open(file, "r") as read_obj:
        user_data = read_obj.read()
        
    text=Label(login, text='Welcome ' + str(user_data) , fg='gray', padx=10, pady=2,font=("Century Gothic", 16)).pack()
    empty_space=Label(login,  text='', pady=2,font=("Century Gothic", 12)).pack()
    
    text=Label(login, text='Enter Password', padx=10, pady=2,font=("Century Gothic", 12)).pack()

    #IMAGE #ICON #PASSWORD
    img1 = Image.open("icon/padlock.png")
    image1 = img1.resize((18, 18))
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test
    label1.place(x=160, y=315)

    #PASSWORD ENTRY
    password_entry = tk.StringVar()
    entry=Entry(login, textvariable=password_entry, width=30, font=("Century Gothic", 12), show='*').pack()

    empty_space=Label(login, text='', pady=4,font=("Century Gothic", 10)).pack()


    def load2():
        with open(file_password, 'w') as fp_object:
            fp = (password_entry.get())
            fp_object.write(fp)
            fp_object.close()
            
        #VALID FUNCTION CALL    
        valid()

   
    #LOGIN BUTTON
    button=Button(login, text='Login', padx=2, pady=2, width=22,
                  fg='white', bg='#4285F4"',
                  font=('Century Gothic', 12), command=load2).pack()


    #APP INFO
    #IMAGE #ICON #APPICON
    img1 = Image.open("icon/Account_Manager.png")
    image1 = img1.resize((18, 18))
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test
    label1.place(x=466, y=578)

    dashLabel = Label(login, text='____________________________',padx=1, pady=0,
                   font=("Century Gothic", 10)).place(x=460, y=560)

    #VERSION ID
    AmLabelL = Label(login,text=version_ID, fg='blue', padx=10, pady=2,
                    font = ("Segoe UI Semibold", 8)).place(x=480, y=578)



"""===========================================================
                          CREATE FORM
============================================================="""

def create_new():

    #FRAME
    create=Frame()
    create.place(x=0, y=0, width=650, height=600)

    #HEADER
    title=Label(create, text=Title, fg='blue', padx=10, pady=2, font=("Segoe UI Semibold", 32)).place(x=10, y=10)

    #IMAGE #ICON #BACK
    img1 = Image.open("icon/back.png")
    image1 = img1.resize((21, 21))
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test
    label1.place(x=520, y=32)
    
    back=Button(create, text='Back', bg='lightblue', padx=10, pady=1, font=("Century Gothic", 10),
                  command=dashboard).place(x=550, y=30)

    dashLabel = Label(create, text='__________________________________________________________________________________',
               padx=1, pady=0,
               font=("Century Gothic", 10)).place(x=0, y=80)


    """===========================================================
                             ADD FUNCTION
    ============================================================="""

    def add():
        backend.insert(title.get(), username.get(), password.get(), url.get(), comment.get())
        messagebox.showwarning("Warning", "Record has been saved successfully")
        dashboard()
    
    #SAVE BUTTON
    save=Button(create, text='Save', bg='lightblue', padx=10, pady=1, font=("Century Gothic", 10),
                command=add).place(x=550, y=500)


    #CREATE NEW LABEL
    text_label=Label(create, text='Create New', padx=30, pady=2, font=("Century Gothic", 22)).place(x=20, y=120)

    #IMAGE #ICON #CREATE PEN
    img1 = Image.open("icon/pen.png")
    image1 = img1.resize((23, 23))
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test
    label1.place(x=240, y=130)    
    t_label=Label(create, text='    Title', padx=0, pady=0, font=('Calibri', 14)).place(x=70, y=200)

    #IMAGE #ICON #TITLE
    img1 = Image.open("icon/title_icon.png")
    image1 = img1.resize((20, 20))
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test
    label1.place(x=210, y=200)
    
    title = tk.StringVar()
    t_entry=Entry(create, textvariable=title, width=28, font=('Calibri', 14)).place(x=250, y=200)
    
    u_label=Label(create, text='   Username', padx=0, pady=0, font=('Calibri', 14)).place(x=70, y=250)

    #IMAGE #ICON #USENAME
    img1 = Image.open("icon/user_reg.png")
    image1 = img1.resize((20, 20))
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test
    label1.place(x=210, y=250)
    
    username = tk.StringVar()
    u_entry=Entry(create,textvariable=username, width=28, font=('Calibri', 14)).place(x=250, y=250)
    
    p_label=Label(create, text='   Password', padx=0, pady=0, font=('Calibri', 14)).place(x=70, y=300)

    #IMAGE #ICON #PASSWORD
    img1 = Image.open("icon/padlock.png")
    image1 = img1.resize((20, 20))
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test
    label1.place(x=210, y=300)
    
    password = tk.StringVar()
    p_entry=Entry(create,textvariable=password, width=28, font=('Calibri', 14)).place(x=250, y=300)
    
    url_label=Label(create, text='   Url', padx=0, pady=0, font=('Calibri', 14)).place(x=70, y=350)

    #IMAGE #ICON #URL
    img1 = Image.open("icon/url_icon.png")
    image1 = img1.resize((20, 20))
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test
    label1.place(x=210, y=350)
    
    url = tk.StringVar()
    url_entry=Entry(create,textvariable=url, width=28, font=('Calibri', 14)).place(x=250, y=350)

    c_label=Label(create, text='   #Comment', padx=0, pady=0, font=('Calibri', 14)).place(x=70, y=400)

    #IMAGE #ICON #COMMENTS
    img1 = Image.open("icon/notes_icon.png")
    image1 = img1.resize((20, 20))
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test
    label1.place(x=210, y=400)
    
    comment = tk.StringVar()
    c_entry=Entry(create,textvariable=comment, width=28, font=('Calibri', 14)).place(x=250, y=400)



"""===========================================================
                      MAIN DASHBOARD FRAME
============================================================="""


def dashboard():
    db=Frame()
    db.place(x=0, y=0, width=650, height=600)


    #GET SELECTED ROW FUNCTION
    def get_selected_row(event):
        global selected_row
    
        index = listbox.curselection()[0]
        selected_row = listbox.get(index)
    
        e1.delete(0, END)
        e1.insert(END,selected_row[1])
        e2.delete(0, END)
        e2.insert(END,selected_row[2])
        e3.delete(0, END)
        e3.insert(END,selected_row[3])
        e4.delete(0, END)
        e4.insert(END,selected_row[4])
        e5.delete(0, END)
        e5.insert(END,selected_row[5])

    
    #HEADER
    #IMAGE #ICON #DASHBOARD
    img1 = Image.open("icon/home_icon.png")
    image1 = img1.resize((38, 38))
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test
    label1.place(x=20, y=20)

    #TITLE LABEL
    title=Label(db, text='Dashboard', fg='red', padx=10, pady=2, font=("Spectral", 32)).place(x=60, y=16)

    #CRETE BUTTON
    db=Button(db, text='Create', bg='lightblue', padx=10, pady=2, font=("Century Gothic", 10),
              command=create_new).place(x=480, y=30)

    #EXIT BUTTON
    ex=Button(db, text=' Exit ', bg='orange', padx=10, pady=2, font=("Century Gothic", 10),
              command=win.destroy).place(x=560, y=30)

    text=Label(db, text='__________________________________________________________________________________',
               padx=0, pady=0,
               font=("Century Gothic", 10)).place(x=0, y=64)



    #SCROLLBAR FRAME    
    scrollframe = Frame(db)

    scroll = Scrollbar(scrollframe)
    scroll.pack(side=RIGHT, fill=Y)


    #LISTBOX
    global listbox
    
    listbox = Listbox(scrollframe, font=("Segoe UI Semibold", 18), yscrollcommand=scroll.set)


    #FETCHING DATA IN SIDE LISTBOX
    listbox.delete(0, END)
    for row in backend.view():
        listbox.insert(END, row)

    listbox.pack(side=LEFT, fill=Y)

    scroll.config(command=listbox.yview)

    scrollframe.place(x=2, y=84, width=180, height=500)

    listbox.bind('<<ListboxSelect>>', get_selected_row)

    
    #FETCH ENTRY BOX
    t_label=Label(db, text='Title', padx=0, pady=0, font=('Calibri', 12)).place(x=240, y=110) #Title

    #IMAGE #ICON #TITLE
    img1 = Image.open("icon/title_icon.png")
    image1 = img1.resize((24, 24))
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test
    label1.place(x=200, y=140)

    #TITLE ENTRY
    entryt = tk.StringVar()
    e1=Entry(db, textvariable=entryt, width=28, font=('Calibri', 18)) #FetchTitle
    e1.place(x=240, y=140)


    #USERNAME LABEL
    u_label=Label(db, text='Username', padx=0, pady=0, font=('Calibri', 12)).place(x=240, y=200) #Username

    #IMAGE #ICON #USERNAME
    img1 = Image.open("icon/user_reg.png")
    image1 = img1.resize((24, 24))
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test
    label1.place(x=200, y=230)

    #USERNAME ENTRY
    entryu = tk.StringVar()
    e2=Entry(db, width=28, font=('Calibri', 18)) #FetchUsername
    e2.place(x=240, y=230)
    
    
    #PASSWORD LABEL
    p_label=Label(db, text='Password', padx=0, pady=0, font=('Calibri', 12)).place(x=240, y=280) #Password

    #IMAGE #ICON #PASSWORD
    img1 = Image.open("icon/padlock.png")
    image1 = img1.resize((24, 24))
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test
    label1.place(x=200, y=310)
    
    #PASSWORD ENTRY
    entryp = tk.StringVar()
    e3=Entry(db, width=28, font=('Calibri', 18),) #FetchPassword
    e3.place(x=240, y=310)


    #URL LABEL
    url_label=Label(db, text='Url', padx=0, pady=0, font=('Calibri', 12)).place(x=240, y=360) #URL

    #IMAGE #ICON #URL
    img1 = Image.open("icon/url_icon.png")
    image1 = img1.resize((24, 24))
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test
    label1.place(x=200, y=390)
    
    #URL ENTRY
    entryurl = tk.StringVar()
    e4=Entry(db, width=28, font=('Calibri', 18)) #FetchURL
    e4.place(x=240, y=390)


    #COMMENT LABEL
    c_label=Label(db, text='#Comment', padx=0, pady=0, font=('Calibri', 12)).place(x=240, y=440) #Comment

    #IMAGE #ICON #COMMENT
    img1 = Image.open("icon/notes_icon.png")
    image1 = img1.resize((24, 24))
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test
    label1.place(x=200, y=470)
    
    #COMMENT ENTRY
    entryc = tk.StringVar()
    e5=Entry(db, width=28, font=('Calibri', 18)) #FetchComment
    e5.place(x=240, y=470)


    #IMAGE #ICON #DELETE
    img1 = Image.open("icon/delete_icon.png")
    image1 = img1.resize((21, 21))
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test
    label1.place(x=510, y=562)
    
    #DELETE BUTTON
    del_button = Button(db, text='Delete', fg='white', bg='red',
                        padx=10, pady=2, font=("Century Gothic", 10), command=delete_function)
    del_button.place(x=540, y=560)


"""===========================================================
                         STARTING MAIN
============================================================="""

#CALLING MAIN FUNCTION
main()    


win.mainloop()
