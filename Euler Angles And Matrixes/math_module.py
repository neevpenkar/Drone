import math

PI = math.pi
accuracy = 3

R = 0
D = 1

class Angle:
    ''' 0 -> Radians | 1 -> Degrees '''

    def __init__(self, value, flag):
        if flag == 0:
            self.rad = value
            self.deg = round(value * 57.2958, accuracy) # See below
        elif flag == 1:
            self.deg = value
            self.rad = round(value * 0.0174533, accuracy) # See below
        else:
            raise ValueError("Illegal Flag")
        return
    
    #def rad(self):
    #    return self.radian

    #def deg(self):
    #    return self.degree

def convert2deg(rad: float):
    ans = 57.2958 * rad
    return  #The magic number is the conversion value

def convert2rad(deg: float):
    ans = 0.0174533 * deg
    return round(ans, accuracy) #The magic number is the conversion value

#def cos(x: float):
#    return round(math.cos(x), accuracy)

#def sin(x: float):
#    return round(math.sin(x), accuracy)

#def tan(x: float):
#    return round(math.tan(x), accuracy)

#def arctan(x: float):
#    return round(math.atan(x), accuracy)

# --

def cos(ang: Angle):
    return round(math.cos(ang.rad), accuracy)

def sin(ang: Angle):
    return round(math.sin(ang.rad), accuracy)

def tan(ang: Angle):
    return round(math.tan(ang.rad), accuracy)

def arctan(x: float):
    ang = Angle(round(math.atan(x), accuracy), R)
    return ang

def arctan2(y: float, x: float):
    ang = Angle(round(math.atan2(y,x), accuracy), R)
    return ang