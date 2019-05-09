name = input("name: ")

if len(name) < 3:
    print("name must be 3 charachter")

elif len(name) > 50:
    print("name must be less then 50 character")

else:
    print("name looks good")