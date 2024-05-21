from tkinter import*
import tkinter as  tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import pyodbc 
import cv2
import os
import numpy as np



class train_data:
   
    def __init__(self,root):
        self.root=root
        self.root.title("Train Data")
        self.root.geometry("1650x900+0+0")
#image1
        img1=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\face_d.jpeg")
        img1=img1.resize((300,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lbl_img1=Label(root,image=self.photoimg1)
        lbl_img1.place(x=0,y=0)
#image2
        img2=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\face2.jpg")
        img2=img2.resize((300,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lbl_img2=Label(root,image=self.photoimg2)
        lbl_img2.place(x=300,y=0)
#image3
        img3=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\face3.jpeg")
        img3=img3.resize((300,150),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lbl_img3=Label(root,image=self.photoimg3)
        lbl_img3.place(x=600,y=0)
#image4
        img4=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\face5.jpeg")
        im4=img4.resize((300,150),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        lbl_img4=Label(root,image=self.photoimg4)
        lbl_img4.place(x=900,y=0)
#image5
        img5=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\min5.jpg")
        img5=img5.resize((335,150),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        lbl_img5=Label(root,image=self.photoimg5)
        lbl_img5.place(x=1200,y=0)

        frame=Frame(root,bg="light green",highlightthickness=2,highlightbackground="black")
        frame.place(x=0,y=150,width=1550,height=55)
        t_lbl=Label(frame,text="TRAIN DATA SET",font=("Times new Roman", 28, "bold"), fg="brown",bg= "light green")
        t_lbl.place(x=600,y=2)
        
        imgs=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\photo1.jpg")
        imgs=imgs.resize((1550,900),Image.ANTIALIAS)
        self.photoimgs=ImageTk.PhotoImage(imgs)
        lbl_imgs=Label(root,image=self.photoimgs)
        lbl_imgs.place(x=0,y=205)

        ##trin button
        train_btn=Button(lbl_imgs, text="Train Data",command=lambda:[self.train_classifier(),self.trainn()],font=("Times new Roman", 26, "bold"),fg="Black",bg= "blue",bd=3,activebackground="gray",cursor="hand2")
        train_btn.place(x=550,y=250,width=300,height=100)
        ####
    def trainn(self):
        from Admin_Welcome import Face_Recog_Sys
        self.new_window=Toplevel(self.root)
        self.app1=Face_Recog_Sys(self.new_window)
        self.root.withdraw()
    
    def train_classifier(self):
        data_dir=("photo")
        path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]
        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert("L") #image converted into grayscale
            image_np=np.array(img,"uint8")
            id=int(os.path.split(image)[1].split('.')[1])
            faces.append(image_np)
            ids.append(id)
            cv2.imshow("Training",image_np)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        ########Train the classifier

        train_clf= cv2.face.LBPHFaceRecognizer_create()

        train_clf.train(faces,ids)
        train_clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("result","Training dataset completed")
                


        












if __name__== "__main__" :
    root=Tk()
    log=train_data(root)
    root.mainloop()
