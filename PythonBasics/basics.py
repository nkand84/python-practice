print("hello nk")

x = 5
y = 15
sum = x + y
# print("sum of x and y is " + sum)

# simple if else there should be space before the print stat
# or else indentation error is thrown
if x > y:
    print("x is greater than y")
else:
    print("y is greater")


# trying a multiline string
"""
are you going to ignore this
print("really ignoring you now??")

"""

a = " Hello! "
print(a.strip())

print(len(a))
print(a.lower())

# format method
age = 34
job = "engineer"
name = "NK"
txt = "My name is {}, I am {} years old, and I am an {}"
print(txt.format(name,age,job))

# list is a collection that is ordered, changeable, and duplicates are allowed(just like arrays)
thislist = ["apple", "banana", "kiwi"]
print(thislist)
thislist[1] = "orange"
print(thislist)

# to loop through the list
for x in thislist:
    print(x)

# to check if item exists in the list
if "melon" in thislist:
    print("yes its in the list")
else:
    print("its not in the list")
thislist.append("pinapple")
print(thislist)
thislist.pop()
# thislist.insert(2,"watermelon")
print(thislist)
# print(len(thislist))

# dictionary
thisdict = {
    "make" : "acura",
    "year" : 2015,
    "model": "MDX"
}

# add a new item to the dict
thisdict["color"] = "grey"
# mydict = thisdict.copy()
# thisdict.pop("model")
# mydictmeth = dict(thisdict)
print(thisdict)
thisdict["color"] = "grey"
print(thisdict)
# print(mydictmeth)
# print(thisdict.get("color"))
# create dict with 3 keys and same value
# x = ("key1","key2","key3")
# y = 0
# persondict = dict.fromkeys(x,y)
# print(persondict)