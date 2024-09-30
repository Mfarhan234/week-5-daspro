# Masukan jumlah murid N, jumlah baris r, dan jumlah kolom c
N, r, c = map(int, input().split())

posisi_siswa = []

for _ in range (N):
    P, x, y = map(int, input().split())
    posisi_siswa.append((P, x, y))
    
for siswa in posisi_siswa:
    P, x, y = siswa
    bersebelahan = []
    for s in posisi_siswa: # s adalah keterangan untuk satu siswa
        if s[1] == x:
            if s[2] == y-1 :
                bersebelahan.append(s[0])
            elif s[2] == y+1 :
                bersebelahan.append(s[0])
if bersebelahan:
    for nomor in bersebelahan:
        print (nomor, end=' ')
else:
    print (0)
    
print()

