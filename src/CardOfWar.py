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
    def __init__ (self, PlayerType):        # 처음 생성시 데이터를 입력해주는 함수
        self.Hp = 100 # 시작시 체력은 100으로 설정한다.
        self.Mp = 100 # 시작시 마력은 100으로 설정한다.
        self.Hero = input("Insert Character Number you want : ")
        if(PlayerType == 1):
            self.Position = [0, 1] # player1은 (0,1)위치에서 시작하도록 한다.
        elif(PlayerType == 2):
            self.Position = [4, 2] # player2는 (4,2)위치에서 시작하도록 한다.
       
        if(self.Hero == 1):     # n번 hero를 골랐다면 Transport_Skill_Hero(n)함수가 실행되도록 한다.
           Transport_Skill_Hero1 (self, self.SkillBook) #각 hero마다 가지고있는 skill의 종류가 다르다.
        elif(self.Hero == 2):
           Transport_Skill_Hero2 (self, self.SkillBook)
        elif(self.Hero == 3):
           Transport_Skill_Hero3 (self, self.SkillBook)

        print((" You are Player %d ! and, You choose Hero %d ! ") % (PlayerType) (self.Hero) )


    def PatternSetting (self, cardnumber, AnotherPlayer):   # 선택한 카드번호에 따라 행동하게 하는 함수
        if(cardnumber == 0):    # stay 카드(그자리에 정지)
           self.Position[0] = self.Position[0] + 0 
           self.Position[1] = self.Position[1] + 0
        elif(cardnumber == 1):  # up 카드 (위로 한칸 이동)
           self.Position[0] = self.Position[0] + 0
           self.Position[1] = self.Position[1] + 1
        elif(cardnumber == 2):  # down 카드 (아래로 한칸 이동)
           self.Position[0] = self.Position[0] + 0
           self.Position[1] = self.Position[1] - 1
        elif(cardnumber == 3):  # left 카드 (왼쪽으로 한칸 이동)
           self.Position[0] = self.Position[0] + 1
           self.Position[1] = self.Position[1] + 0
        elif(cardnumber == 4):  # right 카드 (오른쪽으로 한칸 이동)
           self.Position[0] = self.Position[0] - 1
           self.Position[1] = self.Position[1] + 0
        elif(cardnumber == 5):  # skill_A 발동
           Act_Skill_A(AnotherPlayer)
        elif(cardnumber == 6):  # skill_B 발동
           Act_Skill_B(AnotherPlayer)
        elif(cardnumber == 7):  # skill_C 발동
           Act_Skill_C(AnotherPlayer)
        elif(cardnumber == 8):  # skill_D 발동
           Act_Skill_D(AnotherPlayer)

    def Act_Skill_A(self, AnotherPlayer): #Skill_A가 발동하였을 경우 실행한다.
        SR = Skill_A[0] # SR에 공격 범위를 저장한다.
        SD = Skill_A[1] # SD에 공격 데미지를 저장한다.
        SM = Skill_A[2] # SM에 소모되는 마력을 저장한다.
        for i in range(len(SR)): # 공격범위에 저장되어있는 좌표 갯수만큼 반복하여 동작한다. 
            pos = SR[i] 
            if(AnotherPlayer.Position == [self.Position[0] + pos[0], self.Position[1] + pos[1]]):
                # 적군의 위치가 현재 skill의 공격범위내에 있다면 
                AnotherPlayer.HP = AnotherPlayer.HP - SD # 공격 데미지만큼 체력을 깎아준다.
        self.Mp = self.Mp - SM # 소모된 마력만큼 현재 마력에서 깎아준다.
    def Act_Skill_B(self, AnotherPlayer): #Skill_B가 발동하였을 경우 실행한다.
        SR = Skill_B[0] 
        SD = Skill_B[1] 
        SM = Skill_A[2]
        for i in range(len(SR)):
            pos = SR[i]
            if(AnotherPlayer.Position == [self.Position[0] + pos[0], self.Position[1] + pos[1]]):
                AnotherPlayer.HP = AnotherPlayer.HP - SD 
        self.Mp = self.Mp - SM
    def Act_Skill_C(self, AnotherPlayer): #Skill_C가 발동하였을 경우 실행한다.
        SR = Skill_C[0]
        SD = Skill_C[1]
        SM = Skill_A[2]
        for i in range(len(SR)):
            pos = SR[i]
            if(AnotherPlayer.Position == [self.Position[0] + pos[0], self.Position[1] + pos[1]]):
                AnotherPlayer.HP = AnotherPlayer.HP - SD 
        self.Mp = self.Mp - SM    
    def Act_Skill_D(self, AnotherPlayer): #Skill_D가 발동하였을 경우 실행한다.
        SR = Skill_D[0]
        SD = Skill_D[1]
        SM = Skill_A[2]
        for i in range(len(SR)):
            pos = SR[i]
            if(AnotherPlayer.Position == [self.Position[0] + pos[0], self.Position[1] + pos[1]]):
                AnotherPlayer.HP = AnotherPlayer.HP - SD 
        self.Mp = self.Mp - SM

