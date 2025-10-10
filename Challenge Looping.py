angka_rahasia = 19
percobaan = 0

while True:
    tebakan = int(input("Masukkan angka: (1-20) "))
    percobaan += 1

    if tebakan == angka_rahasia:
        print("Anda benar, dalam percobaan ke - ", percobaan)
        break
    elif tebakan < angka_rahasia:
        print("Terlalu kecil")
    elif tebakan > angka_rahasia:
        print("Terlalu besar")
    else: 
        print("Coba lagi")

