# class student:
#     rollno=101 #data member

#     def msg(self):  #member function
#         print("hello world")

# obj=student()
# print(obj.rollno)
# obj.msg()

# Q2
# class demo:
#     def __init__(self):
#        print("i am constructor and i always called first")
    
#     #instance method
#     def info(self):
#         print("one object")

# obj=demo()
# obj.info()
# obj2=demo()

# Q3
# class hod:
#     def __init__(self):  # constructor
#         self.name='divya shinde'  #2byte
#         self.age='22'             #3byte
#         self.empid=1001           #1byte
#     def info(self):  #instance method
#         print("my name is:",self.name)
#         print("my age is:",self.age)
#         print("my emp id:",self.empid)
# obj=hod()#obj create
# obj.info()

# Q4
# class hod:
#     def __init__(self ,name,age,rollno):  # parameterize cons
#         self.name= name 
#         self.age= age          
#         self.rollno= rollno 

#     def info(self):  
#         print('name=',self.name)
#         print('age=',self.age)
#         print( 'rollno=',self.rollno)
# obj=hod(divya,22,85)
# obj.show()

# Q5

# class new:
#     def __init__(self):
#         self.a= 10

# obj1 = new()
# obj2 = new()
# obj3 = new()
# obj1.a=20
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)

# Q6

# class new:
#     a=10#static

#     def __init__(self):
#         self.name="divya"

# obj1 = new()
# obj2 = new()
# obj3 = new()
# new.a=50
# print(new.a)
# print(obj1.a)
       
# Q7

# class College
#     collegename= "modern college"
#     def __init__(self)
#         self.studentname= "divya"

# principal = Colleg()
# teacher = Colleg()
# accountant = "college"()
# print("principal=",principal.collegename,"...",principal.studentname)
# print("teacher=",teacher.collegename,"...",teacher.studentname)
# print("accountant=",accountant.collegename,"...",accountant.studentname) 

# college.collegename="hbd"
# principal.studentname="divya"

# print("principal=",principal.collegename,"...",principal.studentname)
# print("teacher=",teacher.collegename,"...",teacher.studentname)
# print("accountant=",accountant.collegename,"...",accountant.studentname) 

# Q8

# class student:
#     def __init__(self):
#         self.s_name  =input("enter your name")
#         self._rollno = 101

#     def getdata(self):
#         self.s_mb   = 2828282828282   #instance var

# obj = student()
# obj.getdada()
# obj.s_branch = "AIDS"  #adding instance variable
# del obj.s_rollno
# print(obj.__dict__)

# Q9 static method

# class student:
#     #by using class name we can access static method
#     @staticmethod  #decorator
#     def get_personal_detail(firstname,lastname):
#         print("your personal detail=",firstname,lastname)
    
#     @staticmethod
#     def contact_detail(mobile_no, rollno):
#         print("your contact detail=",mobil_no,rollno)

# student.get_personal_detail("divya","shinde")
# student.contact_detail_(1234567890,1001)

# Q10single level

# class college:    # parent class
#     def college_name(self):  #member function of college
#         print("modern college")

# class student(college):  #child class
#     def student_info(self):   #member function
#         print("name: divya shinde")
#         print("branch: aids")

# obj = student()  #object create child class
# obj.college_name()
# obj.student_info()

# Q11multilevel

# class college:       #first class first level
#     def college_name(self):
#         print("modern college")

# class student(college):     #second class 2nd level
#     def student_info(self):
#         print("name: divya shinde")
#         print("branch: aids")

# class exam(student):       #child class
#     def subject(self):
#         print("subject1: designe engineering")
#         print("subject2:math")
#         print("subject3:C-Language")

# obj = exam()
# obj.college_name()
# obj.student_info()
# obj.subject()

# Q12multiple

# class subjmarks:   #class1
#     math = int(input("enter paper marks of math:"))
#     de = int(input("enter paper marks of design engineering:"))
#     c = int(input("enter paper marks of c language"))
#     english = int(input("enter paper marks of english"))

# class practmarks:   #class2
#     cpract = int(input("enter practicals marks of c language:"))

# class result(subjmarks,practmarks):   #child class
#     def result(self):
#         if self.math>=40 and self.de>=40 and self.c>40 and self.english>=40 and self.cpract>=20:
#            print("pass")
#         else:
#             print("fail")

# obj = result()
# obj.total()

# abstraction
# Q13

