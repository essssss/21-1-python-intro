age = 19
is_birthday = True

if age >= 21:
    print("you can drink")
    if is_birthday:
        print("happy birthday! Drinks are on Chad!")
elif age >= 18:
    print("come in, but don't drink")
    if is_birthday:
        print("happy birthday! Still don't get a beer")
else:
    print("sorry, go home.")