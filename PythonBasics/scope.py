# a = 10
# def my_func_scope(a):
#     print("*"*20)
#     print("function called")
#     print("value of var 'a' inside this func is: " + str(a))
#     a = 2
#     print("va;ue of var 'a' after we assigned a new value to a: " + str(a))
# print("value of a before function is called: " + str(a))
# my_func_scope(a)
# print("value of global a is " + str(a))

# global variables donot change in the function
# local variables only have scope only inside the method
# they get garbage collected once method ends


#  global scope
a = 10
def my_func_scope():
    global a
    print("*"*20)
    print("function called")
    print("value of var 'a' inside this func is: " + str(a))
    a = 2
    print("va;ue of var 'a' after we assigned a new value to a: " + str(a))
print("value of a before function is called: " + str(a))
my_func_scope()
print("value of global a is " + str(a))
