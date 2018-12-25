class Hero ():
    def __init__(self, name):
        self.name = name
        self.age = 20
    def display (self):
        print(self.name, self.age)

hero1 = Hero('Aktan')
hero1.display()
print(hero1.name)
