import numpy as np
import matplotlib.pyplot as grafik

x1 = int(input('Masukan nilai x1  : '))
y1 = int(input('Masukan nilai y1  : '))
x2 = int(input('Masukan nilai x2  : '))
y2 = int(input('Masukan nilai y2  : '))

print('=====================================================')

x = x1
y = y1

if x1 == x2:
    titik_A = []
    titik_B = []
    for i in range(1, y2, 1):
        print('Garis yang di lewati oleh titik A da titik B yaitu', x, ',', y+i)
        titik_A.append(x)
        titik_B.append(y+i)
    grafik.plot(titik_A, titik_B)
    grafik.show()


elif y1 == y2:
    titik_A = []
    titik_B = []
    for i in range(1, x2, 1):
        print('Garis yang di lewati oleh titik A dan B yaitu', x+i, ',', y)
        titik_A.append(x+i)
        titik_B.append(y)
    grafik.plot(titik_A, titik_B)
    grafik.show()


else:
    titik_A = []
    titik_B = []
    m_gradiengaris = (y2 - y1) / (x2 - x1)
    N = x2 - x1 + 1
    for i in range (1,N,1):
        nilai_y = m_gradiengaris * (x - x1) + y1
        ya = round(nilai_y)
        print('Garis yang di lewati oleh titik A da titik B yaitu ', x-1,',', ya)
        titik_A.append(x-1)
        titik_B.append(ya)
        x+=1

    grafik.plot(titik_A,titik_B)
    grafik.show()