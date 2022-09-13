from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


root=Tk()
root.title('login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

#ShowPasswordFunction
def ShowPasswordFunc():
    if CheckedShowPassword.get() == 1:
        Entry.config(show=' ')
    elif CheckedShowPassword.get()==0:
        Entry.config(show='*')

def signin():
    username=user.get()
    password=code.get()

    if username=='admin' and password=='1234':
        screen=Toplevel(root)
        screen.title('App')
        screen.geometry('925x500+300+200')
        screen.config(bg='white')

        Label(screen, text='Hello Everyone!', bg='#fff', font=('calibri(Body)',50,'bold')).pack(expand=True)

        screen.mainloop()

    elif username!='admin' and password!='1234':
        messagebox.showerror('invalid', 'invalid username and password')

    elif password!="1234":
        messagebox.showerror('invalid', 'invalid password')

    elif username!= "admin":
        messagebox.showerror('invalid', 'invalid username')


#Image
path = "Pos4.jpg"
img = ImageTk.PhotoImage(Image.open(path))
Label(root,image=img,bg='white').place(x=100, y=100)

frame=Frame(root,width=350, height=350,bg='white')
frame.place(x=600, y=77)

heading=Label(frame,text='Sign in', fg='black',bg='white',font=('arial',23,'bold'))
heading.place(x=100,y=5)

##########..............................................................

def on_enter(e):
    user.delete(0, 'end')
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')

user=Entry(frame,width=25,fg='black',  bg='white',font=('arial',11))
user.place(x=50, y=80)
user.insert(0,'Username:')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>', on_leave)





##############.............................................................
def on_enter(e):
    code.delete(0, 'end')
def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')

#ShowPasswordFunction
code=Entry(frame,width=25,fg='black', bg='white',font=('arial',11))
code.place(x=50, y=150)
code.insert(0, 'Password:')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>', on_leave)


#CheckBox Show Password
CheckedShowPassword=IntVar()

ShowPasswordCheckbox=Checkbutton(root,text="showPassword",variable=CheckedShowPassword,command=ShowPasswordFunc)
ShowPasswordCheckbox.place(x=700, y=260)


###################################################################################

Button(frame, width=15, pady=7, text='Sign in', bg='#34282c', fg='white',border=0, command=signin).place(x=100, y=220)
label=Label(frame,text="Don't have an account?",fg='black',bg='white', font=('arial',9))
label.place(x=75, y=270)

sign_up=Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#34282c',command=signin)
sign_up.place(x=200,y=270)



root.mainloop()