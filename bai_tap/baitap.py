# 1.Viết chương trình tìm tất cả các số chia hết cho 7
# nhưng không phải bội số của 5, nằm trong đoạn 2000 và 3200
# (tính cả 2000 và 3200). Các số thu được sẽ được in thành
# chuỗi trên một dòng, cách nhau bằng dấu phẩy.

# string = []
# for i in range(2000, 3000):
#     if (i%7 == 0 ) and (i%5 != 0):
#        string.append(str(i))
# print(string)

# ---------------------------------------
# 2.Viết một chương trình có thể tính giai thừa
# của một số cho trước. Kết quả được in thành chuỗi
# trên một dòng, phân tách bởi dấu phẩy.
# Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.

# x=int(input("Nhap so can tinh giai thua: "))
# def fact(x):
#     if x == 0:
#         return 1
#     return x * fact(x -1)
# print(fact(x))

# ---------------------------------------
# 3.Với số nguyên n nhất định, hãy viết chương trình
# để tạo ra một dictionary chứa (i, i*i) như là 
# số nguyên từ 1 đến n (bao gồm cả 1 và n) sau đó 
# in ra dictionary này. Ví dụ: Giả sử số n là 8 thì đầu ra sẽ là: 
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}.

# x = int(input("Nhap 1 so nguyen: "))
# obj = dict()
# for i in range(1, x+1):
#     obj[i] = i*i
# print(obj)

# ---------------------------------------
# 4.Viết chương trình chấp nhận một chuỗi số,
# phân tách bằng dấu phẩy từ giao diện điều khiển,
# tạo ra một danh sách và một tuple chứa mọi số.

# value = input("Nhap vao day so: ")
# v = value.split(',')
# t = tuple(v)
# print(v)
# print(t)

# ---------------------------------------
# 5.Định nghĩa một class có ít nhất 2 method:
# getString: để nhận một chuỗi do người dùng nhập vào từ giao diện điều khiển.
# printString: in chuỗi vừa nhập sang chữ hoa.
# Thêm vào các hàm hiểm tra đơn giản để kiểm tra method của class.

# class InputOutStrings(object):
    
#     def __init__(self):
#         self.s = ""
        
#     def getString(self):
#         self.s = input("Nhap chuoi: ")
        
#     def printString(self):
#         print("ket qua: ", self.s.upper())    

# strObj = InputOutStrings()
# strObj.getString()
# strObj.printString()

# ---------------------------------------
# 6.Viết một method tính giá trị bình phương của một số.

# class squareNumber(object):

#     def __init__(self):
#         self.s = 0
    
#     def square(self):
#         self.s = int(input("Nhap so muon tinh: "))
#         print("Ket qua: ", self.s * 2)

# x = squareNumber()
# x.square()

# ---------------------------------------
# 7.