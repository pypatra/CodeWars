#Cara 1
def accum(st: str,) -> str:
    return "-".join(l.upper() + l.lower() * i for i, l in enumerate(st))

# Cara 2
def accum(st: str,) -> str:
    return "-".join((l + l * i).title() for i, l in enumerate(st))


# print(accum("ZpglnRxqenU"))
