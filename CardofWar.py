class Player():
	HP = 0
	MP = 0
	Position = (0, 0)
	def __init__ (self, Character,PlayerType):
		self.HP = 100
		self.MP = 100
		if(PlayerType == 1):
			self.Position = (3, 0)
		elif(PlayerType == 2):
			self.Position = (1, 3)
	
	def MovePattern (self, Move):
		if(Move==0):		##stay
			self.Position = self.Position
		elif(Move==1):		##right
			self.Position = self.Position + (0, 1)
		elif(Move==2):		##left
			self.Position = self.Position + (0, -1)
		elif(Move==3):		##up
			self.Position = self.Position + (1, 0)
		elif(Move==4):		##down
			self.Position = self.Position + (-1, 0)
		
		return self.Position
	
	
class Character_A(Player):
	CardSelection = [0, 0, 0]
	
	def CardCounting(self):
		for i in range(len(self.CardSelection)):
			self.CardSelection[i] = input ((	"Insert Card Number that is %d' used : ") % (i+1))
		return self.CardSelection
	
	def  MP_Empty(self):
	
	def Skill_A(self, AnotherPlayer):
	
	def Skill_B(self, AnotherPlayer):
	
	def Skill_C(self, AnotherPlayer):
	
	def Skill_D(self, AnotherPlayer):
	
class Character_B(Player):
	CardSelection = [0, 0, 0]
	
	def CardCounting(self):
		for i in range(len(self.CardSelection)):
			self.CardSelection[i] = input ((	"Insert Card Number that is %d' used : ") % (i+1))
		return self.CardSelection
	
	def  MP_Empty(self):
	
	def Skill_A(self, AnotherPlayer):
	
	def Skill_B(self, AnotherPlayer):
	
	def Skill_C(self, AnotherPlayer):
	
	def Skill_D(self, AnotherPlayer):
	
class Character_C(Player):
	CardSelection = [0, 0, 0]
	
	def CardCounting(self):
		for i in range(len(self.CardSelection)):
			self.CardSelection[i] = input ((	"Insert Card Number that is %d' used : ") % (i+1))
		return self.CardSelection
	
	def PatternPlay(self, AnotherPlayer):
		for i in range(len(self.CardSelection)):
			if( self.CardSelection[i]<5 ):
				self.Position = MovePattern(self.CardSelection[i])
			else:
				AttackPattern( self.CardSelection[i], AnotherPlayer)
				
	def AttackPattern (self, Skill, AnotherPlayer):
		if(Skill==5):
			Skill_A(AnotherPlayer)
		elif(Skill==6):
			Skill_B(AnotherPlayer)
		elif(Skill==7):
			SKill_C(AnotherPlayer)
		elif(Skill==8):
			Skill_D(AnotherPlayer)

	def  MP_Empty(self):
	
	def Skill_A(self, AnotherPlayer):
		if( (AnotherPlayer.Position == self.Position + (1, 0)) ll (AnotherPlayer.Position == self.Position + (0, 1)) ):
			AnotherPlayer.HP = AnotherPlayer.HP - 10
			self.MP = self.MP - 20
	
	def Skill_B(self, AnotherPlayer):
		if():
			AnotherPlayer.HP = AnotherPlayer.HP - 20
			self.MP = self.MP - 30
			
	def Skill_C(self, AnotherPlayer):
		if():
			AnotherPlayer.HP = AnotherPlayer.HP - 15
			self.MP = self.MP - 25
			
	def Skill_D(self, AnotherPlayer):
		if():
			AnotherPlayer.HP = AnotherPlayer.HP - 5
			self.MP = self.MP - 15
			
class GamePlay (Player1, Player2):

def main()
	
	