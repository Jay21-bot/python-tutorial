
# ============================================================
# A : STAR PATTERN
# ============================================================

z = 10

# -------------------- TOP HALF --------------------

# Start from z and decrease i by 1 until i becomes 1
for i in range(z, 0, -1):

    # "#" * i       → prints i number of #
    # "*" * (z-i)   → prints stars based on the difference
    # "*" * (z-i)   → prints the same number of stars again
    # "#" * i       → prints i number of # again

    print("#" * i, "*" * (z-i), "*" * (z-i), "#" * i)


# -------------------- BOTTOM HALF --------------------

# Start from 0 and increase i by 1 until i reaches z-1
for i in range(z):

    # "#" * i       → prints i number of #
    # "*" * (z-i)   → prints stars based on the remaining value
    # "*" * (z-i)   → prints the same number of stars again
    # "#" * i       → prints i number of # again

    print("#" * i, "*" * (z-i), "*" * (z-i), "#" * i)
    
z=21

for i in range(z,0,-1):
  print('#'*z,'*'*(z-i),'*'*(z-i),'#'*z)
for i in range(z):
    print('#'*z,'*'*(z-i),'*'*(z-i),'#'*z)
 