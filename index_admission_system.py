import tkinter as tk
from tkinter import messagebox
import tkinter.filedialog as file
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import pymysql
import time
import datetime
import os
from shutil import copyfile

class homepage:
    def __init__(self, master):
        #window property
        self.master = master
        self.master.geometry("1200x720")
        #self.master.resizable(False, False)
        self.master.title("Login Page")
        self.master.config(background="cyan")

        #add frame to that window
        self.structure = tk.Frame(self.master, bg="cyan")
        self.structure.pack()

        #add content to the main frame
        self.heading = tk.Label(self.structure, text="Admission", fg="white", bg="indigo", font="elephant 25 bold", padx="700").pack()
        self.dummy=tk.Label(self.structure, text="", bg="cyan").pack()

        #add left align frame
        self.left_structure = tk.Frame(self.structure, bg="cyan",width="100")
        self.left_structure.pack(side=tk.LEFT)

        self.admin_login_label = tk.Label(self.left_structure,text="",bg="cyan",font="calibri 10 italic",width="50").pack()

        self.middle_structure_user_login = tk.Frame(self.structure, bg="royal blue",padx="20")
        self.middle_structure_user_login.pack(side=tk.LEFT)

        self.middle_structure_user_signup = tk.Frame(self.structure, bg="navy blue",padx="20")

        self.middle_structure_admin_login = tk.Frame(self.structure, bg="royal blue",padx="20")

        self.middle_structure_admin_signup = tk.Frame(self.structure, bg="navy blue",padx="20")

        self.middle_structure_forgot_password = tk.Frame(self.structure, bg="navy blue",padx="20")

        #this is for user login module
        self.userid_login = tk.StringVar()
        self.password_login = tk.StringVar()
        
        self.admin_login_label = tk.Label(self.middle_structure_user_login,text="",bg="royal blue",font="calibri 10 italic",).pack()
        self.admin_login_label = tk.Label(self.middle_structure_user_login,text="",bg="royal blue",font="calibri 10 italic",).pack()
        
        self.heading1 = tk.Label(self.middle_structure_user_login, text="user Login Here", fg="white", bg="royal blue", font="calibri 20 italic",padx="20").pack(fill=tk.X)
        self.dummy=tk.Label(self.middle_structure_user_login, text="", bg="royal blue").pack()

        self.left_userid_structure = tk.Frame(self.middle_structure_user_login, bg="royal blue")
        self.left_userid_structure.pack()
        
        self.admin_login_label_userid = tk.Label(self.left_userid_structure, text="     USER ID :",bg="royal blue", fg="white", font="arial 15 bold").pack(side=tk.LEFT)
        self.admin_login_txtbox_userid = tk.Entry(self.left_userid_structure, textvariable=self.userid_login, width=20, bg="teal",fg="white", font="cambria 15").pack(side=tk.LEFT)
        
        self.admin_login_label = tk.Label(self.middle_structure_user_login, text="", bg="royal blue", font="calibri 10 italic",).pack()

        self.left_password_structure = tk.Frame(self.middle_structure_user_login,bg="royal blue")
        self.left_password_structure.pack()
        
        self.admin_login_label_pass = tk.Label(self.left_password_structure,text="PASSWORD :",bg="royal blue",fg="white",font="arial 15 bold").pack(side=tk.LEFT)
        self.admin_login_txtbox_pass = tk.Entry(self.left_password_structure,textvariable=self.password_login,width=20,bg="teal",show="*",fg="white",font="cambria 15").pack(side=tk.LEFT)

        self.admin_login_label = tk.Label(self.middle_structure_user_login,text="",bg="royal blue",font="calibri 10 italic",).pack()

        self.left_btn_structure = tk.Frame(self.middle_structure_user_login,bg="royal blue")
        self.left_btn_structure.pack()
        
        self.admin_login_btn = tk.Button(self.left_btn_structure,text="Log In...",command=self.user_login,bg="green",fg="white",font="arial 15 bold").pack(side=tk.LEFT)

        self.user_login_message_login_label = tk.Label(self.middle_structure_user_login,text="",bg="royal blue",fg="white",font="calibri 10 italic")
        self.user_login_message_login_label.pack()
        
        self.admin_login_label = tk.Label(self.middle_structure_user_login,text="",bg="royal blue",font="calibri 10 italic",).pack()
        self.admin_login_label = tk.Label(self.middle_structure_user_login,text="",bg="royal blue",font="calibri 10 italic",).pack()

        self.extra_btn_structure = tk.Frame(self.middle_structure_user_login,bg="royal blue")
        self.extra_btn_structure.pack()

        self.admin_login_btn = tk.Button(self.extra_btn_structure,text="New User?",command=self.display_signup_module_user,bg="green",fg="white",font="arial 15 bold").pack(side=tk.RIGHT)
        
        self.admin_login_btn = tk.Button(self.extra_btn_structure,text="Forgot Password?",command=self.display_forgot_password_module,bg="red",fg="white",font="arial 15 bold").pack(side=tk.LEFT)
        self.admin_login_label = tk.Label(self.extra_btn_structure,text="",bg="royal blue",font="calibri 10 italic",width=5).pack(side=tk.LEFT)

        self.admin_login_label = tk.Label(self.middle_structure_user_login,text="",bg="royal blue",font="calibri 10 italic",).pack()
        self.admin_login_btn = tk.Button(self.middle_structure_user_login,text="Admin!!",command=self.display_admin_login_module,bg="blue",fg="white",font="arial 15 bold").pack()
        
        #forgot password module
        self.userid_forgot = tk.StringVar()
        self.secu_ans_forgot = tk.StringVar()
        self.password_forgot = tk.StringVar()
        self.conf_password_forgot = tk.StringVar()
        
        self.heading2 = tk.Label(self.middle_structure_forgot_password,text="user Sign Up Here",fg="white",bg="navy blue",font="calibri 20 italic",padx="85").pack(fill=tk.X)
        self.dummy=tk.Label(self.middle_structure_forgot_password,text="",bg="navy blue").pack()

        self.user_id_structure = tk.Frame(self.middle_structure_forgot_password,bg="navy blue")
        self.user_id_structure.pack()
        
        self.admin_signup_label_adminname = tk.Label(self.user_id_structure,text="USER ID :",bg="navy blue",fg="white",font="arial 15 bold").pack(side=tk.LEFT)
        self.admin_signup_txtbox_adminname = tk.Entry(self.user_id_structure,textvariable=self.userid_forgot,width=25,bg="teal",fg="white",font="cambria 15").pack(side=tk.LEFT)

        self.admin_signup_label = tk.Label(self.middle_structure_forgot_password,text="",bg="navy blue",font="calibri 10 italic",).pack()

        self.search_user_forgot = tk.Frame(self.middle_structure_forgot_password,bg="navy blue")
        self.search_user_forgot.pack()
        
        self.btn1 = tk.Button(self.search_user_forgot,text="Search User",command=self.Search_user_forgot,bg="green",fg="white",font="arial 15 bold").pack(side=tk.RIGHT)

        self.admin_login_btn = tk.Button(self.search_user_forgot,text="Back!!",command=self.display_login_module_user,bg="blue",fg="white",font="arial 15 bold").pack(side=tk.LEFT)
        self.admin_login_label = tk.Label(self.search_user_forgot,text="",bg="navy blue",font="calibri 10 italic",width=25).pack(side=tk.LEFT)
        
        self.forgot_frame = tk.Frame(self.middle_structure_forgot_password,bg="navy blue")

        self.admin_signup_label = tk.Label(self.forgot_frame,text="Security Question and Answer?",bg="navy blue",fg="white",font="calibri 15 italic",).pack()
        
        self.security_structure = tk.Frame(self.forgot_frame,bg="navy blue")
        self.security_structure.pack()
        
        self.security_question_label = tk.Label(self.security_structure,text="",bg="navy blue",fg="white",font="arial 15 bold")
        self.security_question_label.pack(side=tk.LEFT)
        self.admin_signup_txtbox_adminname = tk.Entry(self.security_structure,textvariable=self.secu_ans_forgot,width=25,bg="teal",fg="white",font="cambria 15").pack(side=tk.LEFT)

        self.admin_signup_label = tk.Label(self.middle_structure_forgot_password,text="",bg="navy blue",font="calibri 10 italic",).pack()

        self.right_pass_structure = tk.Frame(self.forgot_frame,bg="navy blue")
        self.right_pass_structure.pack()
        
        self.admin_signup_label_adminname = tk.Label(self.right_pass_structure,text="NEW PASSWORD :",bg="navy blue",fg="white",font="arial 15 bold").pack(side=tk.LEFT)
        self.admin_signup_txtbox_adminname = tk.Entry(self.right_pass_structure,textvariable=self.password_forgot,show="*",width=25,bg="teal",fg="white",font="cambria 15").pack(side=tk.LEFT)

        self.admin_signup_label = tk.Label(self.middle_structure_forgot_password,text="",bg="navy blue",font="calibri 10 italic",).pack()

        self.right_conf_pass_structure = tk.Frame(self.forgot_frame,bg="navy blue")
        self.right_conf_pass_structure.pack()
        
        self.admin_signup_label_adminname = tk.Label(self.right_conf_pass_structure,text="REENTER PASSWORD :",bg="navy blue",fg="white",font="arial 15 bold").pack(side=tk.LEFT)
        self.admin_signup_txtbox_adminname = tk.Entry(self.right_conf_pass_structure,textvariable=self.conf_password_forgot,show="*",width=25,bg="teal",fg="white",font="cambria 15").pack(side=tk.LEFT)

        self.admin_signup_label = tk.Label(self.forgot_frame,text="",bg="navy blue",font="calibri 10 italic",).pack()

        self.extra_btn_structure = tk.Frame(self.forgot_frame,bg="navy blue")
        self.extra_btn_structure.pack()

        self.admin_login_btn = tk.Button(self.extra_btn_structure,text="Update Password",command=self.forgot_password,bg="green",fg="white",font="arial 15 bold").pack(side=tk.RIGHT)
        
        self.admin_login_btn = tk.Button(self.extra_btn_structure,text="Back!!",command=self.display_login_module_user,bg="blue",fg="white",font="arial 15 bold").pack(side=tk.LEFT)
        self.admin_login_label = tk.Label(self.extra_btn_structure,text="",bg="navy blue",font="calibri 10 italic",width=25).pack(side=tk.LEFT)

        self.admin_login_label = tk.Label(self.forgot_frame,text="",bg="navy blue",font="calibri 10 italic",).pack()
        
        #this is for user sign Up module
        self.user_name_signup = tk.StringVar()
        self.user_security_question_signup = tk.StringVar()
        self.user_security_answer_signup = tk.StringVar()
        self.user_password_signup = tk.StringVar()
        self.user_confirm_password_signup = tk.StringVar()
        
        self.heading2 = tk.Label(self.middle_structure_user_signup,text="user Sign Up Here",fg="white",bg="navy blue",font="calibri 20 italic",padx="85").pack(fill=tk.X)
        self.dummy=tk.Label(self.middle_structure_user_signup,text="",bg="navy blue").pack()

        self.right_adminname_structure = tk.Frame(self.middle_structure_user_signup,bg="navy blue")
        self.right_adminname_structure.pack()
        
        self.admin_signup_label_adminname = tk.Label(self.right_adminname_structure,text="USER NAME :",bg="navy blue",fg="white",font="arial 15 bold").pack(side=tk.LEFT)
        self.admin_signup_txtbox_adminname = tk.Entry(self.right_adminname_structure,textvariable=self.user_name_signup,width=25,bg="teal",fg="white",font="cambria 15").pack(side=tk.LEFT)

        self.admin_signup_label = tk.Label(self.middle_structure_user_signup,text="",bg="navy blue",font="calibri 10 italic",).pack()

        self.right_usersec_ques_structure = tk.Frame(self.middle_structure_user_signup,bg="navy blue")
        self.right_usersec_ques_structure.pack()
        
        self.admin_signup_label_userid = tk.Label(self.right_usersec_ques_structure,text="Enter Security Question : ",bg="navy blue",fg="white",font="arial 15 bold").pack(side=tk.LEFT)
        self.admin_signup_txtbox_userid = tk.Entry(self.right_usersec_ques_structure,textvariable=self.user_security_question_signup,width=25,bg="teal",fg="white",font="cambria 15").pack(side=tk.LEFT)
        
        self.admin_signup_label = tk.Label(self.middle_structure_user_signup,text="",bg="navy blue",font="calibri 10 italic",).pack()

        self.right_usersec_ans_structure = tk.Frame(self.middle_structure_user_signup,bg="navy blue")
        self.right_usersec_ans_structure.pack()
        
        self.admin_signup_label_userid = tk.Label(self.right_usersec_ans_structure,text="Answer the Security Question : ",bg="navy blue",fg="white",font="arial 15 bold").pack(side=tk.LEFT)
        self.admin_signup_txtbox_userid = tk.Entry(self.right_usersec_ans_structure,textvariable=self.user_security_answer_signup,width=25,bg="teal",fg="white",font="cambria 15").pack(side=tk.LEFT)
        
        self.admin_signup_label = tk.Label(self.middle_structure_user_signup,text="",bg="navy blue",font="calibri 10 italic",).pack()
        
        self.right_password_structure = tk.Frame(self.middle_structure_user_signup,bg="navy blue")
        self.right_password_structure.pack()
        
        self.admin_signup_label_pass = tk.Label(self.right_password_structure,text=" PASSWORD : ",bg="navy blue",fg="white",font="arial 15 bold").pack(side=tk.LEFT)
        self.admin_signup_txtbox_pass = tk.Entry(self.right_password_structure,textvariable=self.user_password_signup,width=25,bg="teal",show="*",fg="white",font="cambria 15").pack(side=tk.LEFT)

        self.admin_signup_label = tk.Label(self.middle_structure_user_signup,text="",bg="navy blue",font="calibri 10 italic",).pack()

        self.right_conf_password_structure = tk.Frame(self.middle_structure_user_signup,bg="navy blue")
        self.right_conf_password_structure.pack()
        
        self.admin_signup_label_pass = tk.Label(self.right_conf_password_structure,text="Confirm PASSWORD : ",bg="navy blue",fg="white",font="arial 15 bold").pack(side=tk.LEFT)
        self.admin_signup_txtbox_pass = tk.Entry(self.right_conf_password_structure,textvariable=self.user_confirm_password_signup,width=25,bg="teal",show="*",fg="white",font="cambria 15").pack(side=tk.LEFT)

        self.admin_signup_label = tk.Label(self.middle_structure_user_signup,text="",bg="navy blue",font="calibri 10 italic",).pack()

        self.right_btn_structure = tk.Frame(self.middle_structure_user_signup,bg="navy blue")
        self.right_btn_structure.pack()
        
        self.admin_signup_btn = tk.Button(self.right_btn_structure,text="Sign Up...",command=self.user_signup,bg="blue",fg="white",font="arial 15 bold").pack(side=tk.LEFT)

        self.admin_signup_label = tk.Label(self.middle_structure_user_signup,text="",bg="navy blue",fg="white",font="calibri 10 italic").pack()
        self.user_signup_message_signup_label = tk.Label(self.middle_structure_user_signup,text="",bg="navy blue",fg="white",font="calibri 10 italic")
        self.user_signup_message_signup_label.pack()
        
        self.extra_btn_structure = tk.Frame(self.middle_structure_user_signup,bg="navy blue")
        self.extra_btn_structure.pack()

        self.admin_login_btn = tk.Button(self.extra_btn_structure,text="Log In?",command=self.display_login_module_user,bg="green",fg="white",font="arial 15 bold").pack(side=tk.RIGHT)
        
        self.admin_login_btn = tk.Button(self.extra_btn_structure,text="Admin!!",command=self.display_admin_login_module,bg="blue",fg="white",font="arial 15 bold").pack(side=tk.LEFT)
        self.admin_login_label = tk.Label(self.extra_btn_structure,text="",bg="navy blue",font="calibri 10 italic",width=25).pack(side=tk.LEFT)

        self.admin_login_label = tk.Label(self.middle_structure_user_signup,text="",bg="navy blue",font="calibri 10 italic",).pack()

        #this is for admin login module
        self.userid_admin_login = tk.StringVar()
        self.password_admin_login = tk.StringVar()
        
        self.heading1 = tk.Label(self.middle_structure_admin_login, text="Admin Login Here", fg="white", bg="royal blue", font="calibri 20 italic",padx="100").pack(fill=tk.X)
        self.dummy=tk.Label(self.middle_structure_admin_login, text="", bg="royal blue").pack()

        self.left_userid_structure = tk.Frame(self.middle_structure_admin_login, bg="royal blue")
        self.left_userid_structure.pack()
        
        self.admin_login_label_userid = tk.Label(self.left_userid_structure, text=" Admin ID :",bg="royal blue", fg="white", font="arial 15 bold").pack(side=tk.LEFT)
        self.admin_login_txtbox_userid = tk.Entry(self.left_userid_structure, textvariable=self.userid_admin_login, width=20, bg="teal",fg="white", font="cambria 15").pack(side=tk.LEFT)
        
        self.admin_login_label = tk.Label(self.middle_structure_admin_login, text="", bg="royal blue", font="calibri 10 italic",).pack()

        self.left_password_structure = tk.Frame(self.middle_structure_admin_login,bg="royal blue")
        self.left_password_structure.pack()
        
        self.admin_login_label_pass = tk.Label(self.left_password_structure,text="PASSWORD :",bg="royal blue",fg="white",font="arial 15 bold").pack(side=tk.LEFT)
        self.admin_login_txtbox_pass = tk.Entry(self.left_password_structure,textvariable=self.password_admin_login,width=20,bg="teal",show="*",fg="white",font="cambria 15").pack(side=tk.LEFT)

        self.admin_login_label = tk.Label(self.middle_structure_admin_login,text="",bg="royal blue",font="calibri 10 italic",).pack()

        self.left_btn_structure = tk.Frame(self.middle_structure_admin_login,bg="royal blue")
        self.left_btn_structure.pack()
        
        self.admin_login_btn = tk.Button(self.left_btn_structure,text="Log In...",command=self.admin_login,bg="green",fg="white",font="arial 15 bold").pack(side=tk.LEFT)

        self.admin_login_label = tk.Label(self.middle_structure_admin_login,text="",bg="royal blue",font="calibri 10 italic",).pack()

        self.admin_login_message_login_label = tk.Label(self.middle_structure_admin_login,text="",bg="royal blue",fg="white",font="calibri 10 italic")
        self.admin_login_message_login_label.pack()
        
        self.admin_login_label = tk.Label(self.middle_structure_admin_login,text="",bg="royal blue",font="calibri 10 italic",).pack()
        self.admin_login_label = tk.Label(self.middle_structure_admin_login,text="",bg="royal blue",font="calibri 10 italic",).pack()

        self.admin_login_label = tk.Label(self.middle_structure_admin_login,text="",bg="royal blue",font="calibri 10 italic",).pack()

        self.extra_btn_structure = tk.Frame(self.middle_structure_admin_login,bg="royal blue")
        self.extra_btn_structure.pack()

        self.admin_login_btn = tk.Button(self.extra_btn_structure,text="Sign Up?",command=self.display_signup_module_admin,bg="green",fg="white",font="arial 15 bold").pack(side=tk.RIGHT)
        
        self.admin_login_btn = tk.Button(self.extra_btn_structure,text="User!!",command=self.display_login_module_user,bg="blue",fg="white",font="arial 15 bold").pack(side=tk.LEFT)
        self.admin_login_label = tk.Label(self.extra_btn_structure,text="",bg="royal blue",font="calibri 10 italic",width=25).pack(side=tk.LEFT)

        self.admin_login_label = tk.Label(self.middle_structure_admin_login,text="",bg="royal blue",font="calibri 10 italic",).pack()

        #this is for admin signup module
        self.admin_name_signup = tk.StringVar()
        self.admin_conf_password_signup = tk.StringVar()
        self.admin_password_signup = tk.StringVar()
        
        self.heading2 = tk.Label(self.middle_structure_admin_signup,text="Admin Sign Up Here",fg="white",bg="navy blue",font="calibri 20 italic",padx="20").pack(fill=tk.X)
        self.dummy=tk.Label(self.middle_structure_admin_signup,text="",bg="navy blue").pack()

        self.right_adminname_structure = tk.Frame(self.middle_structure_admin_signup,bg="navy blue")
        self.right_adminname_structure.pack()
        
        self.admin_signup_label_adminname = tk.Label(self.right_adminname_structure,text="ADMIN NAME :",bg="navy blue",fg="white",font="arial 15 bold").pack(side=tk.LEFT)
        self.admin_signup_txtbox_adminname = tk.Entry(self.right_adminname_structure,textvariable=self.admin_name_signup,width=25,bg="teal",fg="white",font="cambria 15").pack(side=tk.LEFT)

        self.admin_signup_label = tk.Label(self.middle_structure_admin_signup,text="",bg="navy blue",font="calibri 10 italic",).pack()


        self.right_password_structure = tk.Frame(self.middle_structure_admin_signup,bg="navy blue")
        self.right_password_structure.pack()
        
        self.admin_signup_label_pass = tk.Label(self.right_password_structure,text=" PASSWORD : ",bg="navy blue",fg="white",font="arial 15 bold").pack(side=tk.LEFT)
        self.admin_signup_txtbox_pass = tk.Entry(self.right_password_structure,textvariable=self.admin_password_signup,width=25,bg="teal",show="*",fg="white",font="cambria 15").pack(side=tk.LEFT)

        self.admin_signup_label = tk.Label(self.middle_structure_admin_signup,text="",bg="navy blue",font="calibri 10 italic",).pack()

        self.right_userid_structure = tk.Frame(self.middle_structure_admin_signup,bg="navy blue")
        self.right_userid_structure.pack()
        
        self.admin_signup_label_userid = tk.Label(self.right_userid_structure,text="Confirm PASSWORD : ",bg="navy blue",fg="white",font="arial 15 bold").pack(side=tk.LEFT)
        self.admin_signup_txtbox_userid = tk.Entry(self.right_userid_structure,textvariable=self.admin_conf_password_signup,show="*",width=25,bg="teal",fg="white",font="cambria 15").pack(side=tk.LEFT)
        
        self.admin_signup_label = tk.Label(self.middle_structure_admin_signup,text="",bg="navy blue",font="calibri 10 italic",).pack()
        
        self.right_btn_structure = tk.Frame(self.middle_structure_admin_signup,bg="navy blue")
        self.right_btn_structure.pack()
        
        self.admin_signup_btn = tk.Button(self.right_btn_structure,text="Sign Up...",command=self.admin_signup,bg="blue",fg="white",font="arial 15 bold").pack(side=tk.LEFT)

        self.admin_signup_label = tk.Label(self.middle_structure_admin_signup,text="",bg="navy blue",fg="white",font="calibri 10 italic").pack()

        self.admin_signup_message_signup_label = tk.Label(self.middle_structure_admin_signup,text="",bg="navy blue",fg="white",font="calibri 10 italic")
        self.admin_signup_message_signup_label.pack()

        self.extra_btn_structure = tk.Frame(self.middle_structure_admin_signup,bg="navy blue")
        self.extra_btn_structure.pack()

        self.admin_login_btn = tk.Button(self.extra_btn_structure,text="Log In!",command=self.display_admin_login_module,bg="green",fg="white",font="arial 15 bold").pack(side=tk.RIGHT)
        
        self.admin_login_btn = tk.Button(self.extra_btn_structure,text="User!!",command=self.display_login_module_user,bg="blue",fg="white",font="arial 15 bold").pack(side=tk.LEFT)
        self.admin_login_label = tk.Label(self.extra_btn_structure,text="",bg="navy blue",font="calibri 10 italic",width=25).pack(side=tk.LEFT)

        self.admin_login_label = tk.Label(self.middle_structure_admin_signup,text="",bg="navy blue",font="calibri 10 italic",).pack()


    def display_login_module_user(self):
        self.middle_structure_user_login.pack(side=tk.LEFT)
        self.middle_structure_user_signup.pack_forget()
        self.middle_structure_admin_signup.pack_forget()
        self.middle_structure_admin_login.pack_forget()
        self.middle_structure_forgot_password.pack_forget()
        self.user_signup_message_signup_label.config(text="")
        self.user_login_message_login_label.config(text="")

    def display_forgot_password_module(self):
        self.middle_structure_user_login.pack_forget()
        self.middle_structure_forgot_password.pack(side=tk.LEFT)

        self.forgot_frame.pack_forget()
        self.search_user_forgot.pack()

        s = ""
        self.userid_forgot.set(s)
        self.secu_ans_forgot.set(s)
        self.password_forgot.set(s)
        self.conf_password_forgot.set(s)

    def display_signup_module_user(self):
        self.middle_structure_user_login.pack_forget()
        self.middle_structure_user_signup.pack(side=tk.LEFT)
        self.middle_structure_admin_signup.pack_forget()
        self.middle_structure_admin_login.pack_forget()
        self.user_signup_message_signup_label.config(text="")
        self.user_login_message_login_label.config(text="")
        self.user_signup_message_signup_label.config(text="")

    def display_admin_login_module(self):
        self.middle_structure_admin_login.pack(side=tk.LEFT)
        self.middle_structure_user_signup.pack_forget()
        self.middle_structure_user_login.pack_forget()
        self.middle_structure_admin_signup.pack_forget()

    def display_signup_module_admin(self):
        self.middle_structure_admin_signup.pack(side=tk.LEFT)
        self.middle_structure_admin_login.pack_forget()
        self.middle_structure_user_signup.pack_forget()
        self.middle_structure_user_login.pack_forget()

    def Search_user_forgot(self):
        userid = self.userid_forgot.get()
        
        conn = pymysql.connect(host="localhost",user="root",passwd="",db="admission_system_python")
        cursor = conn.cursor()

        if userid == "":
            messagebox.showinfo("Error!","Some Fields are Empty. Try again!!")
        else:
            cursor.execute("SELECT count(*) from user where user_id=%s",(userid))
            result = cursor.fetchone()

            if result[0] == 0:
                messagebox.showinfo("Error!","Wrong User Id!!")
            else:
                cursor.execute("SELECT security_question from user where user_id=%s",(userid))
                res = cursor.fetchone()

                self.forgot_frame.pack()
                self.search_user_forgot.pack_forget()
                self.security_question_label.config(text=res[0])


    def forgot_password(self):
        userid = self.userid_forgot.get()
        security_ans = self.secu_ans_forgot.get()
        password = self.password_forgot.get()
        conf_password = self.conf_password_forgot.get()

        conn = pymysql.connect(host="localhost",user="root",passwd="",db="admission_system_python")
        cursor = conn.cursor()
        
        if userid == "" or security_ans == "" or password == "" or conf_password == "":
            messagebox.showinfo("Error!","Some Fields are Empty. Try again!!")
        else:
            cursor.execute("SELECT count(*) from user where user_id=%s",(userid))
            result = cursor.fetchone()

            if result[0] == 0:
                messagebox.showinfo("Error!","Wrong User Id!!")
            else:
                cursor.execute("SELECT security_answer from user where user_id=%s",(userid))
                res = cursor.fetchone()

                if res[0] != security_ans:
                    messagebox.showinfo("Error!","Wrong Security Answer!!")
                else:
                    if password != conf_password:
                        messagebox.showinfo("Error!","Both Password should Matches!!")
                    else:
                        cursor.execute("UPDATE user set user_pass=%s where user_id=%s",(password,userid))
                        conn.commit()
                        cursor.close()
                        conn.close()

                        s = ""

                        self.userid_forgot.set(s)
                        self.secu_ans_forgot.set(s)
                        self.password_forgot.set(s)
                        self.conf_password_forgot.set(s)
                        
                        self.forgot_frame.pack_forget()
                        self.search_user_forgot.pack()

                        self.display_login_module_user()
                        messagebox.showinfo("Success!","PASSWORD RESETED!!")

        
    def admin_login(self):
        global adminid_after_login
        
        user_id = self.userid_admin_login.get()
        password = self.password_admin_login.get()

        conn = pymysql.connect(host="localhost",user="root",passwd="",db="admission_system_python")
        cursor = conn.cursor()

        if user_id == "" or password == "":
            messagebox.showinfo("Error!","Some Fields are Empty. Try again!!")
        else:
            cursor.execute("select count(*) from admin where admin_id=%s and admin_pass=%s",(user_id,password))
            result = cursor.fetchone()
            
            print(result)
            if result[0] == 1:
                adminid_after_login = user_id
                self.admin_login_message_login_label.config(text="Authenticated Admin...")
                s = ""
                self.password_admin_login.set(s)

                self.master.wm_state('iconic')#it will make old window as icon in taskbar and minimize it
                
                self.newflash = tk.Toplevel(self.structure)
                self.app = admin_home(self.newflash)
            else:
                s = ""
                self.password_admin_login.set(s)
                messagebox.showinfo("Error!","Authentication Failed!!")




    def user_login(self):
        global userid_after_login
        
        user_id = self.userid_login.get()
        password = self.password_login.get()

        if user_id == "" or password == "":
            messagebox.showinfo("Error!","Some Fields are Empty. Try again!!")
        else:
            conn = pymysql.connect(host="localhost",user="root",passwd="",db="admission_system_python")
            cursor = conn.cursor()

            cursor.execute("select count(*) from user where user_id=%s and user_pass=%s",(user_id,password))
            result = cursor.fetchone()
            
            print(result)
            if result[0] == 1:
                userid_after_login = user_id
                self.user_login_message_login_label.config(text="Authenticated user...")
                s = ""
                self.password_login.set(s)

                self.master.wm_state('iconic')#it will make old window as icon in taskbar and minimize it
                
                self.newflash = tk.Toplevel(self.structure)
                self.app = user_home(self.newflash)
            else:
                s = ""
                self.password_login.set(s)
                messagebox.showinfo("Error!","Authentication Failed!!")

        

    def admin_signup(self):
        admin_name = self.admin_name_signup.get()
        password = self.admin_password_signup.get()
        conf_password = self.admin_conf_password_signup.get()
        
        conn = pymysql.connect(host="localhost",user="root",passwd="",db="admission_system_python")
        cursor = conn.cursor()

        if admin_name == "" or password == "" or conf_password == "":
            messagebox.showinfo("Error!","Some Fields are Empty. Try again!!")
        else:
            if password != conf_password:
                messagebox.showinfo("Error!","PASSWORD and confirm PASSWORD are not matches. Try to match them!!")
            else:
                cursor.execute("SELECT count(*) from admin")
                result = cursor.fetchone()
                admin_id = "admin_2018" + str(result[0] + 1)
                
                cursor.execute("INSERT into admin(admin_id,admin_name,admin_pass) values(%s,%s,%s)",(admin_id,admin_name,password))
                conn.commit()
                cursor.close()
                conn.close()

                s=""
                self.admin_name_signup.set(s)
                self.admin_password_signup.set(s)
                self.admin_conf_password_signup.set(s)
                self.admin_signup_message_signup_label.config(text="SignUp Successfully for user id : "+admin_id)
                messagebox.showinfo("Please Note This!","Admin Id : " + admin_id)



        
    def user_signup(self):
        user_name = self.user_name_signup.get()
        security_ques = self.user_security_question_signup.get()
        security_ans = self.user_security_answer_signup.get()
        password = self.user_password_signup.get()
        conf_password = self.user_confirm_password_signup.get()

        conn = pymysql.connect(host="localhost",user="root",passwd="",db="admission_system_python")
        cursor = conn.cursor()

        if user_name == "" or security_ques == "" or security_ans == "" or password == "" or conf_password == "":
            messagebox.showinfo("Error!","Some Fields are Empty. Try again!!")
        else:
            if password != conf_password:
                messagebox.showinfo("Error!","PASSWORD and confirm PASSWORD are not matches. Try to match them!!")
            else:
                cursor.execute("SELECT COUNT(*) from user")
                result = cursor.fetchone()

                user_id = "reg_2018" + str(result[0]+1)
                #print(user_id)

                cursor.execute("INSERT into user(user_id,user_name,security_question,security_answer,user_pass) values(%s,%s,%s,%s,%s)",(user_id,user_name,security_ques,security_ans,password))

                conn.commit()
                cursor.close()
                conn.close()

                s=""
                self.user_name_signup.set(s)
                self.user_security_question_signup.set(s)
                self.user_security_answer_signup.set(s)
                self.user_password_signup.set(s)
                self.user_confirm_password_signup.set(s)
                
                self.user_signup_message_signup_label.config(text="SignUp Successfully for user id : "+user_id)
                messagebox.showinfo("Please Note This!","User Id : " + user_id)

        


