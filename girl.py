from female import Female

class Girl(Female):
    def __init__(self):
        super().__init__()
        self.__fav_colour = "blue"
        self._nature = "happy"
        self.heart = 1

    def _study(self):
        try:
            return girl_object._study()

        except RecursionError:
            return "this information is protected"

    def play(self):
        return "Play everyday"

    def paint(self):
        return "Love to paint"

girl_object = Girl()
print(girl_object._nature)
print(girl_object._study())
# print(girl_object.__fav_colour)