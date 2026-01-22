def cabin_class():
    cabin = input("Enter the cabin class (LUX, A, B, C): ")

    if cabin == "LUX":
        print("LUX: upper-deck cabin with a balcony.")
    elif cabin == "A":
        print("A: above the car deck, equipped with a window.")
    elif cabin == "B":
        print("B: windowless cabin above the car deck.")
    elif cabin == "C":
        print("C: windowless cabin below the car deck.")
    else:
        print("Invalid cabin class.")

cabin_class()