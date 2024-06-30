import random
class Player:
    def __init__(self, name):
        self.name=name
        self.score = 0
    def roll_dice(self):
        roll = random.randint(1,6)
        print (f"{self.name}:- self.score : {self.score}  roll : {roll}")
    def get_score(self):
        self.score +=1
        return self.score
class ComputerPlayer(Player):
    pass 
class Game:
    def __init__(self,player_name):
      self.player=Player(player_name)
      self.computer=ComputerPlayer("Computer")

      print("part 1")
    def play_round(self):
       print("player is rolling")
       self.player.roll_dice()
       print("computer is rolling")
       self.computer.roll_dice()
       print("part 2")
    def display_scores(self):
       print(f"{self.player.name} score : {self.player.get_score()}")
       print(f"{self.computer.name} score :{self.computer.get_score()}")
       #print(f"{self.player.name} Vs : {self.player.roll_dice()}")
       #print(f"{self.computer.name} Vs : {self.computer.roll_dice()}")
       print("part 3")
    def determine_winner(self):
        if self.player.get_score() > self.computer.get_score():
         print(f"{self.player.name} {self.player.get_score()}")
        else:
         print(f"{self.computer.name} {self.computer.get_score()}")
        print("part 4")
    def play(self):
        while True:
         self.play_round()
         self.display_scores()
         self.determine_winner()
         user_choice=input("Do you want Play again ? (yes-no)" )
         if user_choice == "no":
           break
         elif user_choice == "yes":
           continue       
user_choice_Name=input("welcom : Plase Enter Your Name")
game=Game(user_choice_Name)
game.play()