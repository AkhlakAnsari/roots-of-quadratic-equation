# roots of quadratic equation ax**2 + bx + c = 0

# best way to import complex math module
import cmath
a = float(input('ENTER THE COEFFICIENT OF X^2='))
b = float(input('ENTER THE COEFFICIENT OF X='))
c = float(input('ENTER THE CONSTANT VALUE='))

# calculate the discriminant
d = (b**2) - (4*a*c)

# ROOT OF QUARDRATIC EQUATION IS
root1 = (-b-cmath.sqrt(d))/(2*a)
root2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(root1,root2))
#thanks akhlakansari94@gmail.com
