""" class Person:
    name="Ulfet"
    age=34

# create instances from object
person1 = Person()
person2 = Person()

print(person1.name)  # Ulfet
print(person2.name)  # Ulfet

# add property to object
Person.job = "developer"
print(person1.job)  # developer
print(person2.job)  # developer

# Class attributes and instance attributes
# person1 "name" adında kendi attribute'u old. için class attribute'dan etkilenmedi.Kendi attribute'u olmasaydı yukarı yani class attribute'na bakacaktı.person2'nin attribute'u olmadığı için class attribute olan "name" aldı.
Person.name = "Andy"
person1.name = "Henry"
print(person1.name)  # Henry
print(person2.name)  # Andy """

""" 
# SELF Keyword
class Person:
    name="Ulfet"
    age=34
    
    def test(self):  # self Person objesinin bir metodu old. göstermek için kullanılır.(JS'de this gibi)
        print("test")
        
    def get_details(self):
        print("name:",self.name, "age:",self.age, "location:",self.location)
        
    def set_details(self,name,age,location):
        self.name = name
        self.age = age
        self.location = location
        
    
person1 = Person()
person1.test()  # test
Person.test(person1)  # test
person1.set_details("Henry",38,"Ankara")  # set'den önce get kullanılırsa hata verecektir.
person1.get_details()  # name: Henry age: 38 location: Ankara """

# static method & decorator
# static method tanımlayabilmek için decorator kullanılmalı.

""" class Person:
    name="Ulfet"
    age=34
    
    def get_details(self):
        print("name:",self.name, "age:",self.age, "location:",self.location)
        
    def set_details(self,name,age,location):
        self.name = name
        self.age = age
        self.location = location
        
    @staticmethod
    def salute():
        print("Hi there!",Person.name)
    
Person.salute()  # Hi there! Ulfet
person1 = Person()
person1.set_details("Henry",39,"Izmir")  # Hi there! Ulfet => staticmethod class üzerinde çalışır.Instances'lara ulaşamaz.
person1.salute()  # Hi there! Ulfet """


# special methods

""" class Person:
    company = "Clarusway"  # ortak olan attribute'lar class altında tanımlanır.
    
    def __init__(self,name,age) :  ## init constructor fonksiyonudur.
        self.name = name
        self.age = age
person1 = Person("Ulfet",34)
print(person1.name,person1.age)  # Ulfet 34 """

""" class Person:
    company = "Clarusway"
    
    def __init__(self,name,age) : 
        self.name = name
        self.age = age
    def __str__(self):
        return f"Name: {self.name}  Age:{self.age}"

person1 = Person("Ulfet",34)
lst = [1,2,3]
print(lst)  # [1,2,3]
print(person1)  #  Name: Ulfet  Age:34 => print denildiğinde Person içerisinde str metodunu arar.Bu metodu bulamazsa : "<__main__.Person object at 0x00000256E6348E20>" sonucunu gösterir. str bulursa içindeki işlemleri yapar. """



# Bir kodun oop olabilmesi için 4 özelliği olmalı.Bunlar:

# abstraction(soyutlama;detaylardan arındırma,program çalışırken arka planda neler olduğunu bilmemize gerek yok).User is familiar with that "what function does" but they don't know "how it does."

# encapsulation=>methotların ve variable’ların erişimlerini kısıtlamak anlamına gelir.Metotlara veya variable’lara direk erişme ve değiştirme kısıtı özelliği getirilir.Python'da 100% koruma yok.Bir değeri değiştirmek isterseniz değiştirebilirsiniz.Encapsulation için; değiştirilmesini kısıtlamak istediğimiz attribute'lar için önüne "__" ekliyoruz.

