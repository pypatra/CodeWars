def disemvowel(string_: str) -> str:
    return "".join(
        i
        for i in string_
        if i not in ["a", "i", "u", "e", "o", "A", "I", "U", "E", "O"]
    )


print(disemvowel("Pypatra"))
