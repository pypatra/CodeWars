# Kuadrat Sempurna


# Cara 1
def is_square(n: int) -> bool:
    if n < 0:
        return False
    akar: int = int(n**0.5)
    if akar * akar == n:
        return True
    else:
        return False


# Cara 2
def is_square(n: int) -> bool:
    return n >= 0 and n**0.5 % 1 == 0
