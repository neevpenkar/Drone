from typing import Iterable
from math_module import *

size = 3
def dot_product(vec1, vec2):
    sum = 0
    for i in range(3):
        sum += vec1[i] * vec2[i]
        sum = round(sum, accuracy)
    return sum

class Matrix:
    def __init__(self, values: Iterable):
        self.row1 = [values[0], values[1], values[2]]
        self.row2 = [values[3], values[4], values[5]]
        self.row3 = [values[6], values[7], values[8]]

        self.col1 = [values[0], values[3], values[6]]
        self.col2 = [values[1], values[4], values[7]]
        self.col3 = [values[2], values[5], values[8]]

        self.rows = [self.row1, self.row2, self.row3]
        self.columns = [self.col1, self.col2, self.col3]
        return
    
    def printMatrix(self):
        print(self.row1)
        print(self.row2)
        print(self.row3)
        return


def multiply1(vec, mat: Matrix):
    newVec = []
    newVec.append(dot_product(vec, mat.col1))
    newVec.append(dot_product(vec, mat.col2))
    newVec.append(dot_product(vec, mat.col3))

    for i in newVec:
        i = round(i, accuracy)
    return newVec

def multiply2(mat1: Matrix, mat2: Matrix):
    temp = []
    for i in range(size):
        for j in range(size):
            temp.append(dot_product(mat1.rows[i], mat2.columns[j]))
    t = Matrix(temp)
    return t

def RotationX(psi: Angle):
    ''' Angle Object '''
    temp = [1.0,0.0,0.0,0.0,cos(psi),-sin(psi),0.0,sin(psi),cos(psi)]
    tempMat = Matrix(temp)
    return tempMat

def RotationY(theta: Angle):
    ''' Angle Object '''
    temp = [cos(theta),0.0,sin(theta),0.0,1.0,0.0,-sin(theta),0.0,cos(theta)]
    tempMat = Matrix(temp)
    return tempMat

def RotationZ(phi: Angle):
    ''' Angle Object '''
    temp = [cos(phi),-sin(phi),0.0,sin(phi),cos(phi),0.0,0.0,0.0,1.0]
    tempMat = Matrix(temp)
    return tempMat

def rotationOfAxis(theta: Angle):
    '''Angle Object '''
    temp = [cos(theta),sin(theta),-sin(theta),cos(theta)]
    tempMat = Matrix(temp)
    return tempMat

