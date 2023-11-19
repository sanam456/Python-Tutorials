# print('hel world\nline2')
# print('name\tSana')
# print("g\\") 
# print('s\\s')
# print("\\\"\\\'")
# print("this is \\\\ double")
# print("this is /\\/\\")
# print("he is \t awesome")
# print(r"\\\" \\n \\t \\\'")
# print(2/3)
# print(4//2)
# print(2**0.5)
# print(round(2**0.5, 4))
# # print(2**3/2*6-4*(3-4/2))
# num1=2
# print(num1)
# name="Sana"
# print(name)
# print("
# hel" 'g')
# n1="sana"
# n2="jahangir"
# full_nam=n1 + " " +n2 
# print(full_nam)
# print(n1+" "+"3")
# n1=input("type ur name ")
# n2=input("type ur age ")
# print(n1 + n2)
# n1=int(input("enter no.1"))
# n2=int(input("enter no.2"))
# tot=n1+n2
# print("total is "+float(tot))
# number_1=int(input("enter the first number"))
# number_2=int(input('enter the second number'))
# number_3=number_1+number_2
# print("sum of the numbers is",number_3)
# n1=int(4)
# n2=float(5)
# print(n1+n2)
# name, age = "Sana", "27"
# print("hello "+ name + " your age is "+ age)
# name, age= input("enter your name and age ").split(",")
# print(name)
# print(age)
######string formatting
# name="sana"
# age=22
# print("hi {} your age is {}".format(name,age))
# print(f"hi {name} your age is {age+2}")
# num1,num2,num3=input("enter no.").split(",")
# avg= (int(num1)+int(num2)+int(num3))/3
# print(f"hi first no is {num1} second no is {num2}third no is {num3} and avg is {avg}")
###string indexing and slicing and step argument
# lan="sana"
# print(lan[-1])
# print(lan[0:2])
# print(lan[1:])
# print(lan[:3])
# print("Sana"[0:3:2])
# print("Sana"[0::2])
# print("Sana"[::2])
# print("Sana"[-3::-1])
#####string function and methods
# name= "Sana jah"
# print(len(name))
# print(name.lower())
# print(name.title())
# print(name.count("a"))
# name =input("enter your name: ")
# print(f"name is {name} and reverse is {name[::-1]}")
##print(f"length of {name.lower()} is len("name.lower()") and total characters {character.lower()} are name.lower().count(character.lower())")
# username, single_char = input("Enter username and a single char followed by comma: ").split(",")
# print(f"length is {len(username.lower())}")
# print(username.lower().count(single_char.lower()))
###strip method
# username, single_char = input("Enter username and a single char followed by comma: ").split(",")
# print(f"length is {len(username.strip().lower())}")
# # print(username.strip().lower().count(single_char.strip().lower()))
# ###replace find method
# str="I love you Allah and I will forever"
# print(str.replace("I","we"))
# # str_a1= str.find("a")
# print(str.find("a",str_a1+1)) ##count spaces too
##centre method
# nam="sana"
# print(nam.center(len(nam),"*"))
###strings are immutable
##operators
# nam=24
# nam+=1
# print(nam)
# ###if 
# age=int(input("enter age"))
# if age >= 14:
#     print("eligible")
# else:
#     print("sorry")
# import random
# n = random.randint(0,10)
# user_guess = int(input("enter any number between 0 and 10 : "))
# if n > user_guess : 
#     print("high")
# else :
#     if n < user_guess :
#         print("too low") 
#     else :
#         print("win")
# print(n)
# age=19
# nam=("Sana")
# n=print(nam.lower())
# if age ==49 or nam!="Sana":
#      print("eligible")
# else:
#      print("sorry")
# age=int(input("enter age"))
# nam=input("enter nam")
# n=nam[0]
# if age > 10 and (n=="a" or n=="A"):
#      print("eligible")
# else:
#      print("sorry")  
###else,elif
# age=int(input("enter age"))   
# if age==0 or age<0:
#     print("sorry")  
# elif 0<age<=3:
#     print("price:50")
# elif 3<age<=6:
#     print("price:100")
# else:
#     print("price:150")
###check empty
# nam=input("enter name")
# if nam:
#     print(f"your name is {nam}")
# else:
#     print("oye enter name")
# total=0
# num=int(input("enter number"))
# i=1
# while i<=num:
#     total+=i
#     i=i+1
#     print(total)
# total=0
# num=input("enter numbers") #1234
# length=len(num) #4
# i=0
# while i<length: #1<4
#     total=total+int(num[i])        #0+(1+2+3+4)
#     i=i+1
#     print(total)     
# total=0
# nam=input("enter name") #sana jahangir
# length=len(nam) #4
# i=0
# temp=""
# while i<length: #1<4
#     CHAR= nam.count(nam[i])     
#     print(CHAR)      #0+(1+2+3+4)
#     if nam[i] not in temp:
#        temp=temp+nam[i]
#        print(f"total of {nam[i]} is {CHAR}")     
#     i+=1
# name=input("enter name")
# I=0
# while I<len(name):
#         char=name[I]
#         print (name[I], name.count(char))
#         I+=1
####for loop
# for i in range(1,10):
#     print("sana")
#     print(i)
# tot=0
# for i in range(0,21):
#     tot+=i
# print(tot)
 ##break
