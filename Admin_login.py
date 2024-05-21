from tkinter import*
import tkinter as  tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from Admin_Welcome import Face_Recog_Sys

import pyodbc 


class admin_login:
   
    def __init__(self,root):
        self.root=root
        self.root.title("Admin Login Page")
        self.root.geometry("1550x900+0+0")

       




        

        frame1=LabelFrame(root,bg="black")
        frame1.place(x=0,y=0,width=1550,height=900)
        lbl=Label(frame1,text="Welcome",font=("Times new Roman", 34, "bold"), fg="white",bg= "black")
        lbl.place(x=1080,y=100)

        img1=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\admin.jpg")
        img1=img1.resize((750,900),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lbl_img=Label(frame1,image=self.photoimg1)
        lbl_img.place(x=0,y=0)

        frame2=LabelFrame(frame1,bg="black",highlightthickness=2,highlightbackground="black")
        frame2.place(x=1000,y=200,width=360,height=430)

        
        self.var_name1=StringVar()
        self.var_pas1=StringVar()
        
        img2=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\icon11.png")
        img2=img2.resize((75,75),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lbl_img=Label(frame2,image=self.photoimg2,bd=0)
        lbl_img.place(x=140,y=20)

        #user name
        user_lbl1=Label(frame2,text="Username",font=("Times new Roman", 18, "bold"), fg="white",bg= "black")
        user_lbl1.place(x=80,y=120)
        self.user_lbl_entry1=tk.Entry(frame2,textvariable=self.var_name1,font=("Times new Roman", 14),foreground="white",background="black",highlightcolor="red",highlightthickness=1,highlightbackground="white")
        self.user_lbl_entry1.place(x=70,y=165,width=200,height=35)
         #button,
        log_btn1=Button(frame2, text="Login",command=lambda:[self.admin_data(),self.new_window()],font=("Times new Roman", 20, "bold"),border="2",fg="white",bg="blue",relief="ridge",activeforeground="white",activebackground="gray",cursor="hand2")
        log_btn1.place(x=125,y=345,width=80,height=40)
        #entry field validation
        validate_uname1=self.root.register(self.validate_usr)
        self.user_lbl_entry1.config(validate="key",validatecommand=(validate_uname1,"%P"))
        #password
        pas_lbl1=Label(frame2,text="Password",font=("Times new Roman", 18, "bold"), fg="white",bg= "black")
        pas_lbl1.place(x=80,y=220)
        self.pass_entry1=tk.Entry(frame2,textvariable=self.var_pas1,font=("Times new Roman", 14),show="*",foreground="white",background="black",highlightcolor="black",highlightthickness=1)
        self.pass_entry1.place(x=70,y=265,width=200,height=35)

        validate_pas1 = self.root.register(self.validate_pass)
        self.pass_entry1.config(validate="key", validatecommand=(validate_pas1, "%P"))

        self.show_password_var = BooleanVar()
        self.show_password_checkbutton = Checkbutton(frame2,variable=self.show_password_var, onvalue=True, offvalue=False, command=self.toggle_password_visibility,bg="black")
        self.show_password_checkbutton.place(x=240,y=270)

    def toggle_password_visibility(self):
        if self.show_password_var.get():
            self.pass_entry1.config(show="")
        else:
            self.pass_entry1.config(show="*")
       
        
       
    def new_window(self):
        if self.var_name1.get() == "archana" and self.var_pas1.get() == "archu":
            self.new_window = Toplevel(self.root)
            self.app5 = Face_Recog_Sys(self.new_window)
        else:
            return
           # messagebox.showerror("Error", "Invalid username or password")
        
        
    def admin_data(self):
            if self.var_name1.get()=="" or self.var_pas1.get()=="":
                messagebox.showerror("error","All fields are required",parent=self.root) 
            
            elif self.var_name1.get()=="archana" and self.var_pas1.get()=="archu":

                try:
                 conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=SRISHTI\SQLEXPRESS;'
                      'Database=archana;'
                      'Trusted_Connection=yes;')
                 cursor1=conn.cursor()
                 cursor1.execute("insert into admin_login values(?,?)",self.var_name1.get(),self.var_pas1.get())
                 messagebox.showinfo("success","Login successfull")
                 self.new_window()
                 conn.commit()
                 conn.close()
                except Exception as e:
                    messagebox.showerror("error",f"Due to:{str(e)}",parent=self.root)

            
            else:
                messagebox.showerror("error","Invalid username and password",parent=self.root) 

    def validate_usr(self,usr_name):
          if len(usr_name)>10:
              messagebox.showwarning("alert","username does not excced 10 digit")
          
          elif usr_name.isalnum():
               return True
                   
          else:
            messagebox.showerror("error","Special charcters are not allowed")
            return False    
        
    def validate_pass(self, pas_word):
        if len(pas_word) > 8:
            messagebox.showwarning("alert", "password should be at least 8 characters")
            return False
        elif not pas_word.isalnum():
            messagebox.showerror("error", "Special characters are not allowed")
            return False
        else:
            return True                




 
            
            
             

            
if __name__== "__main__" :
    root=Tk()
    logs=admin_login(root)
    root.mainloop()

