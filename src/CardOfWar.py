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
    def __init__ (self, PlayerType):
        self.Hp = 100
        self.Mp = 100
        self.Hero = input("Insert Character Number you want : ")
        if(PlayerType == 1):
            self.Position = [0, 1]
        elif(PlayerType == 2):
            self.Position = [4, 2]
       
        if(self.Hero == 1):
           Transport_Skill_Hero1 (self, self.SkillBook)
        elif(self.Hero == 2):
           Transport_Skill_Hero2 (self, self.SkillBook)
        elif(self.Hero == 3):
           Transport_Skill_Hero3 (self, self.SkillBook)

    def PatternSetting (self, cardnumber):
        if(cardnumber == 0):
           self.Position[0] = self.Position[0] + 0
           self.Position[1] = self.Position[1] + 0
        elif(cardnumber == 1):
           self.Position[0] = self.Position[0] + 0
           self.Position[1] = self.Position[1] + 1
        elif(cardnumber == 2):
           self.Position[0] = self.Position[0] + 0
           self.Position[1] = self.Position[1] - 1
        elif(cardnumber == 3):
           self.Position[0] = self.Position[0] + 1
           self.Position[1] = self.Position[1] + 0
        elif(cardnumber == 4):
           self.Position[0] = self.Position[0] - 1
           self.Position[1] = self.Position[1] + 0
        elif(cardnumber == 5):
           Act_Skill_A(AnotherPlayer)
        elif(cardnumber == 6):
           Act_Skill_B(AnotherPlayer)
        elif(cardnumber == 7):
           Act_Skill_C(AnotherPlayer)
        elif(cardnumber == 8):
           Act_Skill_D(AnotherPlayer)

    def Act_Skill_A(self, AnotherPlayer):
        for Skill_range in range(len(
    def Act_Skill_B(self, AnotherPlayer):
    def Act_Skill_C(self, AnotherPlayer):    
    def Act_Skill_D(self, AnotherPlayer):
            

class SkillList():
    
    damage = ['10', '10' ,'20' ,'20' ,'30' ,'30' ,'40' ,'40' ,'50' ,'50']
    Skill = []*9
    attackrange = []*9
    
    # [-1,1],[0,1],[1,1]
    
    # [-1,0],[0,0],[0,1]
    
    # [-1,-1],[0,-1],[1,-1]
    
    attackrange[0] = [[-1,1],[0,1],[1,1],[-1,0],[0,0],[0,1]]    #789456
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
        
        Skill[i] =  [attackrange[i] , damage[i]]
        
    def getskillnum(self,num):
        
        return self.Skill[num]

def Transport_Skill_Hero1 (Player, SkillList):
    Player.Skill_A = SkillList.getskillnum(0)
    Player.Skill_B = SkillList.getskillnum(3)
    Player.Skill_C = SkillList.getskillnum(6)
    Player.Skill_D = SkillList.getskillnum(9)

def Transport_Skill_Hero2 (Player, SkillList):
    Player.Skill_A = SkillList.getskillnum(0)
    Player.Skill_B = SkillList.getskillnum(2)
    Player.Skill_C = SkillList.getskillnum(5)
    Player.Skill_D = SkillList.getskillnum(8)


def Transport_Skill_Hero3 (Player, SkillList):
    Player.Skill_A = SkillList.getskillnum(0)
    Player.Skill_B = SkillList.getskillnum(1)
    Player.Skill_C = SkillList.getskillnum(4)
    Player.Skill_D = SkillList.getskillnum(7)