# for i in range(0,10):   
#     if i==5:
#       continue   ##break
#     print(i)

# import random
# n = random.randint(0,11)
# for i in range(0,100):
#     user_guess = int(input("enter any number between 0 and 10 :")) 
#     if n<user_guess:
#       print("high")
#     elif n>user_guess:
#       print("low")
#     else:
#       print(f"you guesses right in {i} attempt")
#       break
###########DRY
# num=input("enter no.s")
# sum=0
# for i in num:
#   sum+=int(i)
#   print(sum)
###functions
# def add_two(a,b):
#   return a+b
# print(add_two(2,7))
# def last_char(name):
#   return name[-1]
# print(last_char("sana"))
# def odd_even(num):
#   if num%2!=0:
#     return("odd")
#   else:
#     return("even")
# print(odd_even(5))
# def odd_even(num):
#   if num%2==0:
#     return True
#   else:
#     return False
# print(odd_even(5))
# def is_even(num):
#   return num%2==0
# print(is_even(5))
# def song():
#   return "my song"
# print(song())
###function inside function call
# def greater(a,b):
#   if a>b:
#     return a
#   else:
#     if b>a:
#       return b
# def new_greater(a,b,c):
#   bigger=greater(a,b)
#   return greater(bigger,c)
# print(new_greater(11,10,7))
# name=("sana")
# def is_reversable(name):
#   if name[::]==name[::-1]:
#      print("true")
#   else:
#      print("false")
# print(is_reversable("sana"))
# def user_info(name="ali",age,weight=78):
#   print(f"name is {name} age {age} and weight {weight}")
# user_info("sana",23,26)
####LIST
#mixed=["sana",1,1.5,None,"A"]
# mixed=[1,9,7,10]
# f=[1,2,3]
# #mixed.sort()
# mixed.reverse()
# print(mixed)
# if "a" in mixed:
#   print("present")
# else:
#   print("not present")
# print(mixed[0:2])
# # mixed[2]="dost"
# # print(mixed)
# # mixed[:3]="dost"
# # print(mixed)
# # mixed[:3]=["dost",6]
# # print(mixed)
# # mixed.append('mango')
# # print(mixed)
# mixed.insert(1,'mango')
# f=["apples"]
# fm=mixed+f
# print(fm)
# mixed.extend(f)
# print(mixed)
# mixed.pop(2)
# print(mixed)
# del mixed[3]
# print(mixed)
###split join
# list="sana,24".split(",")
# print(list)
# list=["sana 24"]
# print(" ".join(list))
##list vs array vs string
# m=[[1,2,3],[4,5,6],[7,8,9]]
# for i in m:
#   for j in i:
#     print(j)
# n=list(range(1,11))
# print(n.index(10))
# def neg_list (list):
#     neg=[]
#     for i in list:
#         neg.append(-i)
#     return neg
# print(neg_list(n))
# ################
# n=[1,2,3]
# def sq_number (l):  ##l is argument
#     list=[]
#     for i in l:
#         list.append(i*i)
#     return list
# print(sq_number(n))
#####input list from user
# n=[1,2,3,6]
# def sq_number (l):  ##l is argument*
#      list1=[]
#      for i in range(len(l)):
#         poped=l.pop()
#         list1.append(poped)
#      return list1
# print(sq_number(n))
# n=["abc","efg","uyt"]
# def rev_word (l):  ##l is argument*
#      list1=[]
#      for i in l:
#         list1.append(i[::-1])
#      return list1
# print(rev_word(n))
# n=[1,2,3,4,5,6,7,8,9]    #Good
# def odd_even (l):  ##l is argument*
#      list1=[]
#      list2=[]
#      for i in l:
#         if i%2==0:
#             list1.append(i)
#         if i%2!=0:
#             list2.append(i)
#      return [list1,list2]
# print(odd_even(n))
# n1=[1,2,3,4,5,6,7,8,9]
# n2=[1,7,0,4]    #Good
# def odd_even (l1,l2):  ##l is argument*
#      list1=[]
#      list2=[]
#      for i in l1:
#         for j in l2:
#             if i==j:
#                 list1.append(j)
#      return list1
# print(odd_even(n1,n2))
# n1=[[1,2,3],4,5,6,7,[8,9],["sana"]]   
# def typefunc (l):
#     count=0
#     for i in l:
#         if type(i)==list:
#             count+=1
#     return count
# print(typefunc(n1))
####TUPLE
# t=(5,8,9.9,7)
# i=0
# while i < len(t):
#     print(t[i])
#     i+=1
###tuple unpacking
# s=("sana","hassaan","haniya")
# a,b,c=(s)
# print(c)
# def func(i,j):
#     add=i+j
#     mul=i*j
#     return (add,mul)
# print(func(4,7))
# add,mul=func(4,7)
# print(add,mul)
# n=(7,9,4)
# print(n.count(4))
###Dictionaries
# user={
#     "name":"hani",
#     "age": 27,
#     "fvrt_movies": ["coco","avatar"],
#     "fvrt_song": ["s1","s2"]
# }
# # print(user["name"])
# # user={}
# # user["name"]="sana"
# # print(user)
# # if "hani" in user.values():
# #     print("yes")
# # else:
# # #     print("no")
# # for i in user:
# #     print(i)
# ##values method
# # user_values=user.values()
# # print(user_values)
# # print(type(user_values))
# # for i in user:
# #     print(user[i])

