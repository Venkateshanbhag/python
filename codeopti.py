# Algebraic Simplification

code = [
    "a = b + 0", 
    "c = 0 + d", 
    "e = f * 1",
    "g = 1 * h", 
    "i = j * 0", 
    "k = 0 * l"
]

for line in code:
    lhs,rhs = line.split("=")
    if "+ 0" in rhs or "0 +" in rhs:
        rhs = rhs.replace("+ 0","").replace("0 +","")
    if "* 1" in rhs or "1 *" in rhs:
        rhs = rhs.replace("* 1","").replace("1 *","")
    if "* 0" in rhs or "0 *" in rhs:
        rhs = "0"

    print(f"{lhs} = {rhs}")




print("\n\n____________________________\n\n")

# Common Subexpression Elimination

code = [
    "a = b + c", "d = b + c", "e = d + 1", "f = b + c"
]

seen = []

for line in code:
    lhs, rhs = line.split("=")
    if rhs not in seen:
        print(line)
    seen.append(rhs)




# Dead Code Elimination

print("\n\n____________________________\n\n")


code = [
    "a = 5", "b = 10", "c = a + b", "d = 20", "e = c * 2"
]
used = {"a","c","e"}

for line in code:
    lhs,rhs = line.split("=")
    lhs = lhs.strip()    
    if lhs in used:
        print(line)




print("\n\n____________________________\n\n")

# Simple Constant Propagation

code = [
    "a = 10",
    "b = a + 5",
    "c = b + 2"
]

constants = {"a":"10" , "b":"a + 5"}

for line in code:
    lhs, rhs = line.split("=")
    lhs = lhs.strip()
    for key,val in constants.items():
        rhs = rhs.replace(key,val)
    print(f"{lhs} = {rhs}")