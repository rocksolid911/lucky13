cmd = ""
start = False
while True:
    cmd = input("> ").lower()
    if cmd =="start":
        if start:
            print("car is already started")

        else:
            start =True
            print("car is started.....")
    elif cmd == "stop":
        if not start:
            print("car is already stoped")
        else:
            start = False
            print("car is stoped...")
    elif cmd == "help":
        print('''
start -> to start the car
stop -> to stop the car
quit -> to quit the game
        
        ''')
    elif cmd == "quit":
        break
    else:
     print("enter correct commnd")

