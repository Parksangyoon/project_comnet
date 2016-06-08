from .SkillList import SkillBook
from django.http import HttpResponse
class Client:
    Data = []
    image =[]
    Field = []

class Controll:
    stackplayer=0
    joinnum=0
    location=0
    selectok=0
    Fieldloc=0
    imloc=0
    join=0
    
def player_Setting(mynum, enemynum, myloc, enemyloc, position):
    player={'playnum':mynum, 
             'enemynum':enemynum, 
             'myloc':myloc,
             'enemyloc':enemyloc, 
             'Position':position, 
             'HP' :100, 
             'MP' :100, 
             'Readcard':0,
             'Prior':0,
             'imloc':0,
             'Error':0,
             'wait':3,
             'fieldloc':Controll.Fieldloc
           }
    return player
def stack_Setting():
    StackList={'stack1':0,
                'stack2':0,
                'stack3':0
            }
    return StackList

def Izreal_Setting(myloc):

    Client.Data[myloc]['character'] = 1                     #플레이어의 데이터에 character 를 추가한다.(선택 이즈)
    Client.Data[myloc]['Skill_A'] = SkillBook.Skill[5]
    Client.Data[myloc]['Skill_B'] = SkillBook.Skill[0]
    Client.Data[myloc]['Skill_C'] = SkillBook.Skill[3]
    Client.Data[myloc]['Skill_D'] = SkillBook.Skill[1]
    Client.Data[myloc]['settingcard'] ={'card1':"game/IZ_MOVE1.png", 'card2' : "game/IZ_MOVE2.png", 'card3': "game/IZ_MOVE3.png",
                                        'card4':"game/IZ_MOVE4.png", 'card5' : "game/IZ_MOVE5.png", 'card6': "game/IZ_SKILL1.png",
                                        'card7':"game/IZ_SKILL2.png", 'card8' : "game/IZ_SKILL3.png", 'card9': "game/IZ_SKILL4.png",
                                        'card10': "game/MpPlus.png", 'background':"game/Back_Is.jpg"}
    if(myloc < Client.Data[myloc]['enemyloc']):
        Client.Data[myloc]['settingcard']['profile']= "game/WHO3.PNG";
    else:
        Client.Data[myloc]['settingcard']['profile']= "game/WHO7.PNG";
def Xvii_Setting(myloc):
    Client.Data[myloc]['character'] = 2                     #플레이어의 데이터에 character 를 추가한다.(선택 바이)
    Client.Data[myloc]['Skill_A'] = SkillBook.Skill[0]
    Client.Data[myloc]['Skill_B'] = SkillBook.Skill[5]
    Client.Data[myloc]['Skill_C'] = SkillBook.Skill[3]
    Client.Data[myloc]['Skill_D'] = SkillBook.Skill[7]
    Client.Data[myloc]['settingcard'] ={'card1':"game/VI_MOVE1.png", 'card2' : "game/VI_MOVE2.png", 'card3': "game/VI_MOVE3.png",
                                        'card4':"game/VI_MOVE4.png", 'card5' : "game/VI_MOVE5.png", 'card6': "game/VI_SKILL1.png",
                                        'card7':"game/VI_SKILL2.png", 'card8' : "game/VI_SKILL3.png", 'card9': "game/VI_SKILL4.png",
                                        'card10': "game/MpPlus.png", 'background':"game/Back_Vi.jpg"}
    if(myloc < Client.Data[myloc]['enemyloc']):
        Client.Data[myloc]['settingcard']['profile']= "game/WHO2.PNG";
    else:
        Client.Data[myloc]['settingcard']['profile']= "game/WHO6.PNG";

def Piz_Setting(myloc):
    Client.Data[myloc]['character'] = 3                     #플레이어의 데이터에 character 를 추가한다.(선택 피즈)
    Client.Data[myloc]['Skill_A'] = SkillBook.Skill[1]
    Client.Data[myloc]['Skill_B'] = SkillBook.Skill[4]
    Client.Data[myloc]['Skill_C'] = SkillBook.Skill[8]
    Client.Data[myloc]['Skill_D'] = SkillBook.Skill[6]
    Client.Data[myloc]['settingcard'] ={'card1':"game/PIZ_MOVE1.png", 'card2' : "game/PIZ_MOVE2.png", 'card3': "game/PIZ_MOVE3.png",
                                        'card4':"game/PIZ_MOVE4.png", 'card5' : "game/PIZ_MOVE5.png", 'card6': "game/PIZ_SKILL1.png",
                                        'card7':"game/PIZ_SKILL2.png", 'card8' : "game/PIZ_SKILL3.png", 'card9': "game/PIZ_SKILL4.png",
                                        'card10': "game/MpPlus.png", 'background':"game/Back_Piz.jpg"}
    if(myloc < Client.Data[myloc]['enemyloc']):
        Client.Data[myloc]['settingcard']['profile']= "game/WHO1.PNG";
    else:
        Client.Data[myloc]['settingcard']['profile']= "game/WHO5.PNG";

