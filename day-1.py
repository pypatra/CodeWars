# Cara 1
def even_or_odd(number: int) -> str:
    if number % 2 == 0:
        return "Even"
    return "Odd"


# Cara 2
def even_or_odd(number: int) -> str:
    return "Even" if number % 2 == 0 else "Odd"


# Cara 3
even_or_odd: str = lambda number: "Even" if number % 2 == 0 else "Odd"


# Cara 4
def even_or_odd(number: int) -> str:
    return ["Even", "Odd"][number % 2]


"""
? Cara Kerjanya:
*["Even","Odd"] list yang tidak ditampung dalam variabel kalo di tampung bentuknya kek gini

* x = ["Even","Odd"]
* def even_or_odd(number):
     *return x[number%2]
    
[number%2] nah hasil dari Mod 2 itu pasti 0 kalo ngga 1 
tapi ini juga kurang bagus karena
konsep python adalah lebih baik explisit dari pada impisit 
yang baik seperti ini 

def even_or_odd(number: int):
    if number % 2 == 0:
        return "Even"
    elif number % 2 == 1:
        return "Odd"
    else:
        return "Input Harus Angka"
        
    """
