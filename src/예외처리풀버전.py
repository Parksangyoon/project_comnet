def Transport_Skill_Hero1 (Player, SkillList):  # Hero 1�� ������ �ִ� ��ų�� 0,3,6,9������ �����Ѵ�.
    Player.Skill_A = SkillList.getskillnum(0)
    Player.Skill_B = SkillList.getskillnum(3)
    Player.Skill_C = SkillList.getskillnum(6)
    Player.Skill_D = SkillList.getskillnum(9)

def Transport_Skill_Hero2 (Player, SkillList):  # Hero 1�� ������ �ִ� ��ų�� 0,2,5,8������ �����Ѵ�.
    Player.Skill_A = SkillList.getskillnum(0)
    Player.Skill_B = SkillList.getskillnum(2)
    Player.Skill_C = SkillList.getskillnum(5)
    Player.Skill_D = SkillList.getskillnum(8)


def Transport_Skill_Hero3 (Player, SkillList):  # Hero 1�� ������ �ִ� ��ų�� 0,1,4,7������ �����Ѵ�.
    Player.Skill_A = SkillList.getskillnum(0)
    Player.Skill_B = SkillList.getskillnum(1)
    Player.Skill_C = SkillList.getskillnum(4)
    Player.Skill_D = SkillList.getskillnum(7)

class SkillList():
    
    damage=[10, 10 ,20 ,20 ,30 ,30 ,40 ,40 ,50 ,50]
    UsingMP=[10, 10, 20, 20, 30, 30, 40, 40, 50, 50]
    Skill = []*9
    attackrange = []*9
    # [-1,1],[0,1],[1,1]
    
    # [-1,0],[0,0],[0,1]
    
    # [-1,-1],[0,-1],[1,-1]
    
    attackrange[0] = [[-1,1],[0,1],[1,1],[-1,0],[0,0],[0,1]]    #789456  <-���� Ű�е��� ����� ���� ���ݹ����� ǥ���� ��
    attackrange[1] = [[-1,0],[0,0],[0,1],[-1,-1],[0,-1],[1,-1]] #456123
    attackrange[2] = [[-1,1],[0,1],[-1,0],[0,0],[-1,-1],[0,-1]] #784512
    attackrange[3] = [[0,1],[1,1],[0,0],[0,1],[0,-1],[1,-1]]    #895623
    attackrange[4] = [[-1,1],[1,1],[0,0],[-1,-1],[1,-1]]        #79513
    attackrange[5] = [[0,1],[-1,0],[0,0],[0,1],[0,-1]]          #84562
    attackrange[6] = [[0,0],[-1,-1],[0,-1],[1,-1]]              #5123
    attackrange[7] = [[-1,1],[0,1],[1,1],[0,0]]                 #7895
    attackrange[8] = [[-1,1],[0,1],[1,1],[-1,0],[0,0],[0,1],[-1,-1],[0,-1],[1,-1]]#789456123 
    attackrange[9] = [[0,0],[1,1],[0,1]]                        #569
    
    for i in range(9):
        
        Skill[i]=  [attackrange[i],damage[i],UsingMP[i]]
        
    def getskillnum(self,num):
        
        return self.Skill[num]

