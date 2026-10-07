def Tinh_Max(a,b):
    if a>b:
        return a;
    else:
        return b;
print("Chương trình tính max của 3 số")
x = int(input('Nhập số thứ nhất:'))
y = int(input('Nhập số thứ hai:'))
z = int(input('Nhập số thứ ba:'))

Max = Tinh_Max(x,y)
Max = Tinh_Max(Max,z)
print(f"Max của {x}, {y}, {z} là: {Max}")

