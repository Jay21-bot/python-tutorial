# ============================================================
# 📚 LIST DATA TYPE IN PYTHON
# ============================================================

print()
print("╔══════════════════════════════════════════════════════════╗")
print("║                  📚 LIST DATA TYPE                      ║")
print("╚══════════════════════════════════════════════════════════╝")
print()


# ============================================================
# 🔹 WHAT IS A LIST?
# ============================================================

print("🔹 What is a List?")
print()

print("A List is a collection of multiple elements.")
print("It can store elements of different or similar data types.")
print()


# ============================================================
# 🔹 FEATURES OF LIST
# ============================================================

print("🔹 Features of List")
print()

print("1. A list can store multiple elements.")
print("2. It can store different or similar data types.")
print("3. A list is created using square brackets [ ].")
print("4. Elements are separated using commas (,).")
print("5. A list can contain another list.")
print("6. List data can be accessed and manipulated")
print("   using predefined functions and methods.")
print("7. Indexing, Slicing and Step concepts are applicable.")
print()


# ============================================================
# 🔹 NATURE OF LIST
# ============================================================

print("🔹 Nature of List")
print()

print("List is MUTABLE in nature.")
print()
print("Mutable means:")
print("We can change, add or remove elements")
print("from an existing list.")
print()


# ============================================================
# 🔹 CREATING A LIST
# ============================================================

print("🔹 Creating a List")
print()

L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("List L1       :", L1)
print("Dtype of L1   :", type(L1))
print()


# ============================================================
# 🔹 MATHEMATICAL FUNCTIONS WITH LIST
# ============================================================

print("🔹 Mathematical Functions with List")
print()

print("⚠️ Note:")
print("These functions work properly when the list")
print("contains only int or float elements.")
print()

print("Sum            :", sum(L1))
print("Minimum Value  :", min(L1))
print("Maximum Value  :", max(L1))
print("Length         :", len(L1))

print()


# ============================================================
# 🔹 MIXED DATA TYPE LIST
# ============================================================

print("🔹 Mixed Data Type List")
print()

x = 10

L2 = [1, 2, 3, 2, 2, "hello", x, "name", True]

print("List L2       :", L2)
print("Dtype of L2   :", type(L2))
print()


# ============================================================
# 🔹 LIST METHODS
# ============================================================

print("🔹 Important List Methods")
print()


# ------------------------------------------------------------
# 1. append()
# ------------------------------------------------------------

L2.append("ram")

print("append()")
print("Adds a single element at the end of the list.")
print("L2 :", L2)
print()


# ------------------------------------------------------------
# 2. extend()
# ------------------------------------------------------------

L2.extend([30, 40, "bhuvan", False])

print("extend()")
print("Adds multiple elements at the end of the list.")
print("L2 :", L2)
print()


# ------------------------------------------------------------
# 3. insert()
# ------------------------------------------------------------

L2.insert(1, "ravi")

print("insert()")
print("Adds a single element at a particular index.")
print("L2 :", L2)
print()


# ------------------------------------------------------------
# 4. insert() with another list
# ------------------------------------------------------------

L2.insert(4, [4, 5, 6])

print("insert() with List")
print("A complete list can also be inserted")
print("at a particular index position.")
print("L2 :", L2)
print()


# ============================================================
# 🔹 OTHER IMPORTANT LIST METHODS
# ============================================================

print("🔹 Other Important List Methods")
print()

print("1. sort()")
print("   → Sorts numeric elements in ascending order.")
print()

print("2. pop()")
print("   → Removes the last element by default.")
print()

print("3. remove()")
print("   → Removes a particular element from the list.")
print()

print("4. clear()")
print("   → Removes all elements from the list.")
print()

print("5. reverse()")
print("   → Reverses the order of elements.")
print()

print("6. count()")
print("   → Counts how many times an element occurs.")
print()


# ============================================================
# 🔹 INDEXING
# ============================================================

print("🔹 Indexing")
print()

print("Elements of a list can be accessed using indexing.")
print()

print("Example:")
print("L2[1]")

print()


# ============================================================
# 🔹 SLICING
# ============================================================

print("🔹 Slicing")
print()

print("A range of elements can be accessed using slicing.")
print()

print("Example:")
print("L2[4:8]")

print()


# ============================================================
# 🔹 STEP
# ============================================================

print("🔹 Step")
print()

print("Step is used to access elements with a specific gap.")
print()

print("Example:")
print("L2[::2]")

print()


# ============================================================
# 🔹 QUICK REVISION
# ============================================================

print("╔══════════════════════════════════════════════════════════╗")
print("║                    📌 QUICK REVISION                    ║")
print("╚══════════════════════════════════════════════════════════╝")
print()

print("✔ List is used to store multiple elements.")
print("✔ List can store different data types.")
print("✔ List is created using [ ].")
print("✔ Elements are separated using commas.")
print("✔ List is MUTABLE.")
print("✔ Indexing is applicable.")
print("✔ Slicing is applicable.")
print("✔ Step is applicable.")
print("✔ A list can contain another list.")
print("✔ append(), extend(), insert(), pop(),")
print("  remove(), clear(), reverse(), sort() are")
print("  commonly used list methods.")

print()
print("----------------------------------------------------------------")
print()

# print("Dtype of L2: ",type(l2))
# print("Values of L2: ",l2)

# x = 10
# L2 = [...]





# print("Dtype of L2: ",type(l2))
# print("Values of L2: ",l2)

# x = 10
# L2 = [...]