# # user_item=user.items()
# # print(user_item)
# # for key,value in user.items():
# #     print(f" {key} and {value}")
# # for key in user.items():
# #     print(f" {key} ")
# # user["songs"]=["s1","s2"]
# # print(user)
# # poped= user.pop("songs","name")
# # print(user)
# # print(poped)
# # poped= user.popitem()
# # print(user)
# # print(poped)
# more_info={"name":"sana","state":"isb", "hobbies":"sleep"}
# user.update(more_info)    
# print(user)
# d=dict.fromkeys((("name","age")),"unkown")
# print(d.get("name","not found"))
# # d=dict.fromkeys(range(0,8),("unkown","none"))
# # print(d)
###cube finder
# def cube_finder(n):
#     d={}
#     for i in range(0,n+1):
#         d[i]=i*i*i
#

# d=dict(name="saman",age=33)
# print(d)
# l=[6,8,0,6,7,8,9]
# s1=list(set(l))
# print(s1)
# s={1,2,3}
# s2={3,7,9}
# union_set=s&s2
# #union_set=s|s2
# # s.add(6)
# # s.remove(3)
# print(union_set)
# ##union intersection
######LIST COMPREHENSION
# sq=[i**2 for i in range(1,11)]
# print(sq)
# def reverse_words(l):
#     list=[]
#     for i in l:
        
#         list.append(i[::-1])
#     return list
# print(reverse_words(["abc","def"]))
# ###
# def reverse_words(l):
#     return[i[::-1] for i in l]
# print(reverse_words(["abc","def"]))   
# n=[6,9,0,4,8,2]
# even_list=[i for i in n if i%2==0]
# print(even_list)
# def list_num(l):
#     l_empty=[]
#     for i in l:
#         if type(i)==int or type(i)==float:
#             l_empty.append(str(i))
#     return l_empty
# l1=[1,9.0,[6,8,9],"yes","no"]
# print(list_num(l1))
###dict_comprehension
# sq={num:num**2 for num in range(0,11)}
# print(sq)
#***arg
# def total1(num,*args):
#     cube=[]
#     for i in args:
#         if len(args)!=0:
#            cube.append(i**num)
#         else:
#            print("give args")
#     return cube
# print(total1(2,7,9))
# def total1(num,*args):
#     if args:
#        return [i**num for i in args]
#     else:
#         return "oye" 

