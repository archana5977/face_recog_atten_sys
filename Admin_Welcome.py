from tkinter import *
from tkinter import ttk
import tkinter as tk
from  PIL import Image,ImageTk
from admin_view import stu_detail
import os
from train import train_data
from tkinter import messagebox
from face_recognition import face_recog
from attendance import face_Attendance

class Face_Recog_Sys:
    def __init__(self,root):
        
        self.root=root
        self.root.geometry("1550x1345+0+0")
        self.root.title("Face Recognition Attendance System")
        
      

        
        #image1
        img1=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\face4.jpg")
        img1=img1.resize((155,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lbl_img1=Label(root,image=self.photoimg1,borderwidth=2)
        lbl_img1.place(x=0,y=0)
       
        #image2
        img2=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\face2.jpg")
        img2=img2.resize((200,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lbl_img2=Label(root,image=self.photoimg2,borderwidth=2)
        lbl_img2.place(x=150,y=0)
        #image3
        img3=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\face5.jpeg")
        img3=img3.resize((200,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lbl_img3=Label(root,image=self.photoimg3,borderwidth=0)
        lbl_img3.place(x=350,y=0)
        #image4
        img4=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\f3.jpeg")
        img4=img4.resize((200,130),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        lbl_img4=Label(root,image=self.photoimg4,borderwidth=0)
        lbl_img4.place(x=550,y=0)
        #image5
        img5=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\f2.png")
        img5=img5.resize((200,130),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        lbl_img5=Label(root,image=self.photoimg5,borderwidth=0)
        lbl_img5.place(x=750,y=0)
        #image6
        img6=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\min6.png")
        img6=img6.resize((210,130),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        lbl_img6=Label(root,image=self.photoimg6,borderwidth=0)
        lbl_img6.place(x=950,y=0)
         #image7
        img_7=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\f1.jpg")
        img_7=img_7.resize((200,130),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img_7)
        lbl_img7=Label(root,image=self.photoimg7,borderwidth=0)
        lbl_img7.place(x=1160,y=0)
        #image8
        img8=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\face3.jpeg")
        img8=img8.resize((200,130),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        lbl_img8=Label(root,image=self.photoimg8,borderwidth=0)
        lbl_img8.place(x=1350,y=0)



        #frame
        frame=Frame(self.root,bg="orange")
        frame.place(x=0,y=130,width=1550,height=50,bordermode="outside")
        #title label
        title_lbl=Label(frame,text="Face Recognition Attendance System",font=("Times new Roman", 28, "bold"), fg="black",bg="Orange")
        title_lbl.place(x=480,y=2)
        
        #bgimage ----------like a frame
        img=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\back1.jpg")
        img=img.resize((1540,620),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        bg_img=Label(root,image=self.photoimg,borderwidth=0)
        bg_img.place(x=0,y=180)

        # buttons
          
        #Student_deatail
        stu_img=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\student.jpg")
        stu_img=stu_img.resize((150,150),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(stu_img)
        b1=Button(bg_img,image=self.photoimage,command=self.details,cursor="hand2",bd=2)
        b1.place(x=250,y=50,width=150,height=150)
        b1_txt=Button(bg_img,text="Student Details",command=self.details,cursor="hand2",font=("Times new Roman", 16, "bold"), fg="white",bg="blue",border=0)
        b1_txt.place(x=250,y=190,width=150,height=40)
        #face detector
        face_img=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\photo2.jpg")
        face_img=face_img.resize((150,150),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(face_img)
        b2=Button(bg_img,image=self.photoimage1,command=self.face_detector,cursor="hand2")
        b2.place(x=550,y=50,width=150,height=150)
        b2_txt=Button(bg_img,text="Attendance",command=self.face_detector,cursor="hand2",font=("Times new Roman", 16, "bold"), fg="white",bg="blue")
        b2_txt.place(x=550,y=190,width=150,height=40)
       
        
        #Train data
        train_img=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\img2.jpg")
        train_img=train_img.resize((150,150),Image.ANTIALIAS)
        self.photoimage4=ImageTk.PhotoImage(train_img)
        b5=Button(bg_img,image=self.photoimage4,command=self.train,cursor="hand2")
        b5.place(x=850,y=50,width=150,height=150)
        b5_txt=Button(bg_img,text="Train Data",command=self.train,cursor="hand2",font=("Times new Roman", 16, "bold"), fg="white",bg="blue")
        b5_txt.place(x=850,y=190,width=150,height=40)
         #Attendance
        attend_img=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\attend.png")
        attend_img=attend_img.resize((150,150),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(attend_img)
        b3=Button(bg_img,image=self.photoimage2,command=self.attendance,cursor="hand2")
        b3.place(x=250,y=300,width=150,height=150)
        b3_txt=Button(bg_img,text="Report",command=self.attendance,cursor="hand2",font=("Times new Roman", 16, "bold"), fg="white",bg="blue")
        b3_txt.place(x=250,y=440,width=150,height=40)

        #Photo Sample
        photo_img=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\photo1.jpg")
        photo_img=photo_img.resize((150,150),Image.ANTIALIAS)
        self.photoimage5=ImageTk.PhotoImage(photo_img)
        b6=Button(bg_img,image=self.photoimage5,command=self.open_img,cursor="hand2")
        b6.place(x=550,y=300,width=150,height=150)
        b6_txt=Button(bg_img,text="Photo Sample",command=self.open_img,cursor="hand2",font=("Times new Roman", 16, "bold"), fg="white",bg="blue")
        b6_txt.place(x=550,y=440,width=150,height=40)
         
          #Exit
        exit_img=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\exit.jpg")
        exit_img=exit_img.resize((150,150),Image.ANTIALIAS)
        self.photoimage7=ImageTk.PhotoImage(exit_img)
        b8=Button(bg_img,image=self.photoimage7,command=self.exit,cursor="hand2")
        b8.place(x=850,y=300,width=150,height=150)
        b8_txt=Button(bg_img,text="Exit",command=self.exit,cursor="hand2",font=("Times new Roman", 16, "bold"), fg="white",bg="blue")
        b8_txt.place(x=850,y=440,width=150,height=40)
        

#############function button 

    def details(self):
        self.new_window=Toplevel(self.root)
        self.app1=stu_detail(self.new_window)
        
        
##########
    def open_img(self):
        os.startfile("photo")
    #######
    def train(self):
        self.new_window=Toplevel(self.root)
        self.app1=train_data(self.new_window) 
        #self.root.withdraw()
       
        #########
    def face_detector(self):
        self.new_window=Toplevel(self.root)
        self.app2=face_recog(self.new_window) 
        #self.root.withdraw()   
        ##########3
    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=face_Attendance(self.new_window)    
###########
    def exit(self):
        self.exit=tk.messagebox.askyesno("close_win","Are you sure want to exit the Face Recognition Attendance System",parent=self.root)
        if self.exit >0:
            self.root.destroy()
        else:
            return 



        

if __name__ =="__main__":
    root=Tk()
    obj=Face_Recog_Sys(root)
    root.mainloop()
