# Membaca input
N, K = map(int, input().split())
harga_buah = list(map(int, input().split()))

jumlah_buah_dibeli = 0
# Cek setiap harga buah apakah bisa dibeli
for harga in harga_buah:
    if K >= harga: # Jika uang cukup untuk membeli buah ini
        jumlah_buah_dibeli += 1# Hitung buah yang bisa dibeli

print(jumlah_buah_dibeli)