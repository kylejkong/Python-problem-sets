def formula():
    x, y, z = input("Sample 1 + 1(Leave one space between first and last number(s)): ").split(" ")
    # print(x, y, z)
    fx = float(x)
    fz = float(z)
    #print(f"{answer:.2f}")  2 decimals



    if y == "+":
        answer = fx + fz

        print(f"{answer:.1f}")

    if y == "-":
        answer = fx - fz
        print(f"{answer:.1f}")

    if y == "*":
        answer = fx * fz
        print(f"{answer:.1f}")

    if y == "/":
       answer = fx / fz
       print(f"{answer:.1f}")



formula()