class Bird():
    def __init__(self, name, voice, color):
        self.name = name
        self.voice = voice
        self.color = color

    def fly(self):
        print(f"{self.name} Летает")

    def sing(self):
        print(f"{self.name} Поет - Чирик")

    def eat(self):
        print(f"{self.name} Кушает")

    def info(self):
        print(f"Имя: {self.name}")
        print(f"Голос: {self.voice}")
        print(f"Окрас птицы: {self.color}")

class Pinguin(Bird):
    def __init__(self, name, voice, color, favorite_food):
        super().__init__(name, voice, color)
        self.favorite_food = favorite_food

    def sing(self):
        print(f"{self.name} Поет - Курлык")

    def walk(self):
        print(f"{self.name} Гуляет")

bird1 = Pinguin("Гоша", "Курлык", "Серый", "Хлебные крошки")

bird2 = Bird("Петя", "Чирик", "Коричневый", )

bird1.sing()
bird1.info()
bird1.walk()
