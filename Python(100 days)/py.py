# ----------------------------------------------------------

# day29 doc strings:- 
# used to print the comments or text in the def fcn, just below the def line or just above the def body 

# ----------------Q--------------------

# usr=int(input("Enter a no.:- "))
# def square():
#     '''Takes a number n and returns the square of n
#     this is an example of doc string in python 
#     '''
#     sq=usr**2
#     print(sq)

# square()
# print(square.__doc__)


#-----------------------------Day 30-----------------------------


# day 30, recursion fncs :-
# recursion fncs:- fncs that call themselves are called recursion fncs.
# n=int(input("enter a number:- "))

# def factorial(n):
#     if (n==1 or n==0):
#         return 1
#     else:
#         return n*factorial(n-1)

# print(factorial(n))

# -----------------fibonacci series--------------------

# n=int(input ("enter a no :- "))

# f(0) = 0
# f(1) = 1
# f(2) = f(0) + f(1)
# f(n)= f(n-1) + f(n-2)

# def f(n):
#     if n==1 or n==0:
#         return n
#     else:
#         for i in range(n+1):

#         return f(n+1) + f(n+2)

# print(f(n))

# --------------------------------------  Day 31 & 32 (Sets) ------------------------------------

# sets are unordered collection of datas

# METHODS IN SETS:-
# s=set()
# print(type(s))

#--  How to acces items in sets:-  ----
# se={1,2,3,"pulkit","xyz",True,False}
# for values in se:
#     print(values)

#---- union fnc in sets :- ----
# s1= {1,2,3,"pulkit"}
# s2={4,5,6, "xyz",1,2,3}
# print(s1.union(s2))

#----- adds more characters in the set excluding the dupkicates:- ----
# s3=s2.update(s1)
# print(s3)
# print(s1,s2)

# ---- Symmetric difference fnc in sets:- ----
# s1={1,2,3,4,5}
# s2={1,3,5,7,9}
# s3=s1.symmetric_difference(s2)
# print(s3)

# ---- difference fnc in sets:- ----
# ---- used to print the values which are in set1 but not in set2 unlike symmetric_difference ---
#                      basically set1-set2

# s1={1,3,5,7,9}
# s2={1,2,3,4,5}
# print(s1.difference(s2))

# there are more fncs in sets,  in maths 

#IMPORTANT TERMS IN SETS:-
#disjoints :- if two sets have no values in common, they are called disjoint sets
# print(s1.isdisjoint(s2))


# superset :- if set1 has all the values of set2 and more then set1 is called superset of set2, (basically set1 contains set2)
# print(s1.issuperset(s2))

#subset(opposite of superset):- if set2 has all the values of set1 and more, then set2 is called subset of set1
# print(s2.issubset(s1))

#add :- s1= {1,2,3}
# s1.add(4) , result s1={1,2,3,4}

#update :- (updates the list by ading more values either 1 or more than 1 )
# s1={"pulkit","xyz"}  
# s2={"abc","pqr",1,2}
# print(s1.update(s2))
# print(s1)

#remove:- helps to remove values from the given set
# s1={"pulkit",1,2,3}  
# print(s1.remove("pulkit"))
# print(s1)

#discard:- helps to remove values from the given set but if the value is not present in the set it dosent gives error unlike remove fnc

#   discard                                      remove
# s1={"pulkit",1,2,3}             |           # s1={"pulkit",1,2,3}  
# print(s1.discard("$ulkit"))     |   # print(s1.remove("$ulkit"))
# print(s1)                       |             # print(s1)

#pop:- removes and returns the last item usually but as set is unordered it removes randomly   set.pop()
#del:- deletes the set entirely      del set
#clear:- clears all the values and makes the set empty  set.clear()
#if-else works in sets also


#---------------------------------------------------------- Day 33 (DICT  ----------------------------------------------------------------

# Methods of dictionaries in python :-
# print(dict)
# print(dict[key/value])
# print(dict.keys())
# print(dict.get(key/value))
# print(dict[key/value]) & print(dict.get(key/value)) are both the same but the diff is that if the key/value is not present in the dict then the first one gives error while the second one gives - none

#FOR KEYS IN DICT :-
# for key in dict.keys():
#     print(dict[key])

#--------Metods for dicts:-  -------
#  .upadte :- used to change the values/keys of dct and also adds elements of another as wel
# ep={122:45, 123:89, 567:69,456:78}
# ep2={122:98, 789:54, 890:32,478:61}
# ep.update(ep2)
# print(ep)

