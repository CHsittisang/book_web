from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from account import *
from pathlib import Path
from tkinter import messagebox as msg
import tkinter as tk
from system import *
from account import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path("backend/src/img")



LARGE_FONT= ("Verdana", 12)


class Bookstore(tk.Tk):
    def __init__(self, *args ,**kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.geometry(self, "1440x924")
        tk.Tk.title(self, "Bookstore")
        tk.Tk.resizable(self, False, False)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        
        for F in {Mainpage, Loginpage, Registerpage, Cartpage ,MangaPage, NovelPage, AccountPage, Seriespage}:
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Mainpage)
        
        
    
    def show_frame(self, cont):
    
        frame = self.frames[cont]
        frame.tkraise()
        


class Mainpage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        self.canvas = Canvas(self, bg="#1895F5", height=110, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack()
        self.controller = controller

        self.showname = "Guest"
        self.TKshowname = StringVar()
        self.TKshowname.set(self.showname)
        
        self.Lable_main = Label(self, text=self.TKshowname.get(), bg="#1895F5", fg="white", font=("Inter", 16))
        self.Lable_main.place(x=1331, y=45)
        
        self.button_account_image = PhotoImage(file=ASSETS_PATH.joinpath("button_account.png"))
        self.button_account = Button(self, image=self.button_account_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(AccountPage) if len(server.customerlogin) == 1 else controller.show_frame(Loginpage),relief="flat")
        self.button_account.place(x=1207.0,y=30.0,width=56.0,height=56.0)
        
        self.button_manga_image = PhotoImage(
        file=ASSETS_PATH.joinpath("button_manga.png"))
        self.button_manga = Button(self, image=self.button_manga_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(MangaPage),relief="flat")
        self.button_manga.place(x=274, y=43)
        
        self.button_novel_image = PhotoImage(
        file=ASSETS_PATH.joinpath("button_novel.png"))
        self.button_novel = Button(self, image=self.button_novel_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(NovelPage),relief="flat")
        self.button_novel.place(x=408, y=43)
        
        
        self.button_cart_image = PhotoImage(
        file=ASSETS_PATH.joinpath("button_cart.png"))
        self.button_cart = Button(self,image=self.button_cart_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Cartpage),relief="flat")
        self.button_cart.place(x=1083.0, y=30.0, width=56.0, height=56.0)
        
        self.button_bookstore_image = PhotoImage(file=ASSETS_PATH.joinpath("button_Bookstore.png"))
        self.button_bookstore = Button(self, image=self.button_bookstore_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Mainpage),relief="flat")
        self.button_bookstore.place(x=22.0, y=30.0, width=218.0, height=54.0)
        
        self.button_serries1_image = PhotoImage(file=ASSETS_PATH.joinpath(serverseries.series[0].img))
        self.button_serries1 = Button(self, image=self.button_serries1_image, borderwidth=0, highlightthickness=0, relief="flat", command=lambda: [controller.show_frame(Seriespage), setattr(serverseries, 'current_series', 0)])
        self.button_serries1.place(x=126.0, y=663.0, width=149.0, height=149.0)
        
        self.label_serries1 = Label(self, text=serverseries.series[0].series_name, fg="Black", font=("Inter", 8))
        self.label_serries1.place(x=126.0, y=812.0, width=149.0, height=30.0)
        
        self.button_serries2_image = PhotoImage(file=ASSETS_PATH.joinpath(serverseries.series[1].img))
        self.button_serries2 = Button(self, image=self.button_serries2_image, borderwidth=0, highlightthickness=0, relief="flat", command=lambda: [controller.show_frame(Seriespage), setattr(serverseries, 'current_series', 1)])
        self.button_serries2.place(x=326.0, y=663.0, width=149.0, height=149.0)
        
        self.label_serries2 = Label(self, text=serverseries.series[1].series_name, fg="Black", font=("Inter", 8))
        self.label_serries2.place(x=326.0, y=812.0, width=149.0, height=30.0)
        
        self.button_serries3_image = PhotoImage(file=ASSETS_PATH.joinpath(serverseries.series[2].img))
        self.button_serries3 = Button(self, image=self.button_serries3_image,borderwidth=0,highlightthickness=0,command=lambda: [controller.show_frame(Seriespage), setattr(serverseries, 'current_series', 2)],relief="flat")
        self.button_serries3.place(x=526.0, y=663.0, width=149.0, height=149.0)
        
        self.label_serries3 = Label(self, text=serverseries.series[2].series_name, fg="Black", font=("Inter", 8))
        self.label_serries3.place(x=526.0, y=812.0, width=149.0, height=30.0)
        
        self.button_serries4_image = PhotoImage(file=ASSETS_PATH.joinpath(serverseries.series[3].img))
        self.button_serries4 = Button(self, image=self.button_serries4_image,borderwidth=0,highlightthickness=0,command=lambda: [controller.show_frame(Seriespage), setattr(serverseries, 'current_series', 3)],relief="flat")
        self.button_serries4.place(x=726.0, y=663.0, width=149.0, height=149.0)
        
        self.label_serries4 = Label(self, text=serverseries.series[3].series_name, fg="Black", font=("Inter", 8))
        self.label_serries4.place(x=726.0, y=812.0, width=149.0, height=30.0)
        
        self.button_serries5_image = PhotoImage(file=ASSETS_PATH.joinpath(serverseries.series[4].img))
        self.button_serries5 = Button(self, image=self.button_serries5_image,borderwidth=0,highlightthickness=0,command=lambda: [controller.show_frame(Seriespage), setattr(serverseries, 'current_series', 4)],relief="flat")
        self.button_serries5.place(x=926.0, y=663.0, width=149.0, height=149.0)
        
        self.label_serries5 = Label(self, text=serverseries.series[4].series_name, fg="Black", font=("Inter", 8))
        self.label_serries5.place(x=926.0, y=812.0, width=149.0, height=30.0)
        
        self.button_serries6_image = PhotoImage(file=ASSETS_PATH.joinpath(serverseries.series[5].img))
        self.button_serries6 = Button(self, image=self.button_serries6_image,borderwidth=0,highlightthickness=0,command=lambda: [controller.show_frame(Seriespage), setattr(serverseries, 'current_series', 5)],relief="flat")
        self.button_serries6.place(x=1126.0, y=663.0, width=149.0, height=149.0)
        
        self.label_serries6 = Label(self, text=serverseries.series[5].series_name, fg="Black", font=("Inter", 8))
        self.label_serries6.place(x=1126.0, y=812.0, width=149.0, height=30.0)
               
        image_files = ["bannermain1.png", "bannermain2.png", "bannermain3.png"]
        image_paths = [str(ASSETS_PATH.joinpath(file)) for file in image_files]
        self.images = [PhotoImage(file=path) for path in image_paths]
        self.canvas = Canvas(self, bg="#1895F5", height=423, width=2245, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=-404, y=158)
        self.current_image = 0
        self.image_item = self.canvas.create_image(0, 0, anchor="nw", image=self.images[self.current_image])
        self.after(10000, self.switch_image)
    
    def series_select(self):
        self.controller.show_frame(Seriespage)
        serverseries.current_series = 0


    def switch_image(self):
        self.current_image = (self.current_image + 1) % len(self.images)
        self.canvas.itemconfig(self.image_item, image=self.images[self.current_image])
        self.after(10000, self.switch_image)
    
    
        
