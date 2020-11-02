def challenge1IfElse(a):
    if (a%2 == 1):
        return("Weird")
    elif (a%2 == 0) and (2 <= a <=5):
        return("Not Weird")
    elif (a%2 == 0) and (6 <= a <=20):
        return("Weird")
    elif (a%2 == 0) and (a > 20):
        return("Not Weird")

print(challenge1IfElse(2))
print(challenge1IfElse(4))
print(challenge1IfElse(5))
print(challenge1IfElse(14))
print(challenge1IfElse(24))
print(challenge1IfElse(25))