def PatternPlaying(player1,player2,cardnumber, waitting):
    cardnumber = int(cardnumber)  

    if(cardnumber>=6 and cardnumber<=9 ):
        Client.Field[player1['fieldloc']]['stack3']+=1
        #Controll.adad+=1
        while(Client.Field[player1['fieldloc']]['stack3']%2!=0):
            pass
    else:
        pass


    if(0<cardnumber and cardnumber<6):  #이동이나 마나 카드를 실행했더라도 스택을 1올려줌
        cardmove(cardnumber, player1['Position'])
        Client.Field[player1['fieldloc']]['stack3']+=1

    elif(cardnumber==10):

        if(player1['MP']<=80):
            player1['MP'] += 20
        else:
            player1['MP'] = 100
        Client.Field[player1['fieldloc']]['stack3']+=1

    else:
        if(cardnumber == 6):
            cardskill(player1, player2, player1['Skill_A'])

        elif(cardnumber == 7):
            cardskill(player1, player2, player1['Skill_B'])

        elif(cardnumber == 8):
            cardskill(player1, player2, player1['Skill_C'])

        elif(cardnumber == 9):
            cardskill(player1, player2, player1['Skill_D'])
    
    for i in range(3000000):        #핑조절
        pass

    waitting= waitting + 1       


def cardmove (cardnum,myPOS):        #선택한 카드 정보, 플레이어의 좌표
         
    Move =  [[0,0],[0,-1],[-1,0],[0,1],[1,0]]   #  0- 1↑ 2← 3↓ 4→ 

    myPOS[0] = myPOS[0] + Move[cardnum-1][0]
    myPOS[1] = myPOS[1] + Move[cardnum-1][1]

    if(myPOS[0]<1):
        myPOS[0]+=1
    elif(myPOS[0]>5):
        myPOS[0]-=1

    if(myPOS[1]<1):
        myPOS[1]+=1
    elif(myPOS[1]>4):
        myPOS[1]-=1

def cardskill (player1,player2,skill):

    skillrange = skill[0] 
    skilldamage = skill[1]
    skillMP = skill[2]
    player1['MP'] = player1['MP'] - skillMP
    for i in range(len(skillrange)) :  
        if(player2['Position']==[player1['Position'][0] + skillrange[i][0], player1['Position'][1] + skillrange[i][1]]):
            player2['HP'] = player2['HP'] - skilldamage
            if(player2['HP'] < 0):
                player2['HP']=0
        else:
            pass

    

def getskillmana(player,num):

    if(num==6):
        return player['Skill_A'][2]
    elif(num==7):
        return player['Skill_B'][2]
    elif(num==8):
        return player['Skill_C'][2]
    elif(num==9):
        return player['Skill_D'][2]
    else:
        return 0

def CardCheck(player,card1, card2, card3):  #에러코드 0:문제없음 1: 숫자입력 안함. 2: 카드범위를 초과함. 3: 카드가같음  4: 마나부족.
    
    ErrorCode = 0
    if( (card1.isdigit()) and (card2.isdigit()) and (card3.isdigit()) ):
        card1 = int(card1)
        card2 = int(card2)
        card3 = int(card3)
        if( (card1 > 0 and card1 < 11) and (card2 > 0 and card2 < 11) and (card3 > 0 and card3 < 11) ):
            
            if( (card1 != card2) and (card2 != card3) and (card3 != card1) ):
                if( player['MP'] < (getskillmana(player,card1) + getskillmana(player,card2) + getskillmana(player,card3)) ):
                    
                    if( card1==10 or card2==10 or card3==10 ):
                        if( player['MP'] + 20 > (getskillmana(player,card1) + getskillmana(player,card2) + getskillmana(player,card3)) ):
                            return ErrorCode
                        else:
                            return ErrorCode + 4  #4
                    
                else:
                    return ErrorCode  #0
            else:
                return ErrorCode + 3  #3
        else:
            return ErrorCode + 2  #2
    else:
        return ErrorCode + 1  #1
