print("==========================================")
# simple function definition and call
def my_function():
    print("hello first function")
    print("==========================================")
my_function()

# function with paramaters
def my_func(fname = "Nishanth"):
    print(fname + " Akula")

my_func("Nithya")
my_func("Sreshta")
my_func()
print("==========================================")

# if function is called with out any parameter it uses the default value


# you can pass anything to a function like list, dictionary, sets etc
# passing a list
def my_list_func(food):
    for x in food:
        print(x)
fruits = ["apple","pear",'banana']
my_list_func(fruits)
print("==========================================")
# function to return value
def my_func_ret(x):
    return 5 * x
print(my_func_ret(3))
print(my_func_ret(5))
print("==========================================")

l = ['sfo','nyc','la']
def isMetro(city):
    if city in l:
        return True
    else:
        return False
x = isMetro('san')
print(x)