class Loginpage(tk.Frame):
    
    count_account=0

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        
        
        self.canvas = Canvas(self, bg="#1895F5", height=110, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack()
        self.button_account_image = PhotoImage(file=ASSETS_PATH.joinpath("button_account.png"))
        self.button_account = Button(self, image=self.button_account_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(AccountPage) if len(server.customerlogin) == 1 else controller.show_frame(Loginpage),relief="flat")
        self.button_account.place(x=1207.0,y=30.0,width=56.0,height=56.0)
        
        self.button_manga_image = PhotoImage(file=ASSETS_PATH.joinpath("button_manga.png"))
        self.button_manga = Button(self, image=self.button_manga_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(MangaPage),relief="flat")
        self.button_manga.place(x=274, y=43)
        
        self.button_novel_image = PhotoImage(file=ASSETS_PATH.joinpath("button_novel.png"))
        self.button_novel = Button(self, image=self.button_novel_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(NovelPage),relief="flat")
        self.button_novel.place(x=408, y=43)
        
        
        self.button_cart_image = PhotoImage(file=ASSETS_PATH.joinpath("button_cart.png"))
        self.button_cart = Button(self,image=self.button_cart_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Cartpage),relief="flat")
        self.button_cart.place(x=1083.0, y=30.0, width=56.0, height=56.0)
        
        self.button_bookstore_image = PhotoImage(file=ASSETS_PATH.joinpath("button_Bookstore.png"))
        self.button_bookstore = Button(self, image=self.button_bookstore_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Mainpage),relief="flat")
        self.button_bookstore.place(x=22.0, y=30.0, width=218.0, height=54.0)
        
        self.canvas = Canvas(self, bg="#82C9FF", height=1000, width=811, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=1030, y=110)
        
        self.Lable_main = Label(self, text="Sign in Bookstore", bg="#82c9ff", fg="white", font=("Inter", 16))
        self.Lable_main.place(x=1047.0,y=153.0)
        self.textIdlogin = Label(self, text="ID" ,bg="#82c9ff", fg="#FFFFFF", font=("Inter", 12))
        self.textIdlogin.place(x=1049.0, y=200.0)
        self.textpasslogin = Label(self, text="Password" ,bg="#82c9ff", fg="#FFFFFF", font=("Inter", 12))
        self.textpasslogin.place(x=1047.0, y=290.0)
        
        
        self.entry_image_textfill = PhotoImage(file=ASSETS_PATH.joinpath("button_bookstore.png"))
        self.canvas.create_image(1237.0, 241.5, image=self.entry_image_textfill)
        self.entry_ID = Entry(self, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0 ,font=("Inter", 15)) 
        self.entry_ID.place(x=1064.0, y=230.0, width=346.0, height=35.0)
        
        self.entry_Password = Entry(self, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0 , show="·",font=("Inter", 40))
        self.entry_Password.place(x=1063.0, y=320.0, width=346.0, height=35.0)
        
        self.button_image_Signin = PhotoImage(file=ASSETS_PATH.joinpath("button_signin.png"))
        self.button_Signin = Button(self, image=self.button_image_Signin,borderwidth=0,highlightthickness=0,command=self.system_login,relief="flat")
        self.button_Signin.place(x=1188.0,y=380.0,width=97.0,height=33.0)

        self.canvas1 = Canvas(self, bg="#FEFCFF", height=2, width=348, bd=0, highlightthickness=0, relief="ridge")
        self.canvas1.place(x=1064, y=440)
        
        self.Lable_main = Label(self, text="Don't have an account?", bg="#82c9ff", fg="white", font=("Inter", 16))
        self.Lable_main.place(x=1120.0,y=480.0)
        
        self.button_image_signup = PhotoImage(file=ASSETS_PATH.joinpath("button_signup.png"))
        self.button_signup = Button(self, image=self.button_image_signup,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Registerpage),relief="flat")
        self.button_signup.place(x=1188.0,y=530.0,width=97.0,height=33.0)
            

        
    def system_login(self):
        self.id = self.entry_ID.get()
        self.password = self.entry_Password.get()
        self.entry_ID.delete(0,END)
        self.entry_Password.delete(0,END)
        print(server.customer)
        for i in server.customer:
            print(i)
            print(server.count_account)
            if i.id == self.id and i.password == self.password and i.status == False and i.id != "admin" and i.id != "Guest":
                print(server.customer[server.count_account].status)
                server.customer[server.count_account].status = True
                print(server.customer[server.count_account].status)
                print(server.count_account)
                msg.showinfo("Login", "Login Success")
                self.controller.show_frame(Mainpage)
                server.add_customerlogin(server.customer[server.count_account])
                break
            else:
                server.count_account += 1
        if server.count_account == len(server.customer):
            server.count_account = 0
            msg.showerror("Login", "Login Failed Plase try again")
            raise Exception("Login Failed")


