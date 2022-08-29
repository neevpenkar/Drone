from math import atan2
from matrix_h import *

AxisZ = -PI / 2
AxisY = 0
AxisX = 0

start = [1,0,0]

psi = Angle(AxisX, R)
theta = Angle(AxisY, R)
phi = Angle(AxisZ,R)

rotation = multiply2(RotationZ(phi), RotationY(theta))
rotation = multiply2(rotation, RotationX(psi))

rotation.printMatrix()
print('\n')

l = multiply1(start, rotation)
print(l)












#a = PI / 2
#b = PI / 4
#c = PI / 2

#phi = Angle(a,R)
#theta = Angle(b,0)
#psi = Angle(c,0)

#rotation = multiply2(RotationZ(psi), RotationY(theta))
#rotation = multiply2(rotation, RotationX(phi))

#rotation.printMatrix()

#print("Psi: ", atan2(rotation.row3[1], rotation.row3[2]))
#print("Phi: ", atan2(rotation.row2[0], rotation.row1[0]))

#starting_position = [0,0,1]
#ry = RotationY(PI / 2.0)

#rot1 = multiply1(starting_position, ry)

#print(rot1)
#rx.printMatrix()

#mat1 = Matrix([1,2,3,4,5.89,6,7.9,8,9])
#mat2 = Matrix([9.980,8,7,6,5,4,3,2.4,1])

#print(mat2.rows)
#print(mat2.columns)

#t = multiply2(mat1, mat2)
#t.printMatrix()

#a = Angle(2*PI, 0)
#print(a.deg)
#print(a.rad)

