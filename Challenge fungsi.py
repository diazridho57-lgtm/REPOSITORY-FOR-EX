def total_harga(jumlah, harga_per_item=10000, diskon=0.0, pajak= 0.1):
    subtotal = jumlah * harga_per_item
    potongan = subtotal * diskon
    total_setelah_diskon = subtotal - potongan
    total_akhir = total_setelah_diskon * (1 + pajak)
    return total_akhir

print(total_harga(3))
print(total_harga(5, 15000, diskon=0))
print(total_harga(2, 20000, diskon=0.2, pajak=0.15))
print(total_harga(4, pajak=0.05))
