print()
print("╔══════════════════════════════════════════════════════════════╗")
print("║                       🔁 FOR LOOP                            ║")
print("╚══════════════════════════════════════════════════════════════╝")
print()


# ==============================================================
# 🔹 BASIC CONCEPTS OF FOR LOOP
# ==============================================================

# 'for' → Loop keyword used to perform a task repeatedly.

# 'i' → Iterator
#       • Technically, it is a variable.
#       • You can give the iterator any valid variable name.
#       • It is called an iterator because its value changes
#         sequentially during each iteration.
#       • In range(), the value starts from 0 by default.

# 'in' → Keyword used to check / take values from a sequence.

# range() → A predefined function used to generate a sequence
#           of numbers using start, stop and step values.


# ==============================================================
# 1️⃣ RANGE WITH ONE VALUE
# ==============================================================

print("┌──────────────────────────────────────────────────────────────┐")
print("│  1️⃣  RANGE WITH ONE VALUE                                    │")
print("└──────────────────────────────────────────────────────────────┘")
print()

# When you put a SINGLE number in range(),
# it works like:
#
#       range(stop)
#
# The sequence starts from 0
# and ends BEFORE the given number.
#
# Example:
#
#       for i in range(5):
#           print(i)
#
# Output:
#       0
#       1
#       2
#       3
#       4

print("📌 Example: range(5)")
print()

for i in range(5):
    print(i)

print()
print("➡️  Output: 0, 1, 2, 3, 4")
print()


# ==============================================================
# 2️⃣ RANGE WITH TWO VALUES
# ==============================================================

print("┌──────────────────────────────────────────────────────────────┐")
print("│  2️⃣  RANGE WITH TWO VALUES                                   │")
print("└──────────────────────────────────────────────────────────────┘")
print()

# When you put TWO numbers in range(),
# they represent:
#
#       range(start, stop)
#
# • Starts from the first value.
# • Ends BEFORE the second value.
#
# Example:
#
#       for y in range(1, 11):
#           print(y)
#
# Output:
#       1, 2, 3, 4, 5, 6, 7, 8, 9, 10

print("📌 Example: range(1, 11)")
print()

for y in range(1, 11):
    print(y)

print()
print("➡️  Output: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
print()


# ==============================================================
# 3️⃣ RANGE WITH THREE VALUES
# ==============================================================

print("┌──────────────────────────────────────────────────────────────┐")
print("│  3️⃣  RANGE WITH THREE VALUES                                 │")
print("└──────────────────────────────────────────────────────────────┘")
print()

# When you put THREE numbers in range(),
# they represent:
#
#       range(start, stop, step)
#
# • start → Starting value
# • stop  → Ending limit (not included)
# • step  → Number of values to skip/jump
#
# Example:
#
#       for z in range(0, 11, 2):
#           print(z)
#
# Output:
#       0, 2, 4, 6, 8, 10

print("📌 Example: range(0, 11, 2)")
print()

for z in range(0, 11, 2):
    print(z)

print()
print("➡️  Output: 0, 2, 4, 6, 8, 10")
print()


# ==============================================================
# 📝 IMPORTANT NOTES
# ==============================================================

print("╔══════════════════════════════════════════════════════════════╗")
print("║                    📝 IMPORTANT NOTES                        ║")
print("╚══════════════════════════════════════════════════════════════╝")
print()

print("🔹 1. Use FOR LOOP when the number of iterations is fixed.")
print()
print("🔹 2. FOR LOOP can be used with sequential data types.")
print()
print("🔹 3. Use RANGE() when you don't have sequential data")
print("     and need to generate a sequence of numbers.")

