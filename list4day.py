#1st ex
# mylist = ["Laxmi", "Gopika", "Avanti", "Ketan", "Ananda", 77, "Riya", 80.54, "Siya"]

# print(mylist)              # Prints the whole list
# print(type(mylist))        # Shows it's a list
# print(mylist[0])           # First element
# print(mylist[1])           # Second element
# print(mylist[2])           # Third element
# print(mylist[-1])          # Last element
# print(mylist[2:5])         # Slice from index 2 to 4
# print(mylist[:5])          # First 5 elements
# print(mylist[1:])          # From index 1 to end
# print(mylist[:])           # Entire list
# print(mylist[1:8:2])       # Step slicing (every 2nd element from index 1 to 7)
# print(mylist[:])           # Entire list again
# print(mylist[::-1])        # Reversed list

#2nd ex 

# mylist[2]="Aarti"
# print(mylist)  // the list is can change

# #3

# if "laxmi" in mylist:
#     print("yes laxmi is available")
# else:
#     print('not avilable')

# #4

# if "Laxmi" in mylist:
#     print("yes Laxmi is available")
# else:
#     print('not avilable')

#5

#append add last mei element

# mylist.append('harsh')
# mylist.append("divya")
# print(mylist)

#7

#insert used for add specific index

#actual index and actual value or obj like (1, "Roshan")

# mylist.insert(1,"Roshan")
# print(mylist)

#8
# #remove used for remove obj
# mylist.remove(1,"Roshan")
# mylist(mylist)

#9
#copy that make a clone of obj

# mylist= mylist.copy() #cloning
# print(mylist)


#multidimentional list examples
#10

# mylist = [['laxmi','Sanas'],[80,65],[440032,"yyy"]]
# print("ex of multidimentional list:")
# print(mylist)
# st[row][col])
# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[1][0])
# print(mylist[2][0])
# print(mylist[2][1])

#11

# list1=["Laxmi","sanas"]
# print(list1*2) o/p:['Laxmi', 'sanas', 'Laxmi', 'sanas']

# #12

# list2=[50,25.50]
# print(list1+list2)

#13

# list2 =[50,50.50,'Laxmi']
# # del list2[2]
# del list2
# print(list2)


#14
# list2 = [220,20.40,'Laxmi']
# list2.clear()
# print(list2)

#15
# name= "Laxmi"
# print(name)
# myname=list(name)  #typecasting and o/p like Laxmi ['L', 'a', 'x', 'm', 'i']
# print(myname )  

#16
# mylist= [10,20,30]
# mylist.reverse()
# print(mylist)

#17
# mylist=[20,30,1,2,0,60]
# mylist.sort()
# print(mylist)

#18
# mylist=[20,30,1,2,0,60]
# mylist.sort(reverse=True)
# print(mylist)

#19
# mylist=[20,30,60]
# mylist.sort()
# print(mylist)

#20
# mylist=[-1,20,30,1,2,0,60]
# mylist.sort()
# print(mylist)

#21

# mylist=[19,20,39]
# print(mylist)
# newlist = mylist
# print(id(mylist))
# print(id(newlist))
# mylist[0]="Laxmi"
# print(mylist)
# print(newlist)

#for loop range you know then we used 

#membership operator : value is exist on storing data (data check karta hai character available hai ki nahi)
#1.in    2.not in 

#22
# name="Laxmi"
# print("L" in name)
# print("z" not in name)

#23

# for i in range(5): #i=0 i is 0 
#     print(i)

#24
# for (intialization; condition; ince/dec)
# for i in range(1,20,2):  
#     print(i)

#25

# for i in range(5,0,-1): #perform desending format 
#     print(i)

#26

# Tables from 2 to 10

# for i in range(1, 11):              # Multipliers 1 to 10
#     for n in range(2, 11):          # Tables 2 to 10
#         print(f"{n * i:4}", end=" ")  # :4 ensures fixed width spacing
#     print()

# print("______________________________________")

# # Tables from 11 to 20 side by side
# for i in range(1, 11):              # Multipliers 1 to 10
#     for n in range(11, 21):         # Tables 11 to 20
#         print(f"{n * i:4}", end=" ")
#     print()

# print("______________________________________")

#27 new way to print 1 to 20 table i mean not 1 its 2 
# for i in range(1,11):
#     print(i*2, "" , i*3,"",i*4,"",i*5, "",i*6,"",i*7,"",i*8,"",i*9,"",i*10,"")
#     print("=============================================================================")

# for j in range(1,11):
#     print(j*11, "", j*12 ,"",j*13, "" ,j*14,"",j*15,"",j*16,"",j*17,"",j*18,"",j*19,"",j*20)

#28

# list3=[10,20,30,40,50]

# for i in list3: # in is membership operator we used 
#     print(i)

#29
# list=[1,2,3,4,5,6,7,8,9,10]
# sum=0  #sum=10
# for x in list: #x=3:4
#     sum=sum+x
# print("The sum=",sum )

#30

# mycart=[10,20,300,800,80,700,25]
# for i in mycart:
#     if i>400:
#         print("This is my purchased cart item")
#         # continue  #it means bypass next things
#         break # this terminate the loop 
#         print(i)

#31

# count = 0
# for i in range(9):
#     if i%2 == 0: #% modulus print reminder in screen 
#         print(i)
#     else:
#         print(i)
#         count +=1
#     print("count=",count)   

#32

