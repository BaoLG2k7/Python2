print ("Enter a:")
a = int(input())
print ("Enter b:")
b = int(input())
print ("Enter c:")
c = int(input())

if a+b>=c and b+c>=a and c+a>=b:
    p = (a + b + c) / 2
    S1 = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("The are of the triangle is: ", S1)
else:
    print("a, b, and c are not sides of a triangle")