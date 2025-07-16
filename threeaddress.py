statements = [
    "A = B + C",
    "B = A - D",
    "C = B + C",
    "D = B"
]

for line in statements:
    lhs,rhs = line.split("=")

    reg  = "R1"

    if "+" in rhs:
        op1,op2 = rhs.split("+")
        print(f"MOV {reg} , {op2}")
        print(f"ADD {reg} , {op1}")
        print(f"MOV {lhs} , {reg}")

    elif "-" in rhs:
        op1,op2 = rhs.split("-")
        print(f"MOV {reg} , {op2}")
        print(f"SUB {reg} , {op1}")
        print(f"MOV {lhs} , {reg}")

    elif "*" in rhs:
        op1,op2 = rhs.split("*")
        print(f"MOV {reg} , {op2}")
        print(f"MUL {reg} , {op1}")
        print(f"MOV {lhs} , {reg}")

    elif "/" in rhs:
        op1,op2 = rhs.split("/")
        print(f"MOV {reg} , {op2}")
        print(f"DIV {reg} , {op1}")
        print(f"MOV {lhs} , {reg}")

    else:
        print(f"MOV {lhs} , {rhs}")