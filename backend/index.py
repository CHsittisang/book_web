from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from account import *
from pathlib import Path
from tkinter import messagebox as msg
import tkinter as tk
from system import *
from account import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\Desktop\Project TKver\backend\src\img")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

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
        
        for F in {Mainpage, Loginpage, Registerpage, Cartpage ,MangaPage, NovelPage, AccountPage}:
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
        use_count_account = Loginpage.get_count_account(self)

        self.showname = "Guest"
        self.TKshowname = StringVar()
        self.TKshowname.set(self.showname)
        
        self.Lable_main = Label(self, text=self.TKshowname.get(), bg="#1895F5", fg="white", font=("Inter", 16))
        self.Lable_main.place(x=1331, y=45)
        
        self.button_account_image = PhotoImage(file=relative_to_assets("button_account.png"))
        self.button_account = Button(self, image=self.button_account_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(AccountPage) if server.customer[use_count_account].status else controller.show_frame(Loginpage),relief="flat")
        self.button_account.place(x=1207.0,y=30.0,width=56.0,height=56.0)
        
        self.button_manga_image = PhotoImage(
        file=relative_to_assets("button_manga.png"))
        self.button_manga = Button(self, image=self.button_manga_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(MangaPage),relief="flat")
        self.button_manga.place(x=274, y=43)
        
        self.button_novel_image = PhotoImage(
        file=relative_to_assets("button_novel.png"))
        self.button_novel = Button(self, image=self.button_novel_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(NovelPage),relief="flat")
        self.button_novel.place(x=408, y=43)
        
        
        self.button_cart_image = PhotoImage(
        file=relative_to_assets("button_cart.png"))
        self.button_cart = Button(self,image=self.button_cart_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Cartpage),relief="flat")
        self.button_cart.place(x=1083.0, y=30.0, width=56.0, height=56.0)
        
        self.button_bookstore_image = PhotoImage(file=relative_to_assets("button_Bookstore.png"))
        self.button_bookstore = Button(self, image=self.button_bookstore_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Mainpage),relief="flat")
        self.button_bookstore.place(x=22.0, y=30.0, width=218.0, height=54.0)
        

class Loginpage(tk.Frame):
    
    count_account=0

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        
        self.canvas = Canvas(self, bg="#1895F5", height=110, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack()
        self.button_account_image = PhotoImage(file=relative_to_assets("button_account.png"))
        self.button_account = Button(self, image=self.button_account_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(AccountPage) if server.customer[self.count_account].status else controller.show_frame(Loginpage),relief="flat")
        self.button_account.place(x=1207.0,y=30.0,width=56.0,height=56.0)
        
        self.button_manga_image = PhotoImage(file=relative_to_assets("button_manga.png"))
        self.button_manga = Button(self, image=self.button_manga_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(MangaPage),relief="flat")
        self.button_manga.place(x=274, y=43)
        
        self.button_novel_image = PhotoImage(file=relative_to_assets("button_novel.png"))
        self.button_novel = Button(self, image=self.button_novel_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(NovelPage),relief="flat")
        self.button_novel.place(x=408, y=43)
        
        
        self.button_cart_image = PhotoImage(file=relative_to_assets("button_cart.png"))
        self.button_cart = Button(self,image=self.button_cart_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Cartpage),relief="flat")
        self.button_cart.place(x=1083.0, y=30.0, width=56.0, height=56.0)
        
        self.button_bookstore_image = PhotoImage(file=relative_to_assets("button_Bookstore.png"))
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
        
        
        self.entry_image_textfill = PhotoImage(file=relative_to_assets("button_bookstore.png"))
        self.canvas.create_image(1237.0, 241.5, image=self.entry_image_textfill)
        self.entry_ID = Entry(self, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0 ,font=("Inter", 15)) 
        self.entry_ID.place(x=1064.0, y=230.0, width=346.0, height=35.0)
        
        self.entry_Password = Entry(self, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0 , show="·",font=("Inter", 40))
        self.entry_Password.place(x=1063.0, y=320.0, width=346.0, height=35.0)
        
        self.button_image_Signin = PhotoImage(file=relative_to_assets("button_signin.png"))
        self.button_Signin = Button(self, image=self.button_image_Signin,borderwidth=0,highlightthickness=0,command=self.system_login,relief="flat")
        self.button_Signin.place(x=1188.0,y=380.0,width=97.0,height=33.0)

        self.canvas1 = Canvas(self, bg="#FEFCFF", height=2, width=348, bd=0, highlightthickness=0, relief="ridge")
        self.canvas1.place(x=1064, y=440)
        
        self.Lable_main = Label(self, text="Don't have an account?", bg="#82c9ff", fg="white", font=("Inter", 16))
        self.Lable_main.place(x=1120.0,y=480.0)
        
        self.button_image_signup = PhotoImage(file=relative_to_assets("button_signup.png"))
        self.button_signup = Button(self, image=self.button_image_signup,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Registerpage),relief="flat")
        self.button_signup.place(x=1188.0,y=530.0,width=97.0,height=33.0)
            

    def system_login(self):
        self.id = self.entry_ID.get()
        self.password = self.entry_Password.get()
        self.entry_ID.delete(0,END)
        self.entry_Password.delete(0,END)
        for i in server.customer:
            print(i)
            print(self.count_account)
            if i.id == self.id and i.password == self.password and i.status == False:
                print(server.customer[self.count_account].status)
                server.customer[self.count_account].status = True
                print(server.customer[self.count_account].status)
                print(self.count_account)
                msg.showinfo("Login", "Login Success")
                self.controller.show_frame(Mainpage)
                
                return self.count_account
            else:
                self.count_account += 1
        if self.count_account == len(server.customer):
            msg.showerror("Login", "Login Failed Plase try again")
            raise Exception("Login Failed")
        
    def get_count_account(self):
        return Loginpage.count_account
