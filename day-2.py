def digitize(n: int):
    n = str(n)
    result = []
    for i in n:
        result.append(int(i))
    result.reverse()
    return result


# print(digitize(35231))


def digitize(n: int):
    return [int(x) for x in str(n)[::-1]]


x = "ajnsjnajnajsj"

print(x[::-1])