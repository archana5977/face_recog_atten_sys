from tkinter import*
import tkinter as  tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from PIL import Image,ImageTk
import cv2
import os
import csv
import pyodbc
from time import strftime
from datetime import datetime
from admin_view import stu_detail
from train import train_data




class face_recog:
   
    def __init__(self,root):
        self.root=root
        self.root.title("Student Detail")
        self.root.geometry("1550x900+0+0")
        

        img1=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\detect1.jpg")
        img1=img1.resize((1600,900),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lbl_img=Label(root,image=self.photoimg1)
        lbl_img.place(x=0,y=0)

        frame=Frame(lbl_img,bg="orange",highlightthickness=2,highlightbackground="black")
        frame.place(x=0,y=0,width=1550,height=60)

        t_lbl=Label(frame,text="Face Recognition",font=("Times new Roman", 32, "bold"), fg="black",bg="orange")
        t_lbl.place(x=660,y=0)
        img11=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\img5.png")
        img11=img11.resize((350,600),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        lbl_img1=Label(root,image=self.photoimg11)
        lbl_img1.place(x=560,y=100)
         ##login button
        detect_btn=Button(lbl_img1, text="Face Detector",command=self.recog,font=("Times new Roman", 20, "bold"),fg="white",bg="purple",relief="ridge",activeforeground="white",activebackground="purple",cursor="hand2")
        detect_btn.place(x=62,y=555,width=270,height=40)
        
        #########
    #def recognize(self):
     #   from Admin_Welcome import Face_Recog_Sys
      #  self.new_window=Toplevel(self.root)
       # self.app1=Face_Recog_Sys(self.new_window)
        #self.root.withdraw()
        ##########Attendance
    def mark_Attendance(self,i,j,k):
        with open("archu.csv","r+",newline="\n")as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split(",")
                name_list.append(entry[0])
            
            if((i not in name_list ) and (j not in name_list) and (k not in name_list)):  # i not in name_list means once attendance marked , donot repeat again
                now=datetime.now()
                d1=now.strftime("%d/%m/%y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{j},{k},{dtString},{d1},Present")

    
    
    def recog(self):
        
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,train_clf):
            #face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
            gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_img,scaleFactor,minNeighbors)

            co_ordinate=[]

            

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=train_clf.predict(gray_img[y:y+h,x:x+w])
                
                confidence=int(100*(1-predict/300))

                conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=SRISHTI\SQLEXPRESS;'
                      'Database=archana;'
                      'Trusted_Connection=yes;')
                my_cursor=conn.cursor()
                my_cursor.execute("select id from students where id=?",str(id))
                i=my_cursor.fetchone()
                if i:
                    i=str(i[0])
                    i=i.strip("('")
                    i=i.strip("')")
                
                my_cursor.execute("select name from students where id=?",str(id))
                j=my_cursor.fetchone()
                if j:
                    j=str(j[0])
                    j=j.strip("('")
                    j=j.strip("')")
                
                


                my_cursor.execute("select dept from students where id=?",(id))
                k=my_cursor.fetchone()
             
                if k:
                    k=str(k[0])
                    k=k.strip("('")
                    k=k.strip("')")

               
                
                
                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{j}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{k}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                    
                    self.mark_Attendance(i,j,k)
                    
                else: 
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

                    cv2.putText(img,f"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                co_ordinate=[x,y,w,h]
            return co_ordinate

        def face_recog(img,train_clf,faceCascade):
            co_ordinate=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",train_clf)
            return img
        face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        train_clf=cv2.face.LBPHFaceRecognizer_create()
        train_clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
           
            img=face_recog(img,train_clf,face_classifier)
            
            cv2.imshow("welcome to the face recognition",img)
           
        

            if cv2.waitKey(1)==13:
                  break
        video_cap.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("result","Face Recognized successfully")
                


        

        
            
        
                


                     




if __name__== "__main__" :
    root=Tk()
    log=face_recog(root)
    root.mainloop()

