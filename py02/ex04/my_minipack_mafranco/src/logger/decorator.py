import time
from random import randint
import os

def log(func):
    def wrapper(self, *args, **kwargs):
        start = time.time()
        ret = func(self, *args, **kwargs)
        end = time.time()
        dif = end - start
        if dif < 1:
            dif *= 1000
            dif = "{:.3f}ms".format(dif)
        else:
            dif = "{:.3f}s".format(dif)
        with open("machine.log", "a") as file:
            file.write("(fmathis)Running: {:20}[ exec-time = {}]\n".format(func.__name__, dif))
        return ret
    return wrapper

class CoffeeMachine():
    water_level = 100
    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)