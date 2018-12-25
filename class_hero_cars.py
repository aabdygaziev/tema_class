class Cars():
    def __init__(self):
        self.km = 0
        self.bak = 100
        self.iznos = 0
        self.driver = None

    def set_driver(self, driver):
        self.driver = driver

    def drive(self):
        if self.bak - 10 > 0 and self.iznos < 100:
            self.bak -= 10
            self.iznos += 5
            self.km += 100
            self.driver.money += 100

    def service(self):
        if self.driver.money > 20  and self.iznos > 100 and self.bak < 20:
            self.iznos -= 4
            self.driver.money -= 50

    def zapravka(self):
        if self.bak <20 and self.driver.money > 20 and self.iznos > 100:
            self.bak += 10
            self.driver.money -= 10

    def display(self):
        print(self)

