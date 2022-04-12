import random
import time


class Tank:
    def __init__(self, name, weight, speed, bullet_count=10, petrol=100, money=1000):
        self.name = name
        self.weight = weight
        self.speed = speed
        self.bullet_count = bullet_count
        self.petrol = petrol
        self.money = money

    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        pass

    def shoot(self):
        if self.bullet_count > 0:
            print("Произведен выстрел")
            self.bullet_count -= 1
            time.sleep(2)
            if random.randint(0, 2):
                lvl_shoot = random.randint(1, 10)
                prize = 50 + 10 * lvl_shoot
                print(f"Снаряд попал в цель, вы получаете {prize} рублей")
                self.money += prize
            else:
                print("Мимо\n")

        else:
            print("Недостаточно снарядов, произведите закупку\n")

    def ride(self, km: int):
        is_done = True
        for i in range(km):
            if self.petrol > 0:
                print(
                    f"{self.name} проехал 1 километр"
                    if i + 1 == 1
                    else f"{self.name} проехал ещё 1 километр"
                )
                self.petrol -= 10
            else:
                print("Недостаточно топлива чтобы доехать доконца, произведите закупку")
                is_done = False
        if is_done:
            print(f"{self.name} доехал до места назначения")

    def info(self):
        print(
            f"Название танка: {self.name}\n"
            f"Вес: {self.weight}\n"
            f"Скорость: {self.speed}\n"
            f"Количество снарядов: {self.bullet_count}\n"
            f"Топливо: {self.petrol}\n"
            f"Деньги: {self.money}\n"
        )


tank1 = Tank("Т34", 1000, 20, 2)
tank1.info()
tank1.shoot()
tank1.ride(5)
tank1.info()

# tank2 = Tank("MOUSE", 10000, 10, 34)
# tank2.info()
