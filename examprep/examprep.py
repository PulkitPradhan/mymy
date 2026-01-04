# #oop practice :-

# # 1. Grandparent
# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand

# # 2. Parent (Inherits from Vehicle)
# class Car(Vehicle):
#     def __init__(self, brand, seats):
#         super().__init__(brand)  # Call parent to set brand
#         self.seats = seats

# # 3. Child (Inherits from Car)
# class ElectricCar(Car):
#     def __init__(self, brand, seats, battery):
#         super().__init__(brand, seats) # Call parent to set brand/seats
#         self.battery = battery

#     def display(self):
#         print(f"{self.brand} Car with {self.seats} seats and {self.battery}kWh battery.")

# # Usage
# tesla = ElectricCar("Tesla", 5, 100)
# tesla.display()


#     def display(self):
#         print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")

# class Manager(Employee):
#     def __init__(self, name, age, salary, department):
#         super().__init__(name, age, salary)
#         self.department = department

#     def display(self):
#         super().display()
#         print(f"Department: {self.department}")

# manager = Manager("John", 30, 5000, "IT")
# manager.display()

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# INHERITANCE :-

# class Employee:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print(f"Name:{self.name}, Age:{self.age}")       


# prsn1 = Employee("Pulkit",20)
# prsn1.display()

# class emp(Employee):
#     def __init__(self,name,age,salary ,join year):
        

# ------------------------------------------------------------------------------- YEILDING --------------------------------------------------------------------------------

# def get_squares():
#     l=[]
#     for i in range(2,6):
#         l.append(i*i)
#         yield l    

# get = (i*i for i in range(2, 10))
# for i in get:
#     print(i)

# -----------------------------------------------

# get = (i*i for i in range(2,10))
# print(next(get))
# print(next(get))

# The Loop (Automatic Mode)

# ----------------------------------------------------------------------------
# print((get)) 
# for i in range(6):


# def get_evens():
#     res = []

# ---------------------------------------------------------    ques  ------------------------------------------------------------------

# class VEHICLE():
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
    
#     def display(self):
#         print(f"Brand-{self.brand}, Model- {self.model}")    

# # class Car inherits Vehicle and adds seating_capacity. 

# class CAR(VEHICLE):
#     def __init__(self,brand, model,seating_capacity):
#         super().__init__(brand,model)
#         self.seating_capacity=seating_capacity

#     def display(self):
#         print(f"Brand-{self.brand}, Model- {self.model}, Seating Capacity- {self.seating_capacity}")    

# # Class ElectricCar inherits Car and adds battery_range. 

# class Electrical_car(CAR):
#     def __init__(self,brand, model,seating_capacity,battery_range):
#         super().__init__(brand, model,seating_capacity)
#         self.battery_range=battery_range

#     def display(self):
#         print(f"Brand-{self.brand}, Model- {self.model}, Seating Capacity- {self.seating_capacity}, Battery Range- {self.battery_range}")    

# prsn1=CAR("BMW",ZOP67,3)
# prsn2=Electrical_car("FRR",kop,5,"100kw")
# prsn3=VEHICLE("LOP",hui56,)


# prsn1.display()
# prsn2.display()
# prsn3.display()

# ----------------------------------------------------------------------------    ques    ---------------------------------------------------------------------------------

# a,b,c,d=10,10.5,True,"Hello"
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

# ----------------------------------------------------------------------------    ques    ---------------------------------------------------------------------------------

# for i in range(1, 51):
#     if (i % 3 == 0) or (i % 5 == 0): # XOR operator handles "not both"
#         print(i)

# ----------------------------------------------------------------------------    ques    ---------------------------------------------------------------------------------


# while True:
#     try:
#         choice= int(input("""Enter your choice:- 
#         1. Circle, 
#         2. Rectangle, 
#         3. Triangle. 
#         :- """))
#         #
#         if choice == 1:
#             print("You have chosen option 1, Circles area ,")
#             r=int(input("pls enter radius:- "))
#             area=3.14*r*r
#             print("Area of circle is:- ",area)
#             break
#         elif choice == 2:
#             print("You have chosen option 2, Rectangles area ,")
#             l=int(input("pls enter length:- "))
#             b=int(input("pls enter width:- ")) 
#             area=l*b
#             print("Area of rectangle is:- ",area)
#             break
#         elif choice == 3:
#             print("You have chosen option 3, Triangles area ,")
#             b=int(input("pls enter base:- "))
#             h=int(input("pls enter height:- "))
#             area=b*h/2
#             print("Area of triangle is:- ",area)
#             break
#         else:   
#             print("Invalid choice")
#     except ValueError:
#         print("Please enter a valid integer.")

