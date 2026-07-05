# # #day 5 dictionary:

# # #1
# # # mydict={
# # #     101:"Laxmi",
# # #     102:"Ketan",
# # #     "103":"Avanti",
# # #     "104":"Gopika",
# # #     101:"ananda",
# # #     104:"ananda"
# # # }
# # # print(mydict)
# # # print(type(mydict))
# # #with the help of key we have to print values 

# # #2
# # # a = mydict[102]
# # # print(a)

# # #3
# # #we will replace old value by new value
# # # mydict[102]="Kanha"
# # # print(mydict)

# # #4
# # #only print key x=0,1
# # # for x in mydict:
# # #     print(x)

# # #5
# # #only print values x=0
# # for x in mydict.values():
# #     print(x)

# # #6
# # #printitng key and values both
# # # for x,y in mydict.values():
# # #     print(x,y)

# # #7
# # #if i have to ad new key and value pair in my dictionary
# # # mydict["mobile_no"]=4646467878
# # # print(mydict)

# #8
# mydict = {
#     101: "Laxmi",
#     "Professional":"developer",
#     "empid": 1001
# }
# mydict.pop(101)
# print(mydict)

# #9
# mydict = {
#     "name": "Laxmi",
#     "Professional":"developer",
#     "empid": 1001
# }
# newdict = mydict.copy()
# print(newdict)

#10
# def is_empty(d):
#     if not d:   # yaad rakho: bas ek hi condition
#         print("Empty")
#     else:
#         print("Not Empty")

# # Test
# is_empty({})                # Output: Empty
# # is_empty({"name": "Laxmi"}) # Output: Not Empty

#11

# def max_value_key(d):
#     max_key = None
#     max_val = float('-inf')   # sabse chhoti possible value se start

#     for key, value in d.items():
#         if value > max_val:   # agar current value badi hai
#             max_val = value
#             max_key = key

#     return max_key

# # Test
# data = {"A": 50, "B": 30, "C": 70}
# print(max_value_key(data))   # Output: "C"

#12

# Function to find common key-value pairs in two dictionaries

# def common_key_value_pairs(dict1, dict2):
#     common = {}

#     for key in dict1:
#         if key in dict2 and dict1[key] == dict2[key]:
#             common[key] = dict1[key]

#     return common


# # Sample Input
# dict1 = {"A": 1, "B": 2, "C": 3}
# dict2 = {"B": 2, "C": 4, "D": 5}

# # Function Call
# result = common_key_value_pairs(dict1, dict2)

# # Output
# print(result)

#13
# Function to reverse a dictionary

# def reverse_dictionary(d):
#     reversed_dict = {}

#     for key, value in d.items():
#         reversed_dict[value] = key

#     return reversed_dict


# # Sample Input
# d = {"A": 1, "B": 2, "C": 3}

# # Function Call
# result = reverse_dictionary(d)

# # Output
# print(result)

#__________________________________________________#

#File Handling:Linear search:

#___________________________________________________#
#14
# def linearsearch(array,target):
#     for i in range(len(array)):#i=0
#         if array[i] == target:
#             return i
      
#     return -1

# array=[1,2,3,4,5,6,7,8,9]
# target = 7
# result= linearsearch(array,target)#calling function

# if result != -1:
#     print("element found at index no:",result)
# else:
#     print("Element not found")

#15

# def find_min_max(arr):
#     min_val = arr[0]
#     max_val = arr[0]

#     for num in arr:
#         if num < min_val:
#             min_val = num
#         if num > max_val:
#             max_val = num
#         print(f"Checking {num} -> min={min_val}, max={max_val}")  # use -> instead of →

#     return max_val, min_val

# arr = [5, 3, 9, 2, 8]
# max_val, min_val = find_min_max(arr)
# print("Final Result -> Max:", max_val, "Min:", min_val)

#16 

# f = open("myfile.txt","w")
# print("name of file:",f.name)
# print("file mode",f.mode)
# print("readable",f.readable())
# print("writeable",f.writable())
# print("file is closed:",f.closed)

# f.close()
# print("file closed:", f.closed)

#17

# f = open("myfile.txt", "w")
# f.write("\n Nashik ")
# f.write("\n pune")
# f.write("\n Nagpur")
# f.write("\n shirdi")
# f.write("\n indore")
# f.close()
# print("file operation are done ")

#18

