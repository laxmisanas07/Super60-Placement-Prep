# #day 3 of super60 batch the topic from dsa

# #first
# a = int(input("Enter the value of A: "))
# b = int(input("Enter the value of B: "))
# try:
#     print(a / b)
# except ZeroDivisionError:
#     print("cant divided by zero")
# except ValueError:
#     print("Enter on;y integer value ")
# print("Continue")

# #second

# a = int(input("Enter the value of A: "))
# b = int(input("Enter the value of B: "))
# try:
#     print(a / b)
# except ZeroDivisionError as message:
#     print("cant divided by zero:",message)
# except ValueError as message:
#     print("Enter on;y integer value:", message )
# print("Continue")

# third

# Handling multiple different kinds of exception 
# single except block 
# try:
#     a = int(input("Enter the value of A: "))
#     b = int(input("Enter the value of B: "))
#     print(a/b)
# except (ValueError, ZeroDivisionError) as message:
#     print(message)   #the value error are shows when you enter the value with the $ sign like ("invalid literal for int() with base 10: '$'")

# fourth

# imp: if we have requirement of  multiple except nlock then
# in that switiation default expcet block
# should be i last other wise syntax error will encounter
# from email import message


# try:
#         a = int(input("Enter the value of A: "))
#         b = int(input("Enter the value of B: "))
#     print(a/b)
# except:
#     print("this is defalut part of except block")
# except (ValueError, ZeroDivisionError) as message:
#     print("Enter correct no:", message)  


# fifth
# we can use else block id no error will generate 
# it is depend on our own need and neccessity

# try:
#      a = int(input("Enter the value of A: "))
#      b = int(input("Enter the value of B: "))
#      print(a 4/ b)
# except (ValueError, ZeroDivisionError) as message:
#     print("Enter correct no:", message)  
# else:
#     print("everything is okay")
       

# sixth

# try:
#      a = int(input("Enter the value of A: "))
#      b = int(input("Enter the value of B: "))
#      print(a / b)
# except (ValueError, ZeroDivisionError) as message:
#     print("Enter correct no:", message)  
# finally:
#     print("I will always executed")

# seventh

# try:
#     a = int(input("Enter the value of A: "))#4
#     b = int(input("Enter the value of B: "))#0

#     try:
#         print(a / b)
#     except ZeroDivisionError as message:
#         print(message)

# except ValueError as message:
#     print(message)

# 8th

# # try block: Code that may raise an exception
# try:
#     # Take input from the user
#     a = int(input("Enter the value of A: "))
#     b = int(input("Enter the value of B: "))

#     # Perform division
#     print(a / b)

# # except block: Executes if ValueError or ZeroDivisionError occurs
# except (ValueError, ZeroDivisionError) as message:
#     print(message)

# # else block: Executes only if no exception occurs in the try block
# else:
#     print("No error")

# # finally block: Always executes, whether an exception occurs or not
# finally:
#     print("Always executed")


# 10th
# python logging level 

# import logging 
# logging.basicConfig(filename="newfile.txt",level=logging.DEBUG) 
# logging.debug("this indicates the debugging information") 
# logging.info("this indicates the important information") 
# logging.error("this indicates the error information") 
# logging.warning("this indicates the warning infromation") 
# logging.critical ("this indicates the critical information")

# 11th

# import logging

# logging.basicConfig(
#     filename="arithmatic.txt",
#     level=logging.DEBUG
# )

# try:
#     a = int(input("Enter first integer: "))
#     b = int(input("Enter second integer: "))

#     print(a / b)

# except (ZeroDivisionError, ValueError) as message:
#     print(message)
#     logging.exception(message)

# print("Logging level is set up. Check 'arithmatic.txt' for log details.")

# # #12th 
# (WAP to accept three paper marks (Physics, Chemistry, Math), calculate total and percentage, and display them.

# Conditions:

# If the student passes all subjects (passing marks = 40), print "Pass", otherwise print "Fail".
# If percentage >= 65 and gender is male, print "Eligible for Placement", otherwise print "Not Eligible for Placement".)
# # the question is given by sir

# # Accept marks
# phy = int(input("Enter Physics marks: "))
# chem = int(input("Enter Chemistry marks: "))
# math = int(input("Enter Mathematics marks: "))

# # Accept gender
# gender = input("Enter Gender (Male/Female): ").lower()

# # Calculate total and percentage
# total = phy + chem + math
# percentage = total / 3

# # Display result
# print("\nTotal Marks =", total)
# print("Percentage = {:.2f}%".format(percentage))

# # Pass or Fail
# if phy >= 40 and chem >= 40 and math >= 40:
#     print("Result: PASS")
# else:
#     print("Result: FAIL")

# # Placement Eligibility
# if percentage >= 65 and gender == "male":
#     print("Eligible for Placement")
# else:
#     print("Not Eligible for Placement")

# ##########################################################################################

# DSA STARTS NOW:

# DSA: data stucture is a different ways of organizing a data on your computer , that can be used effectively.


# menu access 1st ex
# import sys 

# def add():
#     a = int(input("Enter value of A:"))
#     b= int(input("Enter value of B:"))
#     print(a+b)

