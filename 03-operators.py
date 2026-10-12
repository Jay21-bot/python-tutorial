# operators in python

print()
print("-----------------------------------------------------------")
print()

# 1.arithmetic operators
# :- (+,-,*,**,/,//,%)
# its used for maths calculations in python
# it generally returns o/p in numeric dtype
# note:- (+) is used for concatenation as well

print("A. Arithmetical operators:- \n")
print("10 + 3:",10 + 3) # 13
print("10 - 3:",10 - 3) # 7 
print("10 * 3:",10 * 3) # 30
print("10 ** 3:",10 ** 3) # 10 x 10 x 10 = 1000
print("10 / 3:",10 / 3) # 10 / 3 = 3.333333333335
print("10 // 3:",10 // 3) # 10 // 3 = 3 (removes decimal values)
print("10 % 3:",10 % 3) # 10 % 3 = 1 (returns remainder)

print()
print("-----------------------------------------------------------")
print()

# 2.assignment operators
# :- (+=,-=,*=,**=,/=,//=,%=)
# it is used to update the value of a variable
# it generally returns o/p in numeric dtype

print("B. Assignment operator:-\n")

x = 10

x += 3
print("x += 3:",x)

x -= 3
print("x -= 3:",x)

x *= 3
print("x *= 3:",x)

x **= 3
print("x **= 3:",x)

x /= 3
print("x /= 3:",x)

x //= 3
print("x //= 3:",x)

x %= 3
print("x %= 3:",x)

print()
print("-----------------------------------------------------------")
print()

# 3.relational/(comparison) operator
# :- (>,<,>=,<=,==,!==)

# it genrally used to compare the values of a variable
# it always returns o/p in boolean dtype
# majorly/commonly used in control flow chapter

print("C. Relational operator:-\n")

print("10 > 3:",10 > 3)
print("10 < 3:",10 < 3)
print("10 > 10:",10 > 10)
print("10 < 10:",10 < 10)
print("10 >= 10:",10 >= 10)
print("10 <= 10:",10 <= 10)
print("10 == 3:",10 == 3)
print("10 != 3:",10 != 3)

print()
print("-----------------------------------------------------------")
print()

# 4.logical operator
# :- and , or , not

# this operator is used to compare between pair of conditions
# even this operator also returns o/p in boolean dtype

print("D. Logical operator\n")

# 1. And operators
# this operators only returns true when both the conditions are true

print("1. AND operator:-")

print("10 > 3 and 3 < 10 :",10 > 3 and 3 < 10) # T + T = T
print("10 > 3 and 3 > 10 :",10 > 3 and 3 > 10) # F + T = F
print("10 < 3 and 3 < 10 :",10 < 3 and 3 < 10) # T + F = F
print("10 < 3 and 3 > 10 :",10 < 3 and 3 > 10) # F + F = F

print()

print("2. OR operator:-")
# this operator only rerturns false when both the conditions are false

print("10 > 3 or 3 < 10 :", 10 > 3 or 3 < 10) # T + T = T
print("10 < 3 or 3 < 10 :", 10 < 3 or 3 < 10) # F + T = T
print("10 > 3 or 3 > 10 :", 10 > 3 or 3 > 10) # T + F = T
print("10 < 3 or 3 > 10 :", 10 < 3 or 3 > 10) # F + F = F

print()

print("3. NOT operator:-")
# this operator is used to reverse the boolean dtype

print("not True :",not True) # False
print("not False :",not False) # True

print()
print("-----------------------------------------------------------")
print()

