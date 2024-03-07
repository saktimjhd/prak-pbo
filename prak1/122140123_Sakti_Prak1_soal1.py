def hitung(batas1, batas2):
    if batas1 < 0 or batas2 < 0:
        print("Batas bawah dan atas yang dimasukan tidak boleh di bawah Nol")
        return

    ganjil = 0
    for i in range(batas1, batas2):
        if i % 2 != 0:
            print(i)
            ganjil += i

    print("Total:", ganjil)

batas1 = int(input("batas bawah : "))
batas2 = int(input("batas atas : "))

hitung(batas1, batas2)