from tkinter import*
import tkinter as  tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from PIL import Image,ImageTk
import pyodbc 
import cv2
import string

class stu_detail:
   
    def __init__(self,root):
        self.root=root
        self.root.title("Student Detail")
        self.root.geometry("1650x900+0+0")
        root['background']="purple"

         ###########variables
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_divs=StringVar()
        self.var_classes=StringVar()
        self.var_dob=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_dept=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_pname=StringVar()
        self.var_foccu=StringVar()
        self.var_mname=StringVar()
        self.var_moccu=StringVar()
        self.var_fno=StringVar()
        self.var_mno=StringVar()
        
    
    #first image
        image1=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\min6.png")
        image1=image1.resize((200,125),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(image1)
        lbl_img1=Label(root,image=self.photoimage1,borderwidth=0)
        lbl_img1.place(x=0,y=0)
        #image2
        image2=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\f1.jpg")
        image2=image2.resize((200,125),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(image2)
        lbl_image2=Label(root,image=self.photoimage2,borderwidth=0)
        lbl_image2.place(x=200,y=0)
        #image3
        image4=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\face2.jpg")
        image4=image4.resize((200,125),Image.ANTIALIAS)
        self.photoimage4=ImageTk.PhotoImage(image4)
        lbl_image4=Label(root,image=self.photoimage4,borderwidth=2)
        lbl_image4.place(x=400,y=0)
        #image4
        imag5=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\photo2.jpg")
        imag5=imag5.resize((200,125),Image.ANTIALIAS)
        self.photoimag5=ImageTk.PhotoImage(imag5)
        lbl_imag5=Label(root,image=self.photoimag5,borderwidth=0)
        lbl_imag5.place(x=600,y=0)
        #image5
        imag6=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\f3.jpeg")
        imag6=imag6.resize((200,125),Image.ANTIALIAS)
        self.photoimag6=ImageTk.PhotoImage(imag6)
        lbl_imag6=Label(root,image=self.photoimag6,borderwidth=0)
        lbl_imag6.place(x=800,y=0)
        #image6
        imag7=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\f2.png")
        imag7=imag7.resize((200,125),Image.ANTIALIAS)
        self.photoimag7=ImageTk.PhotoImage(imag7)
        lbl_imag7=Label(root,image=self.photoimag7,borderwidth=0)
        lbl_imag7.place(x=1000,y=0)
        #image7
        imag8=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\main1.png")
        imag8=imag8.resize((200,125),Image.ANTIALIAS)
        self.photoimag8=ImageTk.PhotoImage(imag8)
        lbl_img8=Label(root,image=self.photoimag8,borderwidth=0)
        lbl_img8.place(x=1200,y=0)
        #image8
        imag9=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\main3.jpg")
        imag9=imag9.resize((140,125),Image.ANTIALIAS)
        self.photoimag9=ImageTk.PhotoImage(imag9)
        lbl_imag7=Label(root,image=self.photoimag9,borderwidth=0)
        lbl_imag7.place(x=1400,y=0)


        #frame
        frame=Frame(self.root,bg="light gray")
        frame.place(x=0,y=175,width=1550,height=620,bordermode="outside")
        #frame1
        frame1=Frame(self.root,bg="light green",bd=2)
        frame1.place(x=0,y=125,width=1550,height=50,bordermode="outside")

        #title label
        title_lbl=Label(frame1,text="Face Recognition Attendance System",font=("Times new Roman", 28, "bold"), fg="black",bg="light green")
        title_lbl.place(x=550,y=1)

        
        #left label frame 
        left_frame=LabelFrame(frame,bg="pink",fg="red",bd=2,relief=RIDGE, text="Student Information",font=("Times new Roman", 14, "bold"))
        left_frame.place(x=0,y=1,width=910,height=240,bordermode="outside")
        
           #Class Student Information
        id_lbl=Label(left_frame,text="Student ID",font=("Times new Roman", 14, "bold"), fg="black",bg="pink")
        id_lbl.place(x=0,y=10)
        self.id_lbl_entry=ttk.Entry(left_frame,textvariable=self.var_id,font=("Times new Roman", 14))
        self.id_lbl_entry.place(x=105,y=10,width=180,height=35)
        #entry field validation
        validate_id=self.root.register(self.id1)
        self.id_lbl_entry.config(validate="key",validatecommand=(validate_id,"%P"))
        #name
        name_lbl=Label(left_frame,text="Student Name",font=("Times new Roman", 14, "bold"), fg="black",bg="pink")
        name_lbl.place(x=305,y=10)
        self.name_lbl_entry=ttk.Entry(left_frame,textvariable=self.var_name,font=("Times new Roman", 14))
        self.name_lbl_entry.place(x=440,y=10,width=180,height=35)
        #entry field validation
        validate_name1=self.root.register(self.usr_name1)
        self.name_lbl_entry.config(validate="key",validatecommand=(validate_name1,"%P"))
        #div
        div_lbl=Label(left_frame,text="Division",font=("Times new Roman", 14, "bold"), fg="black",bg="pink")
        div_lbl.place(x=640,y=10)
        var_div=["Select Division","A","B","C","D"]
        div_combo=ttk.Combobox(left_frame,textvariable=self.var_divs,font=("Times new Roman", 14),state="readonly",values=var_div)
        div_combo.current(0)
        div_combo.place(x=730,y=10,width=170,height=35)
        
        #class
        class_lbl=Label(left_frame,text="Class",font=("Times new Roman", 14, "bold"), fg="black",bg="pink")
        class_lbl.place(x=0,y=80)
        var_class=["Select Class","First Year","Second Year","Third Year"]
        class_combo=ttk.Combobox(left_frame,textvariable=self.var_classes,font=("Times new Roman", 14),state="readonly",values=var_class)
        class_combo.current(0)
        class_combo.place(x=105,y=80,width=180,height=35)
        
        #Gender
        gender_lbl=Label(left_frame,text="Gender",font=("Times new Roman", 14, "bold"), fg="black",bg="pink")
        gender_lbl.place(x=305,y=80)
        self.var_gens=StringVar()
        var_gen=["Select Gender","Male","Female","Others"]
        gen_combo=ttk.Combobox(left_frame,textvariable=self.var_gens,font=("Times new Roman", 14),state="readonly",values=var_gen)
        gen_combo.current(0)
        gen_combo.place(x=440,y=80,width=180,height=35)
        
        # DOB
        dob_lbl=Label(left_frame,text="DOB ",font=("Times new Roman", 14, "bold"), fg="black",bg="pink")
        dob_lbl.place(x=640,y=80)
        dob_lbl_entry=DateEntry(left_frame,textvariable=self.var_dob,font=("Times new Roman", 14))
        dob_lbl_entry=DateEntry(left_frame,Selectmode="day",date_pattern="dd-mm-yy")
        dob_lbl_entry.place(x=730,y=80,width=170,height=35)
        #contact
        contact_lbl=Label(left_frame,text="Contact No.",font=("Times new Roman", 14, "bold"), fg="black",bg="pink")
        contact_lbl.place(x=0,y=150)
        self.contact_entry=ttk.Entry(left_frame,textvariable=self.var_contact,font=("Times new Roman", 16))
        self.contact_entry.place(x=105,y=150,width=180,height=35)
        #entry field validation
        validate_con1=self.root.register(self.contact1)
        self.contact_entry.config(validate="key",validatecommand=(validate_con1,"%P"))
        #email
        email_lbl=Label(left_frame,text="Email",font=("Times new Roman", 14, "bold"), fg="black",bg="pink")
        email_lbl.place(x=305,y=150)
        self.email_lbl_entry=ttk.Entry(left_frame,textvariable= self.var_email,font=("Times new Roman", 16))
        self.email_lbl_entry.place(x=440,y=150,width=185,height=35)
        #Address
        self.var_add=StringVar()
        add_lbl=Label(left_frame,text="Address",font=("Times new Roman", 14, "bold"), fg="black",bg="pink")
        add_lbl.place(x=640,y=150)
        self.add_lbl_entry=tk.Entry(left_frame,textvariable=self.var_add,font=("Times new Roman", 14))
        self.add_lbl_entry.place(x=730,y=150,width=170,height=50)
        #entry field validation
        validate_add1=self.root.register(self.address1)
        self.add_lbl_entry.config(validate="key",validatecommand=(validate_add1,"%P"))
        
        
        #course frame
        course_frame=LabelFrame(frame,text="Current Course Information",font=("Times new Roman", 14, "bold"),bg="pink",fg="red",bd=2,relief=RIDGE)
        course_frame.place(x=0,y=243,width=910,height=100,bordermode="outside")

        dept_lbl=Label(course_frame,text="Department",font=("Times new Roman", 14, "bold"), fg="black",bg="pink")
        dept_lbl.place(x=0,y=20)
        dept=["Select Department","BScIT","BScCS","BAMS","BAF","BScChemistry","BScPhysics"]
        dept_combo=ttk.Combobox(course_frame,textvariable=self.var_dept,font=("Times new Roman", 14),state="readonly",values=dept)
        dept_combo.current(0)
        dept_combo.place(x=110,y=20,width=180,height=35)
         
        #year
        year_lbl=Label(course_frame,text="Year",font=("Times new Roman", 14, "bold"), fg="black",bg="pink")
        year_lbl.place(x=320,y=20)
        year=["Select Year","2020-21","2021-22","2022-23","2023-24"]
        dept_combo2=ttk.Combobox(course_frame,textvariable=self.var_year,font=("Times new Roman", 14),state="readonly",values=year)
        dept_combo2.current(0)
        dept_combo2.place(x=420,y=20,width=180,height=35)
        #semester
        sem_lbl=Label(course_frame,text="Semester",font=("Times new Roman", 14, "bold"), fg="black",bg="pink")
        sem_lbl.place(x=630,y=20)
        sem=["Select Semester","sem1","sem2","sem3","sem4","sem5","sem6","sem7","sem8"]
        dept_combo3=ttk.Combobox(course_frame,textvariable=self.var_sem,font=("Times new Roman", 14),state="readonly",values=sem)
        dept_combo3.current(0)
        dept_combo3.place(x=730,y=20,width=170,height=35)

        #Parent Information
        parent_frame=LabelFrame(frame,text="Parent Information",font=("Times new Roman", 16, "bold"),bg="pink",fg="red",bd=2,relief=RIDGE)
        parent_frame.place(x=0,y=345,width=910,height=147,bordermode="outside")
        #father name
        father_name_lbl=Label(parent_frame,text="Father Name",font=("Times new Roman", 14, "bold"), fg="black",bg="pink")
        father_name_lbl.place(x=0,y=10)
        self.father_name_entry=ttk.Entry(parent_frame,textvariable=self.var_pname,font=("Times new Roman", 14))
        self.father_name_entry.place(x=125,y=10,width=170,height=35)
        #entry field validation
        validate_fname1=self.root.register(self.f_name1)
        self.father_name_entry.config(validate="key",validatecommand=(validate_fname1,"%P"))
        #father occupation
        occu_lbl=Label(parent_frame,text="Occupation",font=("Times new Roman", 14, "bold"), fg="black",bg="pink")
        occu_lbl.place(x=320,y=10)
        self.occu_entry=ttk.Entry(parent_frame,textvariable=self.var_foccu,font=("Times new Roman", 14))
        self.occu_entry.place(x=430,y=10,width=170,height=35)
        #entry field validation
        validate_occu1=self.root.register(self.f_occu1)
        self.occu_entry.config(validate="key",validatecommand=(validate_occu1,"%P"))
        #Fathers contact 
        con_lbl=Label(parent_frame,text="Mobile No.",font=("Times new Roman", 14, "bold"), fg="black",bg="pink")
        con_lbl.place(x=620,y=10)
        self.con_entry=ttk.Entry(parent_frame,textvariable=self.var_fno,font=("Times new Roman", 14))
        self.con_entry.place(x=730,y=10,width=170,height=35)
        #entry field validation
        validate_fcon1=self.root.register(self.f_contact1)
        self.con_entry.config(validate="key",validatecommand=(validate_fcon1,"%P"))
    
    
        #mother name
        mother_name_lbl=Label(parent_frame,text="Mother Name",font=("Times new Roman", 14, "bold"), fg="black",bg="pink")
        mother_name_lbl.place(x=0,y=80)
        self.mother_name_entry=ttk.Entry(parent_frame,textvariable=self.var_mname,font=("Times new Roman", 14))
        self.mother_name_entry.place(x=125,y=80,width=170,height=35)
        #entry field validation
        validate_mname1=self.root.register(self.m_name1)
        self.mother_name_entry.config(validate="key",validatecommand=(validate_mname1,"%P"))
        #mother occupation
        occu_lbl1=Label(parent_frame,text="Occupation",font=("Times new Roman", 14, "bold"), fg="black",bg="pink")
        occu_lbl1.place(x=320,y=80)
        self.occu_entry1=ttk.Entry(parent_frame,textvariable=self.var_moccu,font=("Times new Roman", 14))
        self.occu_entry1.place(x=430,y=80,width=170,height=35)
        #entry field validation
        validate_moccu1=self.root.register(self.m_occu1)
        self.occu_entry1.config(validate="key",validatecommand=(validate_moccu1,"%P"))
         
        #Mothers contact 
        con_lbl1=Label(parent_frame,text="Mobile No.",font=("Times new Roman", 14, "bold"), fg="black",bg="pink")
        con_lbl1.place(x=620,y=80)
        self.con_entry1=ttk.Entry(parent_frame,textvariable=self.var_mno,font=("Times new Roman", 14))
        self.con_entry1.place(x=730,y=80,width=170,height=35)
         #entry field validation
        validate_mcon1=self.root.register(self.m_contact1)
        self.con_entry1.config(validate="key",validatecommand=(validate_mcon1,"%P"))

        #center frame
        center_frame=LabelFrame(frame,font=("Times new Roman", 14, "bold"),bg="pink",fg="red",bd=2,relief=RIDGE)
        center_frame.place(x=0,y=493,width=910,height=120,bordermode="outside")
         #phottoample
        photo_lbl=Label(center_frame,text="Photo Sample",font=("Times new Roman", 16, "bold"), fg="black",bg="light pink")
        photo_lbl.place(x=0,y=15)
        #yes
        self.var_radio1=IntVar()
        radio1=tk.Radiobutton(center_frame,variable=self.var_radio1,text="Yes",value="1",bg="light pink",font=("Times new Roman", 14, "bold"))
        radio1.place(x=140,y=15)
        #no photo sample
    
        radio2=tk.Radiobutton(center_frame,variable=self.var_radio1,text="No",value="0",bg="light pink",font=("Times new Roman", 14, "bold"))
        radio2.place(x=210,y=15)
         #Add Photosample Button
        sample_btn=Button(center_frame,text="Take Photo Sample", command=lambda: self.generate_data() if self.var_radio1.get() == 1 else messagebox.showerror("Error", "Please select 'Yes' to take photo sample"), font=("Times new Roman", 18, "bold"),bg="orange",fg="white")
        sample_btn.place(x=300,y=15,width=230,height=40)
        
        #Save Button
        save_btn=Button(center_frame,text="Save",command=self.add_data,font=("Times new Roman", 18, "bold"),bg="blue",fg="white")
        save_btn.place(x=600,y=15,width=120,height=40)
        #Update Button
        update_btn=Button(center_frame,text="Update",command=self.update_data,font=("Times new Roman", 18, "bold"),bg="brown",fg="white")
        update_btn.place(x=500,y=70,width=120,height=40)
        #Delete Button
        delete_btn=Button(center_frame,text="Delete",command=self.delete_data,font=("Times new Roman", 18, "bold"),bg="green",fg="white")
        delete_btn.place(x=330,y=70,width=120,height=40)
        #reset  Button
        reset_btn=Button(center_frame,text="Reset",command=self.reset_data1,font=("Times new Roman", 18, "bold"),bg="green",fg="white")
        reset_btn.place(x=690,y=70,width=120,height=40)
        #right label frame 
        right_frame=LabelFrame(frame,bg="pink",fg="red",bd=2,relief=RIDGE, text="Student Deatails",font=("Times new Roman", 14, "bold"))
        right_frame.place(x=910,y=1,width=720,height=620,bordermode="outside")
        #image
        image3=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Image\face1.jpg")
        image3=image3.resize((650,250),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(image3)
        lbl_image3=Label(right_frame,image=self.photoimage3,borderwidth=0)
        lbl_image3.place(x=2,y=1)
                
        #Table frame
        table_frame=LabelFrame(frame,text="Data System",bg="pink",fg="red",bd=2,relief=RIDGE,font=("Times new Roman", 14, "bold"))
        table_frame.place(x=910,y=250,width=650,height=370,bordermode="outside")
        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        #student table
        self.stu_table=ttk.Treeview(table_frame,columns=("id","name","Div","class","gender","dob","contact","email","add","dept","year","sem","fname","occu1","mname","occu","fno.","mno.","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.stu_table.xview)
        scroll_y.config(command=self.stu_table.yview)
#set heading
        self.stu_table.heading("id",text="Student ID")
        self.stu_table.heading("name",text="Student Name")
        self.stu_table.heading("Div",text="Division")
        self.stu_table.heading("class",text="Class")
        self.stu_table.heading("gender",text="Gender")
        self.stu_table.heading("dob",text="DOB")
        self.stu_table.heading("contact",text="Contact")
        self.stu_table.heading("email",text="Email")
        self.stu_table.heading("add",text="Address")
        self.stu_table.heading("dept",text="Department")
        self.stu_table.heading("year",text="Year")
        self.stu_table.heading("sem",text="Semester")
      
        self.stu_table.heading("fname",text="Father Name")
        self.stu_table.heading("occu1",text="Father Occupation")
        self.stu_table.heading("mname",text="Mother Name")
        self.stu_table.heading("occu",text="Mother Occupation")
        self.stu_table.heading("fno.",text="Father No.")
        self.stu_table.heading("mno.",text="Mother No.")
        self.stu_table.heading("photo",text="Photo")
        self.stu_table["show"]="headings"
#set column width
        self.stu_table.column("id",width=70,anchor=CENTER)
        self.stu_table.column("name",width=70,anchor=CENTER)
        self.stu_table.column("Div",width=50,anchor=CENTER)
        self.stu_table.column("class",width=70,anchor=CENTER)
        self.stu_table.column("gender",width=70,anchor=CENTER)
        self.stu_table.column("dob",width=70,anchor=CENTER)
        self.stu_table.column("contact",width=70,anchor=CENTER)
        self.stu_table.column("email",width=70,anchor=CENTER)
        self.stu_table.column("add",width=70,anchor=CENTER)
        self.stu_table.column("dept",width=70,anchor=CENTER)
        self.stu_table.column("year",width=70,anchor=CENTER)
        self.stu_table.column("sem",width=70,anchor=CENTER)
        self.stu_table.column("fname",width=70,anchor=CENTER)
        self.stu_table.column("occu1",width=70,anchor=CENTER)
        self.stu_table.column("mname",width=70,anchor=CENTER)
        self.stu_table.column("occu",width=70,anchor=CENTER)
        self.stu_table.column("fno.",width=70,anchor=CENTER)
        self.stu_table.column("mno.",width=70,anchor=CENTER)
        self.stu_table.column("photo",width=50,anchor=CENTER)
        
        self.stu_table.pack(fill=BOTH,expand=1)
        self.stu_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        ################function declaration#####################
    def add_data(self):
        if self.var_id.get()=="" :
            #or self.var_name.get()=="" or self.var_divs.get()=="" or self.var_classes.get()=="" or self.var_gens.get()=="" or self.var_dob.get()=="" or self.var_contact.get()==""or self.var_email.get()==""or self.var_add.get()=="" or self.var_dept.get()=="" or self.var_course.get()=="" or  self.var_year.get()=="" or self.var_sem.get()=="" or self.var_sub.get()==""  or self.var_pname.get()=="" or self.var_foccu.get()=="" or self.var_mname.get()== "" or self.var_moccu.get()==""or self.var_fno.get()=="" or self.var_mno.get()=="" or self.var_radio1.get()=="":
              messagebox.showerror("error","All fields are required",parent=self.root)
        else:
            try:
               con= pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=SRISHTI\SQLEXPRESS;'
                      'Database=archana;'
                      'Trusted_Connection=yes;')
               cursor1=con.cursor()
               cursor1.execute("insert into students values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(self.var_id.get(),self.var_name.get(),self.var_divs.get(),self.var_classes.get(),self.var_gens.get(),self.var_dob.get(),self.var_contact.get(),self.var_email.get(),self.var_add.get(),self.var_dept.get(),self.var_year.get(),self.var_sem.get(),self.var_pname.get(),self.var_foccu.get(),self.var_mname.get(),self.var_moccu.get(),self.var_fno.get(),self.var_mno.get(), self.var_radio1.get()))
               
               
               messagebox.showinfo("Success","Student details has been suceesfully added",parent=self.root) 
               con.commit()
               self.fetch_data()
               con.close()    
            except Exception as e:
                messagebox.showerror("error",f"Due to:{str(e)}",parent=self.root)
        ###########fetch data
    def fetch_data(self):
        con= pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=SRISHTI\SQLEXPRESS;'
                      'Database=archana;'
                      'Trusted_Connection=yes;')
        cursor1=con.cursor()
        cursor1.execute("select * from students")
        data=cursor1.fetchall()
        #data = data[0].strip("'")
        #print(data)
        if len(data)!=0:
            self.stu_table.delete(*self.stu_table.get_children())
            for i in data:
                i = [str(j).strip("'") for j in i]
                self.stu_table.insert("",END,values=i)
            con.commit()
            con.close()

            ###########get cursor
    def get_cursor(self,event=""):
                cur_focus=self.stu_table.focus()
                content=self.stu_table.item(cur_focus)
                Data=content["values"]
                self.var_id.set(Data[0])
                self.var_name.set(Data[1])
                self.var_divs.set(Data[2])
                self.var_classes.set(Data[3])
                self.var_gens.set(Data[4])
                self.var_dob.set(Data[5])
                self.var_contact.set(Data[6])
                self.var_email.set(Data[7])
                self.var_add.set(Data[8])
                self.var_dept.set(Data[9])
                self.var_year.set(Data[10])
                self.var_sem.set(Data[11])
                self.var_pname.set(Data[12])
                self.var_foccu.set(Data[13])
                self.var_mname.set(Data[14])
                self.var_moccu.set(Data[15])
                self.var_fno.set(Data[16])
                self.var_mno.set(Data[17])
                self.var_radio1.set(Data[18])
                ##########update
    def update_data(self):
        if self.var_id.get()=="" or self.var_name.get()=="" or self.var_divs.get()=="" or self.var_classes.get()=="" or self.var_gens.get()=="" or self.var_dob.get()=="" or self.var_contact.get()==""or self.var_email.get()==""or self.var_add.get()=="" or self.var_dept.get()=="" or  self.var_year.get()=="" or self.var_sem.get()=="" or self.var_pname.get()=="" or self.var_foccu.get()=="" or self.var_mname.get()== "" or self.var_moccu.get()==""or self.var_fno.get()=="" or self.var_mno.get()=="" or self.var_radio1.get()=="":
            messagebox.showerror("error","All fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update student details",parent=self.root)
                if update>0:
                    con= pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=SRISHTI\SQLEXPRESS;'
                      'Database=archana;'
                      'Trusted_Connection=yes;')
                    cursor1=con.cursor()
                    cursor1.execute("update students set name=?,div=?,class=?,gender=?,dob=?,contact=?,email=?,address=?,dept=?,year=?,sem=?,fname=?,foccu=?,mname=?,moccu=?,fno=?,mno=?,photo=? where id=?",(self.var_name.get(),self.var_divs.get(),self.var_classes.get(),self.var_gens.get(),self.var_dob.get(),self.var_contact.get(),self.var_email.get(),self.var_add.get(),self.var_dept.get(),self.var_year.get(),self.var_sem.get(),self.var_pname.get(),self.var_foccu.get(),self.var_mname.get(),self.var_moccu.get(),self.var_fno.get(),self.var_mno.get(),self.var_radio1.get(),self.var_id.get()
                                            ))
   
                else:
                    if not update:
                      return
                
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo("success","Student details successfully updated",parent=self.root)
            except Exception as es:
                 messagebox.showerror("error",f"Due to {str(es)}",parent=self.root) 

############delete
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("error","student id mmust be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("delete Page","Do you want to delete the student detail",parent=self.root)
                if delete>0:
                    con= pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=SRISHTI\SQLEXPRESS;'
                      'Database=archana;'
                      'Trusted_Connection=yes;')
                    cursor1=con.cursor()
                    sql="delete from students where id=?"
                    val=(self.var_id.get())
                    cursor1.execute(sql,val)
                else:
                    if not delete:
                        return
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo("success","Student details successfully deleted",parent=self.root)

            except Exception as es:
             messagebox.showerror("error",f"Due to {str(es)}",parent=self.root)

    def reset_data1(self):
                            self.var_id.set("")
                            self.var_name.set(""),
                            self.var_divs.set(""),
                            self.var_classes.set(""),
                            self.var_gens.set(""),
                            self.var_dob.set(""),
                            self.var_contact.set(""),
                            self.var_email.set(""),
                            self.var_add.set(""),
                            self.var_dept.set(""),
                            
                            self.var_year.set(""),
                            self.var_sem.set(""),
                            self.var_pname.set(""),
                            self.var_foccu.set(""),
                            self.var_mname.set(""),
                            self.var_moccu.set(""),
                            self.var_fno.set(""),
                            self.var_mno.set(""),
                            self.var_radio1.set("")


             ##############generate data set or take photo sample
    def generate_data(self):
        if self.var_id.get()=="":
            #or self.var_name.get()=="" or self.var_div.get()=="" or self.var_class.get()=="" or self.var_gen.get()=="" or self.var_dob.get()=="" or self.var_contact.get()==""or self.var_email.get()==""or self.var_add.get()=="" or self.var_dept.get()=="" or self.var_course.get()=="" or self.var_year.get()=="" or self.var_sem.get()=="" or self.var_sub.get()=="" or self.var_pname.get()=="" or self.var_foccu.get()=="" or self.var_mname.get()== "" or self.var_moccu.get()==""or self.var_fno.get()=="" or self.var_mno.get()=="" or self.var_radio1.get()=="":
            messagebox.showerror("error","All fields are required",parent=self.root)
        else:
            
                try:
                
                
                    con= pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=SRISHTI\SQLEXPRESS;'
                      'Database=archana;'
                      'Trusted_Connection=yes;')
                    cursor1=con.cursor()
                    cursor1.execute("select *from students")
                    result=cursor1.fetchall()
                    id=1
                    for i in result:
                        id+=1
                        cursor1.execute("update students set name=?,div=?,class=?,gender=?,dob=?,contact=?,email=?,address=?,dept=?,year=?,sem=?,fname=?,foccu=?,mname=?,moccu=?,fno=?,mno=?,photo=? where id=?",(
                            self.var_name.get(),
                            self.var_divs.get(),
                            self.var_classes.get(),
                            self.var_gens.get(),
                            self.var_dob.get(),
                            self.var_contact.get(),
                            self.var_email.get(),
                            self.var_add.get(),
                            self.var_dept.get(),
                            self.var_year.get(),
                            self.var_sem.get(),
                            
                            self.var_pname.get(),
                            self.var_foccu.get(),
                            self.var_mname.get(),
                            self.var_moccu.get(),
                            self.var_fno.get(),
                            self.var_mno.get(),
                            self.var_radio1.get(),
                            self.var_id.get()==id+1
                                            ))
                    con.commit()
                    self.fetch_data()
                    con.close()
                
                 ###################Load predefined face on frontals from opencv
                    face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                    def face_cropped(img):
                        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces=face_classifier.detectMultiScale(gray,1.3,5)  #Scaling factor=1.3 Medium neighbor=5
                        for (x,y,w,h) in faces:
                            face_cropped=img[y:y+h,x:x+w]
                            return face_cropped
            
                    cap=cv2.VideoCapture(0)
                    img_id=0
               # id=0
                    while True:
                        ret,myframe=cap.read()
                        if face_cropped(myframe) is not None:
                          img_id+=1
                          
                         # ids+=1
                          face=cv2.resize(face_cropped(myframe),(450,450))
                          face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                          file_paths="photo/archu."+str(id)+"."+str(img_id)+".jpg"
                          cv2.imwrite(file_paths,face)
                          cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,255),2)
                          cv2.imshow("Cropped face",face)
                          if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
                
                    cap.release()
                    cv2.destroyAllWindows()
                
              
                    messagebox.showinfo("result","Generating data sets completed",parent=self.root)
                except Exception as es:
                    messagebox.showerror("error",f"Due to {str(es)}",parent=self.root)
    



     ##########validation
                #id
    def id1(self,name):
        if name.isdigit():
               return True
        elif name=="":
               return True
                   
        else:
            messagebox.showwarning("alert","Only numbers are allowed")
            return False
        #name
    def usr_name1(self,name):
        if name.isalpha():
               return True
        elif name=="":
        
            return True
                   
        else:
            messagebox.showwarning("alert","only alphabets are allowed")
            return False
        
        #contact
    def contact1(self,con):
        if len(str(con))>10:
             messagebox.showwarning("alert","must be 10 digit")

        elif con.isdigit():
            return True
        elif len(str(con))==10:
            
            return True
        else :
              messagebox.showwarning("alert","Only 10 digits are allowed")
              return False
    
              