class Registerpage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.controller = controller
        self.canvas = Canvas(self, bg="#1895F5", height=110, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack()
        
        use_count_account = Loginpage.get_count_account(self)

        self.button_account_image = PhotoImage(file=relative_to_assets("button_account.png"))
        self.button_account = Button(self, image=self.button_account_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(AccountPage) if server.customer[use_count_account].status else controller.show_frame(Loginpage),relief="flat")
        self.button_account.place(x=1207.0,y=30.0,width=56.0,height=56.0)
        
        self.button_manga_image = PhotoImage(
        file=relative_to_assets("button_manga.png"))
        self.button_manga = Button(self, image=self.button_manga_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(MangaPage),relief="flat")
        self.button_manga.place(x=274, y=43)
        
        self.button_novel_image = PhotoImage(
        file=relative_to_assets("button_novel.png"))
        self.button_novel = Button(self, image=self.button_novel_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(NovelPage),relief="flat")
        self.button_novel.place(x=408, y=43)
        
        
        self.button_cart_image = PhotoImage(
        file=relative_to_assets("button_cart.png"))
        self.button_cart = Button(self,image=self.button_cart_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Cartpage),relief="flat")
        self.button_cart.place(x=1083.0, y=30.0, width=56.0, height=56.0)
        
        self.button_bookstore_image = PhotoImage(file=relative_to_assets("button_Bookstore.png"))
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
        
        self.button_image_signup = PhotoImage(file=relative_to_assets("button_signup.png"))
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
        use_count_account = Loginpage.get_count_account(self)

        self.button_account_image = PhotoImage(file=relative_to_assets("button_account.png"))
        self.button_account = Button(self, image=self.button_account_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(AccountPage) if server.customer[use_count_account].status else controller.show_frame(Loginpage),relief="flat")
        self.button_account.place(x=1207.0,y=30.0,width=56.0,height=56.0)
        
        self.button_manga_image = PhotoImage(
        file=relative_to_assets("button_manga.png"))
        self.button_manga = Button(self, image=self.button_manga_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(MangaPage),relief="flat")
        self.button_manga.place(x=274, y=43)
        
        self.button_novel_image = PhotoImage(
        file=relative_to_assets("button_novel.png"))
        self.button_novel = Button(self, image=self.button_novel_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(NovelPage),relief="flat")
        self.button_novel.place(x=408, y=43)
        
        
        self.button_cart_image = PhotoImage(
        file=relative_to_assets("button_cart.png"))
        self.button_cart = Button(self,image=self.button_cart_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Cartpage),relief="flat")
        self.button_cart.place(x=1083.0, y=30.0, width=56.0, height=56.0)
        
        self.button_bookstore_image = PhotoImage(file=relative_to_assets("button_Bookstore.png"))
        self.button_bookstore = Button(self, image=self.button_bookstore_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Mainpage),relief="flat")
        self.button_bookstore.place(x=22.0, y=30.0, width=218.0, height=54.0)
        
class MangaPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.canvas = Canvas(self, bg="#1895F5", height=110, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack()
        use_count_account = Loginpage.get_count_account(self)

        self.button_account_image = PhotoImage(file=relative_to_assets("button_account.png"))
        self.button_account = Button(self, image=self.button_account_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(AccountPage) if server.customer[use_count_account].status else controller.show_frame(Loginpage),relief="flat")
        self.button_account.place(x=1207.0,y=30.0,width=56.0,height=56.0)
        
        self.button_manga_image = PhotoImage(
        file=relative_to_assets("button_manga.png"))
        self.button_manga = Button(self, image=self.button_manga_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(MangaPage),relief="flat")
        self.button_manga.place(x=274, y=43)
        
        self.button_novel_image = PhotoImage(
        file=relative_to_assets("button_novel.png"))
        self.button_novel = Button(self, image=self.button_novel_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(NovelPage),relief="flat")
        self.button_novel.place(x=408, y=43)
        
        
        self.button_cart_image = PhotoImage(
        file=relative_to_assets("button_cart.png"))
        self.button_cart = Button(self,image=self.button_cart_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Cartpage),relief="flat")
        self.button_cart.place(x=1083.0, y=30.0, width=56.0, height=56.0)
        
        self.button_bookstore_image = PhotoImage(file=relative_to_assets("button_Bookstore.png"))
        self.button_bookstore = Button(self, image=self.button_bookstore_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Mainpage),relief="flat")
        self.button_bookstore.place(x=22.0, y=30.0, width=218.0, height=54.0)
        
