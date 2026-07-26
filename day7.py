# #1
# # Encapsulation
# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.__balance = balance   # private attribute

#     def deposit(self, amount):
#         self.__balance += amount
#         return f"Deposited {amount}, Balance: {self.__balance}"

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             return f"Withdrew {amount}, Balance: {self.__balance}"
#         else:
#             return "Insufficient funds"

#     def get_balance(self):
#         return self.__balance


# # Inheritance
# class SavingsAccount(BankAccount):
#     def add_interest(self, rate):
#         interest = self.get_balance() * rate
#         self.deposit(interest)
#         return f"Interest added: {interest}, Balance: {self.get_balance()}"


# # Polymorphism (Method Overriding)
# class CurrentAccount(BankAccount):
#     def withdraw(self, amount):
#         # Allow overdraft up to 500
#         if amount <= self.get_balance() + 500:
#             self._BankAccount__balance -= amount
#             return f"Withdrew {amount}, Balance: {self.get_balance()}"
#         else:
#             return "Overdraft limit exceeded"


# # Demonstration
# savings = SavingsAccount("Laxmi", 1000)
# print(savings.deposit(500))          # Encapsulation
# print(savings.add_interest(0.05))    # Method Overloading

# current = CurrentAccount("Laxmi", 200)
# print(current.withdraw(600))         # Polymorphism (overridden withdraw)


#2 : Linkedlist in data sturcture 
#static node we execute now:

# class Node:
#     def __init__(self,value):
#         self.data = value #instance var :it depdence on obj its create each and every obj 
#         self.next = None  #(10)

# class LinkedList:
#     def __init__(self):
#         self.head = None  #head indicate the starting node 

# #object creation 
# linkedlist =LinkedList()

# #creating a node 
# linkedlist.head = Node(10) #1st node
# second          = Node(20)
# third           = Node(30)
# fourth          = Node(40)

# #connectiong nodes

# linkedlist.head.next = second
# second.next = third
# third.next = fourth

# #display linkedlist 

# #while loop when used we dont know the loop 

# while linkedlist.head != None:
#     print("|",linkedlist.head.data,"|",linkedlist.head.data,"|","->", end ="")
#     linkedlist.head = linkedlist.head.next

    
# #Tree implementation 

#3 real life ex of tree: the file system on a computer,oraganization structure, xml/html data.
#tree you can implement through also the linkedlist


class TreeNode:
    def __init__(self, data, children=None):
        self.data = data
        self.children = children if children is not None else []

    def __str__(self, level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 2)   # spacing for children
        return ret

    def addChild(self, node):
        self.children.append(node)


# Build tree
root = TreeNode("Drinks")

hot = TreeNode("Hot")
cold = TreeNode("Cold")

tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
non_alcoholic = TreeNode("Non-alcoholic")
alcoholic = TreeNode("Alcoholic")

# Attach children
root.addChild(hot)
root.addChild(cold)

hot.addChild(tea)
hot.addChild(coffee)

cold.addChild(non_alcoholic)
cold.addChild(alcoholic)1

# Print tree
print(root)

#4
