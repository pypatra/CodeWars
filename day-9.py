def high_and_low(numbers: str) -> str:
    result: list[int] = [int(number) for number in numbers.split()]
    return f"{max(result)} {min(result)}"

print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))