# def sub():
#     a = int(input("Enter value of A:"))
#     b= int(input("Enter value of B:"))
#     print(a-b)

# def mul():
#     a = int(input("Enter value of A:"))
#     b= int(input("Enter value of B:"))
#     print(a*b)

# def div():
#     a = int(input("Enter value of A:"))
#     b= int(input("Enter value of B:"))
#     print(a/b)
     
# while True:
#     print("1.Addition")
#     print("2 Subtraction")
#     print("3 Multiplication")
#     print("4. Division")
#     print("5. Exit")

#     choice = int(input("Enter Your choice :"))
#     if choice == 1:
#         add()#calling fun
#     elif choice == 2:
#         sub()
#     elif choice == 3:
#         mul()
#     elif choice == 4:
#         div()
#     elif choice == 5:  # worked for the exit or similar to the break keyword using "import the sys" 
#         sys.exit()

# example 2nd

# def product_except_self(nums):
#     n = len(nums)
#     result = [1] * n

#     # Calculate left products
#     left = 1
#     for i in range(n):
#         result[i] = left
#         left *= nums[i]

#     # Calculate right products
#     right = 1
#     for i in range(n - 1, -1, -1):
#         result[i] *= right
#         right *= nums[i]

#     return result


# # Example 3rd ex
# nums = [1, 2, 3, 4]
# print(product_except_self(nums))

# stack implementation with size limit 
#code made in class 

# import sys
# class stack:
#  def __init__(self,stackSize):
#         self.stackSize = stackSize # stack size is define
#         self.mystack =[] #list rep stack 
#         print("Stack has created")

#  def push(self,value):
#       pass
 
#  def isFull(self):
#      if len(self.mystack) == self.stacksize:
#          return True
#      else:
#          return False
     
#      def isEmpty(self):
#          if self.mystack == []:
#              return True
#          else:
#              return False
        
     
#      def push(self,value):
#          if self.isFull():
#              print("Stack is full")
#          else:
#             self.mystack.append(value)
     
#      def display(self):
#          if self.isEmpty():
#              print("Stack is empty")
#          else:
#             print("Stack=",self.mystack)
    
#      def pop(self):
#         if self.isEmpty():
#          print("Stack is empty")
#         else:
#          print(self.mystack.pop())
        
#      def peek(self):
#         if self.isEmpty():
#          print("Stack is empty")
#         else:
#          print(self.mystack[-1])

#      def deletestack(self):
#         self.mystack = None

  
# size = int(input("Enter the size of stack:"))
# obj = stack(size)

# while True:

#   print("1. Push")
#   print("2.Dispaly")
#   print("3. Pop")
#   print("4. peek")
#   print("5. delete stack")
#   print("6.Exit")
#   choice = int(input("enter your choice"))
#   if choice == 1:
#       value = int(input("Enter the value to push into stack:"))
#       obj.push(value) 
#   elif choice == 2:
#       obj.display()
#   elif choice == 3:
#       obj.pop()
#   elif choice == 4:
#       obj.peek()
#   elif choice == 5:
#       obj.deletestack()
#   elif choice == 6:
#       sys.exit()

      
#previous solved code:

# import sys

# class stack:
#     def __init__(self, stackSize):
#         self.stackSize = stackSize
#         self.myStack = []
#         print("Stack has been created")

#     def isFull(self):
#         return len(self.myStack) == self.stackSize

#     def isEmpty(self):
#         return len(self.myStack) == 0

#     def push(self, value):
#         if self.isFull():
#             print("Stack is full")
#         else:
#             self.myStack.append(value)

#     def display(self):
#         if self.isEmpty():
#             print("Stack is empty")
#         else:
#             print("Stack =", self.myStack)

#     def pop(self):
#         if self.isEmpty():
#             print("Stack is empty")
#         else:
#             print("Popped:", self.myStack.pop())

#     def peek(self):
#         if self.isEmpty():
#             print("Stack is empty")
#         else:
#             print("Top element:", self.myStack[-1])

#     def deletstack(self):
#         self.myStack = []
#         print("Stack deleted")


# size = int(input("Enter the size of stack: "))
# obj = stack(size)

# while True:
#     print("\n1. Push")
#     print("2. Display")
#     print("3. Pop")
#     print("4. Peek")
#     print("5. Delete Stack")
#     print("6. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         value = int(input("Enter value: "))
#         obj.push(value)

#     elif choice == 2:
#         obj.display()

#     elif choice == 3:
#         obj.pop()

#     elif choice == 4:
#         obj.peek()

#     elif choice == 5:
#         obj.deletstack()

#     elif choice == 6:
#         sys.exit()

#     else:
#         print("Invalid choice")


#new code

print('laxmisanas777'.isalnum())      # True

print('laxmisanas'.isalpha())         # True

print('777f'.isdigit())               # False

print('laxmisanas'.islower())         # True

print(''.islower())                   # False

print('LAXMISANASl'.isupper())        # False

print('My Name Is Laxmisanas'.istitle())   # True

print(''.istitle())                   # False

print(''.isspace())                   # False

print("Hello".startswith("He"))       # True

print("Hello".endswith("lo"))         # True