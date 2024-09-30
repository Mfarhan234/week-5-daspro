r, c, N = map(int, input().split())
matrix = []
for i in range (r):
    matrix.append(list(map(int, input().split())))
arah_gerakan = input()

x, y = 0, 0
total_emas = matrix[x][y]
gerakan = 1
for langkah in arah_gerakan:
    if langkah == 'R':
        if y + 1 < c:
            y += 1
            total_emas += matrix[x][y]+3
        else:
            gerakan = 0
            break
    if langkah == 'L':
        if y - 1 < 0:
            y -= 1
            total_emas -= matrix[x][y] - 2
        else:
            gerakan = 0
            break
    if langkah == 'D':
        if x + 1 < 0:
            x += 1
            total_emas += matrix[x][y] + 3
        else:
             gerakan = 0
             break
    if langkah == 'U':
        if x - 1 < 0:
            x -= 1
            total_emas -= matrix[x][y] - 2
        else:
            gerakan = 0
            break
print (total_emas)
if not gerakan :
    print ("gerakanmu salah bung !")