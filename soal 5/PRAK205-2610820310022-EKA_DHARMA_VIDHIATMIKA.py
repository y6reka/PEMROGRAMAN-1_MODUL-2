import math
import sys

input_data = sys.stdin.read().split()
A, B = map(float, input_data)

alas = math.sqrt(B**2 - A**2)
tinggi = A
keliling = alas + tinggi + B
luas = 0.5 * alas * tinggi

print(f"Alas = {alas:.0f} cm")
print(f"Tinggi = {tinggi:.0f} cm")

