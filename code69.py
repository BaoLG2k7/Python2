import math 

def equationroots(a, b, c):

    delta = b * b - 4 * a * c 
    if delta > 0:
        S2 = math.sqrt(abs(delta))
    else:
        S2 = 0 
    return S2

print ("Enter a:")
a = int(input())
if a == 0:
    print("The constant a must be non-zero")
    exit()

print ("Enter b:")
b = int(input())
print ("Enter c:")
c = int(input())
print ("Enter c:")
x = int(input())

S1 = a*x*x + b*x + c
print("S1= ",S1)

S2 = equationroots(a,b,c)
print("S2= ",S2)
