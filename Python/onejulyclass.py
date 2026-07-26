# # # # var = [7,3,9,2,8]
# # # # var.sort()
# # # # print(var)
# # # # print(var[-2])
# # # # 1st largest no

# # # #2nd Program to find the security key :
# # # # n = input()
# # # # d = {}

# # # # for i in n:
# # # #     if i in d:
# # # #         d[i] += 1
# # # #     else:
# # # #         d[i] = 1

# # # # count = 0

# # # # for value in d.values():
# # # #     if value > 1:
# # # #         count += 1

# # # # if count == 0:
# # # #     print(-1)
# # # # else:
# # # #     print(count)

# # # #Q-1
# # # # a=[1,2,3,4,5,6,7,8,9]
# # # # print(a[::2])   #output:[1, 3, 5, 7, 9]


# # # #Q-2
# # # # a=[1,2,3,4,5,6,7,8,9]
# # # # a[::2]=10,20,30,40,50,60
# # # # print(a)       #error:ValueError: attempt to assign sequence of size 6 to extended slice of size 5 ("Just bez the value incress by 2 so the size issue occure")


# # # #Q-3

# # # # a=[1,2,3,4,5]
# # # # print(a[3:0:-1]) #output:[4, 3, 2]


# # # #Q-4:

# # # # def func(value, values)  "PENDING"
    
# # # #Q-5:
# # # arr = [[1,2,3,4],
# # #       [2,4,5,6,7],
# # #       [8,9,10,11],
# # #       [12,13,14,15]]

# # # for i in range(0,4):
# # #     print(arr[i].pop())

# # #     Output:
# # # 4
# # # 7
# # # 11
# # # 15

# # #Q-6

# # # def f(i,values=[]):
# # #     values.append(i)
# # #     print(values)
# # # f(1)
# # # f(2)
# # # f(3) #output:
# # # [1]
# # # [1, 2]
# # # [1, 2, 3]

# # #Q-7

# # arr = [1,2,3,4,5,6]
# # for i in range (1,6):
# #     arr[i - 1] = arr[i]
# # for i in range (0,6):
# #     print(arr[i],end=" ")  #output:2 3 4 5 6 6 


# # #Q-8

# # f_l1=['Apple', 'Berry', 'Cherry','Papaya']


# #solving question the output expected:
# # 1 5
# # 2 4
# # 3 3
# # 4 2
# # 5 1
# # #1st way

# # for i in range(1,6):
# #     print(i, 6 - i)

# # #2nd way

# # for i, j in zip(range(1,6),range(5,0,-1)):
# #     if i == 3 and j == 3:
# #      continue
# # print(i, "", j)

# # #Q--9

# # l=[1,2,3]
# # init_tuple = ('python',) * (l._len_()) - l[::-1][0])
# # print(init_tuple)

# # #Q-10
# # a = {(1,2):1,(2,3):2,(4,5):3}
# # print(a[4,5])

# #Q-11

# # a = {'a':1,'b':2,'c':3}
# # print (a['a','b'])

# # fruit = {}
# # def addone (index):
# #     if index in fruit:
# #         fruit[index] +=1
# #     else:
# #         fruit[index] = 1  #{'Apple':1,'Banana':1,'apple':1} thats why the answer is 3 occures in the system
# # addone('Apple')
# # addone('Banana')
# # addone('apple')
# # print(len(fruit))    


# #Q=12
# arr ={}
# arr[1] =1
# arr['1']=2
# arr[1] += 1
# sum = 0
# for k in arr:
#     sum += arr[k]
# print(sum)   #output:4


# #Q=13
#  my_dict = {}
#  my_dict[1] =1
#  my_dict['1']=2
#  my_dict[1.0] = 4
#     print(my_dict)
#  sum = 0
#  for k in my_dict:
#      sum += my_dict[k]
#     print(sum)   //Not run the code so execute it double



# #reverse string 
# name="hello"
# N =len(name)-1
# newename =""
# for i i    print(r)




my_dict = {}
my_dict[1] =1
my_dict['1'] =2
my_dict[1.0] =4
print(my_dict)
sum =0
for k in my_dict:
    sum += my_dict[k]
    print(sum)