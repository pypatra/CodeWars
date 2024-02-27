#Cara 1
def row_sum_odd_numbers(n: int) -> int:
    angka = n * (n - 1) + 1
    tambah = sum(range(angka, angka + (2 * n), 2))
    return tambah

  
#Cara 2
def row_sum_odd_numbers(n: int) -> int:
  return n**3

print(row_sum_odd_numbers(3))



