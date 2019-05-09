weight = int(input("enter your weight: "))
print(f'''your weight is {weight}
is it in pound or kilos ?''')
unit = input("(l)pound or (k)kilogram: ")
if unit.upper() == "L":
    convert = weight * 0.45
    print(f"you are {convert} kilos")
else:
    convert = weight / 0.45
    print(f"you are {convert} pound")



