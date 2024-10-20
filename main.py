# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

### --> Ham import <---
import math
from math import *     # import ham toan tu

def Thetich_hinhtru(r, h): # BT01: The tich hinh tru
    V = pi * r ** r * h
    return V
# Nhap cac thong so dau vao
    # --> hinh tru
r = float(input('Nhap ban kinh hinh tru = '))
h = float(input('Nhap chieu cao hinh tru = '))

    # --> tam giac radian
a = float(input('Nhap canh a = '))
b = float(input('Nhap canh b = '))
c = float(input('Nhap canh c = '))

def Dientich_tamgiac_radian(a, b, c): # BT02: Tinh dien tich tam giac radian
    Cos_C = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b) # cos(C) = (a^2+b^2-c^2)/2ab ; goc C = acos(C)
    Goc_C = acos(Cos_C)
    S = 1/2 * a * b * sin(Goc_C)
    return S

def Dientich_tamgiacdeu_heron(a): # BT03: Tinh dien tich tam giac deu heron
    S_deu = a**2 * sqrt(3)/4
    return S_deu

def DanhgiaKQ_pro_2tamgiac(S, S_deu):  # So sánh với sai số tuyệt đối
    if math.isclose(S, S_deu, abs_tol=1e-9):
      return 'Kết quả giống nhau trong phạm vi sai số cho phép'
    else:
        return 'Kết quả khác nhau'

# Goi ham phep tinh
    # BT01: Tinh the tich hinh tru nhap vao 2 thong so r va h
V = Thetich_hinhtru(r, h)
    # BT02: Tinh dien tich hinh tam giac bat ky nhap vao 3 canh theo (radian = 1/2 ab sin(C))  -> b1: tim cos(C) -> b2: goc C = acos(C) -> b3: sin(C)
S = Dientich_tamgiac_radian(a, b, c)
    # BT03: Tinh dien tich hinh tam giac deu heron nhap vao canh a
S_deu = Dientich_tamgiacdeu_heron(a)
    # BT04: Danh gia kqua 2 chuong trinh tinh dien tich tam giac
Danhgia_KQ = DanhgiaKQ_pro_2tamgiac(S, S_deu)


# In KQ ra man hinh
    # hinh tru
print('--> The tich hinh tru = ', V)
print('--> Dien tich tam giac tinh theo radian = ', S)
print('--> Dien tich tam giac deu heron = ', S_deu)
print('Ket qua danh gia 2 chuong trinh cua tam giac: ', '--->', Danhgia_KQ)

