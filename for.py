for x in range(5):
    for y in range(4):
        print(f"({x}, {y})")

number = [5, 4, 3, 2, 1]
for x_cnt in number:
    output = ""
    for cnt in range(x_cnt):
        output += "x"

    print(output)