class NovelPage(tk.Frame):
    
    def __init__(self , parent, controller):
        tk.Frame.__init__(self, parent)
        self.canvas = Canvas(self, bg="#1895F5", height=110, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack()
        use_count_account = Loginpage.get_count_account(self)
        
        self.button_account_image = PhotoImage(file=relative_to_assets("button_account.png"))
        self.button_account = Button(self, image=self.button_account_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(AccountPage) if server.customer[use_count_account].status else controller.show_frame(Loginpage),relief="flat")
        self.button_account.place(x=1207.0,y=30.0,width=56.0,height=56.0)
        
        self.button_manga_image = PhotoImage(
        file=relative_to_assets("button_manga.png"))
        self.button_manga = Button(self, image=self.button_manga_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(MangaPage),relief="flat")
        self.button_manga.place(x=274, y=43)
        
        self.button_novel_image = PhotoImage(
        file=relative_to_assets("button_novel.png"))
        self.button_novel = Button(self, image=self.button_novel_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(NovelPage),relief="flat")
        self.button_novel.place(x=408, y=43)
        
        
        self.button_cart_image = PhotoImage(
        file=relative_to_assets("button_cart.png"))
        self.button_cart = Button(self,image=self.button_cart_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Cartpage),relief="flat")
        self.button_cart.place(x=1083.0, y=30.0, width=56.0, height=56.0)
        
        self.button_bookstore_image = PhotoImage(file=relative_to_assets("button_Bookstore.png"))
        self.button_bookstore = Button(self, image=self.button_bookstore_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Mainpage),relief="flat")
        self.button_bookstore.place(x=22.0, y=30.0, width=218.0, height=54.0)
        
class AccountPage(tk.Frame):
    
    def __init__(self , parent , controller):
        tk.Frame.__init__(self, parent)
        self.canvas = Canvas(self, bg="#1895F5", height=110, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack()
        use_count_account = Loginpage.get_count_account(self)
        print("Account page" + str(use_count_account))
        user_Id = server.customer[use_count_account].id
        user_Name = server.customer[use_count_account].name
        user_Email = server.customer[use_count_account].email
        user_Phone = server.customer[use_count_account].phone
        user_Address = server.customer[use_count_account].address
        self.TKuser_Id = StringVar()
        Tkuser_Name = StringVar()
        TKuser_Email = StringVar()
        TKuser_Phone = StringVar()
        TKuser_Address = StringVar()
        self.TKuser_Id.set(user_Id)
        Tkuser_Name.set(user_Name)
        TKuser_Email.set(user_Email)
        TKuser_Phone.set(user_Phone)
        TKuser_Address.set(user_Address)
        


        self.button_account_image = PhotoImage(file=relative_to_assets("button_account.png"))
        self.button_account = Button(self, image=self.button_account_image,borderwidth=0,highlightthickness=0,command=lambda: [controller.show_frame(AccountPage) if server.customer[use_count_account].status else controller.show_frame(Loginpage) , self.update_label(use_count_account)],relief="flat")
        self.button_account.place(x=1207.0,y=30.0,width=56.0,height=56.0)
        
        self.button_manga_image = PhotoImage(
        file=relative_to_assets("button_manga.png"))
        self.button_manga = Button(self, image=self.button_manga_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(MangaPage),relief="flat")
        self.button_manga.place(x=274, y=43)
        
        self.button_novel_image = PhotoImage(
        file=relative_to_assets("button_novel.png"))
        self.button_novel = Button(self, image=self.button_novel_image, borderwidth=0, highlightthickness=0,command=lambda: controller.show_frame(NovelPage) ,relief="flat")
        self.button_novel.place(x=408, y=43)
        
        
        self.button_cart_image = PhotoImage(
        file=relative_to_assets("button_cart.png"))
        self.button_cart = Button(self,image=self.button_cart_image,borderwidth=0,highlightthickness=0,command=lambda: controller.show_frame(Cartpage),relief="flat")
        self.button_cart.place(x=1083.0, y=30.0, width=56.0, height=56.0)
        
        self.button_bookstore_image = PhotoImage(file=relative_to_assets("button_Bookstore.png"))
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
        
        self.Lable_Name = Label(self, text="Name : " + Tkuser_Name.get(), bg="#82c9ff", fg="white", font=("Inter", 16))
        self.Lable_Name.place(x=1047.0,y=253.0)
        
    
    def update_label(self, new_value):
        print("update_label")
        print(new_value)
        self.TKuser_Id.set("ID  : " + str(new_value))


app = Bookstore()

app.mainloop()
