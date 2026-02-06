''''
You have three integers: x, y, and z.
They must satisfy these rules:
All are positive integers
x + y + z = 10
x > y
y > z
x * z = 8
Your task: use Z3 to find valid values of x, y, and z.
'''

from z3 import *

x = Int('x')
y = Int('y')
z = Int('z')

s = Solver()

s.add(x + y + z == 10)
s.add(x > y)
s.add(y > z)
s.add(x * z == 8)

if s.check() == sat:
    m = s.model()
    print("Solution found:")
    print("x =", m[x])
    print("y =",m[y])
    print("z =", m[z])
else:
    print("No solution exists.")
    
    