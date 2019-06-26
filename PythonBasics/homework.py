# create a method takes state and gross income as args
# states_list = ['cali','tex','ten']
# returns net income after decuting taxbased on state

# stateTax for california 8%
def my_tax(state,gross_income):
    fedTax = 0.1 * gross_income
    netIncome = gross_income - fedTax - states_func(state,gross_income)
    return netIncome

def states_func(state,gross_income):
    # cali state
    if state == 'cali':
       return  (0.1 * gross_income)
    elif state == 'ark':
        return (0.09 * gross_income)
    else:
       return  (0.05 * gross_income)

print(my_tax('cali',100000))
print(my_tax('ark',100000))
print(my_tax('tex',100000))
# federl tax 10%
# state tax  ur wish
# do for 2 states