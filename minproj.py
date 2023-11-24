import mysql.connector
import tkinter as tk
from tkinter import *
import customtkinter as ctk
from PIL import Image,ImageTk

# Backend python functions code starts :
mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database="bank")
mycursor=mydb.cursor()
# frontend python functions code starts :
window=ctk.CTk()
def welcome():
    window.geometry("600x450+383+106")
    window.title("Start Page")
    window.config(bg='navy')
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("green")
    frame=ctk.CTkFrame(master=window,fg_color='yellow2')
    frame.pack(pady=50,padx=80,fill="both",expand=True)
    label1=ctk.CTkLabel(master=frame,text="Welcome To Our Bank",font=("TkHeadingFont",26))
    label1.pack(pady=20,padx=40)
    button1=ctk.CTkButton(master=frame,text="admin",command=adminlogin)
    button1.pack(pady=20,padx=40)
    button2=ctk.CTkButton(master=frame,text="customer",command=customerlogin)
    button2.pack(pady=20,padx=40)
    img=ImageTk.PhotoImage(Image.open("./images/bank1.png"))
    label2=Label(image=img)
    label2.image=img
    label2.pack(pady=20)
def deposit():
    print("test")
def withdraw():
    print("test")
def transfer():
    print("transfer")
def status():
    print("test")
def delete():
    print("test")
def support():
    print("transfer")
def menupg():
    newindow2=Toplevel(window)
    newindow2.geometry("1500x700")
    newindow2.title("Menu Page")
    ctk.set_appearance_mode("light")
    newindow2.config(bg='coral1')
    ctk.set_default_color_theme("blue")
    frame3=ctk.CTkFrame(master=newindow2,width=600,height=600,corner_radius=15,fg_color='ivory2')
    frame3.pack(pady=50,padx=150,fill="both",expand=True)
    label7=ctk.CTkLabel(master=frame3,text="MENU",font=("TkHeading",26),text_color='black')
    label7.pack(pady=20,padx=40)
    button8=ctk.CTkButton(master=frame3,text="Deposit",command=deposit,height=100,width=100)
    button8.place(y=100,x=600)
    button9=ctk.CTkButton(master=frame3,text="Withdraw",command=withdraw,height=100,width=100)
    button9.place(y=100,x=730)
    button10=ctk.CTkButton(master=frame3,text="Transfer",command=transfer,height=100,width=100)
    button10.place(y=100,x=860)
    button11=ctk.CTkButton(master=frame3,text="Loan status",command=status,height=100,width=100)
    button11.place(y=300,x=600)
    button12=ctk.CTkButton(master=frame3,text="Request Account Deletion",command=delete,height=100)
    button12.place(y=300,x=730)
    button13=ctk.CTkButton(master=frame3,text="Customer Support",command=support,height=50,width=100)
    button13.place(y=500,x=800)
def csign():
    newindow1=Toplevel(window)
    newindow1.geometry("925x925")
    newindow1.title("cutomer signin")
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("green")
    def show():
        if entry9.cget('show')=='*':
            entry9.configure(show='')

        else:
            entry9.configure(show='*')
    frame2=ctk.CTkScrollableFrame(master=newindow1,width=470,height=510,corner_radius=15,fg_color='lemon chiffon')
    frame2.pack(pady=0,padx=0,fill="both",expand=True)
    label6=ctk.CTkLabel(master=frame2,text="Customer Registeration",font=("Helvetica",26),text_color='black')
    label6.pack(pady=20,padx=10)
    entry3=ctk.CTkEntry(master=frame2,width=300,placeholder_text="FullName")
    entry3.pack(pady=20,padx=15)
    entry4=ctk.CTkEntry(master=frame2,width=220,placeholder_text="Address")
    entry4.pack(pady=20,padx=15)
    entry5=ctk.CTkEntry(master=frame2,width=220,placeholder_text="Email")
    entry5.pack(pady=20,padx=15)
    entry6=ctk.CTkEntry(master=frame2,width=220,placeholder_text="Mobilenumber")
    entry6.pack(pady=20,padx=15)
    entry7=ctk.CTkEntry(master=frame2,width=220,placeholder_text="Age")
    entry7.pack(pady=20,padx=15)
    label6=ctk.CTkLabel(master=frame2,text="Create Username and Password:",font=("Helvetica",16),text_color='black')
    label6.pack(pady=20,padx=10)
    entry8=ctk.CTkEntry(master=frame2,width=220,placeholder_text="Username")
    entry8.pack(pady=20,padx=15)
    entry9=ctk.CTkEntry(master=frame2,width=220,placeholder_text="Password",show='*')
    entry9.pack(pady=20,padx=15)
    button7=ctk.CTkCheckBox(master=frame2,text="Show/Hide",command=show)
    button7.pack(pady=20,padx=15)
    button6=ctk.CTkButton(master=frame2,text="Register",command=menupg)
    button6.pack(pady=20,padx=15)
    img2=ImageTk.PhotoImage(Image.open("./images/cust1.png"))
    label5=Label(image=img2)
    label5=ctk.CTkLabel(newindow1,image=img2,text="")
    label5.image=img2
    label5.place(x=0.5,y=0.5)
def adminlogin():
    print("Test")
def customerlogin():
    newindow=Toplevel(window)
    newindow.geometry("600x600")
    newindow.title("Cutomer Loginpage")
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("green")
    frame1=ctk.CTkFrame(master=newindow,width=600,height=600,corner_radius=15,fg_color='light goldenrod')
    frame1.pack(pady=0,padx=0,fill="both",expand=True)
    img1=ImageTk.PhotoImage(Image.open("./images/adminLogin1.png"))
    label4=tk.Label(newindow,image=img1)
    label4.image=img1
    label4.pack(pady=0,padx=0)
    label3=ctk.CTkLabel(master=frame1,text="Customer Login",font=("TkHeading",26),text_color='black')
    label3.pack(pady=45,padx=50)
    entry1=ctk.CTkEntry(master=frame1,width=220,placeholder_text="Username")
    entry1.pack(pady=20,padx=40)
    entry2=ctk.CTkEntry(master=frame1,width=220,placeholder_text="Password")
    entry2.pack(pady=20,padx=40)
    def close():
        newindow.withdraw()
    button3=ctk.CTkButton(master=frame1,text="Login",command=menupg)
    button3.pack(pady=20,padx=40)
    button4=ctk.CTkButton(master=frame1,text="Signup",command=csign)
    button4.pack(pady=20,padx=40)
    
welcome()
window.mainloop()