# from abc import ABC,abstractmethod
# class help4code(ABC):   #abstract class
#     @abstractmethod       #decorator
#     def training(self):    #absract method
#         pass

#     @abstractmethod         #absract method
#     def placement(self):
#         pass

# class ashish(help4code):
#     def training(self):
#         print('c,c++,java')
#     def placement(self):
#         print("java placemenet")

# class ankush(help4code):
#     def training(self):
#         print("python | django")
#     def placement(self):
#         print("python placemenet students")

# class prashant(help4code):
#     def training(self):
#         print("machine learing")
#     def placement(self):
#         print("data science placemenet")

# obj1 = ashish()
# obj1.training()
# obj1.placement()

# obj2 = ankush()
# obj2.training()
# obj2.placement()

# obj3 = prashant()
# obj3.training()
# obj3.placement()

# Q14

# from abc import ABC,abstractmethod
# class Irctc(ABC):   #abstract class
   
#     @abstractmethod       #decorator
#     def bookticket(self):    #absract method
#         pass

# class makemytrip(Irctc):

#     def bookticket(self):
#         print("")
#         print(" welcome to makemytrio.com")
#         self.source = input("enter a source station name")
#         self.destination = input("enter destination name")
#         self.date = ("enter date")
#         print("")

# class goibibo(Irctc):

#      def bookticket(self):
#          print("welcome to GOIBIBO")

# class yatra(Irctc):
#     def bookticket(self):
#         print("welcome to yatra.com")
        
# m=makemytrip()
# m.bookticket()
# g=goibibo()
# g.bookticket()
# y=yatra()
# y.bookticket()

# Q15

# class arithmatic:
#     def add(self,a):
#         print(a)
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c):
#         print(a+b+c)

# obj = arithmatic()
# obj.add(10)
# obj.add(10,20)
# obj.add(1,2,3)

# Q16

# class arithmatic:
#     def __init__(self):
#         print("there is no argument")
#     def __init__(self,a):
#         print("passing one arguments")
#     def __init__(self,a,b):
#         print("passing two arguments")

# obj = arithmatic()
# obj = arithmatic(10)
# obj = arithmatic(2,2)


# Q17overloa

#     def __init__(self):
#         print("father:=i am on time at breakfast table")
# class Rbi:
#     def homeloan(self):
#         print("home loan rate of interest 8%")
    
#     def carloan(self):
#         print("car loan rate of interest 7%")

# class Sbi(Rbi): #child class
#     def homeloan(self):
#         print("home loean rate of interest 10.5")
#         super().homeloan

# sbiobj = Sbi()
# sbiobj.homeloan()
# sbiobj.carloan()

# Q18overload

# class father:
#     def __init__(self):
#         print("father:i will allready at breakfast table")

# class child(father):
#     def __init__(self):
#         print("child: i will be late for breakfast")
#         #super().__init__()
# obj = child()

# Q19 encapsulation

# class Base:  #parent class
#     def __init(self):
#         print("parent class constructor called")
#         self.a = "Divya"  #public data mrember
#         self.__c = "Laxmi" # private member
#  #creating a derived class\child class

# class Derived(Base):   #child class
#     def __init__(self):
#         #calling constructor of base class
#         Base.__init__(self)
#         #print("callinf private member of base class:")
#         #print(self.a)
#         #print(self.__c)

# #obj1 = Derived()
# #print(obj.a)
# #print(obj.__c)
# obj2 = Base()
# print(obj2.a)  #Accessible
# print(obj2.__c) #Not Accessible

# 20

# class Rbi:
#     #Declaring public method
#     def publicpolicy(self):
#         print("chcek the public policy of RBI")

#      #Declarinf private method
#     def __privatepolicy(self):
#         print("There is some private policy which is not accessible for public")

# class Sbi(Rbi):
#     def __init__(self): #1st sbi class
#         Rbi.__init__(self)  # second parent class constructor called

#     def callingpublicnethod(self):  # child class public method
#         print("\ninside child class")
#         self.publicpolicy()  # calling parent class public method

#     def callingprivatemethod(self):  #child class public method
#         self.__privatepolicy()  #calling parent class private method

# obj1 = Sbi()
# #obj.callingpublicmethod()
# #obj1.callingprivatemethod()
# #obj1.publicpolicy()
# #obj1.__privatepolicy()
# # obj2 = Rbi()
# #obj2.publicpolicy()
# obj2.__privatepolicy()
# obj2 = Rbi()
# obj2.publicpolicy()