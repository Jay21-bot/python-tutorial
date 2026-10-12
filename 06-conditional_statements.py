print()
print("=" * 60)
print()


# ============================================================
# A. IF CONDITIONAL STATEMENT
# ============================================================

print("A. IF Conditional Statement")
print()

# IF statement is used to execute a block of code
# only when the given condition is TRUE.

x = 18

if x >= 18:
    # This block executes only if x is greater than
    # or equal to 18.
    print("You are eligible to vote.")

# If the condition is FALSE, the IF block is skipped.


print()
print("=" * 60)
print()


# ============================================================
# B. IF-ELSE CONDITIONAL STATEMENT
# ============================================================

print("B. IF-ELSE Conditional Statement")
print()

# IF-ELSE is used when there are two possible outcomes:
# TRUE  → IF block executes
# FALSE → ELSE block executes

x = 18

if x >= 18:
    # Executes when the condition is TRUE.
    print("You are eligible to vote.")

else:
    # Executes when the condition is FALSE.
    print("You are not eligible to vote.")


print()
print("=" * 60)
print()


# ============================================================
# C. IF-ELIF-ELSE CONDITIONAL STATEMENT
# ============================================================

print("C. IF-ELIF-ELSE Conditional Statement")
print()

# IF-ELIF-ELSE is used to check MULTIPLE CONDITIONS.

# Python checks the conditions from TOP to BOTTOM.
# The FIRST TRUE condition is executed.
# After that, the remaining conditions are skipped.


# ------------------------------------------------------------
# SIMPLE CALCULATOR
# ------------------------------------------------------------

print("Creating Calculator")
print()

num1 = 10
num2 = 3

# 'op' stores the operator that we want to use.
op = "+"


# Check which operator is given.

if op == "+":
    # Executes when op is "+".
    print("Sum:", num1 + num2)

elif op == "-":
    # Executes when op is "-".
    print("Subtraction:", num1 - num2)

elif op == "*":
    # Executes when op is "*".
    print("Multiplication:", num1 * num2)

elif op == "/":
    # Executes when op is "/".
    print("Division:", num1 / num2)

else:
    # Executes when none of the conditions are TRUE.
    print("Invalid operator.")


print()
print("=" * 60)
print()


# ============================================================
# D. NESTED IF-ELSE CONDITIONAL STATEMENT
# ============================================================

# An IF-ELSE statement written inside another
# IF-ELSE statement is called a NESTED CONDITIONAL STATEMENT.

# First, we check Gate 1.
gate1 = input("Enter 'open' to open Gate 1: ")


# OUTER IF-ELSE
# Checks whether Gate 1 is open.

if gate1 == "open":

    # This block executes only when Gate 1 is open.

    # Now we check Gate 2.
    gate2 = input("Enter 'open' to open Gate 2: ")


    # INNER IF-ELSE
    # This IF-ELSE is inside the outer IF block.

    if gate2 == "open":
        # Executes when Gate 2 is also open.
        print("Gate 1 and Gate 2 are opened.")

    else:
        # Executes when Gate 2 is not open.
        print("Please try again.")

else:
    # Executes when Gate 1 is not open.
    print("Please try again.")