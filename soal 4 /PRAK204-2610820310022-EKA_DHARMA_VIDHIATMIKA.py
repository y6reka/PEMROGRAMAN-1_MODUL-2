import sys

input_data = sys.stdin.read().split()
r, t = map(float, input_data)
phi =3.142857 

volume = phi * r * r * t
luas = 2 * phi * r * (r + t)
keliling = 2 * phi * r

print(f"Volume = {volume:.2f}")
print(f"Luas = {luas:.2f}")
print(f"Keliling = {keliling:.2f}")

