from django.contrib import admin

from .SkillList import SkillBook
def player1_Setting(mynum, myloc, enemyloc):
	player={'playnum':mynum, 
			 'enemynum':"unknown", 
			 'myloc':myloc,
			 'enemyloc':enemyloc, 
		     'select':0, 
		     'position':[4, 2], 
		     'hp' : 100, 
		     'mp' :100, 
		     'readcard':0, 
		     'end':0, 
		     'result':0}
	return player

def player2_Setting(mynum, enemynum, myloc, enemyloc):
	player={'playnum':mynum, 
			 'enemynum':enemy, 
			 'myloc':myloc,
			 'enemyloc':enemyloc, 
		     'select':0, 
		     'position':[0, 1], 
		     'hp' : 100, 
		     'mp' :100, 
		     'readcard':0, 
		     'end':0, 
		     'result':0}
	return player

def Izreal_Setting(player):
	player[myloc]['character'] = 1						#플레이어의 데이터에 character 를 추가한다.(선택 피즈)
	player[myloc]['Skill_A'] = SkillBook.Skill[0]
	player[myloc]['Skill_B'] = SkillBook.Skill[1]
	player[myloc]['Skill_C'] = SkillBook.Skill[2]
	player[myloc]['Skill_D'] = SkillBook.Skill[3]

def Xvii_Setting(player):
	player[myloc]['character'] = 2						#플레이어의 데이터에 character 를 추가한다.(선택 피즈)
	player[myloc]['Skill_A'] = SkillBook.Skill[1]
	player[myloc]['Skill_B'] = SkillBook.Skill[2]
	player[myloc]['Skill_C'] = SkillBook.Skill[5]
	player[myloc]['Skill_D'] = SkillBook.Skill[8]

def Piz_Setting(player):
	player[myloc]['character'] = 3						#플레이어의 데이터에 character 를 추가한다.(선택 피즈)
	player[myloc]['Skill_A'] = SkillBook.Skill[2]
	player[myloc]['Skill_B'] = SkillBook.Skill[1]
	player[myloc]['Skill_C'] = SkillBook.Skill[4]
	player[myloc]['Skill_D'] = SkillBook.Skill[7]