# f = open("myfile.txt", "a")
# f.write("\n Nashik ")
# f.write("\n pune")
# f.write("\n Nagpur")
# f.write("\n shirdi")
# f.write("\n indore")
# f.close()
# print("file operation are done ")

#19
# f = open("newfile.txt","w")
# mylist=["Laxmi","Ananda","Sanas"]
# f.writelines(mylist)
# f.close()
# print("written work has done successfully")

#20
# f = open("myfile.txt","r")
# print(f.read())
# f.close()

# #21
# f = open("newfile.txt","r")
# print(f.read())
# f.close()

#22
# with open("myfile.txt","w") as f:
#     f.write("laxmi\n")
#     f.write("laxmi\n")
#     f.write("laxmi\n")
#     print("file closed:",f.closed)
# print("file closed:",f.closed)

#23

# f1.open("Guide.png","rb")
# f2.open("Rossom.jpg","wb")
# data = f1.read()
# f2.write(data)

#24 csv files :

# import csv
# f=open("student.csv","a",newline="")
# a= csv.writer(f)
# #a.writerow(["studentID","rollno","name","mobileno"])  #used for creating the column 

# studentID = int(input("Enter the student id:"))
# rollno = int(input("Enter the roll no:"))
# name= input("enter the name:")101
# mobileno = int(input("enter the mobile no:"))

# a.writerow([studentID,rollno,name,mobileno])
# print("Student record has save ")

#25
# import csv

# # open the file in append mode
# f = open("newstudent.csv", "a", newline="")
# a = csv.writer(f)

# # write header only once (optional, you can comment this out after first run)
# a.writerow(["rollno","name","mobileno","p1","p2","p3","total","percentage","email","result"])

# # input student details
# rollno = int(input("Enter the roll no: "))
# name = input("Enter the name: ")
# mobileno = int(input("Enter the mobile no: "))
# p1 = int(input("Enter the p1: "))
# p2 = int(input("Enter the p2: "))
# p3 = int(input("Enter the p3: "))
# email = input("Enter the email: ")

# # calculate total and percentage
# total = p1 + p2 + p3
# percentage = total / 3

# # check pass/fail condition
# if p1 >= 40 and p2 >= 40 and p3 >= 40:
#     result = "Pass"
#     print("you are pass")
# else:
#     result = "Fail"
#     print("you are fail")
# # save record into CSV
# a.writerow([rollno, name, mobileno, p1, p2, p3, total, percentage, email, result])
# print("Student record has been saved successfully.")
# f.close()

# #26
# class Queue:
#     def __init__(self, queueSize):
#         self.queueSize = queueSize
#         self.myQueue = []

#     def isFull(self):
#         if len(self.myQueue) == self.queueSize:
#             return True
#         else:
#             return False

#     def isEmpty(self):
#         if len(self.myQueue) == 0:
#             return True
#         else:
#             return False

#     def enQueue(self, value):
#         if self.isFull():
#             print("Queue is Full")
#         else:
#             self.myQueue.append(value)
#             print(value, "Inserted")

#     def deQueue(self):
#         if self.isEmpty():
#             print("Queue is Empty")
#         else:
#             print(self.myQueue.pop(0), "Deleted")

#     def frontpeek(self):
#         if self.isEmpty():
#             print("Queue is Empty")
#         else:
#             print("Front Element :", self.myQueue[0])

#     def deleteQueue(self):
#         self.myQueue.clear()
#         print("Queue Deleted")

#     def display(self):
#         if self.isEmpty():
#             print("Queue is Empty")
#         else:
#             print("Queue :", self.myQueue)


# size = int(input("Enter the size of Queue : "))
# queObj = Queue(size)

# while True:
#     print("\n1. enQueue")
#     print("2. display")
#     print("3. deQueue")
#     print("4. frontpeek")
#     print("5. delete Queue")
#     print("6. Exit")

#     choice = int(input("Enter your choice : "))

#     if choice == 1:
#         value = int(input("Enter value to add in queue : "))
#         queObj.enQueue(value)

#     elif choice == 2:
#         queObj.display()

#     elif choice == 3:
#         queObj.deQueue()

#     elif choice == 4:
#         queObj.frontpeek()

#     elif choice == 5:
#         queObj.deleteQueue()

#     elif choice == 6:
#         print("Program Exited")
#         break

#     else:
#         print("Invalid Choice")