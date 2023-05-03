from account import Admin , Account , Customer
from book import Book, Series , Book_catalog
import csv

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
        
class Seriessystem:
    current_series = 0
    def __init__(self):
        self.series = []
        self.book_catalog_list = []
        self.book_list = []

    def add_series(self, series):
        self.series.append(series)
        
    def read_series_data(self, file_name):
        with open(file_name, mode='r',encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                series_name = row['series_name']
                detail_series = row['detail_series']
                last_update = row['last_update']
                img = row['img']
                author = row['author']
                book_catalog_obj = row['book_catalog_obj']
                self.series.append(Series(series_name, detail_series, last_update, img, author, book_catalog_obj))
                
    def read_book_catalog_data(self, file_name):
        with open(file_name, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                catalog_name = row['catalog_name']
                type = row['type']
                tag = row['tag']
                img = row['img']
                release_date = row['relea_date']
                book_catalog_obj = Book_catalog(catalog_name, type, tag, img, release_date)
                self.book_catalog_list.append(book_catalog_obj)
                catalog_book_list = row['catalog_book_list'].split(';')
                for book_id in catalog_book_list:
                    for book in self.book_list:
                        if book.book_id == book_id:
                            book_catalog_obj.catalog_book_list.append(book)

    def read_book_data(self, file_name):
        with open(file_name, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                book_name = row['book_name']
                book_id = row['book_id']
                detail_in_book = row['detail_in_book']
                type = row['type']
                price = row['price']
                img = row['img']
                release_date = row['relea_date']
                number_of_product = row['number_of_product']
                self.book_list.append(Book(book_name, book_id, detail_in_book, type, price, img, release_date, number_of_product))




# runing
server = System()
serverseries = Seriessystem()
serverseries.read_series_data("backend/data/series.csv")
serverseries.read_book_catalog_data("backend/data/book_catalog.csv")
serverseries.read_book_data("backend/data/book.csv")

Guest = Customer("Guest", "1234", "Guest", "email", "phone", "address")
nut = Customer("nut", "1234", "nut", "email", "phone", "address")
nut1 = Customer("nut1", "1234", "nut1", "email", "phone", "address")
System.add_customer(server , Guest)
System.add_customer(server , nut)
System.add_customer(server , nut1)





# Book_suzume = Book("Suzume no Tojimari \n(LN)", "1", "detail", "LN", 315, "Suzumeimg1.png", "	2022", 10)
# Suzume_LN= Book_catalog("Suzume_LN", "Light Novel", "Drama , Fantasy", "Suzumebanner.png", "2020-01-01")
# Suzume_LN.catalog_book_list.append(Book_suzume)

# Book_Classroom_of_the_Elite = Book("Classroom of the Elite \n(LN)", "1", "detail", "LN", 315, "Classroomimg1.png", "2022", 10)
# Classroom_of_the_Elite_LN = Book_catalog("Classroom of the Elite_LN", "Light Novel", "Drama , Fantasy", "Classroombanner.png", "2020-01-01")
# Classroom_of_the_Elite_LN.catalog_book_list.append(Book_Classroom_of_the_Elite)

print((serverseries.series[0].book_catalog_obj))
print(serverseries.book_catalog_list[0].img)
print(serverseries.book_list[0].img)
print(serverseries.series[0].detail_series)
print(serverseries.book_list[0].img)

# Suzume_no_Tojimari = Series("Suzume no Tojimari", "\tซุซุเมะ เด็กสาววัย 17 ปีอาศัยอยู่กับน้าที่เมืองท่าอันเงียบสงบบนเกาะคิวชู เธอเดินสวนกับเด็กหนุ่มรูปงามขณะเดินทาง\n\nไปโรงเรียนในเช้าวันหนึ่ง เขาคนนั้นบอกว่า" + "“กำลังตามหาประตูอยู่”" + "เป็นเหตุให้เธอตามไปยังกองซากปรักหักพังกลางภูเขา \n\nทว่าสิ่งที่ปรากฏอยู่ตรงนั้นกลับมีเพียงบานประตูสีขาวเก่าคร่ำคร่าซึ่งตั้งอยู่อย่างเดียวดายคล้ายถูกทิ้งร้างหลังสิ่งปลูกสร้างพังทลาย \n\n\tซุซุเมะเอื้อมมือไปหาประตูบานนั้นราวกับมีบางสิ่งดลใจ...","2020-01-01", "suzume_series.png", "Makoto Shinkai", Suzume_LN)
# Classroom_of_the_Elite = Series("Classroom of the Elite","\tโรงเรียนมัธยมปลายโคโดอิคุเซ โรงเรียนชั้นนำของประเทศที่ตอบสนองความปรารถนาในการศึกษาต่อและการทำงานเกือบ 100 เปอร์เซ็นต์\nแน่นอนว่ามีเครื่องอำนวยความสะดวกไว้ให้ใช้ครบครัน แถมยังให้เบี้ยเลี้ยงเป็นแต้มที่มีมูลค่าเท่ากับ 100,000 เยนทุกเดือนอีกด้วย\nทั้งทรงผมหรือข้าวของส่วนตัวก็เลือกได้อย่างอิสระ ช่างเป็นโรงเรียนที่เหมือนกับสรวงสวรรค์เสียนี่กระไร\n\n\tแต่ในความเป็นจริงแล้วมีเพียงแค่นักเรียนที่มีความสามารถอย่างแท้จริงเท่านั้นที่จะได้รับการปฏิบัติเป็นพิเศษ ด้วย\nเหตุผลบางอย่าง อายาโนะโคจิ คิโยทากะ ถูกจัดให้มาอยู่ในห้อง D ที่รวมเอานักเรียนที่เหมือนของมีตำหนิถูกคนคอยล้อ\nเลียนเอาไว้ด้วยกัน การพบเจอกับเพื่อนร่วมห้องอย่างโฮริคิตะ ซึซึเนะ สาวสวยผลการเรียนดีแต่นิสัยมีปัญหา และ\nคุชิดะ คิเคียว สาวน้อยผู้โอบอ้อมอารี ใจดีอย่างกับนางฟ้า กำลังจะทำให้สถานการณ์ของคิโยทากะค่อยๆแปรเปลี่ยนไป", "2020-01-01", "Classroom_series.png", "author", Classroom_of_the_Elite_LN)
# Lala_No_Kekkon = Series("Lala No Kekkon", "2020-01-01","detail", "Lala_No_Kekkon_series.png", "author", "what_obj")
# Silent_Witch = Series("Silent Witch Chinmoku no Majo \nno Kakushigoto","detail", "2020-01-01", "Silent_Witch_series.png", "author", "what_obj")
# Maou_Gakuin = Series("Maou Gakuin no Futekigousha","detail", "2020-01-01", "Maou_Gakuin_no_Futekigousha_series.png", "author", "what_obj")
# Buta_no_Koukou = Series("Buta no Koukou", "2020-01-01","detail", "Buta_Koshaku_ni_Tensei_Shitakara_series.png", "author", "what_obj")





# Seriessystem.add_series(serverseries, Suzume_no_Tojimari)
# Seriessystem.add_series(serverseries, Classroom_of_the_Elite)
# Seriessystem.add_series(serverseries, Lala_No_Kekkon)
# Seriessystem.add_series(serverseries, Silent_Witch)
# Seriessystem.add_series(serverseries, Maou_Gakuin)
# Seriessystem.add_series(serverseries, Buta_no_Koukou)


# print(serverseries.series[0].book_catalog_obj.type)
# print(serverseries.series[0].book_catalog_obj.catalog_book_list[0].img)