class Registerpage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.controller = controller
        self.canvas = Canvas(self, bg="#1895F5", height=110, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack()
        
        

        self.button_account_image = PhotoImage(file=ASSETS_PATH.joinpath("button_account.png"))
        self.button_account = Button(self, image=self.button_account_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(AccountPage) if len(server.customerlogin) == 1 else controller.show_frame(Loginpage),relief="flat")
        self.button_account.place(x=1207.0,y=30.0,width=56.0,height=56.0)
        
        self.button_manga_image = PhotoImage(
        file=ASSETS_PATH.joinpath("button_manga.png"))
        self.button_manga = Button(self, image=self.button_manga_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(MangaPage),relief="flat")
        self.button_manga.place(x=274, y=43)
        
        self.button_novel_image = PhotoImage(
        file=ASSETS_PATH.joinpath("button_novel.png"))
        self.button_novel = Button(self, image=self.button_novel_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(NovelPage),relief="flat")
        self.button_novel.place(x=408, y=43)
        
        
        self.button_cart_image = PhotoImage(
        file=ASSETS_PATH.joinpath("button_cart.png"))
        self.button_cart = Button(self,image=self.button_cart_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Cartpage),relief="flat")
        self.button_cart.place(x=1083.0, y=30.0, width=56.0, height=56.0)
        
        self.button_bookstore_image = PhotoImage(file=ASSETS_PATH.joinpath("button_Bookstore.png"))
        self.button_bookstore = Button(self, image=self.button_bookstore_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Mainpage),relief="flat")
        self.button_bookstore.place(x=22.0, y=30.0, width=218.0, height=54.0)
        
        self.canvas = Canvas(self, bg="#82C9FF", height=1000, width=811, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=1030, y=110)
        
        self.Lable_main = Label(self, text="Sign up Bookstore", bg="#82c9ff", fg="white", font=("Inter", 16))
        self.Lable_main.place(x=1047.0,y=153.0)
        self.textId = Label(self, text="ID" ,bg="#82c9ff", fg="#FFFFFF", font=("Inter", 12))
        self.textId.place(x=1049.0, y=200.0)
        self.textpass = Label(self, text="Password" ,bg="#82c9ff", fg="#FFFFFF", font=("Inter", 12))
        self.textpass.place(x=1047.0, y=290.0)
        self.textname = Label(self, text="Name" ,bg="#82c9ff", fg="#FFFFFF", font=("Inter", 12))
        self.textname.place(x=1047.0, y=380.0)
        self.textemail = Label(self, text="Email" ,bg="#82c9ff", fg="#FFFFFF", font=("Inter", 12))
        self.textemail.place(x=1047.0, y=470.0)
        self.textphone = Label(self, text="Phone" ,bg="#82c9ff", fg="#FFFFFF", font=("Inter", 12))
        self.textphone.place(x=1047.0, y=560.0)
        self.textaddress = Label(self, text="Address" ,bg="#82c9ff", fg="#FFFFFF", font=("Inter", 12))
        self.textaddress.place(x=1047.0, y=650.0)
        

        self.entry_ID = Entry(self, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0 ,font=("Inter", 15)) 
        self.entry_ID.place(x=1064.0, y=230.0, width=346.0, height=35.0)
        
        self.entry_Password = Entry(self, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0 ,show="·",font=("Inter", 40))
        self.entry_Password.place(x=1064.0, y=320.0, width=346.0, height=35.0)
        
        self.entry_Name = Entry(self, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0 ,font=("Inter", 15))
        self.entry_Name.place(x=1064.0, y=410.0, width=346.0, height=35.0)
        
        self.entry_Email = Entry(self, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0 ,font=("Inter", 15))
        self.entry_Email.place(x=1064.0, y=500.0, width=346.0, height=35.0)
        
        self.entry_Phone = Entry(self, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0 ,font=("Inter", 15))
        self.entry_Phone.place(x=1064.0, y=590.0, width=346.0, height=35.0)
        
        self.entry_Address = Entry(self, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0 ,font=("Inter", 15))
        self.entry_Address.place(x=1064.0, y=680.0, width=346.0, height=35.0)
        
        self.button_image_signup = PhotoImage(file=ASSETS_PATH.joinpath("button_signup.png"))
        self.button_signup = Button(self, image=self.button_image_signup,borderwidth=0,highlightthickness=0,command=self.register,relief="flat")
        self.button_signup.place(x=1188.0,y=750.0,width=97.0,height=33.0)
        
    def register(self):
        self.id = self.entry_ID.get()
        self.password = self.entry_Password.get()
        self.name = self.entry_Name.get()
        self.email = self.entry_Email.get()
        self.phone = self.entry_Phone.get()
        self.address = self.entry_Address.get()
        if len(self.entry_ID.get()) == 0 or len(self.entry_Password.get()) == 0 or len(self.entry_Name.get()) == 0 or len(self.entry_Email.get()) == 0 or len(self.entry_Phone.get()) == 0 or len(self.entry_Address.get()) == 0:
            msg.showerror("Error", "Please fill in all fields")
            raise Exception("Please fill in all fields")
        else:
            for i in server.customer:
                if self.id == i.id:
                    self.entry_ID.delete(0, END)
                    self.entry_Password.delete(0, END)
                    msg.showerror("Error", "This ID is already in use")
                    raise Exception("This ID is already in use")
            print(server.customer)
        server.add_customer(Customer(self.id, self.password, self.name, self.email, self.phone, self.address))
        msg.showinfo("Success", "Register Success")
        self.controller.show_frame(Mainpage)
        print(server.customer[-1])
        