#Address
    def address1(self,add):
            
        if add=="":
            messagebox.showwarning("alert","This field is required")
        elif add.isalnum():
            return True
        else:
            messagebox.showwarning("alert","Special charcters are not allowed")
            return False
    #father name
    def f_name1(self,father_name):
        if father_name=="":
             messagebox.showwarning("alert","This field is reqiured")
        elif father_name.isalpha():
               return True
                
        else:
            messagebox.showwarning("alert", "Only alphabets are allowed")
            return False
    #father name
    def m_name1(self,mother_name):
        if mother_name=="":
             messagebox.showwarning("alert","This field is reqiured")
        elif mother_name.isalpha():
               return True
                
        else:
            messagebox.showwarning("alert", "Only alphabets are allowed")
            return False
    #father occupation
    def f_occu1(self,occu):
        if occu=="":
             messagebox.showwarning("alert","This field is reqiured")
        elif occu.isalpha():
               return True
                
        else:
            messagebox.showwarning("alert", "Only alphabets are allowed")
            return False
    #mother occupation
    def m_occu1(self,occu1):
        if occu1=="":
             messagebox.showwarning("alert","This field is reqiured")
        elif occu1.isalpha():
               return True
                
        else:
            messagebox.showwarning("alert", "Only alphabets are allowed")
            return False
    #f_contact
    def f_contact1(self,con1):
        if len(str(con1))>10:
             messagebox.showwarning("alert","must be 10 digit")

        elif con1.isdigit():
            return True
        elif len(str(con1))==10:
            
            return True
        else :
              messagebox.showwarning("alert","Only 10 digits are allowed")
              return False
    #m_contact
    def m_contact1(self,con2):
        if len(str(con2))>10:
             messagebox.showwarning("alert","must be 10 digit")

        elif con2.isdigit():
            return True
        elif len(str(con2))==10:
            
            return True
        else :
              messagebox.showwarning("alert","Only 10 digits are allowed")
              return False
    
    
                
               
        
                
               


























                      
                  




    
        












if __name__== "__main__" :
    root=Tk()
    log=stu_detail(root)
    root.mainloop()

