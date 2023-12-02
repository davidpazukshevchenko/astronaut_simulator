import random

print("Это симулятор космонавта вы летите в космическом корабле выходите в космос роботать, кушать, спать мисси будет "
      "закончена если вы прожевёте на корабле год или же найдёте добрых инопланетян и они поделяться с вами секретными "
      "технологиями тогда ваша миссия закончиться досрочно")

class Astronaut:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.hunger = 50
        self.energy = 100
        self.air = 100
        self.alive = True

    def to_eat(self):
        print("Time to study")
        self.hunger += 1
        self.gladness += 5
        self.energy += 20
        self.air += 20

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3

    def to_spacewalk(self):
        print("Rest time")
        self.gladness -= 8
        self.hunger -= 1
        self.energy -= 50
        self.air -= 20

    def to_evil_aliens(self):
        print("Вы встретили злых инопланетян они растреляли ваш корабыль и вы умерли")
        self.alive = False


    def to_aliens(self):
        print("Вы встретили добрых инопланетян они поделилися с вами секретными технологиями ваша миссия окончена ")
        self.alive = False


def is_alive(self):
    if self.hunger <= 0:
        print("Вы умерли от голода")
        self.alive = False
    elif self.gladness <= 0:
        print("У вас Депрессия")
        self.alive = False
    elif self.energy <= 0:
        print("Вы умерли от усталости")
        self.alive = False
    elif self.air <= 0:
        print("Вы умерли от недостатка кислорода")
        self.alive = False


def end_of_play(self):
    print(f"Gladness = {self.gladness}")
    print(f"Progress = {round(self.hunger, 2)}")
    print(f"Energy = {self.energy}")
    print(f"Air = {self.air}")


def live(self, day):
    day = "Day " + str(day) + " of " + self.name + " life"
    print(f"{day:=^50}")
    live_cube = random.randint(1, 6)

    if live_cube == 1:
        self.to_eat()
    elif live_cube == 2:
        self.to_sleep()
    elif live_cube == 3:
        self.to_spacewalk()
    elif live_cube == 4:
        self.to_evil_aliens()
    elif live_cube == 5:
        self.to_aliens()
    self.end_of_play()
    self.is_alive()


nick = Astronaut(name="Nick")

for day in range(1, 366):
    if nick.alive == False:
        break
nick.live(day)