from human import Human

class Female(Human):

    def __init__(self):
        super().__init__()
        self.fav_colour = "white"
        self.breathe = True
        self.hair = True

    def dance(self):
        return "You can learn to dance whether you have been born with natural talent or not."

    def code(self):
        return "Ada Lovelace is credited for being the world's first programmer"

    def drive(self):
        return "Enjoy driving"

female_object = Female()
# print(female_object.hair)
# print(female_object.code())