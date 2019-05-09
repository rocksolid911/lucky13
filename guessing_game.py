scrt_no = 9
g_count = 0
g_limit = 4
while g_count < g_limit:
    guess = int(input('guess: '))
    g_count += 1
    if guess == scrt_no:
        print("yeeeeeeee!!!!!!!")
        break
else:
    print("try again")