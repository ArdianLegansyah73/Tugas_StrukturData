def bintang_ganjil(jumlah_baris):
    pola = [3]  # list untuk menyimpan setiap baris bintang

    for i in range(1, jumlah_baris + 1):
        bintang = '*' * (2 * i - 1)  # jumlah bintang ganjil: 1, 3, 5, dst.
        pola.append(bintang.center(2 * jumlah_baris - 1))  # diratakan ke tengah

    return pola


jumlah_baris = 3
hasil = bintang_ganjil(jumlah_baris)

for baris in hasil:
    print(baris)
