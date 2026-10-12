print()
print("--------------------------------------------------")
print()


# ==================================================
# IMPLICIT TYPE CONVERSION
# ==================================================

# When the data type gets automatically changed
# because of an operator, it is called
# Implicit Type Conversion (ITC).

print("Implicit Type Conversion:-\n")

x = 10
y = 3

z = x + y

print("Before:", type(z))
print("The value of z:", z)

print()

z = x / y

print("After:", type(z))
print("The value of z:", z)


print()
print("--------------------------------------------------")
print()


# ==================================================
# EXPLICIT TYPE CASTING
# ==================================================

# When you forcefully change the data type,
# it is called Explicit Type Casting.

print("Explicit Type Casting:-\n")


# --------------------------------------------------
# A1. Integer to Float
# --------------------------------------------------

print("A1. Conversion of int to float\n")

i1 = 10

print("-> Value of i1:", i1)
print("-> Before: i1 = float(i1):", type(i1))

i1 = float(i1)

print("-> After: i1 = float(i1)")
print("-> Data type of i1:", type(i1))
print("-> Value of i1:", i1)


print()
print("--------------------------------------------------")
print()


# --------------------------------------------------
# A2. Integer to String
# --------------------------------------------------

print("A2. Conversion of int to str\n")

i2 = 10

print("-> Value of i2:", i2)
print("-> Before: i2 = str(i2):", type(i2))

i2 = str(i2)

print("-> After: i2 = str(i2)")
print("-> Data type of i2:", type(i2))
print("-> Value of i2:", i2)


print()
print("--------------------------------------------------")
print()


# --------------------------------------------------
# B1. Float to Integer
# --------------------------------------------------

print("B1. Conversion of float to int\n")

f1 = 10.13

print("-> Value of f1:", f1)
print("-> Before type casting:", type(f1))

f1 = int(f1)

print("-> After type casting:", type(f1))
print("-> Value of f1:", f1)


print()
print("--------------------------------------------------")
print()


# --------------------------------------------------
# B2. Float to String
# --------------------------------------------------

print("B2. Conversion of float to str\n")

f2 = 10.13

print("-> Value of f2:", f2)
print("-> Before type casting:", type(f2))

f2 = str(f2)

print("-> After type casting:", type(f2))
print("-> Value of f2:", f2)


print()
print("--------------------------------------------------")
print()


# --------------------------------------------------
# C1. String to Integer
# --------------------------------------------------

print("C1. Conversion of str to int\n")

s1 = "123"

print("-> Value of s1:", s1)
print("-> Before type casting:", type(s1))

s1 = int(s1)

print("-> After type casting:", type(s1))
print("-> Value of s1:", s1)


print()
print("--------------------------------------------------")
print()


# --------------------------------------------------
# C2. String to Float
# --------------------------------------------------

print("C2. Conversion of str to float\n")

s2 = "123"

print("-> Value of s2:", s2)
print("-> Before type casting:", type(s2))

s2 = float(s2)

print("-> After type casting:", type(s2))
print("-> Value of s2:", s2)


print()
print("--------------------------------------------------")
print()


# ==================================================
# NOTE
# ==================================================

# A string can only be converted to int or float
# if it contains a valid numeric value.

# Example:

# s3 = "abc"
# s3 = int(s3)       # This will give an error
