from tkinter import*
import tkinter as  tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from PIL import Image,ImageTk
import cv2
import os
import pyodbc
from time import strftime
from datetime import datetime
from admin_view import stu_detail
from train import train_data
import csv
from tkinter import filedialog



mydata=[]
class face_Attendance:
   
    def __init__(self,root):
        self.root=root
        self.root.title("Attendance System")
        self.root.geometry("1550x900+0+0")
        ######variable
        self.var_atten_id=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dept=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_attendance=StringVar()





        img1=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\face1.jpg")
        img1=img1.resize((400,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lbl_img=Label(root,image=self.photoimg1)
        lbl_img.place(x=0,y=0)

        img2=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\main2.jpg")
        img2=img2.resize((400,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lbl_img1=Label(root,image=self.photoimg2)
        lbl_img1.place(x=400,y=0)

        img3=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\main1.png")
        img3=img3.resize((400,150),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lbl_img3=Label(root,image=self.photoimg3)
        lbl_img3.place(x=800,y=0)

        img4=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\face5.jpeg")
        img4=img4.resize((400,150),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        lbl_img4=Label(root,image=self.photoimg4)
        lbl_img4.place(x=1200,y=0)

        frame=Frame(root,bg="orange",highlightthickness=2,highlightbackground="black")
        frame.place(x=0,y=150,width=1550,height=60)

        t_lbl=Label(frame,text="Attendance Report",font=("Times new Roman", 32, "bold"), fg="black",bg="orange")
        t_lbl.place(x=500,y=0)
        #frame
        main_frame=Frame(root,bd=2,bg="light blue",relief=RIDGE)
        main_frame.place(x=0,y=210,width=1550,height=650)
        
                #image
        img5=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\face1.jpg")
        img5=img5.resize((730,500),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        lbl_img5=Label(main_frame,image=self.photoimg5)
        lbl_img5.place(x=795,y=0)
               
        #import Button
        import_btn=Button(main_frame,text="import csv",command=self.importcsv,font=("Times new Roman", 18, "bold"),bg="blue",fg="white")
        import_btn.place(x=900,y=525,width=150,height=45)
        #export Button
        export_btn=Button(main_frame,text="export csv",command=self.exportcsv,font=("Times new Roman", 18, "bold"),bg="green",fg="white")
        export_btn.place(x=1100,y=525,width=150,height=45)
         
        
        #right_frame
        right_frame=LabelFrame(main_frame,text="Student Attendance Details",font=("Times new Roman", 16, "bold"),bg="white",fg="red",bd=2,relief=RIDGE)
        right_frame.place(x=0,y=2,width=800,height=650,bordermode="outside")
        ###tableframe
        table_frame=Frame(right_frame,bg="white",bd=2,relief=RIDGE)
        table_frame.place(x=10,y=28,width=785,height=550,bordermode="outside")
        ########scroll bar
        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.AttendanceTable=ttk.Treeview(table_frame,columns=("id","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceTable.xview)
        scroll_y.config(command=self.AttendanceTable.yview)
        #set heading
        self.AttendanceTable.heading("id",text="Student ID")
        self.AttendanceTable.heading("name",text="Student Name")
        self.AttendanceTable.heading("department",text="Department")
        self.AttendanceTable.heading("time",text="Time")
        self.AttendanceTable.heading("date",text="Date")
        self.AttendanceTable.heading("attendance",text="Attendance")
        self.AttendanceTable["show"]="headings"
        
        self.AttendanceTable.column("id",width=100,anchor=CENTER)
        self.AttendanceTable.column("name",width=130,anchor=CENTER)
        self.AttendanceTable.column("department",width=130,anchor=CENTER)
        self.AttendanceTable.column("time",width=130,anchor=CENTER)
        self.AttendanceTable.column("date",width=130,anchor=CENTER)
        self.AttendanceTable.column("attendance",width=150,anchor=CENTER)
        self.AttendanceTable.pack(fill=BOTH,expand=1)
        self.AttendanceTable.bind("<ButtonRelease>",self.get_cursors)
    
    

        #############fetch data
    def fetch_Data(self,rows):
        self.AttendanceTable.delete(*self.AttendanceTable.get_children())
        for i in rows:
            self.AttendanceTable.insert("",END,values=i)
    def importcsv(self):
        global mydata
        mydata.clear()
        find = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV file", "*csv"), ("All files", "*.*")), parent=self.root)
        with open(find) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            
            for i in csvread:
                mydata.append(i)
            self.fetch_Data(mydata)

            ####export
    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No data found to export",parent=self.root)
                return False
            find = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV file", "*csv"), ("All files", "*.*")), parent=self.root)
            with open(find,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata :
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", os.path.basename(find)+"Your Data exported successfully")
        except Exception as e:
                messagebox.showerror("error",f"Due to:{str(e)}",parent=self.root)
     ###########get cursor
    def get_cursors(self,event=""):
                cursor_focus=self.AttendanceTable.focus()
                content=self.AttendanceTable.item(cursor_focus)
                data=content["values"]
                self.var_atten_id.set(data[0])
                self.var_atten_name.set(data[1])
                self.var_atten_dept.set(data[2])
                self.var_atten_time.set(data[3])
                self.var_atten_date.set(data[4])
                self.var_attendance.set(data[5])
                
                ##########update
   

    






        












if __name__== "__main__" :
    root=Tk()
    log=face_Attendance(root)
    root.mainloop()

        