# inputs=()
# print(total1(2))
# def func(**kwargs):
#     for i,j in kwargs.items():
#         return(f"{i}:{j}")
# print(func(name='sana',age=23, house='beautiful'))
# def func(name="none",age=30):
#     print(name)
#     print(age)
# func("saman")
# def func(name,*args,age=30,**kwargs):
#     print(name)
#     print(args)
#     print(age)
#     print(kwargs)
# func("saman",1,8,a=2)
# def func(names,**kwargs):
#     em_list=[]
#     for i in names:
#       if kwargs.get("reverse_str")==True:
#         em_list.append(i[::-1].title())
#       else:
#         em_list.append(i.title())

        
#     return(em_list)
# print(func(['sana','jah'],reverse_str=False))
# ##comprehension
# def func(names,**kwargs):
#      em_list=[]
#      return [em_list.append(i[::-1].title()) if (kwargs.get("reverse_str")==True) else (em_list.append(i.title())) for i in names ]
# print(func(['sana','jah']))
# #########################
# def caprev(name,**rev):
#     return [ (i[::-1]).title()  if (rev.get('rev_str') == True) else i.title() for i in name]

# names = ['hello','world']
# print(caprev(names, rev_str = True))
###lambda
# add=lambda a,b:a+b
# print(add(4,7))
# func=lambda s:True if len(s)<5 else False
# print(func("sana jah"))
# nam=["sana","jah"]
#pos=0
# for i in nam:
#      print(f"{pos}....>{i}")
#      pos=pos+1
#      print(f"{i}")
# for pos,i in enumerate(nam):
#      print(f"{pos}:{i}")
# def pos_str(l,target):
#      pos=0
#      for i in l:
#           if i==target:
#                pos+=1
#                return pos
#      return -1
# print(pos_str(nam,"jah"))
# def pos_str(l,target):
     
#      for pos,i in enumerate (l):
#           if i==target:
               
#              return pos
#      return -1
# print(pos_str(nam,"jah"))
###map func
# n=[1,2,3,4]
# def sq(a):
#      return a**2
# squares=print(list(map(sq,n)))
# squares=print(list(map(lambda a:a**2,n)))
# print(squares)
# ##list_comp
# nam=["sana","Ajlal"]
# s=list(map(lambda i : len(i),nam))
# print(s)
# nam=["sana","Ajlal"]
# s=map(len,nam)
# for i in s:
# #      print(i)
# l1=[1,2,3]
# l2=[7,9,0]
# l3=[7,8,6]
# l1,l2=list(zip(*l))
# print(l1)
# print(l2)
# def avg_finder(*args):
#      em=[]
#      for i in zip(*args):
#           em.append(sum(i)/len(i))
#      return em
# print(avg_finder(l1,l2,l3))

#new= lambda *args:sum(i)/3 for i in zip(*args)
# names=["sajaja","jjjajhhhh"]
# def func(i):
#      return len(i)
# # print(max(names,key=func))
# s1={ 
#      "sana":{"score":50,"age":5},
#      "Adil":{"score":84,"age":15}
# }
# print(max(s1,key= lambda i : s1[i]["score"]))
# print(len.__doc__)
# print(help(sum))
#######

# def sq(a):
#      return a**2
# s=sq
# print(s(8))
# ####
# def outer_func():
#      def inner_func():
#           print("inside")
#      return inner_func()
# var=outer_func() 
#var()
# def outer_func(msg):
#      def inner_func():
#           print(f"inside is {msg}")
#      return inner_func
# var=outer_func("hi") 
# var()
# users = ["Test User", "Real User 1", "Real User 2"]
# for index, user in enumerate(users):
#      if index == 0:
#         print("Extra verbose output for:", user)
#      print(user)
##########DECORATORS:
# from functools import wraps
# def decorator_func(any_func):
#      @wraps(any_func)
     
#      def wrapper_func(*args,**kwargs):
#           '''THIS IS WRAPPER'''
#           print("sana is nice")
#           return any_func(*args,**kwargs)
          