# --------------------------------------------------------------------------    ques 12   ---------------------------------------------------------------------------------


# for i in range(1,6):
#     print(str(i)*i)
# for i in range(6,0,-1):
#     print(str(i)*i)

# print()
# for i in range(1,6):
#     print(str("*")*i)

# --------------------------------------------------------------------------    ques 13   ---------------------------------------------------------------------------------

# bal = 1000
# while True:
#     mon = float(input(Enter your choice:-\n
#     1. Check Balance\n
#     2. Deposit\n
#     3. Withdraw\n
#     4. Exit\n
#     : ))
#     try:
#         if mon == 1: 
#             print(f"Balance: {bal}")
#         elif mon == 2: 
#             bal += float(input("Enter amount to deposit: "))
#         elif mon == 3: 
#             bal -= float(input("Enter amount to withdraw: "))
#         elif mon == 4: 
#             break
#         else :
#             print("Invalid choice")
#     except ValueError:
#         print("Please enter a valid integer.")

# --------------------------------------------------------------------------    ques 14   ---------------------------------------------------------------------------------
# from dataclasses import dataclass 
# @dataclass
# class Vehicle:
#     brand: str
# class Car(Vehicle):
#     seats: int
# class ElectricCar(Car):
#     range_km: int
# e = ElectricCar("Tesla", 5, 500)
# print(e.brand, e.seats, e.range_km)                                      


# class Vehicle:
#     def __init__(self, brand): self.brand = brand
# class Car(Vehicle):
#     def __init__(self, brand, seats): super().__init__(brand); self.seats = seats
# class ElectricCar(Car):
#     def __init__(self, brand, seats, range_km):
#         super().__init__(brand, seats); self.range_km = range_km
# e = ElectricCar("Tesla", 5, 500)
# print(e.brand, e.seats, e.range_km)

# --------------------------------------------------------------------------    ques 15   ---------------------------------------------------------------------------------
# try:
#     with open("employees.txt", "a+") as f:
#         f.write("101,John,50000\n") 
#         f.seek(0)
#         print(f.read())
# except FileNotFoundError: print("File not found")

# list comprehension
# sq=[x*x for x in range(1,6)]
# print(sq)
# --------------------------------------------------------------------------    ques 16   ---------------------------------------------------------------------------------

# import numpy as np
# arr1=np.array([1,2,3,4,5])
# arr2=np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(f"Shape:{arr1.shape},  Dimension:{arr1.ndim}")
# print(f"Shape:{arr2.shape},  Dimension:{arr2.ndim}")

        
# while True:
#     try:
#         op = input("select your operator (+,-,*,/): ")
#         a,b=float(input("Enter a: ")), float(input("Enter b:"))
#         if op=="+":
#             print("Addition of",a,"and",b,"is",a+b)
#         elif op=="-":
#             print("Subtraction of",a,"and",b,"is",a-b)
#         elif op=="*":
#             print("Multiplication of",a,"and",b,"is",a*b)
#         elif op=="/":
#             print("Division of",a,"and",b,"is",a/b)
#         else:
#             print("Invalid operator")
#     except ValueError:
#         print("Please enter a valid integer.")

    
#     restart = input("Do you want to continue? (y/n): ").lower()
#     if restart != "y":
#         print("Goodbye!")
#         break 
#     else:
#         continue

# --------------------------------------------------------------------------    ques 17   ---------------------------------------------------------------------------------

# l=["sak",564,"add",456,"doap",468]
# for items in l:
#     print(items)

# dic={"sak":564,"add":456,"doap":468}
# for items,values in dic.items():
#     print(items,values)

# --------------------------------------------------------------------------    ques 18   ---------------------------------------------------------------------------------

# d={}
# d["sak"] = 648
# print(d)
# print(d["sak"])

# def factorial_recursive(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial_recursive(n - 1)
# print(f"Recursive Result: {factorial_recursive(10)}")


# def factorial_iterative(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
# print(f"Iterative Result: {factorial_iterative(10)}")


# def fibonacci_recursive(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
# print(f"Recursive Result: {fibonacci_recursive(10)}")


# def fibonacci_iterative(n):
#     if n <= 1:
#         return n
#     a, b = 0, 1
#     for i in range(2, n + 1):
#         a, b = b, a + b
#     return b
# print(f"Iterative Result: {fibonacci_iterative(10)}")

