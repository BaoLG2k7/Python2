import math 

A = float(input("Hệ số A: "))
B = float(input("Hệ số B: "))
C = float(input("Hệ số C: "))

Delta = B*B - 4*A*C 
print("Delta =", Delta ) 

if Delta<0:
    print("Phương trình vô nghiệm")
elif Delta == 0:
    print("Phương trình ")