class Gameplay():
    Playing = [0, 1, 2]
    def CardCounting(self, Player):
        for i in range(len(Player.CardSelection)):
            Player.CardSelection[i] = input (("Insert Card Number that is %d used : ") % (i+1))
    
    def Gaming(self, Player1, Player2):
        while True:
            CardCounting(Player1)
            CardCounting(Player2)
            for i in range(len(Playing)):
                if(Player1.CardSelection[i] < 5 and Player2.CardSelection[i] > 4): 
                    Player1.PatternSetting(Player1.CardSelection[i], Player2)
                    Player2.PatternSetting(Player2.CardSelection[i], Player1)
                elif(Player2.CardSelection[i] < 5 and Player1.CardSelection[i] > 4):
                    Player2.PatternSetting(Player2.CardSelection[i], Player1)
                    Player1.PatternSetting(Player1.CardSelection[i], Player2)
            if(Player1.Hp == 0 or Player2.Hp == 0):
                if(Player1.Hp != 0 and Player2.Hp == 0):
                    print(">>> GameOver Player1 WIN ! ! ! <<<")
                    break
                elif(Player1.Hp == 0 and Player2.Hp != 0):
                    print(">>> GameOver Player2 WIN ! ! ! <<<")
                    break
                elif(Player1.Hp == 0 and Player2.Hp != 0):
                    print(">>> Draw ! ! ! <<<")
                    break
     
        
        
class SkillList():
    
    damage=[10, 10 ,20 ,20 ,30 ,30 ,40 ,40 ,50 ,50]
    UsingMP=[10, 10, 20, 20, 30, 30, 40, 40, 50, 50]
    Skill = []*9
    attackrange = []*9
    # [-1,1],[0,1],[1,1]
    
    # [-1,0],[0,0],[0,1]
    
    # [-1,-1],[0,-1],[1,-1]
    
    attackrange[0] = [[-1,1],[0,1],[1,1],[-1,0],[0,0],[0,1]]    #789456  <-숫자 키패드의 모양을 통해 공격범위를 표현한 것
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


def Transport_Skill_Hero1 (Player, SkillList):  # Hero 1이 가지고 있는 스킬을 0,3,6,9번으로 지정한다.
    Player.Skill_A = SkillList.getskillnum(0)
    Player.Skill_B = SkillList.getskillnum(3)
    Player.Skill_C = SkillList.getskillnum(6)
    Player.Skill_D = SkillList.getskillnum(9)

def Transport_Skill_Hero2 (Player, SkillList):  # Hero 1이 가지고 있는 스킬을 0,2,5,8번으로 지정한다.
    Player.Skill_A = SkillList.getskillnum(0)
    Player.Skill_B = SkillList.getskillnum(2)
    Player.Skill_C = SkillList.getskillnum(5)
    Player.Skill_D = SkillList.getskillnum(8)


def Transport_Skill_Hero3 (Player, SkillList):  # Hero 1이 가지고 있는 스킬을 0,1,4,7번으로 지정한다.
   Player.Skill_A = SkillList.getskillnum(0)
   Player.Skill_B = SkillList.getskillnum(1)
   Player.Skill_C = SkillList.getskillnum(4)
   Player.Skill_D = SkillList.getskillnum(7)

def main():
    P1=Player(1)
    P2=Player(2)

 

if __name__ == '__main__':
    main()