class admin_home:
    def __init__(self,master):
        self.master = master
        #self.master.geometry("1200x720")
        #self.master.resizable(False,False)
        self.master.config(bg="blue")
        self.master.title("Welcome dear Admin")

        self.welcome_frame = tk.Frame(self.master,bg="royal blue")
        self.welcome_frame.pack()
        
        self.admin_details = tk.Label(self.welcome_frame,text="ADMINISTRATION SECTION",fg="white",bg="blue",font="elephant 25 bold",padx="450")
        self.admin_details.pack()

        self.welcome_frame_2 = tk.Frame(self.welcome_frame,bg="royal blue",width="100")
        self.welcome_frame_2.pack()

        self.admin_name_welcome = tk.Label(self.welcome_frame_2,text="",fg="white",bg="royal blue",font="elephant 20 bold",padx="70")
        self.admin_name_welcome.pack(side=tk.LEFT)

        self.btn1 = tk.Button(self.welcome_frame_2,text="LOGOUT..",bg="red",fg="white",padx="25",pady="20",command=self.admin_logout)
        self.btn1.pack(side=tk.RIGHT)
        
        self.admin_id_welcome = tk.Label(self.welcome_frame_2,text="",fg="white",bg="royal blue",font="elephant 20 bold",padx="70")
        self.admin_id_welcome.pack(side=tk.RIGHT)
        
        self.fetch_admin_details(adminid_after_login)
        
        self.admi_start = tk.Frame(self.master,bg="blue")
        self.admi_start.pack()
        
        #self.admin_details = tk.Label(self.admi_start,text="",fg="white",bg="blue",font="elephant 25 bold",padx="450").pack()

        self.admi_start_1 = tk.Frame(self.master,bg="blue")
        self.admi_start_1.pack()

        self.admin_details = tk.Label(self.admi_start_1,text="",fg="white",bg="blue",font="elephant 25 bold",padx="50").pack(side=tk.LEFT)
        
        self.btn23 = tk.Button(self.admi_start_1,text="PENDING FORMS",bg="teal",fg="white",command=self.display_pending_list,padx="25",pady="20",font="helvetica 15 bold")
        self.btn23.pack(side=tk.LEFT)

        self.admin_details = tk.Label(self.admi_start_1,text="",fg="white",bg="blue",font="elephant 25 bold",padx="250").pack(side=tk.LEFT)

        self.btn23 = tk.Button(self.admi_start_1,text="VERIFIED FORMS",bg="teal",fg="white",command=self.display_verified_list,padx="25",pady="20",font="helvetica 15 bold")
        self.btn23.pack(side=tk.LEFT)

        self.admin_details = tk.Label(self.admi_start_1,text="",fg="white",bg="blue",font="elephant 25 bold",padx="50").pack(side=tk.LEFT)

        self.admi_start_pending_1 = tk.Frame(self.master,bg="blue")
        #self.admi_start_pending.pack()

        self.admin_details = tk.Label(self.admi_start_pending_1,text="PENDING FORMS",fg="white",bg="blue",font="elephant 15 bold")
        self.admin_details.grid(row=0,column=1,columnspan=10)

        self.admi_start_pending = tk.Frame(self.admi_start_pending_1,bg="blue")
        self.admi_start_pending.grid(row=1)

        self.admi_start_verified_1 = tk.Frame(self.master,bg="blue")
        #self.admi_start_verified.pack()

        self.admin_details = tk.Label(self.admi_start_verified_1,text="Verified FORMS",fg="white",bg="blue",font="elephant 15 bold",padx="50")
        self.admin_details.grid(row=0,column=1,columnspan=10)

        self.admi_start_verified = tk.Frame(self.admi_start_verified_1,bg="blue")
        self.admi_start_verified.grid(row=1)

        self.form_display = tk.Frame(self.master,bg="blue")

        self.label0001 = tk.Label(self.form_display,text="",fg="red",bg="blue",font="elephant 15 bold",padx="50")
        self.label0001.pack()
        
        self.l_frame = tk.Frame(self.form_display,bg="blue")
        self.l_frame.pack()

        self.label001 = tk.Label(self.l_frame,text="Registration Id : ",fg="white",bg="blue",font="elephant 15 bold",padx="50")
        self.label001.pack(side=tk.LEFT)

        self.label002 = tk.Label(self.l_frame,text="User Name : ",fg="white",bg="blue",font="elephant 15 bold",padx="50")
        self.label002.pack(side=tk.LEFT)

        self.label003 = tk.Label(self.l_frame,text="Full Name : ",fg="white",bg="blue",font="elephant 15 bold",padx="50")
        self.label003.pack(side=tk.LEFT)

        self.l_frame1 = tk.Frame(self.form_display,bg="blue")
        self.l_frame1.pack()

        self.label004 = tk.Label(self.l_frame1,text="Date Of Birth : ",fg="white",bg="blue",font="elephant 15 bold",padx="50")
        self.label004.pack(side=tk.LEFT)

        self.label005 = tk.Label(self.l_frame1,text="Gender : ",fg="white",bg="blue",font="elephant 15 bold",padx="50")
        self.label005.pack(side=tk.LEFT)

        self.label006 = tk.Label(self.l_frame1,text="Occupation : ",fg="white",bg="blue",font="elephant 15 bold",padx="50")
        self.label006.pack(side=tk.LEFT)

        self.l_frame2 = tk.Frame(self.form_display,bg="blue")
        self.l_frame2.pack()

        self.label007 = tk.Label(self.l_frame2,text="Blood Group : ",fg="white",bg="blue",font="elephant 15 bold",padx="50")
        self.label007.pack(side=tk.LEFT)

        self.label008 = tk.Label(self.l_frame2,text="Marital Status : ",fg="white",bg="blue",font="elephant 15 bold",padx="50")
        self.label008.pack(side=tk.LEFT)

        self.label009 = tk.Label(self.l_frame2,text="Mobile Number : ",fg="white",bg="blue",font="elephant 15 bold",padx="50")
        self.label009.pack(side=tk.LEFT)

        self.l_frame3 = tk.Frame(self.form_display,bg="blue")
        self.l_frame3.pack()
        
        self.label010 = tk.Label(self.l_frame3,text="Mother's Name : ",fg="white",bg="blue",font="elephant 15 bold",padx="50")
        self.label010.pack(side=tk.LEFT)
        
        self.label011 = tk.Label(self.l_frame3,text="Father's Name : ",fg="white",bg="blue",font="elephant 15 bold",padx="50")
        self.label011.pack(side=tk.LEFT)

        self.label = tk.Label(self.form_display,text="Educational Qualification (Madhyamik)",fg="red",bg="blue",font="elephant 15 bold",padx="50").pack()

        self.l_frame4 = tk.Frame(self.form_display,bg="blue")
        self.l_frame4.pack()

        self.label012 = tk.Label(self.l_frame4,text="Total Marks : ",fg="white",bg="blue",font="elephant 15 bold",padx="10")
        self.label012.pack(side=tk.LEFT)

        self.label013 = tk.Label(self.l_frame4,text="Board : ",fg="white",bg="blue",font="elephant 15 bold",padx="10")
        self.label013.pack(side=tk.LEFT)

        self.label014 = tk.Label(self.l_frame4,text="Institute : ",fg="white",bg="blue",font="elephant 15 bold",padx="10")
        self.label014.pack(side=tk.LEFT)

        self.label015 = tk.Label(self.l_frame4,text="Year of Passing : ",fg="white",bg="blue",font="elephant 15 bold",padx="10")
        self.label015.pack(side=tk.LEFT)

        self.label016 = tk.Label(self.l_frame4,text="perecntage : ",fg="white",bg="blue",font="elephant 15 bold",padx="10")
        self.label016.pack(side=tk.LEFT)

        self.label = tk.Label(self.form_display,text="Educational Qualification (Higher Secondary)",fg="red",bg="blue",font="elephant 15 bold",padx="50").pack()

        self.l_frame5 = tk.Frame(self.form_display,bg="blue")
        self.l_frame5.pack()

        self.label017 = tk.Label(self.l_frame5,text="Total Marks : ",fg="white",bg="blue",font="elephant 15 bold",padx="10")
        self.label017.pack(side=tk.LEFT)

        self.label018 = tk.Label(self.l_frame5,text="Board : ",fg="white",bg="blue",font="elephant 15 bold",padx="10")
        self.label018.pack(side=tk.LEFT)

        self.label019 = tk.Label(self.l_frame5,text="Institute : ",fg="white",bg="blue",font="elephant 15 bold",padx="10")
        self.label019.pack(side=tk.LEFT)

        self.label020 = tk.Label(self.l_frame5,text="Year of Passing : ",fg="white",bg="blue",font="elephant 15 bold",padx="10")
        self.label020.pack(side=tk.LEFT)

        self.label021 = tk.Label(self.l_frame5,text="perecntage : ",fg="white",bg="blue",font="elephant 15 bold",padx="10")
        self.label021.pack(side=tk.LEFT)

        self.label = tk.Label(self.form_display,text="Educational Qualification (Graduation)",fg="red",bg="blue",font="elephant 15 bold",padx="50").pack()

        self.l_frame6 = tk.Frame(self.form_display,bg="blue")
        self.l_frame6.pack()

        self.label022 = tk.Label(self.l_frame6,text="Total Marks : ",fg="white",bg="blue",font="elephant 15 bold",padx="10")
        self.label022.pack(side=tk.LEFT)

        self.label023 = tk.Label(self.l_frame6,text="Board : ",fg="white",bg="blue",font="elephant 15 bold",padx="10")
        self.label023.pack(side=tk.LEFT)

        self.label024 = tk.Label(self.l_frame6,text="Institute : ",fg="white",bg="blue",font="elephant 15 bold",padx="10")
        self.label024.pack(side=tk.LEFT)

        self.label025 = tk.Label(self.l_frame6,text="Year of Passing : ",fg="white",bg="blue",font="elephant 15 bold",padx="10")
        self.label025.pack(side=tk.LEFT)

        self.label026 = tk.Label(self.l_frame6,text="perecntage : ",fg="white",bg="blue",font="elephant 15 bold",padx="10")
        self.label026.pack(side=tk.LEFT)

        self.label = tk.Label(self.form_display,text="Entrance Examination Details",fg="red",bg="blue",font="elephant 15 bold",padx="50").pack()

        self.l_frame10 = tk.Frame(self.form_display,bg="blue")
        self.l_frame10.pack()

        self.label027 = tk.Label(self.l_frame10,text="JECA Roll : ",fg="white",bg="blue",font="elephant 15 bold",padx="10")
        self.label027.pack(side=tk.LEFT)

        self.label028 = tk.Label(self.l_frame10,text="JECA Rank : ",fg="white",bg="blue",font="elephant 15 bold",padx="10")
        self.label028.pack(side=tk.LEFT)

        self.label029 = tk.Label(self.l_frame10,text="JECA Reg : ",fg="white",bg="blue",font="elephant 15 bold",padx="10")
        self.label029.pack(side=tk.LEFT)

        self.label = tk.Label(self.form_display,text="Demand Draft Details",fg="red",bg="blue",font="elephant 15 bold",padx="50").pack()

        self.l_frame7 = tk.Frame(self.form_display,bg="blue")
        self.l_frame7.pack()

        self.label030 = tk.Label(self.l_frame7,text="DD No : ",fg="white",bg="blue",font="elephant 15 bold",padx="10")
        self.label030.pack(side=tk.LEFT)

        self.label031 = tk.Label(self.l_frame7,text="Drawee Bank : ",fg="white",bg="blue",font="elephant 15 bold",padx="10")
        self.label031.pack(side=tk.LEFT)

        self.label032 = tk.Label(self.l_frame7,text="Drawee Branch : ",fg="white",bg="blue",font="elephant 15 bold",padx="10")
        self.label032.pack(side=tk.LEFT)

        self.label = tk.Label(self.form_display,text="CONTACT INFORMATION",fg="red",bg="blue",font="elephant 15 bold",padx="50").pack()

        self.l_frame8 = tk.Frame(self.form_display,bg="blue")
        self.l_frame8.pack()

        self.label033 = tk.Label(self.l_frame8,text="Address : ",fg="white",bg="blue",font="elephant 15 bold",padx="10")
        self.label033.pack(side=tk.LEFT)

        self.l_frame9 = tk.Frame(self.form_display,bg="blue")
        self.l_frame9.pack()
        
        self.label034 = tk.Label(self.l_frame9,text="City : ",fg="white",bg="blue",font="elephant 15 bold",padx="10")
        self.label034.pack(side=tk.LEFT)

        self.label035 = tk.Label(self.l_frame9,text="Distict : ",fg="white",bg="blue",font="elephant 15 bold",padx="10")
        self.label035.pack(side=tk.LEFT)

        self.label036 = tk.Label(self.l_frame9,text="State : ",fg="white",bg="blue",font="elephant 15 bold",padx="10")
        self.label036.pack(side=tk.LEFT)

        self.label037 = tk.Label(self.l_frame9,text="Pin code : ",fg="white",bg="blue",font="elephant 15 bold",padx="10")
        self.label037.pack(side=tk.LEFT)

        self.l_frame11 = tk.Frame(self.form_display,bg="blue")
        self.l_frame11.pack()
        
        self.admin_login_btn_0001 = tk.Button(self.l_frame11,text="BACK !",bg="green",fg="white",font="arial 15 bold")
        self.admin_login_btn_0001.pack(side=tk.LEFT)

        self.pending_pdf_dummy_label = tk.Label(self.l_frame11,text="",bg="blue",fg="white",font="arial 20 bold",width="50").pack(side=tk.LEFT)

        self.btn_pending_pdf_download_0001 = tk.Button(self.l_frame11,text="VERIFy?",bg="yellow",fg="black",font="arial 15 bold")
        self.btn_pending_pdf_download_0001.pack(side=tk.LEFT)

        

    def admin_logout(self):
        self.master.destroy()

    def display_pending_list(self):
        self.admi_start_1.pack_forget()
        self.admi_start_verified_1.pack_forget()
        if self.admi_start_verified.winfo_exists():
            self.admi_start_verified.destroy()
            self.admi_start_verified = tk.Frame(self.admi_start_verified_1,bg="blue")
            self.admi_start_verified.grid(row=1)

        if self.admi_start_pending.winfo_exists():
            self.admi_start_pending.destroy()
            self.admi_start_pending = tk.Frame(self.admi_start_pending_1,bg="blue")
            self.admi_start_pending.grid(row=1)
            #print("there")
        #print(a)
        self.admi_start_pending_1.pack()
        self.form_display.pack_forget()
        
        conn = pymysql.connect(host="localhost",user="root",passwd="",db="admission_system_python")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM user WHERE is_pending=1")
        res = cursor.fetchall()
        
        index = 1
        
        #self.admi_start_pending = tk.Frame(self.admi_start_pending_1,bg="blue")
        #self.admi_start_pending.pack()
        
        if len(res) > 0:
            self.admin_details = tk.Label(self.admi_start_pending,text="REG. ID",fg="white",bg="green",font="elephant 15 bold",width="10")
            self.admin_details.grid(row=index,column=1)

            self.admin_details = tk.Label(self.admi_start_pending,text="User Name",fg="white",bg="green",font="elephant 15 bold",width="10")
            self.admin_details.grid(row=index,column=2)

            self.admin_details = tk.Label(self.admi_start_pending,text="Full Name",fg="white",bg="green",font="elephant 15 bold",width="15")
            self.admin_details.grid(row=index,column=3)

            self.admin_details = tk.Label(self.admi_start_pending,text="Status?",fg="white",bg="green",font="elephant 15 bold",width="10")
            self.admin_details.grid(row=index,column=4)

            self.admin_details = tk.Label(self.admi_start_pending,text="Action!",fg="white",bg="green",font="elephant 15 bold",width="10")
            self.admin_details.grid(row=index,column=5)

            index = index + 1
            
            for details in res:
                reg_id = details[1]
                self.admin_details = tk.Label(self.admi_start_pending,text=details[1],fg="white",bg="blue",font="elephant 15 bold",width="10")
                self.admin_details.grid(row=index,column=1)

                self.admin_details = tk.Label(self.admi_start_pending,text=details[2],fg="white",bg="blue",font="elephant 15 bold",width="10")
                self.admin_details.grid(row=index,column=2)

                self.admin_details = tk.Label(self.admi_start_pending,text=details[6] + " " + details[7] + " " + details[8],fg="white",bg="blue",font="elephant 15 bold",width="15")
                self.admin_details.grid(row=index,column=3)
                
                self.admin_details = tk.Label(self.admi_start_pending,text="PENDING",fg="white",bg="blue",font="elephant 15 bold",width="10")
                self.admin_details.grid(row=index,column=4)

                self.admin_details = tk.Button(self.admi_start_pending,text="Verify",fg="black",bg="yellow",font="elephant 15 bold",command=lambda reg_id=reg_id:self.view_pending_form_individual(reg_id))
                self.admin_details.grid(row=index,column=5)

                index = index + 1

            self.btn23 = tk.Button(self.admi_start_pending,text="Click to view VERIFIED FORMS",bg="teal",fg="white",command=self.display_verified_list,padx="15",pady="10",font="helvetica 10 bold")
            self.btn23.grid(row=index,column=2,columnspan=3)

        else:
            self.admin_details = tk.Label(self.admi_start_pending,text="",fg="white",bg="blue",font="elephant 15 bold")
            self.admin_details.grid(row=index,column=1,columnspan=10)
            
            self.admin_details = tk.Label(self.admi_start_pending,text="NO FORMS FOUND.",fg="red",bg="blue",font="elephant 15 bold")
            self.admin_details.grid(row=index+1,column=1,columnspan=10)

            self.btn23 = tk.Button(self.admi_start_pending,text="Click to view VERIFIED FORMS",bg="teal",fg="white",command=self.display_verified_list,padx="15",pady="10",font="helvetica 10 bold")
            self.btn23.grid(row=index+2,column=2,columnspan=3)
            

    def display_verified_list(self):
        self.admi_start_1.pack_forget()
        self.admi_start_verified_1.pack()
        self.admi_start_pending_1.pack_forget()
        self.form_display.pack_forget()
        if self.admi_start_verified.winfo_exists():
            self.admi_start_verified.destroy()
            self.admi_start_verified = tk.Frame(self.admi_start_verified_1,bg="blue")
            self.admi_start_verified.grid(row=1)

        if self.admi_start_pending.winfo_exists():
            self.admi_start_pending.destroy()
            self.admi_start_pending = tk.Frame(self.admi_start_pending_1,bg="blue")
            self.admi_start_pending.grid(row=1)
        
        conn = pymysql.connect(host="localhost",user="root",passwd="",db="admission_system_python")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM user WHERE is_verified=1")
        res = cursor.fetchall()
        
        index = 1

        if len(res) > 0:
            self.admin_details = tk.Label(self.admi_start_verified,text="REG. ID",fg="white",bg="green",font="elephant 15 bold",width="10")
            self.admin_details.grid(row=index,column=1)

            self.admin_details = tk.Label(self.admi_start_verified,text="User Name",fg="white",bg="green",font="elephant 15 bold",width="10")
            self.admin_details.grid(row=index,column=2)

            self.admin_details = tk.Label(self.admi_start_verified,text="Full Name",fg="white",bg="green",font="elephant 15 bold",width="15")
            self.admin_details.grid(row=index,column=3)

            self.admin_details = tk.Label(self.admi_start_verified,text="Status?",fg="white",bg="green",font="elephant 15 bold",width="10")
            self.admin_details.grid(row=index,column=4)

            self.admin_details = tk.Label(self.admi_start_verified,text="Action!",fg="white",bg="green",font="elephant 15 bold",width="10")
            self.admin_details.grid(row=index,column=5)

            index = index + 1
            
            for details in res:
                reg_id = details[1]
                self.admin_details = tk.Label(self.admi_start_verified,text=details[1],fg="white",bg="blue",font="elephant 15 bold",width="10")
                self.admin_details.grid(row=index,column=1)

                self.admin_details = tk.Label(self.admi_start_verified,text=details[2],fg="white",bg="blue",font="elephant 15 bold",width="10")
                self.admin_details.grid(row=index,column=2)

                self.admin_details = tk.Label(self.admi_start_verified,text=details[6] + " " + details[7] + " " + details[8],fg="white",bg="blue",font="elephant 15 bold",width="15")
                self.admin_details.grid(row=index,column=3)
                
                self.admin_details = tk.Label(self.admi_start_verified,text="VERIFIED",fg="white",bg="blue",font="elephant 15 bold",width="10")
                self.admin_details.grid(row=index,column=4)

                self.admin_details = tk.Button(self.admi_start_verified,text="View",fg="black",bg="yellow",font="elephant 15 bold",command=lambda reg_id=reg_id:self.view_verified_form_individual(reg_id))
                self.admin_details.grid(row=index,column=5)

                index = index + 1

            self.btn23 = tk.Button(self.admi_start_verified,text="Click to view PENDING FORMS",bg="teal",fg="white",command=self.display_pending_list,padx="15",pady="10",font="helvetica 10 bold")
            self.btn23.grid(row=index,column=2,columnspan=3)

        else:
            self.admin_details = tk.Label(self.admi_start_verified,text="",fg="white",bg="blue",font="elephant 15 bold")
            self.admin_details.grid(row=index,column=1,columnspan=10)
            
            self.admin_details = tk.Label(self.admi_start_verified,text="NO FORMS FOUND.",fg="red",bg="blue",font="elephant 15 bold")
            self.admin_details.grid(row=index+1,column=1,columnspan=10)

            self.btn23 = tk.Button(self.admi_start_verified,text="Click to view PENDING FORMS",bg="teal",fg="white",command=self.display_pending_list,padx="15",pady="10",font="helvetica 10 bold")
            self.btn23.grid(row=index+2,column=2,columnspan=10)
            
            
    def view_verified_form_individual(self,reg_id):
        self.admi_start_verified_1.pack_forget()
        self.form_display.pack()
        
        conn = pymysql.connect(host="localhost",user="root",passwd="",db="admission_system_python")
        cursor = conn.cursor()

        cursor.execute("SELECT * from user where user_id=%s",(reg_id))
        res = cursor.fetchone()

        self.label0001.config(text="Personal Details")

        self.label001.config(text="Registration Id : " + res[1])

        self.label002.config(text="User Name : " + res[2])

        self.label003.config(text="Full Name : " + res[6] + " " + res[7] + " " + res[8])

        self.label004.config(text="Date Of Birth : " + res[9])

        self.label005.config(text="Gender : " + res[13])

        self.label006.config(text="Occupation : " + res[12])

        self.label007.config(text="Blood Group : " + res[14])

        self.label008.config(text="Marital Status : " + res[15])

        self.label009.config(text="Mobile Number : " + res[39])
        
        self.label010.config(text="Mother's Name : " + res[10])
        
        self.label011.config(text="Father's Name : " + res[11])

        self.label012.config(text="Total Marks : " + res[16])

        self.label013.config(text="Board : " + res[17])

        self.label014.config(text="Institute : " + res[18])

        self.label015.config(text="Year of Passing : " + res[19])

        self.label016.config(text="perecntage : " + res[20] + " %")

        self.label017.config(text="Total Marks : " + res[21])

        self.label018.config(text="Board : " + res[22])

        self.label019.config(text="Institute : " + res[23])

        self.label020.config(text="Year of Passing : " + res[24])

        self.label021.config(text="perecntage : " + res[25] + " %")

        self.label022.config(text="Total Marks : " + res[26])

        self.label023.config(text="Board : " + res[27])

        self.label024.config(text="Institute : " + res[28])

        self.label025.config(text="Year of Passing : " + res[29])

        self.label026.config(text="perecntage : " + res[30] + " %")

        self.label027.config(text="JECA Roll : " + res[31])

        self.label028.config(text="JECA Rank : " + res[32])

        self.label029.config(text="JECA Reg : " + res[33])

        self.label030.config(text="DD No : " + res[34])

        self.label031.config(text="Drawee Bank : " + res[35])

        self.label032.config(text="Drawee Branch : " + res[36])

        self.label033.config(text="Address : " + res[37])
        
        self.label034.config(text="City : " + res[38])

        self.label035.config(text="Distict : " + res[39])

        self.label036.config(text="State : " + res[40])

        self.label037.config(text="Pin code : " + res[41])
        
        self.admin_login_btn_0001.config(command=self.verify_back)

        self.btn_pending_pdf_download_0001.pack_forget()

        #self.btn_pending_pdf_download = tk.Button(self.l_frame11,text="VERIFy?",bg="yellow",fg="black",font="arial 15 bold",command=self.verify_form(res[1])).pack(side=tk.LEFT)


        
    def view_pending_form_individual(self,reg_id):
        print(reg_id)
        self.admi_start_pending_1.pack_forget()
        self.form_display.pack()
        
        conn = pymysql.connect(host="localhost",user="root",passwd="",db="admission_system_python")
        cursor = conn.cursor()

        cursor.execute("SELECT * from user where user_id=%s",(reg_id))
        res = cursor.fetchone()

        self.label0001.config(text="Personal Details")

        self.label001.config(text="Registration Id : " + res[1])

        self.label002.config(text="User Name : " + res[2])

        self.label003.config(text="Full Name : " + res[6] + " " + res[7] + " " + res[8])

        self.label004.config(text="Date Of Birth : " + res[9])

        self.label005.config(text="Gender : " + res[13])

        self.label006.config(text="Occupation : " + res[12])

        self.label007.config(text="Blood Group : " + res[14])

        self.label008.config(text="Marital Status : " + res[15])

        self.label009.config(text="Mobile Number : " + res[39])
        
        self.label010.config(text="Mother's Name : " + res[10])
        
        self.label011.config(text="Father's Name : " + res[11])

        self.label012.config(text="Total Marks : " + res[16])

        self.label013.config(text="Board : " + res[17])

        self.label014.config(text="Institute : " + res[18])

        self.label015.config(text="Year of Passing : " + res[19])

        self.label016.config(text="perecntage : " + res[20] + " %")

        self.label017.config(text="Total Marks : " + res[21])

        self.label018.config(text="Board : " + res[22])

        self.label019.config(text="Institute : " + res[23])

        self.label020.config(text="Year of Passing : " + res[24])

        self.label021.config(text="perecntage : " + res[25] + " %")

        self.label022.config(text="Total Marks : " + res[26])

        self.label023.config(text="Board : " + res[27])

        self.label024.config(text="Institute : " + res[28])

        self.label025.config(text="Year of Passing : " + res[29])

        self.label026.config(text="perecntage : " + res[30] + " %")

        self.label027.config(text="JECA Roll : " + res[31])

        self.label028.config(text="JECA Rank : " + res[32])

        self.label029.config(text="JECA Reg : " + res[33])

        self.label030.config(text="DD No : " + res[34])

        self.label031.config(text="Drawee Bank : " + res[35])

        self.label032.config(text="Drawee Branch : " + res[36])

        self.label033.config(text="Address : " + res[37])
        
        self.label034.config(text="City : " + res[38])

        self.label035.config(text="Distict : " + res[39])

        self.label036.config(text="State : " + res[40])

        self.label037.config(text="Pin code : " + res[41])
        
        self.admin_login_btn_0001.config(command=self.pending_back)

        self.btn_pending_pdf_download_0001.pack()

        self.btn_pending_pdf_download_0001.config(command=lambda:self.verify_form(res[1]))

        
    def pending_back(self):
        self.display_pending_list()

    def verify_back(self):
        self.display_verified_list()

    def verify_form(self,reg):
        conn = pymysql.connect(host="localhost",user="root",passwd="",db="admission_system_python")
        cursor = conn.cursor()

        cursor.execute("UPDATE user set is_pending=0,is_verified=1 where user_id=%s",(reg))

        conn.commit()
        cursor.close()
        conn.close()
        
        messagebox.showinfo("CONGRATS!",reg + " is Successfully Verified.")
        self.display_verified_list()
        
    
    def fetch_admin_details(self,adminid):
        conn = pymysql.connect(host="localhost",user="root",passwd="",db="admission_system_python")
        cursor = conn.cursor()

        cursor.execute("SELECT * from admin where admin_id=%s",(adminid))
        res = cursor.fetchone()

        self.admin_id_welcome.config(text="Admin ID : " + res[1])
        self.admin_name_welcome.config(text="Admin Name : " + res[2])


