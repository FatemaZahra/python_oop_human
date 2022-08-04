# create a Human class
class Human:
    def __init__(self):
        self.eyes = 2
        self.hand = 2
        self.nose = True

    def eat(self):
        return "Eat three healthy meals everyday!"

    def move(self):
        return "Move, exercise, play. Stay fit"

    def sleep(self):
        return "Happy humans sleep 8 hours a day"

human_object = Human()

print(human_object.nose)
print(human_object.sleep())


