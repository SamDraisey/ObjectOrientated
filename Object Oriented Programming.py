class Participant:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ""
    def choose(self):
        self.choice = input("{name}, select rock, paper or scissor: ".format(name= self.name))
        print("{name} selects {choice}".format(name=self.name, choice = self.choice))

class GameRound:
    def __init__(self, p1, p2):
        p1.choose()
        p2.choose()
    def compareChoices(self):
        print("implement")
    def awardPoints(self):
        print("implement")

class Game:
    def __init__(self):
        self.endGame = False
        self.participant = Participant("player1")
        self.secondParticipant = Participant("player2")
    def start(self):
        game_round = GameRound(self.participant, self.secondParticipant)

    def checkEndCondition(self):
        print("implement")
    def determineWinner(self):
        print("implement")

game = Game()
game.start()

rules = [
    [0, -1, 1],
    [1, 0, -1]''
    [-1, 1, 0]
]

def toNumericalChoice(self):
    switcher = {
        "rock": 0,
        "paper": 1,
        "scissor": 2
    }
    return switcher[self.choice]

def compareChoices(self, p1, p2):
    return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]





    

    
        
