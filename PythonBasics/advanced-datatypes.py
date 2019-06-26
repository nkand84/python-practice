# dictionary practice
# has keys and values
cars = {
     'bmw':{
         'model': {
             'model-num':'550i', 'year' : 2015,'color': 'red'}
     },
    'benz':{
        'model' : 's-class',
        'year':2018
    }
}
# in order to get year on the benz car

print(cars['benz']['year'])

# to get the model num of bmw
print(cars['bmw']['model']['model-num'])

print("*"*50)

# arrays

cars = ["benz","porsche","volvo","ferrari","volvo"]
print(cars)

# diff methods on lists (lists are arrays in python)
print(len(cars))
# remove method can only remove the first instance of item 
# cars.remove("volvo")
cars.pop(4)
print(cars)