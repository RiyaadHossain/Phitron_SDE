def argFunc(*arg):
    for i in arg:
        print(i)
    
argFunc(34, 23, "hello")

""" 
output:
    34
    23
    hello
"""

def kwargFunc(**kargs):
    for k,v in kargs.items():
        print(k,v)

kwargFunc(name="Riyad", age= 23)

""" 
output:
    name Riyad
    age 23
"""