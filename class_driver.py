class Driver():
    def __init__(self, name):
        self.name = name
        self.age = 33
        self.weight = 66
        self.height = 177
        self.money = 100
        self.experience = 0
        self.car = None

    def set_car(self, car):
        self.car = car

    def experience(self):
        if self.car.km > 99:
            self.experience += 1
            self.money += 100

    def display(self):
        print(self)

