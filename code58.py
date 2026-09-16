try: #thực hiện các lệnh và kiểm soát lỗi 
    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))
except: #nếu có lỗi xảy ra sẽ thực hiện theo các lệnh trong except
    print("lỗi nhập số nguyên")
else:
    tong = a+b
    print("Tổng hai số là: ", tong)
print("Kết thúc chương trình")