class user_home:
    def __init__(self,master):
        self.master = master
        #self.master.geometry("1000x1200")
        #self.master.resizable(False,False)
        self.master.config(bg="royal blue")
        #print(userid_after_login)
        
        
        self.master.title("Welcome dear student")

        self.welcome_frame = tk.Frame(self.master,bg="royal blue")
        self.welcome_frame.pack()
        
        self.user_details = tk.Label(self.welcome_frame,text="ASANSOL ENGINEERING COLLEGE",fg="white",bg="teal",font="elephant 25 bold",width="100")
        self.user_details.pack()

        self.welcome_frame_2 = tk.Frame(self.welcome_frame,bg="royal blue",width="100")
        self.welcome_frame_2.pack()

        self.user_name_welcome = tk.Label(self.welcome_frame_2,text="",fg="white",bg="royal blue",font="elephant 25 bold",padx="100")
        self.user_name_welcome.pack(side=tk.LEFT)

        self.btn1 = tk.Button(self.welcome_frame_2,text="LOGOUT..",bg="red",fg="white",padx="25",pady="20",command=self.user_logout)
        self.btn1.pack(side=tk.RIGHT)
        
        self.user_id_welcome = tk.Label(self.welcome_frame_2,text="",fg="white",bg="royal blue",font="elephant 25 bold",padx="100")
        self.user_id_welcome.pack(side=tk.RIGHT)

        self.pending_verified = tk.Label(self.welcome_frame,text="",fg="red",bg="royal blue",font="cambria 10 bold",padx="100")
        self.pending_verified.pack()

        self.conf_pdf_label_dummy_1 = tk.Label(self.welcome_frame,text="",fg="red",bg="royal blue",font="cambria 10 bold",padx="100")

        self.conf_pdf_label_dummy_2 = tk.Label(self.welcome_frame,text="",fg="red",bg="royal blue",font="cambria 10 bold",padx="100")
        
        self.btn_conf_pdf_download = tk.Button(self.welcome_frame,text="Confirmation Download",bg="green",fg="white",padx="25",pady="20",command=self.confirmation_download)

        self.stu = tk.Frame(self.master,bg="royal blue")
        self.stu.pack()

        self.left1 = tk.Frame(self.stu,bg="royal blue")
        self.left1.pack()

        #variable type
        self.f_name = tk.StringVar()
        self.m_name = tk.StringVar()
        self.l_name = tk.StringVar()
        self.dob = tk.StringVar()
        self.ma_name = tk.StringVar()
        self.fa_name = tk.StringVar()
        self.occ = tk.StringVar()
        self.gen = tk.StringVar()
        self.b_g = tk.StringVar()
        self.m_s = tk.StringVar()

        self.tenth = tk.StringVar()
        self.board_10 = tk.StringVar()
        self.ins_10 = tk.StringVar()
        self.yop_10 = tk.StringVar()
        self.perc_10 = tk.StringVar()

        self.twelfth= tk.StringVar()
        self.board_12 = tk.StringVar()
        self.ins_12 = tk.StringVar()
        self.yop_12 = tk.StringVar()
        self.perc_12 = tk.StringVar()

        self.grad= tk.StringVar()
        self.board_grad = tk.StringVar()
        self.ins_grad = tk.StringVar()
        self.yop_grad = tk.StringVar()
        self.perc_grad = tk.StringVar()

        self.jeca_roll = tk.StringVar()
        self.jeca_rank = tk.StringVar()
        self.jeca_reg = tk.StringVar()

        self.ddno = tk.StringVar()
        self.bank_name = tk.StringVar()
        self.branch = tk.StringVar()

        self.addr = tk.StringVar()
        self.city = tk.StringVar()
        self.district = tk.StringVar()
        self.state = tk.StringVar()
        self.pincode = tk.StringVar()
        self.mob = tk.StringVar()
        

        self.left1_0 = tk.Frame(self.left1,bg="blue")
        self.left1_0.pack()

        self.user_details = tk.Label(self.left1_0,text="Personal Information",fg="white",bg="royal blue",font="elephant 15 bold",padx=100)
        self.user_details.pack()

        self.left_0 = tk.Frame(self.left1,bg="green")
        self.left_0.pack()

        self.left1_1 = tk.Frame(self.left_0,bg="green")
        self.left1_1.pack(side=tk.LEFT)

        self.user_details = tk.Label(self.left1_1,text="First Name",fg="white",bg="royal blue",font="elephant 10 bold",width=10)
        self.user_details.pack(side=tk.LEFT)

        self.user_details = tk.Entry(self.left1_1,textvariable=self.f_name,fg="white",bg="blue")
        self.user_details.pack(side=tk.LEFT)


        self.left1_2 = tk.Frame(self.left_0,bg="green")
        self.left1_2.pack(side=tk.LEFT)

        self.user_details = tk.Label(self.left1_2,text="Middle Name",fg="white",bg="royal blue",font="elephant 10 bold",width=10)
        self.user_details.pack(side=tk.LEFT)


        self.user_details = tk.Entry(self.left1_2,textvariable=self.m_name,fg="white",bg="blue")
        self.user_details.pack(side=tk.LEFT)

        self.left1_3 = tk.Frame(self.left_0,bg="green")
        self.left1_3.pack(side=tk.LEFT)

        self.user_details = tk.Label(self.left1_3,text="Last Name",fg="white",bg="royal blue",font="elephant 10 bold",width=10)
        self.user_details.pack(side=tk.LEFT)


        self.user_details = tk.Entry(self.left1_3,textvariable=self.l_name,fg="white",bg="blue")
        self.user_details.pack(side=tk.LEFT)

        self.left1_4 = tk.Frame(self.left_0,bg="green")
        self.left1_4.pack(side=tk.LEFT)

        self.user_details = tk.Label(self.left1_4,text="Date of Birth",fg="white",bg="royal blue",font="elephant 10 bold",width=10)
        self.user_details.pack(side=tk.LEFT)


        self.user_details = tk.Entry(self.left1_4,textvariable=self.dob,fg="white",bg="blue")
        self.user_details.pack(side=tk.LEFT)


        self.left1_5 = tk.Frame(self.left_0,bg="green")
        self.left1_5.pack(side=tk.LEFT)

        self.user_details = tk.Label(self.left1_5,text="Mother's Name",fg="white",bg="royal blue",font="elephant 10 bold",width=10)
        self.user_details.pack(side=tk.LEFT)


        self.user_details = tk.Entry(self.left1_5,textvariable=self.ma_name,fg="white",bg="blue")
        self.user_details.pack(side=tk.LEFT)

        
        self.left_1 = tk.Frame(self.left1,bg="green")
        self.left_1.pack()
        self.left2_1 = tk.Frame(self.left_1,bg="green")
        self.left2_1.pack(side=tk.LEFT)

        self.user_details = tk.Label(self.left2_1,text="Father's Name",fg="white",bg="royal blue",font="elephant 10 bold",width=10)
        self.user_details.pack(side=tk.LEFT)

        self.user_details = tk.Entry(self.left2_1,textvariable=self.fa_name,fg="white",bg="blue")
        self.user_details.pack(side=tk.LEFT)


        self.left3_1 = tk.Frame(self.left_1,bg="green")
        self.left3_1.pack(side=tk.LEFT)

        self.user_details = tk.Label(self.left3_1,text="Occupation",fg="white",bg="royal blue",font="elephant 10 bold",width=10)
        self.user_details.pack(side=tk.LEFT)

        self.user_details = tk.Entry(self.left3_1,textvariable=self.occ,fg="white",bg="blue")
        self.user_details.pack(side=tk.LEFT)
        
        self.left4_1 = tk.Frame(self.left_1,bg="green")
        self.left4_1.pack(side=tk.LEFT)

        self.user_details = tk.Label(self.left4_1,text="Gender",fg="white",bg="royal blue",font="elephant 10 bold",width=10)
        self.user_details.pack(side=tk.LEFT)

        self.user_details = tk.Entry(self.left4_1,textvariable=self.gen,fg="white",bg="blue")
        self.user_details.pack(side=tk.LEFT)
        
        self.left5_1 = tk.Frame(self.left_1,bg="green")
        self.left5_1.pack(side=tk.LEFT)

        self.user_details = tk.Label(self.left5_1,text="Blood Group",fg="white",bg="royal blue",font="elephant 10 bold",width=10)
        self.user_details.pack(side=tk.LEFT)

        self.user_details = tk.Entry(self.left5_1,textvariable=self.b_g,fg="white",bg="blue")
        self.user_details.pack(side=tk.LEFT)

        self.left6_1 = tk.Frame(self.left_1,bg="green")
        self.left6_1.pack(side=tk.LEFT)

        self.user_details = tk.Label(self.left6_1,text="Marital Status",fg="white",bg="royal blue",font="elephant 10 bold",width=10)
        self.user_details.pack(side=tk.LEFT)

        self.user_details = tk.Entry(self.left6_1,textvariable=self.m_s,fg="white",bg="blue")
        self.user_details.pack(side=tk.LEFT)


        self.left2 = tk.Frame(self.stu,bg="royal blue")
        self.left2.pack()


        self.left2_0 = tk.Frame(self.left2,bg="cyan")
        self.left2_0.pack()

        self.user_details = tk.Label(self.left2_0,text="Educational Qualification",fg="white",bg="royal blue",font="elephant 15 bold",padx=100)
        self.user_details.pack()

        self.left_0 = tk.Frame(self.left2,bg="green")
        self.left_0.pack()

        self.user_details = tk.Label(self.left_0,text="Madhyamik / 10th",fg="white",bg="green",font="elephant 10 bold").pack()


        self.left1_1 = tk.Frame(self.left_0,bg="green")
        self.left1_1.pack(side=tk.LEFT)

        self.user_details = tk.Label(self.left1_1,text="Total Marks",fg="white",bg="royal blue",font="elephant 10 bold",width=10)
        self.user_details.pack(side=tk.LEFT)

        self.user_details = tk.Entry(self.left1_1,textvariable=self.tenth,fg="white",bg="blue")
        self.user_details.pack(side=tk.LEFT)


        self.left1_2 = tk.Frame(self.left_0,bg="green")
        self.left1_2.pack(side=tk.LEFT)

        self.user_details = tk.Label(self.left1_2,text="Board",fg="white",bg="royal blue",font="elephant 10 bold",width=10)
        self.user_details.pack(side=tk.LEFT)


        self.user_details = tk.Entry(self.left1_2,textvariable=self.board_10,fg="white",bg="blue")
        self.user_details.pack(side=tk.LEFT)

        self.left1_3 = tk.Frame(self.left_0,bg="green")
        self.left1_3.pack(side=tk.LEFT)

        self.user_details = tk.Label(self.left1_3,text="Institute Name",fg="white",bg="royal blue",font="elephant 10 bold",width=10)
        self.user_details.pack(side=tk.LEFT)


        self.user_details = tk.Entry(self.left1_3,textvariable=self.ins_10,fg="white",bg="blue")
        self.user_details.pack(side=tk.LEFT)

        self.left1_4 = tk.Frame(self.left_0,bg="green")
        self.left1_4.pack(side=tk.LEFT)

        self.user_details = tk.Label(self.left1_4,text="Year of passing",fg="white",bg="royal blue",font="elephant 10 bold",width=10)
        self.user_details.pack(side=tk.LEFT)


        self.user_details = tk.Entry(self.left1_4,textvariable=self.yop_10,fg="white",bg="blue")
        self.user_details.pack(side=tk.LEFT)


        self.left1_5 = tk.Frame(self.left_0,bg="green")
        self.left1_5.pack(side=tk.LEFT)

        self.user_details = tk.Label(self.left1_5,text="Percentage",fg="white",bg="royal blue",font="elephant 10 bold",width=10)
        self.user_details.pack(side=tk.LEFT)


        self.user_details = tk.Entry(self.left1_5,textvariable=self.perc_10,fg="white",bg="blue")
        self.user_details.pack(side=tk.LEFT)

        self.left_2 = tk.Frame(self.left2,bg="green")
        self.left_2.pack()

        self.user_details = tk.Label(self.left_2,text="Higher Secondary / 12th",fg="white",bg="green",font="elephant 10 bold").pack()

        self.leftf_1 = tk.Frame(self.left_2,bg="green")
        self.leftf_1.pack(side=tk.LEFT)

        self.user_details = tk.Label(self.leftf_1,text="Total Marks",fg="white",bg="royal blue",font="elephant 10 bold",width=10)
        self.user_details.pack(side=tk.LEFT)

        self.user_details = tk.Entry(self.leftf_1,textvariable=self.twelfth,fg="white",bg="blue")
        self.user_details.pack(side=tk.LEFT)


        self.leftf_2 = tk.Frame(self.left_2,bg="green")
        self.leftf_2.pack(side=tk.LEFT)

        self.user_details = tk.Label(self.leftf_2,text="Board",fg="white",bg="royal blue",font="elephant 10 bold",width=10)
        self.user_details.pack(side=tk.LEFT)


        self.user_details = tk.Entry(self.leftf_2,textvariable=self.board_12,fg="white",bg="blue")
        self.user_details.pack(side=tk.LEFT)

        self.leftf_3 = tk.Frame(self.left_2,bg="green")
        self.leftf_3.pack(side=tk.LEFT)

        self.user_details = tk.Label(self.leftf_3,text="Institute Name",fg="white",bg="royal blue",font="elephant 10 bold",width=10)
        self.user_details.pack(side=tk.LEFT)


        self.user_details = tk.Entry(self.leftf_3,textvariable=self.ins_12,fg="white",bg="blue")
        self.user_details.pack(side=tk.LEFT)

        self.leftf_4 = tk.Frame(self.left_2,bg="green")
        self.leftf_4.pack(side=tk.LEFT)

        self.user_details = tk.Label(self.leftf_4,text="Year of passing",fg="white",bg="royal blue",font="elephant 10 bold",width=10)
        self.user_details.pack(side=tk.LEFT)


        self.user_details = tk.Entry(self.leftf_4,textvariable=self.yop_12,fg="white",bg="blue")
        self.user_details.pack(side=tk.LEFT)


        self.leftf_5 = tk.Frame(self.left_2,bg="green")
        self.leftf_5.pack(side=tk.LEFT)

        self.user_details = tk.Label(self.leftf_5,text="Percentage",fg="white",bg="royal blue",font="elephant 10 bold",width=10)
        self.user_details.pack(side=tk.LEFT)


        self.user_details = tk.Entry(self.leftf_5,textvariable=self.perc_12,fg="white",bg="blue")
        self.user_details.pack(side=tk.LEFT)

        self.left_3 = tk.Frame(self.left2,bg="green")
        self.left_3.pack(side=tk.LEFT)

        self.user_details = tk.Label(self.left_3,text="Graduation / BCA",fg="white",bg="green",font="elephant 10 bold").pack()

        self.leftf_1 = tk.Frame(self.left_3,bg="green")
        self.leftf_1.pack(side=tk.LEFT)
        
        self.user_details = tk.Label(self.leftf_1,text="Total Marks",fg="white",bg="royal blue",font="elephant 10 bold",width=10)
        self.user_details.pack(side=tk.LEFT)

        self.user_details = tk.Entry(self.leftf_1,textvariable=self.grad,fg="white",bg="blue")
        self.user_details.pack(side=tk.LEFT)


        self.leftf_2 = tk.Frame(self.left_3,bg="green")
        self.leftf_2.pack(side=tk.LEFT)

        self.user_details = tk.Label(self.leftf_2,text="University",fg="white",bg="royal blue",font="elephant 10 bold",width=10)
        self.user_details.pack(side=tk.LEFT)


        self.user_details = tk.Entry(self.leftf_2,textvariable=self.board_grad,fg="white",bg="blue")
        
        self.user_details.pack(side=tk.LEFT)

        self.leftf_3 = tk.Frame(self.left_3,bg="green")
        self.leftf_3.pack(side=tk.LEFT)

        self.user_details = tk.Label(self.leftf_3,text="Institute Name",fg="white",bg="royal blue",font="elephant 10 bold",width=10)
        self.user_details.pack(side=tk.LEFT)


        self.user_details = tk.Entry(self.leftf_3,textvariable=self.ins_grad,fg="white",bg="blue")
        self.user_details.pack(side=tk.LEFT)

        self.leftf_4 = tk.Frame(self.left_3,bg="green")
        self.leftf_4.pack(side=tk.LEFT)

        self.user_details = tk.Label(self.leftf_4,text="Year of passing",fg="white",bg="royal blue",font="elephant 10 bold",width=10)
        self.user_details.pack(side=tk.LEFT)


        self.user_details = tk.Entry(self.leftf_4,textvariable=self.yop_grad,fg="white",bg="blue")
        self.user_details.pack(side=tk.LEFT)


        self.leftf_5 = tk.Frame(self.left_3,bg="green")
        self.leftf_5.pack(side=tk.LEFT)

        self.user_details = tk.Label(self.leftf_5,text="Percentage",fg="white",bg="royal blue",font="elephant 10 bold",width=10)
        self.user_details.pack(side=tk.LEFT)

        self.user_details = tk.Entry(self.leftf_5,textvariable=self.perc_grad,fg="white",bg="blue")
        self.user_details.pack(side=tk.LEFT)

        self.left3 = tk.Frame(self.stu,bg="royal blue")
        self.left3.pack()

        self.left2_0 = tk.Frame(self.left3,bg="blue")
        self.left2_0.pack()

        self.user_details = tk.Label(self.left2_0,text="Admission Details",fg="white",bg="royal blue",font="elephant 15 bold",padx=100)
        self.user_details.pack()

        self.left_0 = tk.Frame(self.left3,bg="green")
        self.left_0.pack()

        self.left1_1 = tk.Frame(self.left_0,bg="green")
        self.left1_1.pack(side=tk.LEFT)

        self.user_details = tk.Label(self.left1_1,text="JECA-ROLLNO",fg="white",bg="royal blue",font="elephant 10 bold",width=20)
        self.user_details.pack(side=tk.LEFT)

        self.user_details = tk.Entry(self.left1_1,textvariable=self.jeca_roll,fg="white",bg="blue")
        self.user_details.pack(side=tk.LEFT)


        self.left1_2 = tk.Frame(self.left_0,bg="green")
        self.left1_2.pack(side=tk.LEFT)

        self.user_details = tk.Label(self.left1_2,text="JECA-Rank",fg="white",bg="royal blue",font="elephant 10 bold",width=20)
        self.user_details.pack(side=tk.LEFT)

        self.user_details = tk.Entry(self.left1_2,textvariable=self.jeca_rank,fg="white",bg="blue")
        self.user_details.pack(side=tk.LEFT)
        
        self.left2_2 = tk.Frame(self.left_0,bg="green")
        self.left2_2.pack(side=tk.LEFT)

        self.user_details = tk.Label(self.left2_2,text="JECA-Reg No",fg="white",bg="royal blue",font="elephant 10 bold",width=10)
        self.user_details.pack(side=tk.LEFT)


        self.user_details = tk.Entry(self.left2_2,textvariable=self.jeca_reg,fg="white",bg="blue")
        self.user_details.pack(side=tk.LEFT)

        self.left4 = tk.Frame(self.stu,bg="royal blue")
        self.left4.pack()

        self.left2_0 = tk.Frame(self.left4,bg="blue")
        self.left2_0.pack()

        self.user_details = tk.Label(self.left2_0,text="Demand Draft Details",fg="white",bg="royal blue",font="elephant 15 bold",padx=100)
        self.user_details.pack()

        self.left_0 = tk.Frame(self.left4,bg="green")
        self.left_0.pack()

        self.left1_1 = tk.Frame(self.left_0,bg="green")
        self.left1_1.pack(side=tk.LEFT)

        self.user_details = tk.Label(self.left1_1,text="DD-No:",fg="white",bg="royal blue",font="elephant 10 bold",width=20)
        self.user_details.pack(side=tk.LEFT)

        self.user_details = tk.Entry(self.left1_1,textvariable=self.ddno,fg="white",bg="blue")
        self.user_details.pack(side=tk.LEFT)

        self.left1_1 = tk.Frame(self.left_0,bg="green")
        self.left1_1.pack(side=tk.LEFT)

        self.user_details = tk.Label(self.left1_1,text="Name of the Bank",fg="white",bg="royal blue",font="elephant 10 bold",width=20)
        self.user_details.pack(side=tk.LEFT)

        self.user_details = tk.Entry(self.left1_1,textvariable=self.bank_name,fg="white",bg="blue")
        self.user_details.pack(side=tk.LEFT)

        self.left1_1 = tk.Frame(self.left_0,bg="green")
        self.left1_1.pack(side=tk.LEFT)

        self.user_details = tk.Label(self.left1_1,text="Branch",fg="white",bg="royal blue",font="elephant 10 bold",width=20)
        self.user_details.pack(side=tk.LEFT)

        self.user_details = tk.Entry(self.left1_1,textvariable=self.branch,fg="white",bg="blue")
        self.user_details.pack(side=tk.LEFT)

        self.left5 = tk.Frame(self.stu,bg="royal blue")
        self.left5.pack()
        
        self.left2_0 = tk.Frame(self.left5,bg="blue")
        self.left2_0.pack()

        self.user_details = tk.Label(self.left2_0,text="contact Address",fg="white",bg="royal blue",font="elephant 15 bold",padx=100)
        self.user_details.pack()

        self.left_0 = tk.Frame(self.left5,bg="green")
        self.left_0.pack()

        self.left1_1 = tk.Frame(self.left_0,bg="green")
        self.left1_1.pack(side=tk.LEFT)

        self.user_details = tk.Label(self.left1_1,text="Address:",fg="white",bg="royal blue",font="elephant 10 bold",width=20)
        self.user_details.pack(side=tk.LEFT)

        self.user_details = tk.Entry(self.left1_1,textvariable=self.addr,fg="white",bg="blue",width=80)
        self.user_details.pack(side=tk.LEFT)

        self.left_2 = tk.Frame(self.left5,bg="green")
        self.left_2.pack()

        self.leftf_1 = tk.Frame(self.left_2,bg="green")
        self.leftf_1.pack(side=tk.LEFT)
        
        self.user_details = tk.Label(self.leftf_1,text="City",fg="white",bg="royal blue",font="elephant 10 bold",width=10)
        self.user_details.pack(side=tk.LEFT)

        self.user_details = tk.Entry(self.leftf_1,textvariable=self.city,fg="white",bg="blue")
        self.user_details.pack(side=tk.LEFT)
        
        self.left1_2 = tk.Frame(self.left_2,bg="green")
        self.left1_2.pack(side=tk.LEFT)

        self.user_details = tk.Label(self.left1_2,text="Distrit",fg="white",bg="royal blue",font="elephant 10 bold",width=10)
        self.user_details.pack(side=tk.LEFT)


        self.user_details = tk.Entry(self.left1_2,textvariable=self.district,fg="white",bg="blue")
        self.user_details.pack(side=tk.LEFT)

        self.left2_2 = tk.Frame(self.left_2,bg="green")
        self.left2_2.pack(side=tk.LEFT)

        self.user_details = tk.Label(self.left2_2,text="State",fg="white",bg="royal blue",font="elephant 10 bold",width=10)
        self.user_details.pack(side=tk.LEFT)


        self.user_details = tk.Entry(self.left2_2,textvariable=self.state,fg="white",bg="blue")
        self.user_details.pack(side=tk.LEFT)

        self.left3_2 = tk.Frame(self.left_2,bg="green")
        self.left3_2.pack(side=tk.LEFT)

        self.user_details = tk.Label(self.left3_2,text="PIN Code",fg="white",bg="royal blue",font="elephant 10 bold",width=10)
        self.user_details.pack(side=tk.LEFT)


        self.user_details = tk.Entry(self.left3_2,textvariable=self.pincode,fg="white",bg="blue")
        self.user_details.pack(side=tk.LEFT)
        
        self.left3_4 = tk.Frame(self.left_2,bg="green")
        self.left3_4.pack(side=tk.LEFT)
        
        self.user_details = tk.Label(self.left3_4,text="Mob. no",fg="white",bg="royal blue",font="elephant 10 bold",width=10)
        self.user_details.pack(side=tk.LEFT)
        self.user_details = tk.Entry(self.left3_4,textvariable=self.mob,fg="white",bg="blue")
        self.user_details.pack(side=tk.LEFT)
               
        self.left_btn_structure = tk.Frame(self.stu,bg="royal blue")
        self.left_btn_structure.pack()

        self.label = tk.Label(self.left_btn_structure,text="",bg="royal blue",fg="white",font="arial 20 bold",width="50").pack()

        self.left_btn_structure_1 = tk.Frame(self.left_btn_structure,bg="royal blue")
        self.left_btn_structure_1.pack()
        
        self.admin_login_btn = tk.Button(self.left_btn_structure_1,text="Submit",command=self.user_submit,bg="green",fg="white",font="arial 15 bold").pack(side=tk.LEFT)

        self.pending_pdf_dummy_label = tk.Label(self.left_btn_structure_1,text="",bg="royal blue",fg="white",font="arial 20 bold",width="50")

        self.btn_pending_pdf_download = tk.Button(self.left_btn_structure_1,text="Form Download",bg="yellow",fg="black",font="arial 15 bold",command=self.pending_form_download)
        
        self.message_success_submit = tk.Label(self.left_btn_structure,text="",bg="royal blue",fg="white",font="arial 20 bold")
        self.message_success_submit.pack()

        self.fetch_user_details(userid_after_login)
        

    def user_logout(self):
        self.master.destroy()
        
        global userid_after_login
        global user_all_details

        userid_after_login = ""
        user_all_details = {}


    def pending_form_download(self):
        file_name = str(int(time.time())) + ".pdf" 
        c = canvas.Canvas(file_name,pagesize=letter)
        c.setLineWidth(.3)
        c.setFont('Helvetica',15)
        
        c.drawString(200,750,"ONLINE ADMISSION SYSTEM")
        c.line(30,746,580,746)
        c.line(30,743,580,743)

        c.setFont('Helvetica',12)
        c.drawString(220,725,"Registration Form for Admission")

        c.drawString(200,700,"Registration Id : ")
        c.drawString(320,700,user_all_details['user_id'])
        c.line(300,695,400,695)

        c.drawString(200,680,"User Name : ")
        c.drawString(320,680,user_all_details['user_name'])
        c.line(300,675,400,675)

        c.drawString(200,660,"Full Name : ")
        c.drawString(320,660,user_all_details['first_name'] + " " + str(user_all_details['middle_name']) + " " + user_all_details['last_name'])
        c.line(300,655,450,655)

        c.drawString(200,640,"Date of Birth : ")
        c.drawString(320,640,user_all_details['date_of_birth'])
        c.line(300,635,400,635)

        c.drawString(200,620,"Gender : ")
        c.drawString(320,620,user_all_details['gender'])
        c.line(300,615,400,615)

        c.drawString(200,600,"Mobile Number : ")
        c.drawString(320,600,user_all_details['mobile_number'])
        c.line(300,595,400,595)

        c.drawString(200,580,"JECA RANK : ")
        c.drawString(320,580,user_all_details['jeca_rank'])
        c.line(300,575,400,575)

        c.drawString(200,560,"JECA ROLL : ")
        c.drawString(320,560,user_all_details['jeca_roll'])
        c.line(300,555,400,555)

        c.drawString(200,540,"JECA REG : ")
        c.drawString(320,540,user_all_details['jeca_reg'])
        c.line(300,535,400,535)

        c.setFont('Helvetica',15)
        c.drawString(120,450,"Status is PENDING. Your Details are submitted.")
        c.drawString(100,425,"ASANSOL ENGINEERING COLLEGE will verify your documents.") 

        c.setFont('Helvetica',12)
        c.drawString(450,390,"Regards")
        c.drawString(380,375,"ASANSOL ENGINEERING COLLEGE")
        c.drawString(430,360,"ADMISSION SECTION")

        cur_date = datetime.datetime.now().strftime("%d-%m-%Y %I-%M-%S %p")
        c.setFont('Helvetica',10)
        c.drawString(200,300,"This PDF downloaded at : " + cur_date)
        
        c.save()
        
        src = os.path.abspath(file_name)
        
        f = file.asksaveasfile(mode="w",filetypes=(("pdf files","*.pdf"),("all files","*.*")),defaultextension="*.pdf")

        try:
            file_path = f.name
            file_path = file_path.split("/")        
            save_file_path = ""
            save_file_path = '\\'.join(file_path)
            copyfile(src,save_file_path)
            os.remove(src)
            messagebox.showinfo("CONGRATS!","pdf file is saved in to desired location!!")

        except:
            print("Something went wrong. Check file extension befor saving")
        

    def confirmation_download(self):
        file_name = str(int(time.time())) + ".pdf" 
        c = canvas.Canvas(file_name,pagesize=letter)
        c.setLineWidth(.3)
        c.setFont('Helvetica',15)
        
        c.drawString(200,750,"ONLINE ADMISSION SYSTEM")
        c.line(30,746,580,746)
        c.line(30,743,580,743)

        c.setFont('Helvetica',12)
        c.drawString(220,725,"Confirmation of Admission")

        c.drawString(200,700,"Registration Id : ")
        c.drawString(320,700,user_all_details['user_id'])
        c.line(300,695,400,695)

        c.drawString(200,680,"User Name : ")
        c.drawString(320,680,user_all_details['user_name'])
        c.line(300,675,400,675)

        c.drawString(200,660,"Full Name : ")
        c.drawString(320,660,user_all_details['first_name'] + " " + str(user_all_details['middle_name']) + " " + user_all_details['last_name'])
        c.line(300,655,450,655)

        c.drawString(200,640,"Date of Birth : ")
        c.drawString(320,640,user_all_details['date_of_birth'])
        c.line(300,635,400,635)

        c.drawString(200,620,"Gender : ")
        c.drawString(320,620,user_all_details['gender'])
        c.line(300,615,400,615)

        c.drawString(200,600,"Mobile Number : ")
        c.drawString(320,600,user_all_details['mobile_number'])
        c.line(300,595,400,595)

        c.drawString(200,580,"JECA RANK : ")
        c.drawString(320,580,user_all_details['jeca_rank'])
        c.line(300,575,400,575)

        c.drawString(200,560,"JECA ROLL : ")
        c.drawString(320,560,user_all_details['jeca_roll'])
        c.line(300,555,400,555)

        c.drawString(200,540,"JECA REG : ")
        c.drawString(320,540,user_all_details['jeca_reg'])
        c.line(300,535,400,535)

        c.setFont('Helvetica',15)
        c.drawString(120,450,"Congratulations. Your Documents are verified.")
        c.drawString(100,425,"You are admitted in ASANSOL ENGINEERING COLLEGE.") 

        c.setFont('Helvetica',12)
        c.drawString(450,390,"Regards")
        c.drawString(380,375,"ASANSOL ENGINEERING COLLEGE")
        c.drawString(430,360,"ADMISSION SECTION")

        cur_date = datetime.datetime.now().strftime("%d-%m-%Y %I-%M-%S %p")
        c.setFont('Helvetica',10)
        c.drawString(200,300,"This PDF downloaded at : " + cur_date)
        
        c.save()
        
        src = os.path.abspath(file_name)
        f = file.asksaveasfile(mode="w",filetypes=(("pdf files","*.pdf"),("all files","*.*")),defaultextension="*.pdf")

        try:
            file_path = f.name
            file_path = file_path.split("/")        
            save_file_path = ""
            save_file_path = '\\'.join(file_path)
            copyfile(src,save_file_path)
            os.remove(src)
            messagebox.showinfo("CONGRATS!","pdf file is saved in to desired location!!")

        except:
            print("Something went wrong. Check file extension befor saving")


    def fetch_user_details(self,userid):
        global user_all_details
        conn = pymysql.connect(host="localhost",user="root",passwd="",db="admission_system_python")
        cursor = conn.cursor()

        cursor.execute("SELECT * from user where user_id=%s",(userid))
        res = cursor.fetchone()

        #for creation dictionary
        data = []
        for j in list(cursor.description):
            j = list(j)
            data.append(j[0])
        data = dict(zip(data,res))

        user_all_details = data
        
        self.user_name_welcome.config(text="Welcome " + res[2])
        self.user_id_welcome.config(text="User Id : " + res[1])

        if data['is_pending'] == 1:
            self.pending_verified.config(text="Your Form is Already Submitted. And it's Status is PENDING..")
            self.pending_pdf_dummy_label.pack(side=tk.LEFT)
            self.btn_pending_pdf_download.pack(side=tk.RIGHT)
            
            self.f_name.set(data['first_name'])
            self.m_name.set(data['middle_name'])
            self.l_name.set(data['last_name']) 
            self.dob.set(data['date_of_birth'])
            self.ma_name.set(data['mother_name']) 
            self.fa_name.set(data['father_name'])
            self.occ.set(data['occupation'])
            self.gen.set(data['gender'])
            self.b_g.set(data['blood_group'])
            self.m_s.set(data['marital_status']) 
            
            self.tenth.set(data['total_marks_10'])
            self.board_10.set(data['board_10'])
            self.ins_10.set(data['institute_10'])
            self.yop_10.set(data['year_of_passing_10']) 
            self.perc_10.set(data['percentage_10'])

            self.twelfth.set(data['total_marks_12'])
            self.board_12.set(data['board_12'])
            self.ins_12.set(data['institute_12'])
            self.yop_12.set(data['year_of_passing_12'])
            self.perc_12.set(data['percentage_12'])

            self.grad.set(data['total_marks_grad'])
            self.board_grad.set(data['board_grad'])
            self.ins_grad.set(data['institute_grad'])
            self.yop_grad.set(data['year_of_passing_grad']) 
            self.perc_grad.set(data['percentage_grad'])
            
            self.jeca_roll.set(data['jeca_roll'])
            self.jeca_rank.set(data['jeca_rank'])
            self.jeca_reg.set(data['jeca_reg'])

            self.ddno.set(data['dd_no'])
            self.bank_name.set(data['dd_bank_name'])
            self.branch.set(data['dd_branch_name'])

            self.addr.set(data['address'])
            self.city.set(data['city'])
            self.district.set(data['distict'])
            self.state.set(data['state'])
            self.pincode.set(data['pincode'])
            self.mob.set(data['mobile_number'])

        elif data['is_verified'] == 1:
            self.stu.pack_forget()

            self.conf_pdf_label_dummy_1.pack()
            self.conf_pdf_label_dummy_2.pack()
            
            self.btn_conf_pdf_download.pack()
            
            self.pending_verified.config(text="Your Form is now Verified. Click below button to Download the PDF.")
        else:
            pass

        
    def user_submit(self):
        f_n=self.f_name.get()
        m_n=self.m_name.get()
        l_n=self.l_name.get() 
        d_o_b=self.dob.get()
        ma_name=self.ma_name.get() 
        fa_name=self.fa_name.get()
        occ=self.occ.get()
        gender=self.gen.get()
        blood_group=self.b_g.get()
        mar_s=self.m_s.get() 
        

        ten=self.tenth.get()
        board10=self.board_10.get()
        ins10=self.ins_10.get()
        yop10=self.yop_10.get() 
        perc10=self.perc_10.get()

        twelve=self.twelfth.get()
        board12=self.board_12.get()
        ins12=self.ins_12.get()
        yop12=self.yop_12.get()
        perc12=self.perc_12.get()

        gradu=self.grad.get()
        boardgrad=self.board_grad.get()
        insgrad=self.ins_grad.get()
        yopgrad=self.yop_grad.get() 
        percgrad=self.perc_grad.get()
        
        jec_roll=self.jeca_roll.get()
        jec_rank=self.jeca_rank.get()
        jeca_reg=self.jeca_reg.get()

        ddnum=self.ddno.get()
        bankname=self.bank_name.get()
        branch_b=self.branch.get()

        address=self.addr.get()
        city1=self.city.get()
        dis=self.district.get()
        state=self.state.get()
        pin=self.pincode.get()
        mobile=self.mob.get()

        update_details = {"first_name":f_n,"middle_name":m_n,"last_name":l_n,"date_of_birth":d_o_b,"mother_name":ma_name,"father_name":fa_name,
                          "occupation":occ,"gender":gender,"blood_group":blood_group,"marital_status":mar_s,"total_marks_10":ten,
                          "board_10":board10,"institute_10":ins10,"year_of_passing_10":yop10,"percentage_10":perc10,"total_marks_12":twelve,
                          "board_12":board12,"institute_12":ins12,"year_of_passing_12":yop12,"percentage_12":perc12,"total_marks_grad":gradu,
                          "board_grad":boardgrad,"institute_grad":insgrad,"year_of_passing_grad":yopgrad,"percentage_grad":percgrad,
                          "jeca_roll":jec_roll,"jeca_rank":jec_rank,"jeca_reg":jeca_reg,"dd_no":ddnum,"dd_bank_name":bankname,
                          "dd_branch_name":branch_b,"address":address,"city":city1,"distict":dis,"state":state,"pincode":pin,
                          "mobile_number":mobile,"is_submitted":1,"is_pending":1}
        #print(update_details)

        flag = 0
        for i in update_details.keys():
            if i == "middle_name":
                continue
            else:
                if update_details[i] == "":
                    flag = 1
                    break

        if flag == 1:
            messagebox.showinfo("Error!","Some Fields are Empty. Try again!!")
        else:
            update_sql = "UPDATE user SET "
            value = ""
            
            for i in update_details.keys():
                update_sql = update_sql + i + "=%s,"
                value = value + str(update_details[i]) + ","
                
            update_sql = update_sql[0:-1]
            update_sql = update_sql + " WHERE user_id=%s"
            
            value = value[0:-1]
            value = value + "," + userid_after_login
            value = list(value.split(','))  #this will convert all entrys to a list
            #print(value)

            conn = pymysql.connect(host="localhost",user="root",passwd="",db="admission_system_python")
            cursor = conn.cursor()

            cursor.execute(update_sql,value)    #passing dynamic sql query and list elements
            conn.commit()
            

            self.btn_pending_pdf_download.pack(side=tk.RIGHT)
            self.message_success_submit.config(text="YOUR FORM IS SUBMITTED")
            messagebox.showinfo("Success!","Your Form Is Submitted. You Can edit this..")

            global user_all_details

            cursor.execute("SELECT * from user where user_id=%s",(userid_after_login))
            res = cursor.fetchone()

            #for creation dictionary
            data = []
            for j in list(cursor.description):
                j = list(j)
                data.append(j[0])
            data = dict(zip(data,res))

            user_all_details = data
            
            cursor.close()
            conn.close()
            
##        sql = "ALTER TABLE user "
##        for i in update_details.keys():
##            sql = sql + "ADD " + i + " VARCHAR(100) NULL, "
##        print(sql)

        
def main():
    global userid_after_login
    global adminid_after_login
    global user_all_details
    root = tk.Tk()
    app = homepage(root)
    root.mainloop()


if __name__ == '__main__':
    main()