#      return wrapper_func
# @decorator_func
# def func_1(a):
#      print ("function 1")
# # var=decorator_func(func_1)
# # var()
# # func_1(5)
# @decorator_func
# def add_func(a,k):
#      '''original'''
#      return a+k
# print(add_func(7,9))
# print(add_func.__doc__)
####
# def time_cal(func):
#      def wrapper(*args,**kwargs):
#           import time
#           t1=time.time()
#           func(*args,**kwargs)
#           t2=time.time()
#           print(t1-t2)
#      return wrapper
# @time_cal
# def func1(a,b):
#      print("good")
#      print("good")
#      print("good")
#      print("good")
#      print("good")
#      return a*b
# func1(899999,100000)
###Generartor
# def generator_func(a):
#      for i in range(1,a+1):
#           if i%2==0:
#              yield i

     
# # n1=(generator_func(10))
# # for i in n1:
# #       print(i)
# for i in generator_func(8):
#       print(i)
# for i in generator_func(8):
#       print(i)
 ###OOP
# class Person:
#       def __init__(self,first_n,last_n,age):
#             print("init called")
#             self.fitst_n=first_n
#             self.last_n1=last_n
#             self.age=age
# p1=Person("sana","jan",28)
# print(p1.last_n1)

# class Laptop:
#       def __init__(self,brand,model,age):
#             print("init called")
#             self.brand=brand
#             self.model=model
#             self.age=age
#             self.fullname= brand + " " + model
#       def full_name(self):
#             return f"{self.brand} {self.model}"
#       def is_above_18(self):
#             if self.age>18:
#                   return True
#             else:
#                   return False
# p1=Laptop("lenovo","550",1)
# print(p1.full_name())
# print(p1.is_above_18())
# # class Laptop:
# #       def __init__(self,brand,model,price):
# #             print("init called")
# #             self.brand=brand
# #             self.model=model
# #             self.price=price
# #             self.fullname= brand + " " + model
# #       def full_name(self):
# #             return f"{self.brand} {self.model}"
# #       def discount(self,dis):
# #             return ((self.price-dis/100)*self.price)
# # p1=Laptop("lenovo","550",10000)
# # p2=Laptop("hp","67",30000)
# # print(p1.full_name())
# # print(p1.discount(8))
# # print(p2.discount(8))
# class Circle:
#       pi=3.14   ###class variable
#       def __init__(self,radius):
#             self.radius=radius
#       def circumference(self):
#             return 2*Class.pi*self.radius
# c1=Circle(5)    ###Radius
# print(c1.circumference())   ###object call=self
# print(c1.pi)  ##class variable call
# Circle.pi=1   
# c2=Circle(8)
# print(c2.circumference())
# print(c2.__dict__)

# class Circle:
#       pi=3.14   ###class variable
#       def __init__(self,radius):
#             self.radius=radius
#       def circumference(self):
#             return 2*self.pi*self.radius   ###have to change class variable
# c1=Circle(5)    ###Radius
# print(c1.circumference())   ###object call=self
# print(c1.pi)  ##class variable call
# Circle.pi=1    ###change of class variable
# c2=Circle(8)
# print(c2.circumference())
# print(c2.__dict__)
# class Person:
#       count=0
#       def __init__(self,name,last_n):
#             Person.count+=1
#             self.name=name
#             self.last_n=last_n
#       @classmethod
#       def count_instances(cls):
#             return f"you created {cls.count} instances of {cls.__name__}"
#       def full_name(self):
#             return f"{self.name} {self.last_n}"
#       @classmethod                ### constructor 
#       def from_str(cls,string):
#             name,last_n=string.split(",")
#             return cls(name,last_n)   ### create obj
#       @staticmethod
#       def static_m():
#             print("hello")
# p1=Person("sana","jah")
# p2=Person("sana","jah")
# p3=Person.from_str("sana,jahangir")
# print(Person.count)
# print(Person.count_instances())
# print(p3.full_name())
# print(Person.static_m())
# print(p3.static_m())
#########################
##Parent class:
# class Phone:  ##base7parent class
#       def __init__(self, brand, model, price):
#             self.brand=brand
#             self.model=model
#             self.price=price
#       def full_name(self):
#             return f"{self.brand} {self.model}"
# class Smartphone(Phone):
#       def __init__(self, brand, model, price,ram,camera):
#             super().__init__(brand, model, price)
#             self.ram=ram
#             self.camera=camera
#       def full_name(self):
#             return f"{self.brand} {self.model} {self.price}"
# class Smartphone2 (Phone):
#       def __init__(self, brand, model, price,ram,camera):
#             super().__init__(brand, model, price)
#             self.ram=ram
#             self.camera=camera
# class Flagship (Smartphone):  ##multilevel inheritence
#       def __init__(self, brand, model, price,ram,camera,specs):
#             super().__init__(brand, model, price,ram,camera)
#             self.specs=specs
#       def full_name(self):
#             return f"{self.brand} {self.model} {self.price} {self.ram}"
# phone=Phone("nokia","1100",1000)
# flag=Flagship("oneplus","nx",3000,"20MP","1Gb","alaa")
# # print(smartphone2.full_name())
# # print(smartphone2.ram)
# print(phone.full_name())     
# #print(help(Smartphone))         
# print(isinstance(phone,Smartphone))
# print(issubclass(Smartphone,Phone))               
# class Phone:  ##base7parent class
#       def __init__(self, brand, model, price):
#             self.brand=brand
#             self.model=model
#             self.price=price

