from class_hero_cars import Cars
from class_driver import Driver


car1 = Cars()
driver1 = Driver('Ahmed')
car1.set_driver(driver1)
driver1.set_car(car1)

driver1.display()
print(car1.driver.name)
print(car1.km)
print(car1.iznos)
print(car1.bak)

while True:
    a = input()
    if a == "drive":
        car1.drive()
    elif a == "zapravka":
        car1.zapravka()
    elif a == "service":
        car1.service()
    elif a == "money":
        driver1.money()