class Player():
    Hp = 0  
    Mp = 0
    Hero = 0
    Position = [0, 0]
    Skill_A = []
    Skill_B = []
    Skill_C = []
    Skill_D = []
    SkillBook = SkillList()
    CardSelection = [0, 0, 0]
    def __init__ (self, PlayerType):        # ó�� ������ �����͸� �Է����ִ� �Լ�
        self.Hp = 100 # ���۽� ü���� 100���� �����Ѵ�.
        self.Mp = 100 # ���۽� ������ 100���� �����Ѵ�.
        self.Hero = input("Insert Character Number you want : ")
        if(PlayerType == 1):
            self.Position = [0, 1] # player1�� (0,1)��ġ���� �����ϵ��� �Ѵ�.
        elif(PlayerType == 2):
            self.Position = [4, 2] # player2�� (4,2)��ġ���� �����ϵ��� �Ѵ�.
       
        if(self.Hero == 1):     # n�� hero�� ����ٸ� Transport_Skill_Hero(n)�Լ��� ����ǵ��� �Ѵ�.
           Transport_Skill_Hero1 (self, self.SkillBook) #�� hero���� �������ִ� skill�� ������ �ٸ���.
        elif(self.Hero == 2):
           Transport_Skill_Hero2 (self, self.SkillBook)
        elif(self.Hero == 3):
           Transport_Skill_Hero3 (self, self.SkillBook)

        print((" You are Player %d ! and, You choose Hero %d ! \n") % (PlayerType, self.Hero) )


    def PatternPlaying (self, cardnumber, AnotherPlayer):   # ������ ī���ȣ�� ���� �ൿ�ϰ� �ϴ� �Լ�
        if(cardnumber == 0):    # stay ī��(���ڸ��� ����)
           self.Position[0] = self.Position[0] + 0 
           self.Position[1] = self.Position[1] + 0
        elif(cardnumber == 1):  # up ī�� (���� ��ĭ �̵�)
           self.Position[0] = self.Position[0] + 0
           self.Position[1] = self.Position[1] + 1
        elif(cardnumber == 2):  # down ī�� (�Ʒ��� ��ĭ �̵�)
           self.Position[0] = self.Position[0] + 0
           self.Position[1] = self.Position[1] - 1
        elif(cardnumber == 3):  # left ī�� (�������� ��ĭ �̵�)
           self.Position[0] = self.Position[0] + 1
           self.Position[1] = self.Position[1] + 0
        elif(cardnumber == 4):  # right ī�� (���������� ��ĭ �̵�)
           self.Position[0] = self.Position[0] - 1
           self.Position[1] = self.Position[1] + 0
        elif(cardnumber == 5):  # skill_A �ߵ�
           self.Act_Skill_A(AnotherPlayer)
        elif(cardnumber == 6):  # skill_B �ߵ�
           self.Act_Skill_B(AnotherPlayer)
        elif(cardnumber == 7):  # skill_C �ߵ�
           self.Act_Skill_C(AnotherPlayer)
        elif(cardnumber == 8):  # skill_D �ߵ�
           self.Act_Skill_D(AnotherPlayer)

    def Act_Skill_A(self, AnotherPlayer): #Skill_A�� �ߵ��Ͽ��� ��� �����Ѵ�.
        SR = self.Skill_A[0] # SR�� ���� ������ �����Ѵ�.
        SD = self.Skill_A[1] # SD�� ���� �������� �����Ѵ�.
        SM = self.Skill_A[2] # SM�� �Ҹ�Ǵ� ������ �����Ѵ�.
        for i in range(len(SR)): # ���ݹ����� ����Ǿ��ִ� ��ǥ ������ŭ �ݺ��Ͽ� �����Ѵ�. 
            pos = SR[i] 
            if(AnotherPlayer.Position == [self.Position[0] + pos[0], self.Position[1] + pos[1]]):
                # ������ ��ġ�� ���� skill�� ���ݹ������� �ִٸ� 
                AnotherPlayer.HP = AnotherPlayer.HP - SD # ���� ��������ŭ ü���� ����ش�.
        self.Mp = self.Mp - SM # �Ҹ�� ���¸�ŭ ���� ���¿��� ����ش�.
    def Act_Skill_B(self, AnotherPlayer): #Skill_B�� �ߵ��Ͽ��� ��� �����Ѵ�.
        SR = self.Skill_B[0] 
        SD = self.Skill_B[1] 
        SM = self.Skill_B[2]
        for i in range(len(SR)):
            pos = SR[i]
            if(AnotherPlayer.Position == [self.Position[0] + pos[0], self.Position[1] + pos[1]]):
                AnotherPlayer.HP = AnotherPlayer.HP - SD 
        self.Mp = self.Mp - SM
    def Act_Skill_C(self, AnotherPlayer): #Skill_C�� �ߵ��Ͽ��� ��� �����Ѵ�.
        SR = self.Skill_C[0]
        SD = self.Skill_C[1]
        SM = self.Skill_C[2]
        for i in range(len(SR)):
            pos = SR[i]
            if(AnotherPlayer.Position == [self.Position[0] + pos[0], self.Position[1] + pos[1]]):
                AnotherPlayer.HP = AnotherPlayer.HP - SD 
        self.Mp = self.Mp - SM    
    def Act_Skill_D(self, AnotherPlayer): #Skill_D�� �ߵ��Ͽ��� ��� �����Ѵ�.
        SR = self.Skill_D[0]
        SD = self.Skill_D[1]
        SM = self.Skill_D[2]
        for i in range(len(SR)):
            pos = SR[i]
            if(AnotherPlayer.Position == [self.Position[0] + pos[0], self.Position[1] + pos[1]]):
                AnotherPlayer.HP = AnotherPlayer.HP - SD 
        self.Mp = self.Mp - SM

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
     
        
def main():
    P1=Player(1)
    P2=Player(2)

if __name__ == '__main__':
    main()