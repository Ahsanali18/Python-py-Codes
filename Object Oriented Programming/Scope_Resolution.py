# variable scope = where a variable is visible and accessible
# scrope resolution = (LEGB) local -> Enclosed -> Global -> Built-in

"""
def function1():
    x=1
    print(x)

def function2():
    x=2
    print(x)

function1()
function2()
"""
"""
def function1():
    x=1
    def function2():
        x=2
        print(x)
    function2()

function1()
"""
"""
def function1():
    print(x)

def function2():
    print(x)
    
x=3

function1()
function2()
"""
from math import e

def function1():
    print(e)

e=4 # The above print statement will print this e value because global comes before any built-in variable in LEGB order.
function1()