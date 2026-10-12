data = []

while len(data) < 6:
    baris = input().split()
    data.extend(baris)

a, b, i, j, x, y = map(float, data[:6])

hasil = ((a - b) * i / j) - (x + y)

print(f"{hasil:.3f}")

