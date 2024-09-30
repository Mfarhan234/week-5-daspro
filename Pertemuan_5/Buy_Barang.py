N, M = map(int, input().split())
Pi = map(int, input().split())
Ci = map(int, input().split())

Harga_barang = [] 
Pecahan_uang = []

for _ in range (Pi):
    Harga_barang.append(Pi)
for _ in range (Ci):
    Pecahan_uang.append(Ci)

total_harga = []
for harga in Harga_barang:
    total_harga += harga
    
total_uang = []
for uang in Pecahan_uang:
    total_uang += uang

Hutang = total_harga - total_uang

