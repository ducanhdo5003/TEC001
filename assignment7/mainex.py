import random

class Car:
    def __init__(self, registration_number, max_speed):
        """(Ex1)"""
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):
        """(Ex2)"""
        self.current_speed += change_of_speed
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        """(Ex3)"""
        self.travelled_distance += self.current_speed * hours

# --- (Ex4) ---

cars = []
for i in range(1, 11):
    reg_num = f"ABC-{i}"
    max_s = random.randint(150, 200)
    cars.append(Car(reg_num, max_s))

race_on = True
while race_on:
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
        if car.travelled_distance >= 10000:
            race_on = False

print(f"{'Reg. Number':<12} | {'Max Speed':<10} | {'Cur. Speed':<10} | {'Distance':<10}")
print("-" * 55)
for car in cars:
    print(f"{car.registration_number:<12} | {car.max_speed:<10} | {car.current_speed:<10} | {car.travelled_distance:<10.1f} km")


# --- (Ex5) ---


time_spent = "3.5"

with open("time_log.txt", "w") as file:
    file.write(time_spent)

print("Created file time_log.txt successfully!")