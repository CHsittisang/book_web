from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from account import *
from pathlib import Path
from tkinter import messagebox as msg
import tkinter as tk
from system import *
from account import *
from cart import *
from payment import *
import tkinter.ttk as ttk
from order import *
from discount import *

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
        
        for F in {Mainpage, Loginpage, Registerpage, Cartpage ,MangaPage, NovelPage, AccountPage, Seriespage, Paymentpage}:
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Cartpage)
        
        
    
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
        self.button_cart = Button(self,image=self.button_cart_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Cartpage)if len(server.customerlogin) == 1 else controller.show_frame(Loginpage),relief="flat")
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
        self.button_cart = Button(self,image=self.button_cart_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Cartpage)if len(server.customerlogin) == 1 else controller.show_frame(Loginpage),relief="flat")
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
        self.button_cart = Button(self,image=self.button_cart_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Cartpage)if len(server.customerlogin) == 1 else controller.show_frame(Loginpage),relief="flat")
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
        self.button_cart = Button(self,image=self.button_cart_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Cartpage)if len(server.customerlogin) == 1 else controller.show_frame(Loginpage),relief="flat")
        self.button_cart.place(x=1083.0, y=30.0, width=56.0, height=56.0)
        
        self.button_bookstore_image = PhotoImage(file=ASSETS_PATH.joinpath("button_Bookstore.png"))
        self.button_bookstore = Button(self, image=self.button_bookstore_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Mainpage),relief="flat")
        self.button_bookstore.place(x=22.0, y=30.0, width=218.0, height=54.0)
        
        self.canvascart = Canvas(self, bg="#82C9FF", height=703, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvascart.place(x=0, y=163)
        
        self.button_refresh_image = PhotoImage(file=ASSETS_PATH.joinpath("Refreshbutton.png"))
        self.button_refresh = Button(self, image=self.button_refresh_image,borderwidth=0,highlightthickness=0,relief="flat",command=self.show_cart)
        self.button_refresh.place(x=1371.0,y=180.0,width=31.0,height=31.0)
        
        self.canvascart.create_text(100, 30, text="รายการสินค้าในตระกล้า", fill="#000000", font=("Angsana New", 20))
        self.canvascart.create_text(900, 30, text="ข้อมูลการสั่งซื้อ", fill="#000000", font=("Angsana New", 20))
        
        
        self.button_cfbuy = Button(self, text="ยืนยันการสั่งซื้อ", bg="#1895F5", fg="white", font=("Angsana New", 10), command= self.check_Paymentprompay)
        self.button_cfbuy.place(x=1313, y=811 , width=100, height=50)
        
        self.button_PrompPay = Button(self, text="PrompPay", bg="#1895F5", fg="white", font=("Angsana New", 10), command=self.show_Paymentprompay)
        self.button_PrompPay.place(x=880, y=400 , width=100, height=30)
        
        self.button_CreditCard = Button(self, text="CreditCard", bg="#1895F5", fg="white", font=("Angsana New", 10), command=self.show_Paymentcreditcard)
        self.button_CreditCard.place(x=1100, y=400 , width=100, height=30)
        
        
        

        
            
        
        
    try:
        def show_cart(self):
            y = 250
            try:
                self.entry_code.destroy()
            except:
                pass
            for widget in self.winfo_children():
                if isinstance(widget, tk.Label):
                    widget.destroy()
            for i in cart.product_cart:
                self.itemcartname = Label(self, text=i.book_name, bg="#82C9FF" ,fg="#000000", font=("Angsana New", 20))
                self.itemcartname.place(x=40, y=y)
                self.itemcartprice = Label(self, text=f"{i.price} บาท", bg="#82C9FF", fg="#000000", font=("Angsana New", 20))
                self.itemcartprice.place(x=600  , y=y)
                sumprice =cart.get_cart_list_price()
                y += 30
            self.itemcartsumprice = Label(self, text=f"ราคารวม {sumprice:.2f} บาท", bg="#82C9FF", fg="#000000", font=("Angsana New", 20))
            self.itemcartsumprice.place(x=40  , y=y+30)
            self.infoshipment1 = Label(self, text=f"ชื่อผู้รับ \t: {server.customerlogin[0].name}" , bg="#82C9FF", fg="#000000", font=("Angsana New", 20))
            self.infoshipment1.place(x=880  , y=250)
            self.infoshipment2 = Label(self, text=f"เบอร์โทร \t: {server.customerlogin[0].phone}" , bg="#82C9FF", fg="#000000", font=("Angsana New", 20))
            self.infoshipment2.place(x=880  , y=280)
            self.infoshipment3 = Label(self, text=f"อีเมล \t: {server.customerlogin[0].email}" , bg="#82C9FF", fg="#000000", font=("Angsana New", 20))
            self.infoshipment3.place(x=880  , y=310)
            self.infoshipment4 = Label(self, text=f"ที่อยู่ \t: {server.customerlogin[0].address}" , bg="#82C9FF", fg="#000000", font=("Angsana New", 20))
            self.infoshipment4.place(x=880  , y=340)
    except print(0):
        pass 

        
        
            
    
    def show_Paymentprompay(self):
        print("show_Paymentprompay")
        try:
            self.label_creditcard.destroy()
            self.entry_creditcard.destroy()
            self.label_creditcardcvv.destroy()
            self.entry_creditcardcvv.destroy()
            self.label_creditcarddate.destroy()
            self.entry_creditcarddate.destroy()
            self.label_codecredit.destroy()
            self.entry_codecredit.destroy()
        except:
            pass
        self.button_CreditCard.configure(state="normal") # ปิดใช้งาน button_CreditCard
        self.button_PrompPay.configure(state="disabled")
        self.label_promppay = Label(self, text="PrompPay", bg="#82C9FF", fg="#000000", font=("Angsana New", 20))
        self.label_promppay.place(x=880  , y=450)
        self.entry_promppay = Entry(self,bg="#FFFFFF", fg="#000000", font=("Angsana New", 20))
        self.entry_promppay.place(x=880  , y=500 , width=250.0, height=35.0)
        self.label_codepromppay = Label(self, text="รหัสส่วนลด", bg="#82C9FF", fg="#000000", font=("Angsana New", 20))
        self.label_codepromppay.place(x=880  , y=550)
        self.entry_codepromppay = Entry(self, bg="#FFFFFF", fg="#000000", font=("Angsana New", 20))
        self.entry_codepromppay.place(x=880  , y=600 , width=250.0, height=35.0)
        # self.button_comfrim_promppay = Button(self, text="ยืนยัน", bg="#1895F5", fg="white", font=("Angsana New", 10),command=self.check_Paymentprompay)
        # self.button_comfrim_promppay.place(x=880, y=550 , width=100, height=30)

        
        
        
    def show_Paymentcreditcard(self):
        print("show_Paymentcreditcard")
        try:
            self.label_promppay.destroy()
            self.entry_promppay.destroy()
            self.label_codepromppay.destroy()
            self.entry_codepromppay.destroy()
        except:
            pass
        self.button_PrompPay.configure(state="normal")  # ปิดใช้งาน button_PrompPay
        self.button_CreditCard.configure(state="disabled")
        self.label_creditcard = Label(self, text="CreditCard", bg="#82C9FF", fg="#000000", font=("Angsana New", 20))
        self.label_creditcard.place(x=880  , y=450)
        self.entry_creditcard = Entry(self,bg="#FFFFFF", fg="#000000", font=("Angsana New", 20))
        self.entry_creditcard.place(x=880  , y=500 , width=250.0, height=35.0)
        self.label_creditcardcvv = Label(self, text="CVV", bg="#82C9FF", fg="#000000", font=("Angsana New", 20))
        self.label_creditcardcvv.place(x=1200  , y=450)
        self.entry_creditcardcvv = Entry(self,bg="#FFFFFF", fg="#000000", font=("Angsana New", 20))
        self.entry_creditcardcvv.place(x=1200  , y=500 , width=50.0, height=35.0)
        self.label_creditcarddate = Label(self, text="วันหมดอายุ Ex 1/01/1999", bg="#82C9FF", fg="#000000", font=("Angsana New", 20))
        self.label_creditcarddate.place(x=880  , y=550)
        self.entry_creditcarddate = Entry(self,bg="#FFFFFF", fg="#000000", font=("Angsana New", 20))
        self.entry_creditcarddate.place(x=880  , y=600 , width=250.0, height=35.0)
        self.label_codecredit = Label(self, text="รหัสส่วนลด", bg="#82C9FF", fg="#000000", font=("Angsana New", 20))
        self.label_codecredit.place(x=880  , y=650)
        self.entry_codecredit = Entry(self, bg="#FFFFFF", fg="#000000", font=("Angsana New", 20))
        self.entry_codecredit.place(x=880  , y=700 , width=250.0, height=35.0)
        
    def check_Paymentprompay(self):
        prompayget = self.entry_promppay.get()
        codediscountget = self.entry_codepromppay.get()
        sumprice =cart.get_cart_list_price()
        if prompayget == "":
            msg.showerror("Error", "กรุณากรอกข้อมูลให้ครบถ้วน")
            raise Exception("กรุณากรอกข้อมูลให้ครบถ้วน")
        for i in discount.code_list:
            if codediscountget == i.discount_code:
                sumprice = sumprice - i.balance
                print(sumprice)
            else:
                msg.showerror("Error", "กรุณากรอกข้อมูลให้ถูกต้อง")
                raise Exception("กรุณากรอกข้อมูลให้ถูกต้อง")
        for i in PrompPay.PrompPay_list:
            if prompayget == i.tel_number:
                if i.payment_balance >= sumprice:
                    PrompPay.PrompPay_list[PrompPay.PrompPay_list.index(i)].payment_balance -= sumprice
                    print(i.payment_balance)
                    msg.showinfo("Success", "ชำระเงินสำเร็จ")
                else:
                    msg.showerror("Error", "ชำระเงินไม่สำเร็จยอดเงินของคุณไม่พอเพียงพอ")
            else:
                msg.showerror("Error", "กรุณากรอกข้อมูลให้ถูกต้อง")
                raise Exception("กรุณากรอกข้อมูลให้ถูกต้อง")
            
    def check_Paymentcreditcard(self):
        creditcardget = self.entry_creditcard.get()
        creditcardcvvget = self.entry_creditcardcvv.get()
        creditcarddateget = self.entry_creditcarddate.get()
        if creditcardget == "" or creditcardcvvget == "" or creditcarddateget == "":
            msg.showerror("Error", "กรุณากรอกข้อมูลให้ครบถ้วน")
            raise Exception("กรุณากรอกข้อมูลให้ครบถ้วน")
        for i in CreditCard.CreditCard_list:
            if creditcardget == i.card_number and creditcardcvvget == i.card_cvv and creditcarddateget == i.card_date:
                if i.payment_balance >= sumprice:
                    CreditCard.CreditCard_list[CreditCard.CreditCard_list.index(i)].payment_balance -= sumprice
                    msg.showinfo("Success", "ชำระเงินสำเร็จ")
                else:
                    msg.showerror("Error", "ชำระเงินไม่สำเร็จยอดเงินของคุณไม่พอเพียงพอ")
    
    
        



class Paymentpage(tk.Frame):
    
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
        self.button_cart = Button(self,image=self.button_cart_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Cartpage)if len(server.customerlogin) == 1 else controller.show_frame(Loginpage),relief="flat")
        self.button_cart.place(x=1083.0, y=30.0, width=56.0, height=56.0)
        
        self.button_bookstore_image = PhotoImage(file=ASSETS_PATH.joinpath("button_Bookstore.png"))
        self.button_bookstore = Button(self, image=self.button_bookstore_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Mainpage),relief="flat")
        self.button_bookstore.place(x=22.0, y=30.0, width=218.0, height=54.0)
        
        self.canvascart = Canvas(self, bg="#82C9FF", height=703, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvascart.place(x=0, y=163)
        
    
        
 
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
        self.button_cart = Button(self,image=self.button_cart_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Cartpage)if len(server.customerlogin) == 1 else controller.show_frame(Loginpage),relief="flat")
        self.button_cart.place(x=1083.0, y=30.0, width=56.0, height=56.0)
        
        self.button_bookstore_image = PhotoImage(file=ASSETS_PATH.joinpath("button_Bookstore.png"))
        self.button_bookstore = Button(self, image=self.button_bookstore_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Mainpage),relief="flat")
        self.button_bookstore.place(x=22.0, y=30.0, width=218.0, height=54.0)

        self.bookmg1_image = PhotoImage(file=ASSETS_PATH.joinpath(serverseries.book_list[6].img))
        self.bookmg1_resize = self.bookmg1_image.subsample(2)
        self.bookmg1 = Button(self, image=self.bookmg1_resize, borderwidth=0, highlightthickness=0,relief="flat")
        self.bookmg1.place(x=187.0, y=227.0, width=150.0, height=210.0)
        
        self.label_bookmg1 = Label(self, text=f"{serverseries.book_list[6].book_name}", fg="#FFffff", font=("Inter", 10))
        self.label_bookmg1.place(x=150.0, y=455.0, width=230.0, height=30.0)
        
        self.button_buymg1 = Button(self, text=f"ซื้อ {serverseries.book_list[6].price} บาท", bg="#1895F5", fg="white" , command=lambda: cart.add_to_cart_list(serverseries.book_list[6]))
        self.button_buymg1.place(x=150.0, y=500.0, width=230.0, height=30.0)
        
        self.bookmg2_image = PhotoImage(file=ASSETS_PATH.joinpath(serverseries.book_list[7].img))
        self.bookmg2_resize = self.bookmg2_image.subsample(2)
        self.bookmg2 = Button(self, image=self.bookmg2_resize, borderwidth=0, highlightthickness=0,relief="flat")
        self.bookmg2.place(x=487.0, y=227.0, width=150.0, height=210.0)
        self.label_bookmg2 = Label(self, text=f"{serverseries.book_list[7].book_name}", fg="#000000", font=("Inter", 10))
        self.label_bookmg2.place(x=450.0, y=455.0, width=230.0, height=30.0)
        self.button_buymg2 = Button(self, text=f"ซื้อ {serverseries.book_list[7].price} บาท", bg="#1895F5", fg="white" , command=lambda: cart.add_to_cart_list(serverseries.book_list[7]))
        self.button_buymg2.place(x=450.0, y=500.0, width=230.0, height=30.0)
        
        self.bookmg3_image = PhotoImage(file=ASSETS_PATH.joinpath(serverseries.book_list[8].img))
        self.bookmg3_resize = self.bookmg3_image.subsample(2)
        self.bookmg3 = Button(self, image=self.bookmg3_resize, borderwidth=0, highlightthickness=0,relief="flat")
        self.bookmg3.place(x=787.0, y=227.0, width=150.0, height=210.0)
        self.label_bookmg3 = Label(self, text=f"{serverseries.book_list[8].book_name}", fg="#000000", font=("Inter", 10))
        self.label_bookmg3.place(x=750.0, y=455.0, width=230.0, height=30.0)
        self.button_buymg3 = Button(self, text=f"ซื้อ {serverseries.book_list[8].price} บาท", bg="#1895F5", fg="white" , command=lambda: cart.add_to_cart_list(serverseries.book_list[8]))
        self.button_buymg3.place(x=750.0, y=500.0, width=230.0, height=30.0)
        
        self.bookmg4_image = PhotoImage(file=ASSETS_PATH.joinpath(serverseries.book_list[9].img))
        self.bookmg4_resize = self.bookmg4_image.subsample(2)
        self.bookmg4 = Button(self, image=self.bookmg4_resize, borderwidth=0, highlightthickness=0,relief="flat")
        self.bookmg4.place(x=1087.0, y=227.0, width=150.0, height=210.0)
        self.label_bookmg4 = Label(self, text=f"{serverseries.book_list[9].book_name}", fg="#000000", font=("Inter", 10))
        self.label_bookmg4.place(x=1050.0, y=455.0, width=230.0, height=30.0)
        self.button_buymg4 = Button(self, text=f"ซื้อ {serverseries.book_list[9].price} บาท", bg="#1895F5", fg="white" , command=lambda: cart.add_to_cart_list(serverseries.book_list[9]))
        self.button_buymg4.place(x=1050.0, y=500.0, width=230.0, height=30.0)
        
        self.bookmg5_image = PhotoImage(file=ASSETS_PATH.joinpath(serverseries.book_list[10].img))
        self.bookmg5_resize = self.bookmg5_image.subsample(2)
        self.bookmg5 = Button(self, image=self.bookmg5_resize, borderwidth=0, highlightthickness=0,relief="flat")
        self.bookmg5.place(x=187.0, y=557.0, width=150.0, height=210.0)
        self.label_bookmg5 = Label(self, text=f"{serverseries.book_list[10].book_name}", fg="#000000", font=("Inter", 10))
        self.label_bookmg5.place(x=150.0, y=785.0, width=230.0, height=30.0)
        self.button_buymg5 = Button(self, text=f"ซื้อ {serverseries.book_list[10].price} บาท", bg="#1895F5", fg="white" , command=lambda: cart.add_to_cart_list(serverseries.book_list[10]))
        self.button_buymg5.place(x=150.0, y=830.0, width=230.0, height=30.0)
        
        self.bookmg6_image = PhotoImage(file=ASSETS_PATH.joinpath(serverseries.book_list[11].img))
        self.bookmg6_resize = self.bookmg6_image.subsample(2)
        self.bookmg6 = Button(self, image=self.bookmg6_resize, borderwidth=0, highlightthickness=0,relief="flat")
        self.bookmg6.place(x=487.0, y=557.0, width=150.0, height=210.0)
        self.label_bookmg6 = Label(self, text=f"{serverseries.book_list[11].book_name}", fg="#000000", font=("Inter", 10))
        self.label_bookmg6.place(x=450.0, y=785.0, width=230.0, height=30.0)
        self.button_buymg6 = Button(self, text=f"ซื้อ {serverseries.book_list[11].price} บาท", bg="#1895F5", fg="white" , command=lambda: cart.add_to_cart_list(serverseries.book_list[11]))
        self.button_buymg6.place(x=450.0, y=830.0, width=230.0, height=30.0)
        
        self.bookmg7_image = PhotoImage(file=ASSETS_PATH.joinpath(serverseries.book_list[12].img))
        self.bookmg7_resize = self.bookmg7_image.subsample(2)
        self.bookmg7 = Button(self, image=self.bookmg7_resize, borderwidth=0, highlightthickness=0,relief="flat")
        self.bookmg7.place(x=787.0, y=557.0, width=150.0, height=210.0)
        self.label_bookmg7 = Label(self, text=f"{serverseries.book_list[12].book_name}", fg="#000000", font=("Inter", 10))
        self.label_bookmg7.place(x=750.0, y=785.0, width=230.0, height=30.0)
        self.button_buymg7 = Button(self, text=f"ซื้อ {serverseries.book_list[12].price} บาท", bg="#1895F5", fg="white" , command=lambda: cart.add_to_cart_list(serverseries.book_list[12]))
        self.button_buymg7.place(x=750.0, y=830.0, width=230.0, height=30.0)
        
        self.bookmg8_image = PhotoImage(file=ASSETS_PATH.joinpath(serverseries.book_list[13].img))
        self.bookmg8_resize = self.bookmg8_image.subsample(2)
        self.bookmg8 = Button(self, image=self.bookmg8_resize, borderwidth=0, highlightthickness=0,relief="flat")
        self.bookmg8.place(x=1087.0, y=557.0, width=150.0, height=210.0)
        self.label_bookmg8 = Label(self, text=f"{serverseries.book_list[13].book_name}", fg="#000000", font=("Inter", 10))
        self.label_bookmg8.place(x=1050.0, y=785.0, width=230.0, height=30.0)
        self.button_buymg8 = Button(self, text=f"ซื้อ {serverseries.book_list[13].price} บาท", bg="#1895F5", fg="white" , command=lambda: cart.add_to_cart_list(serverseries.book_list[13]))
        self.button_buymg8.place(x=1050.0, y=830.0, width=230.0, height=30.0)

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
        self.button_cart = Button(self,image=self.button_cart_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Cartpage) if len(server.customerlogin) == 1 else controller.show_frame(Loginpage),relief="flat")
        self.button_cart.place(x=1083.0, y=30.0, width=56.0, height=56.0)
        
        self.button_bookstore_image = PhotoImage(file=ASSETS_PATH.joinpath("button_Bookstore.png"))
        self.button_bookstore = Button(self, image=self.button_bookstore_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Mainpage),relief="flat")
        self.button_bookstore.place(x=22.0, y=30.0, width=218.0, height=54.0)
        
        self.book1_image = PhotoImage(file=ASSETS_PATH.joinpath(serverseries.book_list[0].img))
        self.book1_resize = self.book1_image.subsample(2)
        self.book1 = Button(self, image=self.book1_resize,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Mainpage),relief="flat")
        self.book1.place(x=187.0, y=227.0, width=150.0, height=210.0)
        
        self.label_book1 = Label(self, text=serverseries.book_list[0].book_name, fg="Black", font=("Inter", 10))
        self.label_book1.place(x=150.0, y=455.0, width=230.0, height=30.0)
          
        self.button_buy1 = Button(self, text=f"ซื้อ {serverseries.book_list[0].price} บาท", bg="#1895F5", fg="white" , command=lambda: cart.add_to_cart_list(serverseries.book_list[0]))
        self.button_buy1.place(x=150 , y=500 , width=230 , height=30)
        
        ############################################################
        self.book2_image = PhotoImage(file=ASSETS_PATH.joinpath(serverseries.book_list[1].img))
        self.book2_resize = self.book2_image.subsample(2)
        self.book2 = Button(self, image=self.book2_resize,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Mainpage),relief="flat")
        self.book2.place(x=487.0, y=227.0, width=148.0, height=210.0)
        
        self.label_book2 = Label(self, text=serverseries.book_list[1].book_name, fg="Black", font=("Inter", 10))
        self.label_book2.place(x=450.0, y=455.0, width=230.0, height=30.0)
        
        self.button_buy2 = Button(self, text=f"ซื้อ {serverseries.book_list[1].price} บาท", bg="#1895F5", fg="white" , command=lambda: cart.add_to_cart_list(serverseries.book_list[1]))
        self.button_buy2.place(x=450 , y=500 , width=230 , height=30)
        
        ############################################################
        self.book3_image = PhotoImage(file=ASSETS_PATH.joinpath(serverseries.book_list[2].img))
        self.book3_resize = self.book3_image.subsample(2)
        self.book3 = Button(self, image=self.book3_resize,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Mainpage),relief="flat")
        self.book3.place(x=787.0, y=227.0, width=148.0, height=210.0)
        
        self.label_book3 = Label(self, text=serverseries.book_list[2].book_name, fg="Black", font=("Inter", 10))
        self.label_book3.place(x=750.0, y=455.0, width=230.0, height=30.0)
        
        self.button_buy3 = Button(self, text=f"ซื้อ {serverseries.book_list[2].price} บาท", bg="#1895F5", fg="white" , command=lambda: cart.add_to_cart_list(serverseries.book_list[2]))
        self.button_buy3.place(x=750.0, y=500.0, width=230.0, height=30.0)
        
        ############################################################
        self.book4_image = PhotoImage(file=ASSETS_PATH.joinpath(serverseries.book_list[3].img))
        self.book4_resize = self.book4_image.subsample(2)
        self.book4 = Button(self, image=self.book4_resize,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Mainpage),relief="flat")
        self.book4.place(x=1087.0, y=227.0, width=148.0, height=210.0)
        
        self.label_book4 = Label(self, text=serverseries.book_list[3].book_name, fg="Black", font=("Inter", 10))
        self.label_book4.place(x=1050.0, y=455.0, width=230.0, height=30.0)
        
        self.button_buy4 = Button(self, text=f"ซื้อ {serverseries.book_list[3].price} บาท", bg="#1895F5", fg="white" , command=lambda: cart.add_to_cart_list(serverseries.book_list[3]))
        self.button_buy4.place(x=1050.0, y=500.0, width=230.0, height=30.0)
        
        ############################################################
        
        self.book5_image = PhotoImage(file=ASSETS_PATH.joinpath(serverseries.book_list[4].img))
        self.book5_resize = self.book5_image.subsample(2)
        self.book5 = Button(self, image=self.book5_resize,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Mainpage),relief="flat")
        self.book5.place(x=187.0, y=557.0, width=148.0, height=210.0)
        
        self.label_book5 = Label(self, text=serverseries.book_list[4].book_name, fg="Black", font=("Inter", 10))
        self.label_book5.place(x=150.0, y=785.0, width=230.0, height=30.0)
        
        self.button_buy5 = Button(self, text=f"ซื้อ {serverseries.book_list[4].price} บาท", bg="#1895F5", fg="white" , command=lambda: cart.add_to_cart_list(serverseries.book_list[4]))
        self.button_buy5.place(x=150.0, y=830.0, width=230.0, height=30.0)
        
        ############################################################
        
        self.book6_image = PhotoImage(file=ASSETS_PATH.joinpath(serverseries.book_list[5].img))
        self.book6_resize = self.book6_image.subsample(2)
        self.book6 = Button(self, image=self.book6_resize,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Mainpage),relief="flat")
        self.book6.place(x=487.0, y=557.0, width=148.0, height=210.0)
        
        self.label_book6 = Label(self, text=serverseries.book_list[5].book_name, fg="Black", font=("Inter", 10))
        self.label_book6.place(x=450.0, y=785.0, width=230.0, height=30.0)
        
        self.button_buy6 = Button(self, text=f"ซื้อ {serverseries.book_list[5].price} บาท", bg="#1895F5", fg="white" , command=lambda: cart.add_to_cart_list(serverseries.book_list[5]))
        self.button_buy6.place(x=450.0, y=830.0, width=230.0, height=30.0)
        
        ############################################################
        

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
        self.canvas_image = self.canvasbanner.create_image(0, 0, anchor=NW, image=self.seriesbanner)
        
        
        self.canvasbginfo = Canvas(self, bg="#FEFCFF", height=760, width=308, bd=0, highlightthickness=0, relief="ridge")
        self.canvasbginfo.place(x=1064, y=140)
        
        self.bginfo = PhotoImage(file=ASSETS_PATH.joinpath("bginfo.png"))
        self.canvasbginfo.create_image(0, 0, anchor=NW, image=self.bginfo)
        
        self.imageinfo = PhotoImage(file=ASSETS_PATH.joinpath(serverseries.book_list[0].img))
        self.canvasimageinfo = self.canvasbginfo.create_image(154, 20, anchor=N, image=self.imageinfo)
        
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
        self.seriesname.config(text=serverseries.series[serverseries.current_series].series_name)
        self.author.config(text="ผู้แต่ง \t" + serverseries.series[serverseries.current_series].author)
        self.release.config(text="วันที่เผยแพร่ \t" + serverseries.book_catalog_list[serverseries.current_series].releae_date)
        self.tag.config(text="Tag \t" + serverseries.book_catalog_list[serverseries.current_series].tag)
        self.seriestype.config(text="รูปแบบ \t" + serverseries.book_catalog_list[serverseries.current_series].type)
        
        new_imginfo = PhotoImage(file=ASSETS_PATH.joinpath(serverseries.book_list[serverseries.current_series].img))
        self.canvasbginfo.itemconfig(self.canvasimageinfo, image=new_imginfo)
        self.imginfo = new_imginfo
        
        new_banner = PhotoImage(file=ASSETS_PATH.joinpath(serverseries.book_catalog_list[serverseries.current_series].img))
        self.canvasbanner.itemconfig(self.canvas_image, image=new_banner)
        self.seriesbanner = new_banner
        
        new_detail = PhotoImage(file=ASSETS_PATH.joinpath(serverseries.series[serverseries.current_series].detail_series))
        self.canvasdetail.itemconfig(self.canvasdetail_image, image=new_detail)
        self.detail = new_detail
        self.after(500, self.updateseries)


        
app = Bookstore()
app.mainloop()