# .pop :- removes the key/value pair of the given key
# dict.clear() :- clears the dict and makes it empty (makes the dict an empty dict)
# del dict :- deletes the entire dict 


# ---------------------------------------------- DAY 34 For loop with else -------------------------------------------------------




#----------------------------------------------- Day 36 Exception Handling ------------------------------------------------------

# num=input("Enter a number: ")
# print(f"Multipeles of {num} is : ")

# try:
#     for i in range(1,11):
#      print(f"{int(num)} X {i} = {int(num)*i}")

# except Exception as e:
#    print(e)
# (this one was for Exception error and or one is for inalid value)
#------------ or -------------

# try:
#    num=int(input("Enter a number: "))
# except ValueError:
#    print('invalid input saaar')
 
# ---------------------------------------- Day 37 - Final clause with expect fnc --------------------------------------

# (wether try/execute worls or not but finally will run even still)

# ex:- 
# try:
#   list=[1,2,3,4,5]
#   num=int(input("Enter the index: "))
#   print(list[num])

# except :
#   print("Error bruhhh!!")

# finally:
#   print("BUT IM ALWAYS EXECUTED HELL YEAHHHH!!")

# --------------------------------- Day 38  Raising custm errors------------------------------------------------

# num= int(input("Enter a number btw 1 to 9: "))
# if(num<1 or num>9):
#     raise ValueError("Bruh select btw 1 to 9")

#----------------------------------- Day 40 Short hand if else --------------------------------------

# as the name suggestes this is used for small on the spot cases for big codes and unlike traditional if-else here we use print before than if statement(js saying)
# ex:-
# a=1000
# b=800
# c="Kaam krle bsdike"
# print(a) if a>b else print ("=") if a==b else print(b)
# c=9 if a>b else 0 
# print(c)

# -------------------------- Day 41 Enumerate Function - gives the index with values-------------------------------------

# marks=[1,12,45,98,89,25]

# for index,  mark in enumerate(marks):
#     print(mark)
#     if( index == 3):
#         print("Fking awesome mate")


# ------------------------------------------------------- Day 42  -----------------------------------------------------

#------------------------------- Day 43 Virtual enviournment in python --------------------------------------


#------------------------------------ Day 44 Import works in python ---------------------------------------------------


# to use builtin:-
# import maths as math_builtin_python
# math_builtin_python= sqrt(10)*math_builtin_python.pi
# print(s)
# ---------------------------------------

# from module import * (import all )
# also works but not reccomended cuz it can lead to confusion , modules can have same fncs(name)

# ----------------------------------

# to know abt the module :-
# import module 
# print(dir(module))

# ----------------------------------------------- Day 45 if __name__ == "__main__"  -----------------------------------------

# import main
# main.wlcm()      #used with main.py 


#---------------------------------------------- Day 46 Os module introduction -----------------------------------------------

#  GO inside the folder of  -  os module introduction

#-------------------------------------------------Day 47 some exercise project -------------------------------------------------


#------------------------------------------------Day 48 Local vs global variable--------------------------------------------
# x=30 #(global variable)
# def yea():
#     global x # writes global x and changes acc to function
#     x=789 # local variable 
#     y=45
#     print(x)
#     print(y)
#     print("hello world")

# yea()

# print(f"{x}")
# print(y) # this will not work as it is local variable and it is inside of the function and it is only accesible only inside of the function 

#--------------------------------- Day 49 File io in python ----------------------------------------------------------



#------------------------------------ Day 50 read(), readlines() and other functions --------------------------------------------

#---------------------------------------------------- Day 51 ques-----------------------------------------------




#---------------------------------------------------- Day 52 Lambda functions -----------------------------------------------

# def double(x):
#     return x*2

# print(double(5))

#name = lambda variable : your function    #can be used to create small funtions inside a bigger function

# double = lambda x: x*2
# print(double(10))

#we can also add another function in def like -
# def hlo(fnx,y,x):
#     return x + fnx(y)

# y=int(input("enter a number:- "))
# dble = lambda x: x*2
# print(hlo(dble,y,10))


#--------------------------------------------- Day 53 map, filter and reduce ------------------------------------------------

# def cube(x):
#     return x*x*x

# l=[1,2,3,4,5,6,3]


# -------------
# long method-
# newl=[]
# for item in l:
#     newl.append(cube(item))

# ----------------------------------
# short method usong map function (used for effeciency)
# var = list(map(fxn, list_name))   #syntax

# newl =list(map(cube,l))
# print(newl)

# ---------------------------------------------- day 53 part 2 - Filter -------------------------------------------------


