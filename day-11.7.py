def validate_pin(pin: str) -> bool:
    return [False, True][(len(pin) == 4 or len(pin) == 6) and (pin.isdigit())]


print(validate_pin("090988"))