""" class RegisterCourse:     
    def __init__(self):
        self.name = "Ulfet"
        self.surname = "Kaçay"
        self.exam1 = 74
        self.exam2 = 80
 
register = RegisterCourse()
# öğrencinin bilgilerine dışarıdan ulaşabiliyoruz hatta değiştirebiliyoruz.
register.exam1 = 50
register.exam2 = 60
print("Exam 1 : ",register.exam1)  # Exam 1 :  50
print("Exam 2 :",register.exam2)  # Exam 2 : 60 """
""" 
class RegisterCourse:     
    def __init__(self):
        self.name = "Ulfet"
        self.surname = "Kaçay"
        self.__exam1 = 74
        self.__exam2 = 80  # koruma sağlamak amaçlı "__" kullanıldı.Değiştirilirse class düzgün çalışmayabilir.

register = RegisterCourse()
print("İsim : ",register.name)
print("Soyisim : ",register.surname)
# sınav bilgilerini private(özel) yaptığımız için sınav bilgilerine ulaşamadığından hata verecektir.Artık bu değerlere yalnız bu sınıf içinde erişebiliriz.
print("Exam 1 : ",register.exam1)
print("Exam 2 :",register.exam2) """


# inheritance and polymorphism

# inheritance : 
""" class Person:
    company = "Clarusway"
    
    def __init__(self,name,age) : 
        self.name = name
        self.age = age
    def __str__(self):
        return f"Name: {self.name}  Age:{self.age}"

class Employee(Person):
    def __init__(self, name, age,path):
        # self.name = name
        # self.age = age
        super().__init__(name,age)  # super:kimden kalıtım özelliklerini aldıysa onun "__init__" fonksiyonunu çalıştırır.Üst satırdaki kodları yazmamıza gerek kalmaz.
        self.path = path
        
emp1 = Employee("Ulfet",34,"FS")
print(emp1)  # Name: Ulfet  Age:34 => Employee içerisinde "__str__" olmadığı için kalıtım özelliği ile bir üst class'daki "__str__" yi kullanır. """


# polymorphism:Her iki nesnede de aynı isimdeki metodu kullanıp farklı çıktılar elde etme işlemine Polymorphism yani Çok Biçimlilik denilmektedir.

""" class Person:
    company = "Clarusway"
    
    def __init__(self,name,age) : 
        self.name = name
        self.age = age
    def __str__(self):
        return f"Name: {self.name}  Age:{self.age}"
    
class Employee(Person):
    def __init__(self, name, age,path):
        super().__init__(name,age)
        self.path = path
        
    # override işlemi
    def __str__(self):
        return f"Name: {self.name}  Age:{self.age} Path:{self.path}"
        
emp1 = Employee("Ulfet",34,"FS")
print(emp1)  # Name: Ulfet  Age:34 Path:FS """

# Example

class Customer:
    def __init__(self,name,age) :
        self.name = name
        self.age = age
        self.__id = 1234
        self.movements = []
    def __str__(self):
        return f"Name:{self.name} Id: {self.__id}"
    def add_movement(self,amount,date,explain):
        self.movements.append(
            {"amount":amount,"date":date,"explain":explain}
        )
    def all_movements(self):
        for i in self.movements:
            print(i["date"],i["amount"],i["explain"])
    def balance(self):
        return sum(i["amount"] for i in self.movements)
        """ total=0
        for i in self.movements:
            total += i["amount"]
        print("total:",total) """
        
custom = Customer("Ulfet",34)
print(custom)  # Name:Ulfet Id: 1234 (id > encapsulation old.için sadece class içerisinden ulaşabiliriz.)
custom.add_movement(5000,"15.10.2021","Salary")
custom.add_movement(-1000,"15.10.2021","Rent")
custom.add_movement(-500,"15.10.2021","Bills")
custom.add_movement(-2000,"15.10.2021","Credit Card")
custom.all_movements()
# custom.balance()
print(custom.balance())

# Output : 
""" 
Name:Ulfet Id: 1234
15.10.2021 5000 Salary
15.10.2021 -1000 Rent
15.10.2021 -500 Bills
15.10.2021 -2000 Credit Card
1500 
"""

