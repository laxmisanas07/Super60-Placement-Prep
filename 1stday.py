None selected 

Skip to content
Using Gmail with screen readers
1 of 5,430
(no subject)
Inbox

Ketan Zode
Attachments
10:35 AM (8 minutes ago)
to me

uuummmm
 One attachment
  •  Scanned by Gmail
# 1
# a=[1,2,3,4,5,6,7,8,9]
# print(a[::2])

# 2
# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60
# print(a)

# 3
# problem to find the security key (count of repeating digits)
# n = input()
# d=[]
# for i in n:
#     if i in d:
#         d[i]+= 1
#     else:
#         d[i]=1

# count=0

# for value in d.values():
#     if value >1:

# if count == 0:
#     print(-1)
# else:
#     print(count)            

# 4
# a=[1,2,3,4,5]
# print(a[3:0:-1])#

# 5

# def func(value, values):
#     var = (this is half code)

# 6

# arr = [[1,2,3,4],
#        [4,5,6,7],
#        [8,9,10,11],
#        [12,13,14,15]]
# for i in range(0,4): #i=2
#     print(arr[i].pop())

# 7
# def f(i, values =[]):
#     values.append(i)
#     print (values)

# f(1) #calling funt
# f(2)
# f(3)


# 8
# arr=[1,2,3,4,5,6]
# for  i in range(1,6):
#     arr[i-1] = arr[i]
# for i in range(0,6):
#     print(arr[i], end = " ") 

# 9

# fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]

# fruit_list2[0] = 'Guava'
# fruit_list2[1] = 'Kiwi'

# sum = 0

# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     if ls[0] == 'Guava':
#         sum += 1
#     if ls[1] == 'Kiwi':
#         sum += 20

# print(sum)

# 10
# for i in range(1, 6):
#     print(i, 6 - i)

# 10 2nd way 

# for i, j in zip(range(1,6),range(5,0,-1)):
#     if i ==3 and j ==3:
#         continue
#     print(i, "" ,j)

# 11

# init_tuple = ()
# print(init_tuple._len_())

# 12
# Compare two tuples

# init_tuple_a = ('a', 'b')
# init_tuple_b = ('a', 'b')

# print(init_tuple_a == init_tuple_b)

# 13
# 1= [1,2,3]
# init_tuple = ('python',) * (1._len_() - 1[::-1][0])
# print(init_tuple)

# 14
# a= {(1,2):1,(2,3):2,(4,5):3}
# print(a[4,5])

# 15
# a= {'a':1,'b':2,'c':3}
# print (a ['a','b'])

# 16
# fruit = {}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1  #     
# addone('Apple') 
# addone('Banana')
# addone('apple')  
# print(len(fruit))     

# 17                                                   ,,,,,,,,,,,,
# arr = {}
# arr[1] = 1 
# arr['1'] = 2
# arr[1] += 1

# sum = 0 #4
# for k in arr: #'1'
#     sum += arr[k]
# print(sum)

# 18
# my_dict = {}
# my_dict[1] = 1
# my_dict['1'] = 2
# my_dict[1,0] = 4
# print(my_dict)
# sum=0


# 19

# my_dict = {}

# my_dict[(1, 2, 4)] = 8
# my_dict[(4, 2, 1)] = 10
# my_dict[(1, 2)] = 12

# sum = 0

# for k in my_dict:
#     sum += my_dict[k]

# print(sum)
# print(my_dict)

# 20














# 21
# dict = {'c': 97, 'a': 96, 'b': 98}
# for _ in sorted(dict):
#     print (dict[_])


# 22
# math = 50
# chem = 60
# phy =  60
# print(id(math))
# print(id(chem))
# print(id(phy))

# 23
# rec = {"Name" : "Python", "Age": "20"}
# r = rec.copy()
# print(id(r) == id(rec))

# 24
# rec = {
#     "Name": "Python",
#     "Age": 25,
#     "Addr": "NJ",
#     "Country": "USA"
# }

# id1 = id(rec)

# del rec

# rec = {
#     "Name": "Python",
#     "Age": 25,
#     "Addr": "NJ",
#     "Country": "USA"
# }

# id2 = id(rec)

# print(id1 == id2)




# TYPECASTING 

# 1
# print(int(3.14))
# print(int(True))
# print(int(False))
# print(int("4"))

# 2
# print(float(3))
# print(float(True))
# print(float(False))
# print(float(4.22))
# print(float("4"))

# 3 true and false

# print(bool(0))
# print(bool(15))
# print(bool(3.14))
# print(bool(0.0))
# print(bool(1+2))
# print(bool(0+0))


# 4  zero to the end 

# arr = [1, 2, 8, 3, 0, 7, 0, 3, 9]
# arr = [i for i in arr if i != 0] + [0] * arr.count(0)
# print(arr)

# 4 2nd way 
# val = [0,1,0,3,12]
# for i in val:
#     if i == 0:
#         val.remove(i)
#         val.append(i)
# print(val)        

#5

# arr1 = [1,2,3]
# arr2 = [2,3,4]
# arr3 = [3,4,5]
# result = list(set(arr1) & set(arr2) & set(arr3))
# print(result)

# 6
# A= [1,1,0,1,1,1,0,1,1,1,1]
# count =0 
# max =0 
# for i in A:
#     if i == 1:
#         count +=1
#     else:
#         count = 0
# print(max)            

# 7

# lst = eval(input())

# if lst == lst[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindome")
    

# 8  revers string code
# s= input()
# print(s[::-1])

# 8 2nd task 
# name ="hello"
# N =len(name)-1
# newname
# for i in range(N, -1,-1):
#     newname += name[i]
#     print(newname)

# 9 remove duplication string   (error)

# s= input()
# r =""

# for i in r:
#    lmmif i not in r:
#      r+=i

# print(r)

# 10

# n= int(input())
# arr= list()
training examples.py
Displaying training examples.py.