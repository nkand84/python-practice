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