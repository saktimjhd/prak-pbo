r = float(input("Masukan jari jari : "))
phi = float(3.14)

if (r >= 0) :

    keliling = float(2*phi*r)
    luas = float(phi**r)

    print("Kelilingnya adalah : ",keliling)
    print("Luasnya adalah : ", luas)
else:
    print("Jari jari tidak boleh negatif")