# --------------------------------------------------------------------------    ques 19   ---------------------------------------------------------------------------------

# Develop a Python class Book with attributes title, author, isbn, and status and methods to: 
# o Display book details 
# o Issue/return a book (update status) 
# o Save details to a text file library.txt 
# o Use try–except for file and input handling 
# Write a main program that allows the user to add and view books using a 
# menu-driven loop.

# class book:
#     def __init__(self,title,author,isbn,status):
#         self.title=title
#         self.author=author
#         self.isbn=isbn
#         self.status=status

#     def display(self):
#         print(self.title,self.author,self.isbn,self.status)

#     def issue(self):
#         if self.status=="available":
#             self.status="issued"
#             return True
#         else:
#             return False

#     def return_book(self):
#         if self.status=="issued":
#             self.status="available"
#             return True
#         else:
#             return False

#     def save_to_file(self):
#         with open("library.txt","a+") as f:
#             f.write(f"{self.title},{self.author},{self.isbn},{self.status}\n")

#     def load_from_file(self):
#         try:
#             with open("library.txt","r") as f:
#                 for line in f:
#                     title,author,isbn,status=line.strip().split(",")
#                     self.title=title
#                     self.author=author
#                     self.isbn=isbn
#                     self.status=status
#         except FileNotFoundError:
#             print("File not found")

#     def __str__(self):
#         return f"{self.title},{self.author},{self.isbn},{self.status}"

import os

class Book:
    def __init__(self, title, author, isbn, status="available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def display(self):
        print(f"Title: {self.title:<20} | Author: {self.author:<15} | ISBN: {self.isbn:<10} | Status: {self.status}")

    def issue_book(self):
        if self.status == "available":
            self.status = "issued"
            return True
        else:
            return False

    def return_book(self):
        if self.status == "issued":
            self.status = "available"
            return True
        else:
            return False

    # Appends a SINGLE new book to the file
    def save_to_file(self):
        try:
            with open("library.txt", "a+") as f:
                f.write(f"{self.title},{self.author},{self.isbn},{self.status}\n")
            print("Book saved to file successfully.")
        except IOError:
            print("Error: Could not save to file.")

# --- Helper Functions ---

def load_books():
    """Reads library.txt and returns a list of Book objects."""
    books = []
    try:
        with open("library.txt", "r") as f:
            for line in f:
                data = line.strip().split(",")
                if len(data) == 4:
                    # Create Book object and add to list
                    new_book = Book(data[0], data[1], data[2], data[3])
                    books.append(new_book)
    except FileNotFoundError:
        # It's okay if file doesn't exist yet
        pass
    return books

def update_file(books_list):
    """Rewrites the entire file with current book statuses."""
    try:
        with open("library.txt", "w") as f:
            for b in books_list:
                f.write(f"{b.title},{b.author},{b.isbn},{b.status}\n")
    except IOError:
        print("Error updating file.")

# --- Main Program ---

def main():
    # Load existing books into memory at startup
    library_books = load_books()

    while True:
        print("\n--- LIBRARY MENU ---")
        print("1. Add New Book")
        print("2. View All Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")
        
        choice = input("Enter choice: ")

        if choice == '1':
            try:
                t = input("Enter Title: ")
                a = input("Enter Author: ")
                i = input("Enter ISBN: ")
                # Create new book
                b = Book(t, a, i)
                b.save_to_file()      # Save to disk
                library_books.append(b) # Add to memory list
            except Exception as e:
                print(f"Error adding book: {e}")

        elif choice == '2':
            if not library_books:
                print("No books in library.")
            else:
                print("\n--- Book List ---")
                for book in library_books:
                    book.display()

        elif choice == '3': # Issue
            search_isbn = input("Enter ISBN to issue: ")
            found = False
            for book in library_books:
                if book.isbn == search_isbn:
                    if book.issue_book():
                        print(f"Book '{book.title}' issued successfully.")
                        update_file(library_books) # Update file with new status
                    else:
                        print("Book is already issued.")
                    found = True
                    break
            if not found:
                print("Book not found.")

        elif choice == '4': # Return
            search_isbn = input("Enter ISBN to return: ")
            found = False
            for book in library_books:
                if book.isbn == search_isbn:
                    if book.return_book():
                        print(f"Book '{book.title}' returned successfully.")
                        update_file(library_books) # Update file with new status
                    else:
                        print("Book was not issued.")
                    found = True
                    break
            if not found:
                print("Book not found.")

        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()