# rollno =[3,5,6,1,11,4,5,2]
# for x in rollno:
#     if x==2 or x==4 or x==6 or x==8 or x==10:
#         print("even no is found", x)
#         break

#33
# Program to check if a given day is weekend or working day

# days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

# day = input("Enter a day (mon-sun): ").lower()

# for d in days:
#     if day == d:
#         if d in ["sat", "sun"]:
#             print("Weekend")
#         else:
#             print("Working day")
#         break
# else:
#     print("Invalid day entered!")

#34

# day = input ("Enter Day")
# if day =="Saturday" or day=="Sunday":
#     print("weekend")
# else:
#     print("Working Day ")

#35

# print(3/2)
# print(3//2) 

#36
# num=123 
# a= num %10
# num = num // 10
# b =num%10
# c= num // 10
# rev = a*100 + b*10 + c*1

# print("reverse=",rev) #1234567

#37
# num = 1234567
# rev = 0

# while num > 0:
#     a = num % 10        # last digit
#     rev = rev * 10 + a  # build reverse
#     num = num // 10     # remove last digit

# print("reverse =", rev)

#38

# Amount = int(input("please enter amount for withdraw:"))
# print("100 notes:",Amount //100)
# print("50 notes:",(Amount % 100) // 50)
# print("20 notes:",((Amount %100)%50)//20)
# print("10 notes:",(((Amount %100)%50)%20)//10)
# print("5 notes:",((((Amount %100)%50)%20)%10)//5)

#39 nested if‑else

# age1 = int(input("Enter first age: "))
# age2 = int(input("Enter second age: "))
# age3 = int(input("Enter third age: "))

# if age1 > age2:
#     if age1 > age3:
#         print("Maximum age is:", age1)
#     else:
#         print("Maximum age is:", age3)
# else:
#     if age2 > age3:
#         print("Maximum age is:", age2)
#     else:
#         print("Maximum age is:", age3)

#40 if‑elif‑else
# ch = input("Enter any one character: ")

# if ch.isupper():
#     print("Entered character is UPPER CASE")
# elif ch.islower():
#     print("Entered character is LOWER CASE")
# elif ch.isdigit():
#     print("Entered character is DIGIT")
# else:
#     print("Entered character is SPECIAL SYMBOL")

#41 new way we solved the probelm no 40:

# ch =ord(input("Enter any character:"))
# if ch>=65 and ch<91:
#     print("upper case")
# elif ch>=97 and ch<=122:
#     print("lower case")
# elif ch>=48 and ch<=57:
#     print("digit")
# else:
#     print("special symbol")

#42

# username= input("Enter Username:")
# paasword = input("Enter Password:")
# if username == password:
#     print("login successfully")
# else:
#     print("Invalid Login")

#43
# username = input("Enter Username: ")
# password = input("Enter Password: ")

# # Correct credentials set (for example)
# correct_username = "Laxmi"
# correct_password = "12345"

# while username != correct_username or password != correct_password:
#     print("Invalid Login! Please try again.")
#     username = input("Enter Username: ")
#     password = input("Enter Password: ")

# print("Login successfully!")

#44
s="Laxmi is student"
print(s.find("Laxmi"))
print(s.find("python"))
print(s.find ("is")) #find function return starting index number of string if it is found else if string doesnt exist then it return-1

######################################

#JOIN FUNCTION

#45

# s= "laxmi","ketan","divya"
# m = '|'.join(s)
# print(m)

#46
# s= "laxmi","ketan","divya"
# m = '@'.join(s)
# print(m)

#47

# s= "Python is a High level programming Language"
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())

# print('Subjects Marks :')
# phy = 50
# chem = 60
# math =70
# print("physics ={} chemistry={} Math={} ".format(phy, chem, math))
# print("physics = {0} chemistry={1} Math={2} ".format(phy, chem, math))
# print("physics = {x} chemistry={y} Math={z} ".format(x=phy,y=chem,z=math))
# total = phy+chem+math
# print("Total Marks", f"{total} ")
# print("Roll No=", "7".zfill(4))

#48
# name="help4code"
#      #012345678
# for i in name:
#     print(i)

#49
# name="Laxmi"
# i=0
# for x in name:
#     if x == 'x':
#         print("The character present at index no ",i," value=:",x)
#         break
#     i=i+1

#50
# a='shiwaleew'
# for i in a:
#     if i=='w':
#         print(i)

#51

# x=['A','B','C']
# y=['A','B','C']
# z=[1,2,3,4]
# print(x==y)
# print(x==z)
# print(x !=z)

#52
# #BODMAS
# a=50
# b=30
# c=20
# d=10
# print((a+b)*c/d)
# print((a-b)*(c/d))
# print(a+(b*c)/d)

#53
#removing space in string 

# city=input("Enter your city Name:")
# scity=city.strip()
# if scity=='Hyderabad':
#     print("Hello Hyderbadi..Adab")
# elif scity=='Chennai':
#     print("Hello Madrasi....Vanakkam")
# elif scity=="Bangalore":
#     print("Hello Kannadiga...Shubhodaya")
# else:
#     print("your entered city is invalid")

#54

#s.replace(oldstring,newstring)
# s=""
# s1=s.replace("difficult","easy")
# print(s1)
# s="ababababababab"
# s1=s.replace("a","b")
# print(s1)

#55

s = 'gasgg54@#vscsd!s*'

# count = 0
# for ch in s:
#     if not ch.isalnum():
#         count += 1
# print(count)