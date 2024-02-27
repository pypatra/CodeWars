def is_triangle(a: int, b: int, c: int) -> bool:
    return a + b > c and c + a > b and c + b > a
