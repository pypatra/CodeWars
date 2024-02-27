def abbrev_name(name: str) -> str:
    return ".".join(i[0].upper() for i in name.split(" "))
  
print(abbrev_name("Python Patra"))
