import random

# Tangga dan ular (posisi_awal : posisi_tujuan)
tangga = {3: 10, 6: 14, 9: 18}
ular = {16: 8, 19: 5, 24: 12}

pos = 1   # posisi awal

while pos < 30:
    input("Tekan ENTER untuk lempar dadu...")
    dadu = random.randint(1, 6)
    print(f"Dadu: {dadu}")

    pos += dadu

    print(f"Kamu sampai di kotak {pos}")

    if pos in tangga:
        pos = tangga[pos]
        print(f"Naik tangga! Sekarang di kotak {pos}")
    elif pos in ular:
        pos = ular[pos]
        print(f"Digigit ular! Turun ke kotak {pos}")

print("Selamat! Kamu sampai di kotak 30 ")
