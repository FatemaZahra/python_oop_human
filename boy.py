from male import Male

class Boy(Male):

    def __init__(self):
        super().__init__()
        self.beard = False
        self.height = 4
        self.hand = "small"

    def play(self):
        return "Kids love to play"

    def run(self):
        return "Running is also a good exercise"

    def laugh(self):
        return "laugh till your stomach hurts"

boy_object = Boy()
print(boy_object.beard)
print(boy_object.run())