# file that has code that you want to include in program
# use import keyword to use these parts of code (include module) these can be built-in or made by yourself
# break down large project in smaller reusable parts of code => good for low coupling and high cohesion ?

# print(help("modules")) # get all built in modules (information)
# print(help("math")) # get all code from module (information)

import math
print(math.pi)

import math as m # import a module and give it an alias => all functions and data from this module has now to be preceded by the alias
print(m.pi)

from math import e, pi # import something specific from a module
# danger with doing this => naming conflicts
# suppose another variable named e than e from math would be overwritten, 'import math' prevents this.
print(e)
print(pi)

import example
print(example.get_author())