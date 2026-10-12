# dictionary dtype
# dictionary has items as elements
# and elements has key and its values
# and in each value u can store almost any dtype's of data
# key in the dictionary needs to be written in string
# values of an key should be assigned with colons ( : )

# u can not access the data with indexing slicing step directly 

# u can use indexing slicing step only if the value allow this for eg(list tuple string)

# u can access the data from the dictionary by its key only

# dictionary is mutable in nature

d = {
    "key" : "value",
    "int" : 12,
    "float" : 3.4,
    "string" : "hello world",
    "list" : [1,3,"@",4.5,"minor",True,False],
    "tuple" : (1,2,3,"major","hello",True),
    "set" : {21,2,2,2,2,"middle","None"},
    "dictionary" : {"name" : "sanju" , "age" : 21 , "subject" : "maths"} 
}


# accessing elements with keys
d["int"]

# this won't work
# d[0]

# indirectly accessing the elements of values with indexing slicing step
d["list"][2]

# used to return keys from the data
d.keys()

# used to return values from the data
d.values()

# used to return items from the data
d.items()

# this used to add a new item in data if key doesn't exist
d.update({"name" : "sanju"})

# this used to update the value if key does exist in the data
d.update({"name" : "vinay"})

# this used to pop the element if pass the particular key
d.pop("name")

# this used to pop the last item without passing its key
d.popitem()

# used to create a new dictioary with none values and with xyz key name
d.fromkeys("xyz")

# used to return the values of an key
d.get("list")