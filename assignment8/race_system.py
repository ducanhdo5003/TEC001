import random


class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours=1):
        self.travelled_distance += self.current_speed * hours


class Race:
    def __init__(self, name, distance_km, car_list):
        self.name = name
        self.distance_km = distance_km
        self.cars = car_list

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        print(f"\nRace: {self.name}")
        header = f"{'Reg. Number':<12} | {'Max Speed':<10} | {'Cur. Speed':<10} | {'Distance':<12}"
        print(header)
        print("-" * len(header))
        for car in self.cars:
            print(
                f"{car.registration_number:<12} | {car.max_speed:<10} | {car.current_speed:<10} | {car.travelled_distance:<10.1f} km")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance_km:
                return True
        return False


# --- (MAIN PROGRAM) ---
if __name__ == "__main__":
    car_participants = []
    for i in range(1, 11):
        car_participants.append(Car(f"ABC-{i}", random.randint(100, 200)))

    grand_derby = Race("Grand Demolition Derby", 8000, car_participants)

    hours_count = 0
    while not grand_derby.race_finished():
        grand_derby.hour_passes()
        hours_count += 1

        if hours_count % 10 == 0:
            print(f"\n--- Status after {hours_count} hours ---")
            grand_derby.print_status()

    print(f"\n--- RACE FINISHED AFTER {hours_count} HOURS ---")
    grand_derby.print_status()
