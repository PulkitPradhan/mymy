
# section-1 
# l-1 - l-3

# --------------------------
# section-2 ( l-4 - l-7 )

# l-4  (Flow Charts and Basic Flow Control Concepts)

# 1) true and false conditions with , or, and, not operators
# 2) comparison operators 

# l-5 (if, elif, else)

# 1) if, elif, else

# l-6 (Loops)  while loop

# l-7 (Loops)  for loop

# --------------------------

# Section-3 ( l-8 - l-10 )

# l-8 Pytho built-in functions

# l-9 Your own functions

# l-10 Global and local scopes(varialbes)

# ----------------------------------------------------------

# Section 4 ERROR HANDLING , TRY AND EXPECT( l-11 )
# l-11 

# ----------------------------------------------------------

# Section 5  Guess the number proggrame

# import random 

# n=input("Enter your name")

# sno = random.randint(1,20)

# print("Hello",n,"Guess a number between 1 to 20")


# nah not worth it


# -----------------------------------------------------------------------
import re
ms="Call me 956-252-2525 or 564-789-7965 "
phonnum=re.compile(r'\d{3}-\d{3}-\d{4}')
nu = phonnum.search(ms)
print(nu.group())