#       def __str__(self):
#             return f"{self.brand} {self.model} {self.price}"
#       def __repr__(self):
#             return f"Phone ({self.brand} , {self.model})"
#       def __len__(self):
#             return len(self.brand)
#       def __add__(self,other):
#             return (self.price + other.price)
# phone=Phone("Nokia","1100",1000)
# phone2=Phone("Nokia","1400",1200)
# print(phone.__repr__())
# print(phone.__len__())
# print(phone + phone2)
# print (3/5)
# a=1
# b=0
# x=a or b

# y=not(a and b)
# print(x)
############Raising errors########
# class Mobile:
#       def __init__(self,name):
#             self.name=name
# class Mobilestore:
#       def __init__(self):
#             self.mobiles=[]
#       def add_mobile(self,newmob):
#             if isinstance(newmob,Mobile):
#                   self.mobiles.append(newmob)
#             else:
#                   raise TypeError("newmob should be in Mobile Class")
# oneplus=Mobile("oneplus5")
# s="samsung5"
# mobo=Mobilestore()
# print(mobo.mobiles)
# mobo.add_mobile(oneplus)
# print(mobo.mobiles)
# mobo_phones=mobo.mobiles
# print(mobo_phones[0].name)
#####exception handling
# while True:
#    try:
#       age=int(input("enter your age : "))
#       break
# except ValueError:
#       print("invalid")
#    except:
#       print("unexpected")
# if age<18:
#       print("good")
# else:
#       print("false")
# while True:
#    try:
#       age=int(input("enter your age : "))
      
#    except ValueError:
#       print("invalid")
#    except:
#       print("unexpected")
#    else:
#       print(f"{age}")
#       break
#    finally: ####always run
#       print("jaooo")
# a=int(input("first"))
# b=int(input("second"))
# def div(a,b):
#             try:
                  
#                   return a/b
#             except ZeroDivisionError:
#                   print("don't devide by zero")
#             except ValueError:
#                   print("dont put string")
#             except:
#                   print("invalid")
# print(div(a,b))
# import pdb
# pdb.set_trace()
# a=int(input("first"))
# b=int(input("second"))
# print(a/b)
##########Read files
# f=open("sana.txt","r")
# print(f.tell())
# #print(f.read())
# # print(f.readline())
# print(f.readlines())
# print(f.seek(3))
# print(f.tell())
# print(f.name)
# f.close()
# with open ("sana.txt") as f:
#       d=f.read()
#       print(d)
# with open ("sana1.txt","w") as f:
#       d=f.write("g")
#       print(d)
# with open ("sana.txt","a") as f:
#      f.write("\nplz ")
# with open ("sana.txt","r+") as f:
#       f.seek(len(f.read()))
#       f.write("\nwowww ")     
#with open("sana.txt","r") as rf:
#      with open("out1.txt","a") as wf:
#            for line in rf.readlines():
#                  if "href=" in line:
#                        pos=line.find("href=")
#                        first_quote=line.find('\"',pos )
#                        second_quote=line.find('\"',first_quote+1 )
#                        url=line[first_quote+1:second_quote]
#                        wf.write(url+"\n")

#type(True)

def x():
      global y
      y=5
      return y
x()
print (y)