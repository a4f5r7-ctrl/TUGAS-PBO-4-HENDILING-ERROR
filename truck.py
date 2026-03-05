class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"{self.brand} {self.model} is driving")

    def honk(self):
        print("Beep beep!")


class Truck(Vehicle):
    def __init__(self, brand, model, load_capacity):
        super().__init__(brand, model)
        self.load_capacity = load_capacity

    def load(self, weight):
        print(f"Loaded {weight} kg.")


def main():
    my_car = Vehicle("Toyota", "Corolla")
    my_truck = Truck("Ford", "F-150", 1000)

    my_car.drive()
    my_car.honk()

    my_truck.drive()
    try:
        my_truck.load(1200)
    except ValueError as error:
        print("Error terjadi:", error)

    print("Program tetap berjalan...")




if __name__ == "__main__":
    main()