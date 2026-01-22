def zander():
    a = float(input("Enter the length: "))
    limit = 42

    if a >= limit:
        print("The fish meets the size limit. Enjoy your catch!")
    else:
        b = limit - a
        print("Release the fish back into the lake.")
        print(b, "centimeters below the size limit the caught fish was.")