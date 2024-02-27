def binary_array_to_number(arr: list[int]) -> int:
    result: int = 0
    for i, j in enumerate(arr[::-1]):
        if j == 1:
            result += 2**i

    return result


# print(binary_array_to_number([0,0,0,1]))


# Cara 2
def binary_array_to_number(arr: list[int]) -> int:
    return int(
        "".join(str(i) for i in arr),
        base=2
    )  # int("",base = 10) default nya base 10



