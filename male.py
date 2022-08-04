from human import Human

class Male(Human):

    def __init__(self):
        super().__init__()
        self.beard = True
        self.height = 7
        self.hobby = "gardening"

    def run(self):
        return "Males run at an average speed of 8 mph"

    def talk(self):
        return "Most common talk is sports and gym"

    def swim(self):
        return "Swimming can improve exercise-induced asthma"

male_object = Male()
print(male_object.beard)
print(male_object.talk())