#------------------------------------------------ day 53 part 3 - Reduce ------------------------------------------------


# ------------------------------------------------- Day 54 "is" and == --------------------------------------------------


# a=[1,2,3]
# b=[1,2,3]
# print(a is b) #output- False  #compares exact location of the data in the memory 
# print(a==b) #Output- True   #compares the assigned values


#--------------------------------------------------------------------------------------------------------------------

# a=3
# b=3
# print(a is b) #output- True  #compares exact location of the data in the memory  (compares identity)
# print(a==b) #Output- True   #compares the assigned values 
#True because this is not mutable while list is mutable and hnce python creates a data pack in the memory for every immutable fnc u give it to py 


#---------------------------------------- Day 55 - Exercise Snake water gun ------------------------------------------------------


#----------------------------------------- Day 56 - OOPs(object-oriented programming) ----------------------------------------

# there are 2 types of approaches - 
# 1- procedural programming  #the basic logics and functions we've used till now
# 2- object-oriented programming #helps to map our variables with real life entities 

#Dunder methods - Double underscore __init__ , __str__ , 

# class railway_form:
#     def __init__(self,name,no,addhaar): #__init__ is the constructor of the class or template we're making cause it makes easier to maintain

# #- self is just the name Python uses for the object itself.
# # - Whenever you create an object from a class, self is how the class refers to that particular object.
# # - It lets each object keep track of its own data.

#         self.name = name
#         self.no = no
#         self.addhaar = addhaar

#     def __str__(self):  #__str__ or __repr__
#         return f"Railway Form: Name={self.name}, No={self.no}, Aadhaar={self.addhaar}"



#----------------------------------------------------------------- Day 57 clases and objects --------------------------------------------------------
# obj1=railway_form("pulkit",955985,"asd444545sdasd")
# print(obj1)
# print(obj1.name)
#------------------------------- Without __init__ -------------------------------

# - pass is a placeholder statement.
# - It tells Python: “Do nothing here, but keep the code valid.”

# class Perseon:
#   pass

# p1 = Perseon()
# p1.name = "Pulkit"    #with this we can change the defaulkt value also just like other fncs
# p1.age = 25

# print(p1.name)
# print(p1.age)


# class Perseon:
#     name = "pulkit"
#     occupation="student"
#     networth="ZERO (Brutal)"
#     def info(self):
#         print("Voke", f"{self.name} is a {self.occupation}")

# a=Perseon()
# a.name = "a"
# a.occupation="Prof"
# a.info()

# b=Perseon()
# b.name = "b"
# b.occupation="slut"
# b.info()

# c=Perseon()
# c.name="c"
# c.occupation="Dlal"
# c.info()

# ------------------------------------------------------------------- Day 58 Constructors ---------------------------------------------------------------------------

# class Perseon:
#     name = "pulkit"
#     occupation="student"
#     networth="ZERO (Brutal)"
#     def info(self):
#         print("Voke", f"{self.name} is a {self.occupation}")

# a=Perseon()

# a.info()

# ------------------------------------------------------------------- Day 59 decorators ---------------------------------------------------------------------------

#DECORATORS:-  fncs which helps to change/update other fncs and return them 

# def greet(fnc):  #fnc that we create for decoration
#     def mfnc():     # main fnc where we want to edit the other fnc
#         print("Good Morning")   # then we sate the changes we want 
#         print("Good Afternoon")
#         fnc()
#     return mfnc

# @greet
# def h():
#     a=34
#     b=33
#     print(a+b)


# h()


# for ex :- 

# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner

# @changecase
# def myfunction():
#   return "Hello Sally"

# @changecase
# def otherfunction():
#   return "I am speed!"

# print(myfunction())
# print(otherfunction())


# ------------------------------------------------------------------- Day 60 getters and setters ------------------------------------------------------------------------

# class Geek: 
# 	def __init__(self, age = 0): 
# 		self._age = age 
	
# 	def get_age(self): 
# 		return self._age 
	
# 	def set_age(self, x): 
# 		self._age = x 


# raj = Geek() 
# raj.set_age(21) 
# print(raj.get_age()) 
# print(raj._age)

# ------------------------------------------------------------------- Day 61 Inheritance ---------------------------------------------------------------------------------


class Pulkit:
    def __init__(self):
        self.__name="Pulkit"
        self.age=21
    def info(self):
        print("Voke", f"{self.name} is a {self.age}")


# ------------------------------------------------------------------- Day 62 STATIC methods ---------------------------------------------------------------------------------