class Cartpage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.canvas = Canvas(self, bg="#1895F5", height=110, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack()
        

        self.button_account_image = PhotoImage(file=ASSETS_PATH.joinpath("button_account.png"))
        self.button_account = Button(self, image=self.button_account_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(AccountPage) if len(server.customerlogin) == 1 else controller.show_frame(Loginpage),relief="flat")
        self.button_account.place(x=1207.0,y=30.0,width=56.0,height=56.0)
        
        self.button_manga_image = PhotoImage(
        file=ASSETS_PATH.joinpath("button_manga.png"))
        self.button_manga = Button(self, image=self.button_manga_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(MangaPage),relief="flat")
        self.button_manga.place(x=274, y=43)
        
        self.button_novel_image = PhotoImage(
        file=ASSETS_PATH.joinpath("button_novel.png"))
        self.button_novel = Button(self, image=self.button_novel_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(NovelPage),relief="flat")
        self.button_novel.place(x=408, y=43)
        
        
        self.button_cart_image = PhotoImage(
        file=ASSETS_PATH.joinpath("button_cart.png"))
        self.button_cart = Button(self,image=self.button_cart_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Cartpage),relief="flat")
        self.button_cart.place(x=1083.0, y=30.0, width=56.0, height=56.0)
        
        self.button_bookstore_image = PhotoImage(file=ASSETS_PATH.joinpath("button_Bookstore.png"))
        self.button_bookstore = Button(self, image=self.button_bookstore_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Mainpage),relief="flat")
        self.button_bookstore.place(x=22.0, y=30.0, width=218.0, height=54.0)
        
        self.canvas = Canvas(self, bg="#82C9FF", height=1000, width=811, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=1030, y=110)
 

class MangaPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.canvas = Canvas(self, bg="#1895F5", height=110, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack()
        

        self.button_account_image = PhotoImage(file=ASSETS_PATH.joinpath("button_account.png"))
        self.button_account = Button(self, image=self.button_account_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(AccountPage) if len(server.customerlogin) == 1 else controller.show_frame(Loginpage),relief="flat")
        self.button_account.place(x=1207.0,y=30.0,width=56.0,height=56.0)
        
        self.button_manga_image = PhotoImage(
        file=ASSETS_PATH.joinpath("button_manga.png"))
        self.button_manga = Button(self, image=self.button_manga_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(MangaPage),relief="flat")
        self.button_manga.place(x=274, y=43)
        
        self.button_novel_image = PhotoImage(
        file=ASSETS_PATH.joinpath("button_novel.png"))
        self.button_novel = Button(self, image=self.button_novel_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(NovelPage),relief="flat")
        self.button_novel.place(x=408, y=43)
        
        
        self.button_cart_image = PhotoImage(
        file=ASSETS_PATH.joinpath("button_cart.png"))
        self.button_cart = Button(self,image=self.button_cart_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Cartpage),relief="flat")
        self.button_cart.place(x=1083.0, y=30.0, width=56.0, height=56.0)
        
        self.button_bookstore_image = PhotoImage(file=ASSETS_PATH.joinpath("button_Bookstore.png"))
        self.button_bookstore = Button(self, image=self.button_bookstore_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Mainpage),relief="flat")
        self.button_bookstore.place(x=22.0, y=30.0, width=218.0, height=54.0)
  

