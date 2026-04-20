x, y, z = input("Expression: ").split(" ",maxsplit=3)
if y == "+":
    ans = float(x) + float(z)
    print(f"{ans}")
elif y == "-":
    ans = float(x) - float(z)
    print(f"{ans}")
elif y == "*":
    ans = float(x) * float(z)
    print(f"{ans}")
elif y == "/":
    ans = float(x) / float(z)
    print(f"{ans}")
else:
    print("Invalid Expression")