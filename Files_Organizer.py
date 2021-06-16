from tkinter import*
from tkinter import ttk, filedialog, messagebox #for boxes, filedialoge gives a pop up in order to select the file in browser
import os,shutil

class Sorting_App:  #constructor
    def __init__(self,root):
        self.root=root #for initializing... coz we will configure it again
        self.root.title("FILES ORGANIZER | Developed by Piyush and Amar")
        self.root.geometry("1350x700+0+0")
        self.root.wm_iconbitmap('folder.ico')
        self.logo_icon=PhotoImage(file="images/folder.png")
        
      
        title = Label(self.root, image=self.logo_icon, compound=LEFT, padx=10, text="FILES ORGANIZER",font=("impact",40), bg="#023548", fg="white", anchor="w").place(x=0,y=0,relwidth=1)
    #=====section1==========
        self.var_foldername=StringVar()
        lbl_select_folder= Label(self.root,text="Select Folder", font=("times new roman",25)).place(x=50,y=100)
        txt_folder_name= Entry(self.root, textvariable=self.var_foldername, font=("times new roman",15), cursor="plus", state="readonly").place(x=250,y=100, width=600, height=40)
        btn_browse= Button(self.root, command=self.browse_function, text="Browse", font=("times new roman",22,"bold"), cursor="hand2", bg="#262626", fg="white", activebackground="#262626", activeforeground="white").place(x=900,y=97, height=45,width=150)
        hr= Label(self.root, bg="#023548",).place(x=50, y=170, height=2, width=1250)

    #======section2==========
    #======all extensions========
        self.image_extensions= ["Image Extensions",".png",".jpg",".jpeg",".JPG"]
        self.audio_extensions= ["Audio Extensions",".amr",".mp3"]
        self.video_extensions= ["Video Extensions",".mp4",".avi", ".mpeg4",".3gp"]
        self.document_extensions= ["Document Extensions", ".doc",".pdf",".xlsx",".ppt",".pptx",".zip",".rar",".txt",".PDF",".docx"]
        self.app_extensions= ["Application Extensions", ".exe",".apk"]

        self.folders = {
    
                'images':self.image_extensions,
                'audios':self.audio_extensions,
                'videos':self.video_extensions,
                'documents':self.document_extensions,
                'applications':self.app_extensions,
            }

        lbl_support_ext= Label(self.root,text="Various Supported Sections", font=("times new roman",25)).place(x=50,y=190)
        self.image_box= ttk.Combobox(self.root,state="readonly", values=self.image_extensions, font=("times new roman",15), justify=CENTER)
        self.image_box.place(x=50,y=240)
        self.image_box.current(0)

        self.audio_box= ttk.Combobox(self.root,state="readonly", values=self.audio_extensions, font=("times new roman",15), justify=CENTER)
        self.audio_box.place(x=300,y=240)
        self.audio_box.current(0)

        self.video_box= ttk.Combobox(self.root,state="readonly", values=self.video_extensions, font=("times new roman",15), justify=CENTER)
        self.video_box.place(x=550,y=240)
        self.video_box.current(0)

        self.document_box= ttk.Combobox(self.root,state="readonly", values=self.document_extensions, font=("times new roman",15), justify=CENTER)
        self.document_box.place(x=800,y=240)
        self.document_box.current(0)

        self.app_box= ttk.Combobox(self.root,state="readonly", values=self.app_extensions, font=("times new roman",15), justify=CENTER)
        self.app_box.place(x=1050,y=240)
        self.app_box.current(0)

    #========section3=======
    #========all image icon=========

        self.image_icon=PhotoImage(file="images/image1.png")
        self.audio_icon=PhotoImage(file="images/audio1.png")
        self.video_icon=PhotoImage(file="images/video1.png")
        self.document_icon=PhotoImage(file="images/document1.png")
        self.app_icon=PhotoImage(file="images/app1.png")
        self.other_icon=PhotoImage(file="images/other1.png")

        Frame1=Frame(self.root,bd=2,relief=RIDGE)
        Frame1.place(x=50, y=300, width=1250, height=300)
        self.lbl_total_files = Label(Frame1,text="Total Files ", font=("times new roman",20))
        self.lbl_total_files.place(x=10,y=10)

        self.lbl_total_image = Label(Frame1,text="",image=self.image_icon,compound=TOP, font=("times new roman",20))
        self.lbl_total_image.place(x=40,y=60,height=200, width=150)

        self.lbl_total_audio = Label(Frame1,text="",image=self.audio_icon,compound=TOP, font=("times new roman",20))
        self.lbl_total_audio.place(x=240,y=60,height=200, width=150)

        self.lbl_total_video = Label(Frame1,text="",image=self.video_icon,compound=TOP, font=("times new roman",20))
        self.lbl_total_video.place(x=440,y=60,height=200, width=150)

        self.lbl_total_document = Label(Frame1,text="",image=self.document_icon,compound=TOP, font=("times new roman",20))
        self.lbl_total_document.place(x=640,y=60,height=200, width=150)

        self.lbl_total_app = Label(Frame1,text="",image=self.app_icon,compound=TOP, font=("times new roman",20))
        self.lbl_total_app.place(x=840,y=60,height=200, width=150)

        self.lbl_total_other = Label(Frame1,text="",image=self.other_icon,compound=TOP, font=("times new roman",20))
        self.lbl_total_other.place(x=1050,y=60,height=200, width=150)

    #=====section4=========

        lbl_status= Label(self.root,text="Status ", font=("times new roman",25),fg="#023548").place(x=50,y=620)

        self.lbl_st_total= Label(self.root,text="", font=("times new roman",20),fg="blue")
        self.lbl_st_total.place(x=300,y=625)

        self.lbl_st_moved= Label(self.root,text="", font=("times new roman",20),fg="green")
        self.lbl_st_moved.place(x=475,y=625)

        self.lbl_st_left= Label(self.root,text="", font=("times new roman",20),fg="orange")
        self.lbl_st_left.place(x=675,y=625)

    #=====buttons=========

        self.btn_clear= Button(self.root,command=self.clear, text="Clear", bd=4, relief=RAISED, font=("times new roman",22,"bold"), cursor="hand2", bg="#607d8b", fg="white", activebackground="#607d8b", activeforeground="white")
        self.btn_clear.place(x=850,y=620, height=45,width=200)

        self.btn_start= Button(self.root,state=DISABLED, command=self.start_function, text="Start", bd=4, relief=RAISED, font=("times new roman",22,"bold"), cursor="hand2", bg="#ff5722", fg="white", activebackground="#ff5722", activeforeground="white")
        self.btn_start.place(x=1100,y=620, height=45,width=200)

        
    
        pass

    def Total_count(self):
        images=0
        audios=0
        videos=0
        documents=0
        applications=0
        others=0
        self.count=0
        cmbine_list=[]
        for i in self.all_files:
            if os.path.isfile(os.path.join(self.directory,i))==True:  #to check wether these are files only or not. not dealing with folder
                self.count += 1
                ext="."+i.split(".")[-1]
                for folder_name in self.folders.items():
                    for x in folder_name[1]:
                        cmbine_list.append(x)
                    if ext.lower() in folder_name[1] and folder_name[0]=="images":
                        images += 1
                    if ext.lower() in folder_name[1] and folder_name[0]=="audios":
                        audios += 1
                    if ext.lower() in folder_name[1] and folder_name[0]=="videos":
                        videos += 1
                    if ext.lower() in folder_name[1] and folder_name[0]=="documents":
                        documents += 1
                    if ext.lower() in folder_name[1] and folder_name[0]=="applications":
                        applications += 1
        
        #==== this is for calculating other files===
        for i in self.all_files:
            if os.path.isfile(os.path.join(self.directory,i))==True:
                ext="."+i.split(".")[-1]
                if ext.lower() not in cmbine_list:
                    others += 1

        self.lbl_total_image.config(text="Total Images\n"+str(images))
        self.lbl_total_audio.config(text="Total Audios\n"+str(audios))
        self.lbl_total_video.config(text="Total Videos\n"+str(videos))
        self.lbl_total_document.config(text="Total Doc.\n"+str(documents))
        self.lbl_total_app.config(text="Total Apps.\n"+str(applications))
        self.lbl_total_other.config(text="Total Others.\n"+str(others))
        self.lbl_total_files.config(text="Total Files :"+str(self.count))


    def browse_function(self):
        op=filedialog.askdirectory(title="Select folder for sorting")
        if op!=None:
            self.var_foldername.set(str(op))
            self.directory=self.var_foldername.get()
            self.other_name="others"
            self.rename_folder()
            self.all_files = os.listdir(self.directory)
            length = len(self.all_files)
            count =1
            self.Total_count()
            self.btn_start.config(state=NORMAL)

    def start_function(self):
        c=0
        if self.var_foldername.get()!="":
            self.btn_clear.config(state=DISABLED)
            for i in self.all_files:
                if os.path.isfile(os.path.join(self.directory,i))==True:  #to check wether these are files only or not
                    c+=1
                    self.create_move(i.split(".")[-1],i)
                    self.lbl_st_total.config(text="Total :"+str(self.count))
                    self.lbl_st_moved.config(text="Moved :"+str(c))
                    self.lbl_st_left.config(text="Left :"+str(self.count-c))

                    self.lbl_st_total.update()
                    self.lbl_st_moved.update()
                    self.lbl_st_left.update()
                    
            messagebox.showinfo("SUCCESS","All Files have been imported")
            self.btn_start.config(state=DISABLED)
            self.btn_clear.config(state=NORMAL)
        else:
            messagebox.showinfo("ERROR","Please select the folder")

    def clear(self):
        self.btn_start.config(state=DISABLED)
        self.var_foldername.set("")
        self.lbl_st_total.config(text="")
        self.lbl_st_moved.config(text="")
        self.lbl_st_left.config(text="")
        self.lbl_total_image.config(text="")
        self.lbl_total_audio.config(text="")
        self.lbl_total_video.config(text="")
        self.lbl_total_document.config(text="")
        self.lbl_total_app.config(text="")
        self.lbl_total_other.config(text="")
        self.lbl_total_files.config(text="Total Files ")

    

            
    
    def rename_folder(self):
        for folder in os.listdir(self.directory):
            if os.path.isdir(os.path.join(self.directory,folder))==True:
                os.rename(os.path.join(self.directory,folder),os.path.join(self.directory,folder.lower()))




    #######making of folder##########
    def create_move(self,ext,file_name):
        find = False
        for folder_name in self.folders:
            
            if "."+ext in self.folders[folder_name]:
                #print("found", folder_name) it extracts the key value of the following extensions
                if folder_name not in os.listdir(self.directory):
                    os.mkdir(os.path.join(self.directory,folder_name))
                shutil.move(os.path.join(self.directory,file_name),os.path.join(self.directory,folder_name))
                find = True
                break

        if find != True:
            if self.other_name not in os.listdir(self.directory):
                os.mkdir(os.path.join(self.directory,self.other_name))
            shutil.move(os.path.join(self.directory,file_name),os.path.join(self.directory,self.other_name))



root=Tk()
root.resizable(False,False)
obj = Sorting_App(root)  #calling constructor as an object
root.mainloop()