
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
       
        if(self.Hero == '1'):     # n번 hero를 골랐다면 Transport_Skill_Hero(n)함수가 실행되도록 한다.
           Transport_Skill_Hero1 (self, self.SkillBook) #각 hero마다 가지고있는 skill의 종류가 다르다.
        elif(self.Hero == '2'):
           Transport_Skill_Hero2 (self, self.SkillBook)
        elif(self.Hero == '3'):
           Transport_Skill_Hero3 (self, self.SkillBook)

        print((" You are Player %d ! and, You choose Hero %s ! \n") % (PlayerType, self.Hero) )


    def PatternPlaying (self, cardnumber, AnotherPlayer):   # 선택한 카드번호에 따라 행동하게 하는 함수
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
           self.Act_Skill_A(AnotherPlayer)
        elif(cardnumber == 6):  # skill_B 발동
           self.Act_Skill_B(AnotherPlayer)
        elif(cardnumber == 7):  # skill_C 발동
           self.Act_Skill_C(AnotherPlayer)
        elif(cardnumber == 8):  # skill_D 발동
           self.Act_Skill_D(AnotherPlayer)

    def Act_Skill_A(self, AnotherPlayer): #Skill_A가 발동하였을 경우 실행한다.
        SR = self.Skill_A[0] # SR에 공격 범위를 저장한다.
        SD = self.Skill_A[1] # SD에 공격 데미지를 저장한다.
        SM = self.Skill_A[2] # SM에 소모되는 마력을 저장한다.
        for i in range(len(SR)): # 공격범위에 저장되어있는 좌표 갯수만큼 반복하여 동작한다. 
            pos = SR[i] 
            if(AnotherPlayer.Position == [self.Position[0] + pos[0], self.Position[1] + pos[1]]):
                # 적군의 위치가 현재 skill의 공격범위내에 있다면 
                AnotherPlayer.HP = AnotherPlayer.HP - SD # 공격 데미지만큼 체력을 깎아준다.
        self.Mp = self.Mp - SM # 소모된 마력만큼 현재 마력에서 깎아준다.
    def Act_Skill_B(self, AnotherPlayer): #Skill_B가 발동하였을 경우 실행한다.
        SR = self.Skill_B[0] 
        SD = self.Skill_B[1] 
        SM = self.Skill_B[2]
        for i in range(len(SR)):
            pos = SR[i]
            if(AnotherPlayer.Position == [self.Position[0] + pos[0], self.Position[1] + pos[1]]):
                AnotherPlayer.HP = AnotherPlayer.HP - SD 
        self.Mp = self.Mp - SM
    def Act_Skill_C(self, AnotherPlayer): #Skill_C가 발동하였을 경우 실행한다.
        SR = self.Skill_C[0]
        SD = self.Skill_C[1]
        SM = self.Skill_C[2]
        for i in range(len(SR)):
            pos = SR[i]
            if(AnotherPlayer.Position == [self.Position[0] + pos[0], self.Position[1] + pos[1]]):
                AnotherPlayer.HP = AnotherPlayer.HP - SD 
        self.Mp = self.Mp - SM    
    def Act_Skill_D(self, AnotherPlayer): #Skill_D가 발동하였을 경우 실행한다.
        SR = self.Skill_D[0]
        SD = self.Skill_D[1]
        SM = self.Skill_D[2]
        for i in range(len(SR)):
            pos = SR[i]
            if(AnotherPlayer.Position == [self.Position[0] + pos[0], self.Position[1] + pos[1]]):
                AnotherPlayer.HP = AnotherPlayer.HP - SD 
        self.Mp = self.Mp - SM

