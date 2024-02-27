def double_char(s):
    result = ""
    for i in s:
        result += i * 2
    return result



def double_char(s):
  return "".join(i*2 for i in s)

print(double_char("afiqi"))