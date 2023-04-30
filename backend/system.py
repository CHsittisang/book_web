from account import Admin , Account , Customer
from book import Book, Series , Book_catalog

class System:
    count_account = 0
    def __init__(self):
        self.admin = []
        self.customer  = []
        self.customerlogin = []


    def add_admin(self, admin: Admin):
        self.admin.append(admin)

    def add_customer(self, customer: Customer):
        self.customer.append(customer)
    
    def add_customerlogin(self, customer: Customer):
        self.customerlogin.append(customer)
        
    def Logout(self, customer: Customer):
        self.customerlogin.remove(customer)
        


class Seriessystem:
    current_series = 0
    def __init__(self):
        self.series = []

    def add_series(self, series):
        self.series.append(series)



# runing
server = System()
serverseries = Seriessystem()

Guest = Customer("Guest", "1234", "Guest", "email", "phone", "address")
nut = Customer("nut", "1234", "nut", "email", "phone", "address")
nut1 = Customer("nut1", "1234", "nut1", "email", "phone", "address")
System.add_customer(server , Guest)
System.add_customer(server , nut)
System.add_customer(server , nut1)


Book_suzume = Book("Suzume no Tojimari \n(LN)", "1", "detail", "LN", 315, "Suzumeimg1.png", "	2022", 10)

Suzume_LN = Book_catalog("Suzume_LN", "Light Novel", "Drama , Fantasy", "Suzumebanner.png", "2020-01-01", )
Suzume_LN.catalog_book_list.append(Book_suzume)


Suzume_no_Tojimari = Series("Suzume no Tojimari", "\tซุซุเมะ เด็กสาววัย 17 ปีอาศัยอยู่กับน้าที่เมืองท่าอันเงียบสงบบนเกาะคิวชู เธอเดินสวนกับเด็กหนุ่มรูปงามขณะเดินทาง\n\nไปโรงเรียนในเช้าวันหนึ่ง เขาคนนั้นบอกว่า" + "“กำลังตามหาประตูอยู่”" + "เป็นเหตุให้เธอตามไปยังกองซากปรักหักพังกลางภูเขา \n\nทว่าสิ่งที่ปรากฏอยู่ตรงนั้นกลับมีเพียงบานประตูสีขาวเก่าคร่ำคร่าซึ่งตั้งอยู่อย่างเดียวดายคล้ายถูกทิ้งร้างหลังสิ่งปลูกสร้างพังทลาย \n\n\tซุซุเมะเอื้อมมือไปหาประตูบานนั้นราวกับมีบางสิ่งดลใจ...","2020-01-01", "suzume_series.png", "Makoto Shinkai", Suzume_LN)
Classroom_of_the_Elite = Series("Classroom of the Elite","detail", "2020-01-01", "Classroom_of the_Elite_series.png", "author", "what_obj")
Lala_No_Kekkon = Series("Lala No Kekkon", "2020-01-01","detail", "Lala_No_Kekkon_series.png", "author", "what_obj")
Silent_Witch = Series("Silent Witch Chinmoku no Majo \nno Kakushigoto","detail", "2020-01-01", "Silent_Witch_series.png", "author", "what_obj")
Maou_Gakuin = Series("Maou Gakuin no Futekigousha","detail", "2020-01-01", "Maou_Gakuin_no_Futekigousha_series.png", "author", "what_obj")
Buta_no_Koukou = Series("Buta no Koukou", "2020-01-01","detail", "Buta_Koshaku_ni_Tensei_Shitakara_series.png", "author", "what_obj")
Seriessystem.add_series(serverseries, Suzume_no_Tojimari)
Seriessystem.add_series(serverseries, Classroom_of_the_Elite)
Seriessystem.add_series(serverseries, Lala_No_Kekkon)
Seriessystem.add_series(serverseries, Silent_Witch)
Seriessystem.add_series(serverseries, Maou_Gakuin)
Seriessystem.add_series(serverseries, Buta_no_Koukou)


print(serverseries.series[0].book_catalog_obj.type)