class NovelPage(tk.Frame):
    
    def __init__(self , parent, controller):
        tk.Frame.__init__(self, parent)
        self.canvas = Canvas(self, bg="#1895F5", height=110, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack()
        
        
        self.button_account_image = PhotoImage(file=ASSETS_PATH.joinpath("button_account.png"))
        self.button_account = Button(self, image=self.button_account_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(AccountPage) if len(server.customerlogin) == 1 else controller.show_frame(Loginpage),relief="flat")
        self.button_account.place(x=1207.0,y=30.0,width=56.0,height=56.0)
        
        self.button_manga_image = PhotoImage(
        file=ASSETS_PATH.joinpath("button_manga.png"))
        self.button_manga = Button(self, image=self.button_manga_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(MangaPage),relief="flat")
        self.button_manga.place(x=274, y=43)
        
        self.button_novel_image = PhotoImage(
        file=ASSETS_PATH.joinpath("button_novel.png"))
        self.button_novel = Button(self, image=self.button_novel_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(NovelPage),relief="flat")
        self.button_novel.place(x=408, y=43)
        
        
        self.button_cart_image = PhotoImage(
        file=ASSETS_PATH.joinpath("button_cart.png"))
        self.button_cart = Button(self,image=self.button_cart_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Cartpage),relief="flat")
        self.button_cart.place(x=1083.0, y=30.0, width=56.0, height=56.0)
        
        self.button_bookstore_image = PhotoImage(file=ASSETS_PATH.joinpath("button_Bookstore.png"))
        self.button_bookstore = Button(self, image=self.button_bookstore_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Mainpage),relief="flat")
        self.button_bookstore.place(x=22.0, y=30.0, width=218.0, height=54.0)
        
        self.book1_image = PhotoImage(file=ASSETS_PATH.joinpath("book1.png"))
        self.book1 = Button(self, image=self.book1_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Mainpage),relief="flat")
        self.book1.place(x=187.0, y=227.0, width=148.0, height=210.0)
        
        self.label_book1 = Label(self, text="Buta Koshaku ni Tensei Shitakara \nเล่ม 1 (LN)", fg="Black", font=("Inter", 10))
        self.label_book1.place(x=150.0, y=455.0, width=230.0, height=30.0)
        
        self.book1button_image = PhotoImage(file=ASSETS_PATH.joinpath("button_money250.png"))
        self.book1button = Button(self, image=self.book1button_image,borderwidth=0,highlightthickness=0,relief="flat")
        self.book1button.place(x=150.0, y=500.0, width=230.0, height=30.0)
        
        ############################################################
        self.book2_image = PhotoImage(file=ASSETS_PATH.joinpath("book2.png"))
        self.book2 = Button(self, image=self.book2_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Mainpage),relief="flat")
        self.book2.place(x=487.0, y=227.0, width=148.0, height=210.0)
        
        self.label_book2 = Label(self, text="Buta Koshaku ni Tensei Shitakara \nเล่ม 2 (LN)", fg="Black", font=("Inter", 10))
        self.label_book2.place(x=450.0, y=455.0, width=230.0, height=30.0)
        
        self.book2button_image = PhotoImage(file=ASSETS_PATH.joinpath("button_money250.png"))
        self.book2button = Button(self, image=self.book2button_image,borderwidth=0,highlightthickness=0,relief="flat")
        self.book2button.place(x=450.0, y=500.0, width=230.0, height=30.0)
        
        ############################################################
        self.book3_image = PhotoImage(file=ASSETS_PATH.joinpath("book3.png"))
        self.book3 = Button(self, image=self.book3_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Mainpage),relief="flat")
        self.book3.place(x=787.0, y=227.0, width=148.0, height=210.0)
        
        self.label_book3 = Label(self, text="Buta Koshaku ni Tensei Shitakara \nเล่ม 3 (LN)", fg="Black", font=("Inter", 10))
        self.label_book3.place(x=750.0, y=455.0, width=230.0, height=30.0)
        
        self.book3button_image = PhotoImage(file=ASSETS_PATH.joinpath("button_money250.png"))
        self.book3button = Button(self, image=self.book3button_image,borderwidth=0,highlightthickness=0,relief="flat")
        self.book3button.place(x=750.0, y=500.0, width=230.0, height=30.0)
        
        ############################################################
        self.book4_image = PhotoImage(file=ASSETS_PATH.joinpath("book4.png"))
        self.book4 = Button(self, image=self.book4_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Mainpage),relief="flat")
        self.book4.place(x=1087.0, y=227.0, width=148.0, height=210.0)
        
        self.label_book4 = Label(self, text="Buta Koshaku ni Tensei Shitakara \nเล่ม 4 (LN)", fg="Black", font=("Inter", 10))
        self.label_book4.place(x=1050.0, y=455.0, width=230.0, height=30.0)
        
        self.book4button_image = PhotoImage(file=ASSETS_PATH.joinpath("button_money250.png"))
        self.book4button = Button(self, image=self.book4button_image,borderwidth=0,highlightthickness=0,relief="flat")
        self.book4button.place(x=1050.0, y=500.0, width=230.0, height=30.0)
        
        ############################################################
        
        self.book5_image = PhotoImage(file=ASSETS_PATH.joinpath("book5.png"))
        self.book5 = Button(self, image=self.book5_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Mainpage),relief="flat")
        self.book5.place(x=187.0, y=557.0, width=148.0, height=210.0)
        
        self.label_book5 = Label(self, text="Buta Koshaku ni Tensei Shitakara \nเล่ม 5 (LN)", fg="Black", font=("Inter", 10))
        self.label_book5.place(x=150.0, y=785.0, width=230.0, height=30.0)
        
        self.book5button_image = PhotoImage(file=ASSETS_PATH.joinpath("button_money250.png"))
        self.book5button = Button(self, image=self.book5button_image,borderwidth=0,highlightthickness=0,relief="flat")
        self.book5button.place(x=150.0, y=830.0, width=230.0, height=30.0)
        
        ############################################################
        
        self.book6_image = PhotoImage(file=ASSETS_PATH.joinpath("book6.png"))
        self.book6 = Button(self, image=self.book6_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Mainpage),relief="flat")
        self.book6.place(x=487.0, y=557.0, width=148.0, height=210.0)
        
        self.label_book6 = Label(self, text="Buta Koshaku ni Tensei Shitakara \nเล่ม 6 (LN)", fg="Black", font=("Inter", 10))
        self.label_book6.place(x=450.0, y=785.0, width=230.0, height=30.0)
        
        self.book6button_image = PhotoImage(file=ASSETS_PATH.joinpath("button_money250.png"))
        self.book6button = Button(self, image=self.book6button_image,borderwidth=0,highlightthickness=0,relief="flat")
        self.book6button.place(x=450.0, y=830.0, width=230.0, height=30.0)
        
        ############################################################
        
        self.book7_image = PhotoImage(file=ASSETS_PATH.joinpath("book7.png"))
        self.book7 = Button(self, image=self.book7_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Mainpage),relief="flat")
        self.book7.place(x=787.0, y=557.0, width=148.0, height=210.0)
        
        self.label_book7 = Label(self, text="Buta Koshaku ni Tensei Shitakara \nเล่ม 7 (LN)", fg="Black", font=("Inter", 10))
        self.label_book7.place(x=750.0, y=785.0, width=230.0, height=30.0)
        
        self.book7button_image = PhotoImage(file=ASSETS_PATH.joinpath("button_money250.png"))
        self.book7button = Button(self, image=self.book7button_image,borderwidth=0,highlightthickness=0,relief="flat")
        self.book7button.place(x=750.0, y=830.0, width=230.0, height=30.0)
        
        ############################################################
        
        self.book8_image = PhotoImage(file=ASSETS_PATH.joinpath("book8.png"))
        self.book8 = Button(self, image=self.book8_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Mainpage),relief="flat")
        self.book8.place(x=1087.0, y=557.0, width=148.0, height=210.0)
        
        self.label_book8 = Label(self, text="Buta Koshaku ni Tensei Shitakara \nเล่ม 8 (LN)", fg="Black", font=("Inter", 10))
        self.label_book8.place(x=1050.0, y=785.0, width=230.0, height=30.0)
        
        self.book8button_image = PhotoImage(file=ASSETS_PATH.joinpath("button_money250.png"))
        self.book8button = Button(self, image=self.book8button_image,borderwidth=0,highlightthickness=0,relief="flat")
        self.book8button.place(x=1050.0, y=830.0, width=230.0, height=30.0)
  

