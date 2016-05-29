
class Gameplay():
    Playing = [0, 1, 2]
    def CardCounting(self, Player):
        repeat = 0
        while repeat != 3:
            Insert_Data = input (("Insert Card Number that is %d used : ") % (repeat+1))
            if(int(Insert_Data) < 0 or int(Insert_Data) > 8):
                print (" You insert Error Card Number ! ! ! \n ")
            else:
                Player.CardSelection[repeat] = int(Insert_Data)
                repeat=repeat+1           
    
    def FieldOut_Check(self, Player):
        Temp_Position=[]
        Temp_Position=Player.Position
        for i in range(len(Player.CardSelection)):
            if(Player.CardSelection[i] < 5):
                if(Player.CardSelection[i] == 1):
                     Temp_Position[0] = Temp_Position[0] + 0
                     Temp_Position[1] = Temp_Position[1] + 1
                elif(Player.CardSelection[i] == 2):
                     Temp_Position[0] = Temp_Position[0] + 0
                     Temp_Position[1] = Temp_Position[1] - 1
                elif(Player.CardSelection[i] == 3):
                     Temp_Position[0] = Temp_Position[0] + 1
                     Temp_Position[1] = Temp_Position[1] + 0
                elif(Player.CardSelection[i] == 4):
                    Temp_Position[0] = Temp_Position[0] - 1
                    Temp_Position[1] = Temp_Position[1] + 0
            if(Temp_Position[0] < 0 or Temp_Position[0] > 4 or Temp_Position[1] < 0 or Temp_Position[1] > 3):
                print("Your Movement is out of Field ! ! ! Reselect Card !\n")
                return False
            else:
                return True

    def Mp_Check(self, Player):
        Temp_Mp = Player.Mp
        Comulating_Mp = 0
        for i in range(len(Player.CardSelection)):
            if(Player.CardSelection[i] > 4):
                if(Player.CardSelection[i] == 5):
                    Comulating_Mp = Comulating_Mp + Player.Skill_A[2]
                elif(Player.CardSelection[i] == 6):
                    Comulating_Mp = Comulating_Mp + Player.Skill_B[2]
                elif(Player.CardSelection[i] == 7):
                    Comulating_Mp = Comulating_Mp + Player.Skill_C[2]
                elif(Player.CardSelection[i] == 8):
                    Comulating_Mp = Comulating_Mp + Player.Skill_D[2]
        if(Temp_Mp < Comulating_Mp):
           print("You have MP overflow ! ! ! Reselect Card !\n")
           return False
        else:
            return True

    def Gaming(self, Player1, Player2):
        while True:
            while True:
                self.CardCounting(Player1)
                x = self.Mp_Check(Player1)
                _x = self.FieldOut_Check(Player1)
                if(x and _x):
                    break
            while True:
                self.CardCounting(Player2)
                y = self.Mp_Check(Player2)
                _y = self.FieldOut_Check(Player2)
                if(y and _y):
                    break

            for i in range(len(self.Playing)):
                if(Player1.CardSelection[i] < 5 and Player2.CardSelection[i] > 4): 
                    Player1.PatternPlaying(Player1.CardSelection[i], Player2)
                    Player2.PatternPlaying(Player2.CardSelection[i], Player1)
                elif(Player2.CardSelection[i] < 5 and Player1.CardSelection[i] > 4):
                    Player2.PatternPlaying(Player2.CardSelection[i], Player1)
                    Player1.PatternPlaying(Player1.CardSelection[i], Player2)
                else:
                    Player1.PatternPlaying(Player1.CardSelection[i], Player2)
                    Player2.PatternPlaying(Player2.CardSelection[i], Player1)
                print (("[ Player %d ] \n HP : %d \n MP : %d \n   Current Position : (%d, %d) \n") % (1, Player1.Hp, Player1.Mp, Player1.Position[0], Player1.Position[1] ))
                print (("[ Player %d ] \n HP : %d \n MP : %d \n   Current Position : (%d, %d) \n") % (2, Player2.Hp, Player2.Mp, Player2.Position[0], Player2.Position[1] ))


            if(Player1.Hp < 0 or Player2.Hp < 0):
                if(Player1.Hp > 0 and Player2.Hp < 0):
                    print(">>> GameOver Player1 WIN ! ! ! <<<\n")
                    break
                elif(Player1.Hp < 0 and Player2.Hp > 0):
                    print(">>> GameOver Player2 WIN ! ! ! <<<\n")
                    break
                elif(Player1.Hp < 0 and Player2.Hp < 0):
                    print(">>> Draw ! ! ! <<<\n")
                    break