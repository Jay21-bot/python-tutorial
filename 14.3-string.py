
x = "characters"
x.split() #used to convert string into list

# only works with aplhabets
string1 = "hello"
string1.lower() # used to convert in lower case
string1.upper() # used to convert in upper case
string1.capitalize() # used to uppercase the fisrt letter only case

# for spaces
string2 = "  hello  world  "
string2.strip() # used to remove the space from left and right side of string
string2.lstrip() # used to remove the space from left side of string
string2.rstrip() # used to remove the space from right side of string


# boolean o/p fucntion for conditions

# with functions
string3 = "Mr. Shyamlal"
string3.startswith("Mr.")

string4 = "Mr. Ramlal"
string4.endswith("lal")


# is functions

string5 = "221"
string5.isdigit()

string6 = "ABCabc"
string6.isalpha()

string7 = "ABC1234"
string7.isalnum()