class AccountPage(tk.Frame):
    
    def __init__(self , parent , controller):
        tk.Frame.__init__(self, parent)
        self.canvas = Canvas(self, bg="#1895F5", height=110, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack()
        self.controller = controller
        
        print("Account page" + str(server.count_account))
        self.TKuser_Id = StringVar()
        self.Tkuser_Name = StringVar()
        self.TKuser_Email = StringVar()
        self.TKuser_Phone = StringVar()
        self.TKuser_Address = StringVar()
        
        
        self.button_account_image = PhotoImage(file=ASSETS_PATH.joinpath("button_account.png"))
        self.button_account = Button(self, image=self.button_account_image,borderwidth=0,highlightthickness=0,command=lambda: [controller.show_frame(AccountPage) if len(server.customerlogin) == 1 else controller.show_frame(Loginpage) , self.update()],relief="flat")
        self.button_account.place(x=1207.0,y=30.0,width=56.0,height=56.0)
        
        self.button_manga_image = PhotoImage(file=ASSETS_PATH.joinpath("button_manga.png"))
        self.button_manga = Button(self, image=self.button_manga_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(MangaPage),relief="flat")
        self.button_manga.place(x=274, y=43)
        
        self.button_novel_image = PhotoImage(
        file=ASSETS_PATH.joinpath("button_novel.png"))
        self.button_novel = Button(self, image=self.button_novel_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(NovelPage) ,relief="flat")
        self.button_novel.place(x=408, y=43)
        
        
        self.button_cart_image = PhotoImage(
        file=ASSETS_PATH.joinpath("button_cart.png"))
        self.button_cart = Button(self,image=self.button_cart_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Cartpage),relief="flat")
        self.button_cart.place(x=1083.0, y=30.0, width=56.0, height=56.0)
        
        self.button_bookstore_image = PhotoImage(file=ASSETS_PATH.joinpath("button_Bookstore.png"))
        self.button_bookstore = Button(self, image=self.button_bookstore_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Mainpage),relief="flat")
        self.button_bookstore.place(x=22.0, y=30.0, width=218.0, height=54.0)
        
        self.canvas = Canvas(self, bg="#82C9FF", height=1000, width=811, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=1030, y=110)
        self.Accountinfo = StringVar()
        

        self.Accountinfo.set("AccountInfo  ")
        self.Lable_main = Label(self, text=self.Accountinfo.get(), bg="#82c9ff", fg="white", font=("Inter", 16))
        self.Lable_main.place(x=1047.0,y=153.0)
        
        self.Lable_ID = Label(self, text="ID  : " + self.TKuser_Id.get() , bg="#82c9ff", fg="white", font=("Inter", 16))
        self.Lable_ID.place(x=1047.0,y=203.0) 
        
        self.Lable_Name = Label(self, text="Name : " + self.Tkuser_Name.get(), bg="#82c9ff", fg="white", font=("Inter", 16))
        self.Lable_Name.place(x=1047.0,y=253.0)
        
        self.Lable_Email = Label(self, text="Email : " + self.TKuser_Email.get(), bg="#82c9ff", fg="white", font=("Inter", 16))
        self.Lable_Email.place(x=1047.0,y=303.0)
        
        self.Lable_Phone = Label(self, text="Phone : " + self.TKuser_Phone.get(), bg="#82c9ff", fg="white", font=("Inter", 16))
        self.Lable_Phone.place(x=1047.0,y=353.0)

        self.Lable_Address = Label(self, text="Address : " + self.TKuser_Address.get(), bg="#82c9ff", fg="white", font=("Inter", 16))
        self.Lable_Address.place(x=1047.0,y=403.0)
        
        self.canvas1 = Canvas(self, bg="#FEFCFF", height=2, width=348, bd=0, highlightthickness=0, relief="ridge")
        self.canvas1.place(x=1064, y=540)

        self.button_logout_image = PhotoImage(
        file=ASSETS_PATH.joinpath("button_logout.png"))
        self.button_logout = Button(self,image=self.button_logout_image,borderwidth=0,highlightthickness=0,command=self.logout ,relief="flat")
        self.button_logout.place(x=1185.0, y=553.0, width=96.0, height=34.0)

        

        self.after(1000, self.update)
        
    def logout(self):
        server.customer[server.count_account].status = False
        server.customerlogin.clear()
        self.controller.show_frame(Mainpage)
        server.count_account = 0

    def update(self):
        if len(server.customerlogin) == 1:
                self.id = server.customerlogin[0].id
                self.name = server.customerlogin[0].name
                self.email = server.customerlogin[0].email
                self.phone = server.customerlogin[0].phone
                self.address = server.customerlogin[0].address
                self.TKuser_Id.set(self.id)
                self.Tkuser_Name.set(self.name)
                self.TKuser_Email.set(self.email)
                self.TKuser_Phone.set(self.phone)
                self.TKuser_Address.set(self.address)
                self.Lable_ID.config(text="ID  : " + self.TKuser_Id.get())
                self.Lable_Name.config(text="Name : " + self.Tkuser_Name.get())
                self.Lable_Email.config(text="Email : " + self.TKuser_Email.get())
                self.Lable_Phone.config(text="Phone : " + self.TKuser_Phone.get())
                self.Lable_Address.config(text="Address : " + self.TKuser_Address.get())
        self.after(1000 , self.update)
            
            
