move = input("Does it move? (yes/no) ")

if move == "yes":
    should1 = input("Should it? (yes/no) ")
    if should1 == "yes":
        print("No problem!")
    elif should1 == "no":
        print("Please use some duct tape.")
    else:
        print("I'm sorry but I don't understand!")
elif move == "no":
    should2 = input("Should it? (yes/no) ")
    if should2 == "yes":
        print("Use a can of WD-40, it should be fine.")
    elif should2 == "no":
        print("No problem!")
    else:
        print("I'm sorry I don't understand!")
else:
    print("You didn't answer my question! Yes or no.")
