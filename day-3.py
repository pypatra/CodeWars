def double_char(s: str) -> str:
    result: str = ""
    for i in s:
        result += i * 2
    return result



def double_char(s: str) -> str:
  return "".join(i*2 for i in s)

print(double_char("afiqi"))