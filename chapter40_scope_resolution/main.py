# variable scope = where a variable is accessible and visible
# scope resolution => LEGB => Local -> Enclosed -> Global -> Built-in

from math import e

def foo():
    print(e)

e = 3

foo() # expected outcome 3 because global overwrites builtin

