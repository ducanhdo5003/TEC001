class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
            print(f"Thang máy đang di chuyển... Tầng {self.current_floor}")
        else:
            print("Đã đạt tầng tối đa.")

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print(f"Thang máy đang di chuyển... Tầng {self.current_floor}")
        else:
            print("Đã ở tầng thấp nhất.")

    def go_to_floor(self, target):
        print(f"--- Di chuyển từ {self.current_floor} đến {target} ---")
        while self.current_floor < target:
            self.floor_up()
        while self.current_floor > target:
            self.floor_down()
        print(f"Thang máy đã dừng tại tầng {self.current_floor}")


class Building:
    def __init__(self, bottom, top, num_elevators):
        self.bottom = bottom
        self.top = top
        self.elevators = [Elevator(bottom, top) for _ in range(num_elevators)]

    def run_elevator(self, index, destination):
        if 0 <= index < len(self.elevators):
            print(f"\n[Điều khiển Thang máy số {index}]")
            self.elevators[index].go_to_floor(destination)
        else:
            print("Số thứ tự thang máy không hợp lệ.")

    def fire_alarm(self):
        print("\n" + "!" * 30)
        print("!!! HỆ THỐNG BÁO CHÁY KÍCH HOẠT !!!")
        print("Đưa tất cả thang máy về tầng trệt...")
        print("!" * 30)
        for i, elevator in enumerate(self.elevators):
            print(f"\nThang máy {i}:")
            elevator.go_to_floor(self.bottom)


# --- (Main Program) ---
if __name__ == "__main__":
    my_building = Building(0, 10, 3)

    my_building.run_elevator(0, 5)
    my_building.run_elevator(1, 8)

    my_building.fire_alarm()