class Seriespage(tk.Frame):
    
    def __init__(self , parent , controller):
        tk.Frame.__init__(self, parent)
        
        self.canvas = Canvas(self, bg="#1895F5", height=110, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack()
        
        self.button_account_image = PhotoImage(file=ASSETS_PATH.joinpath("button_account.png"))
        self.button_account = Button(self, image=self.button_account_image,borderwidth=0,highlightthickness=0,command=lambda: [controller.show_frame(AccountPage) if len(server.customerlogin) == 1 else controller.show_frame(Loginpage)],relief="flat")
        self.button_account.place(x=1207.0,y=30.0,width=56.0,height=56.0)
        
        self.button_manga_image = PhotoImage(
        file=ASSETS_PATH.joinpath("button_manga.png"))
        self.button_manga = Button(self, image=self.button_manga_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(MangaPage),relief="flat")
        self.button_manga.place(x=274, y=43)
        
        self.button_novel_image = PhotoImage(
        file=ASSETS_PATH.joinpath("button_novel.png"))
        self.button_novel = Button(self, image=self.button_novel_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(NovelPage) ,relief="flat")
        self.button_novel.place(x=408, y=43)
        
        
        self.button_cart_image = PhotoImage(
        file=ASSETS_PATH.joinpath("button_cart.png"))
        self.button_cart = Button(self,image=self.button_cart_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Cartpage),relief="flat")
        self.button_cart.place(x=1083.0, y=30.0, width=56.0, height=56.0)
        
        self.button_bookstore_image = PhotoImage(file=ASSETS_PATH.joinpath("button_Bookstore.png"))
        self.button_bookstore = Button(self, image=self.button_bookstore_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Mainpage),relief="flat")
        self.button_bookstore.place(x=22.0, y=30.0, width=218.0, height=54.0)
        
        self.canvasbanner = Canvas(self, bg="#1895F5", height=313, width=839, bd=0, highlightthickness=0, relief="ridge")
        self.canvasbanner.place(x=58, y=140)
        
        self.seriesbanner = PhotoImage(file=ASSETS_PATH.joinpath(serverseries.book_catalog_list[0].img))
        self.canvasbanner.create_image(0, 0, anchor=NW, image=self.seriesbanner)
        self.canvasbginfo = Canvas(self, bg="#FEFCFF", height=760, width=308, bd=0, highlightthickness=0, relief="ridge")
        self.canvasbginfo.place(x=1064, y=140)
        
        self.bginfo = PhotoImage(file=ASSETS_PATH.joinpath("bginfo.png"))
        self.canvasbginfo.create_image(0, 0, anchor=NW, image=self.bginfo)
        
        self.imageinfo = PhotoImage(file=ASSETS_PATH.joinpath(serverseries.book_list[0].img))
        self.canvasbginfo.create_image(154, 20, anchor=N, image=self.imageinfo)
        
        self.seriesname = Label(self, text=serverseries.series[0].series_name,bg="#FCFCFC" ,fg="#000000",font=("Angsana New", int(16.0)))
        self.seriesname.place(x=1070, y=486, width=300, height=40)
        
        self.seriestype = Label(self, text="รูปแบบ \t" + serverseries.book_catalog_list[0].type,bg="#FCFCFC", anchor=W ,fg="#000000",font=("Angsana New", int(16.0)))
        self.seriestype.place(x=1070, y=540, width=300, height=40)
        
        self.author = Label(self, text="ผู้แต่ง \t" + serverseries.series[0].author,bg="#FCFCFC", anchor=W ,fg="#000000",font=("Angsana New", int(16.0)))
        self.author.place(x=1070, y=594, width=300, height=40)
        
        self.release = Label(self, text="วันที่เผยแพร่ \t" + serverseries.book_catalog_list[0].releae_date,bg="#FCFCFC", anchor=W ,fg="#000000",font=("Angsana New", int(16.0)))
        self.release.place(x=1070, y=648, width=300, height=40)
        
        self.tag = Label(self, text="Tag \t" + serverseries.book_catalog_list[0].tag,bg="#FCFCFC" , anchor=W,fg="#000000",font=("Angsana New", int(16.0)))
        self.tag.place(x=1070, y=702, width=300, height=40)
        
        
        self.canvasdetail = Canvas(self, height=429, width=841, bd=0, highlightthickness=0, relief="ridge")
        self.canvasdetail.place(x=56, y=462)
        self.detail = PhotoImage(file=ASSETS_PATH.joinpath(serverseries.series[0].detail_series))
        self.canvasdetail_image = self.canvasdetail.create_image(0, 0, anchor=NW, image=self.detail)
        
        
        
        
        self.after(500, self.updateseries)
    def updateseries(self):
        print(serverseries.current_series)
        self.seriesname.config(text=serverseries.series[serverseries.current_series].series_name)
        self.author.config(text="ผู้แต่ง \t" + serverseries.series[serverseries.current_series].author)
        self.release.config(text="วันที่เผยแพร่ \t" + serverseries.book_catalog_list[serverseries.current_series].releae_date)
        self.tag.config(text="Tag \t" + serverseries.book_catalog_list[serverseries.current_series].tag)
        self.seriestype.config(text="รูปแบบ \t" + serverseries.book_catalog_list[serverseries.current_series].type)
        new_detail = PhotoImage(file=ASSETS_PATH.joinpath(serverseries.series[serverseries.current_series].detail_series))
        self.canvasdetail.itemconfig(self.canvasdetail_image, image=new_detail)
        self.detail = new_detail
        self.after(500, self.updateseries)


        
app = Bookstore()
app.mainloop()