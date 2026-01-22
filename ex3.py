def check_hemoglobin():
    a = input("Enter biological sex (male/female): ")
    b = float(input("Enter hemoglobin value (g/l): "))

    if a == "female":
        if b < 117:
            print("Hemoglobin value is low.")
        elif 117 <= b <= 155:
            print("Hemoglobin value is normal.")
        else:
            print("Hemoglobin value is high.")
    elif a == "male":
        if b < 134:
            print("Hemoglobin value is low.")
        elif 134 <= b <= 167:
            print("Hemoglobin value is normal.")
        else:
            print("Hemoglobin value is high.")
    else:
        print("Invalid input for sex.")
check_hemoglobin()