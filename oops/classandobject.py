class Student:
    def __init__(self,name,age):
        self.age = age
        self.name = name
name = Student("amrit",21)
age = Student("Amrit",21)
print(name.name)
print(age.age)        

class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self) : 
        return self.length*self.breadth  
    
    def perimeter(self):  
        return 2*(self.length+self.breadth)  
    
rect = Rectangle(2,3)
print(rect.area())
print(rect.perimeter())    

class BankAccount:
    def __init__(self,holder_name,balance):
        self.holderName = holder_name
        self.balance = balance

    def deposit(self,amount):
        self.amount = amount
        updated_balance = self.balance+amount
        self.balance = updated_balance
        return updated_balance
    
    def withdraw(self,amount):
        self.amount = amount
        if(amount < self.balance):
            updated_balance = self.balance-amount
            self.balance = updated_balance
            return updated_balance
        else:
            return "insufficient balance"
                
customer = BankAccount("amrit",20000)  
print(customer.deposit(10000))              


class Student:
    def __init__(self,name):
        self.name = name
        self.marks = []
    
    def add_marks(self,mark):
        self.marks.append(mark)

    def avg(self):
        if(len(self.marks) == 0):
            return 0
        else:
            return sum(self.marks)/len(self.marks)
student1 = Student("amrit")            
print(student1.add_marks(3))


class Book:
    def __init__(self,title,pages):
        self.title = title
        self.pages = pages
    def compare(self,other_book):
        if self.pages > other_book.pages:
            print(self.title, "has more pages")
        elif self.pages < other_book.pages:
            print(other_book.title, "has more pages")
        else:
            print("Both books have equal pages")
book1 = Book("atomic habit",5000)
book2 = Book("how to manage time",500)
book1.compare(book2)

class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def login(self,input_username,input_password):
          if input_username == self.username and input_password == self.password:
               return True
          else:
               return False
user1 = User("amrit","123")
print(user1.login("amrit","123"))          