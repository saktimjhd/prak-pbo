class Rectangle:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    
    def hitungLuas(self):
        return self.panjang * self.lebar
    
    def hitungKeliling(self):
        return 2 * (self.panjang + self.lebar)

panjang = float(input("Masukkan panjang : "))
lebar = float(input("Masukkan lebar : "))

persegi_panjang = Rectangle(panjang, lebar)

print("Luas persegi panjang:", persegi_panjang.hitungLuas())
print("Keliling persegi panjang:", persegi_panjang.hitungKeliling())