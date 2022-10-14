from math import *
from end_full import*
from numba import njit
SIN=[]
COS=[]
PI=3.1415

for i in range(3600):
    SIN.append(float(sin(i*PI/1800)))
for i in range(3600):
    COS.append(float(cos(i*PI/1800)))





#@njit(fastmath=True)
def MuMnozh3(Mx,My):
    Mrez = [[1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]]
    Mrez[0][0] = Mx[0][0] * My[0][0] + Mx[0][1] * My[1][0] + Mx[0][2] * My[2][0]
    Mrez[0][1] = Mx[0][0] * My[0][1] + Mx[0][1] * My[1][1] + Mx[0][2] * My[2][1]
    Mrez[0][2] = Mx[0][0] * My[0][2] + Mx[0][1] * My[1][2] + Mx[0][2] * My[2][2]
    Mrez[1][0] = Mx[1][0] * My[0][0] + Mx[1][1] * My[1][0] + Mx[1][2] * My[2][0]
    Mrez[1][1] = Mx[1][0] * My[0][1] + Mx[1][1] * My[1][1] + Mx[1][2] * My[2][1]
    Mrez[1][2] = Mx[1][0] * My[0][2] + Mx[1][1] * My[1][2] + Mx[1][2] * My[2][2]
    Mrez[2][0] = Mx[2][0] * My[0][0] + Mx[2][1] * My[1][0] + Mx[2][2] * My[2][0]
    Mrez[2][1] = Mx[2][0] * My[0][1] + Mx[2][1] * My[1][1] + Mx[2][2] * My[2][1]
    Mrez[2][2] = Mx[2][0] * My[0][2] + Mx[2][1] * My[1][2] + Mx[2][2] * My[2][2]
    return Mrez

def MuMnozh1(Mx,My,coords):
    return[Mx[0][0] * (My[0]) + Mx[0][1] * (My[1]) + Mx[0][2] * (My[2]),
           Mx[1][0] * (My[0]) + Mx[1][1] * (My[1]) + Mx[1][2] * (My[2]),
           Mx[2][0] * (My[0]) + Mx[2][1] * (My[1]) + Mx[2][2] * (My[2])]
    #return Mrez
def Sort(mas_cube,temp):
    for i in range(1,temp):#range(len(mas_cube)):
        j=i
        while(j>0):
            if (mas_cube[j-1][3]<mas_cube[j][3]):
                tmp=mas_cube[j-1]
                mas_cube[j-1]=mas_cube[j]
                mas_cube[j]=tmp
                j-=1
            else:
                break
    return mas_cube