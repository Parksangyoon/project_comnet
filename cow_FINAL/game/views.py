from django.shortcuts import render
from django.http import HttpResponse
from.models import *
from.Gameplaylib import*
from.setimage import*
# Create your views here.

def goto_HowtoGame(request) :
   return render(request, 'Screen/HowtoGame.html')
def goto_Editor(request) :
	return render(request, 'Screen/Editor.html')
def goto_game(request) :
   givenum = Controll.stackplayer + 0         #들어오는 순서데로 번호를 부여해 준다.
   Controll.stackplayer += 1
   data = { 'num' : givenum }
   return render(request, 'Screen/Game.html', data) #context를 넘겨준다.
def goto_Loading(request):
   myloc = int(request.POST['playstart'])
   data={'num':myloc}
   return render(request, 'Screen/Loading.html',data)
def goto_Select_Character(request,playnum) :
   Controll.joinnum += 1                           
   if (Controll.joinnum == 2) :                            #플레이어2가 들어왔을 때
      mynum = int(playnum)                  #부여된 플레이어 번호를 가져온다.
      myloc = int(Controll.location + 1)                              #플레이어 2의 data가 저장될 위치
      enemyloc = int(Controll.location + 0)                           #플레이어 1의 data가 저장되어있는 위치
      Controll.location += 2                                 #두 플레이어 이외 다음 두플레이어가 사용할 위치 설정

      enemynum = int(Client.Data[enemyloc]['playnum'])            #플레이어1의 번호를 가져온다.
      Client.Data[enemyloc]['enemynum'] = mynum            #플레이어1의 data의 enemynum에 자신의 번호를 넣어준다.

      player2 = player_Setting(mynum, enemynum, myloc, enemyloc, [5,3])  #플레이어2의 data
      Client.Data.append(player2)                        #플레이어 2의 data가 저장될 위치에 저장

      Client.Data[myloc]['imloc']=int(Controll.imloc)
      Controll.imloc+=1

      data = {'locnum' : myloc}         #자신의 플레이어 번호와, data를 넘겨준다.
      Controll.Fieldloc+=1         #두명의 플레이어가 서로 결투하게 되었다면 fieldloc을 하나 증가시켜준다.
      return render(request, 'Screen/Select_Character.html', data)
   else:                                          #플레이어 1이 들어왔을 때(2명중 처음 들어온 플레이어)
      Controll.joinnum = 1
      mynum = int(playnum)                  #부여된 플레이어 번호를 가져온다.
      myloc = int(Controll.location + 0)                              #플레이어 1의 data가 저장될 위치
      enemyloc = int(Controll.location + 1)                           #플레이어 2의 data가 저장될 위치

      player1 = player_Setting(mynum,"Unknown", myloc, enemyloc, [1,2])   #플레이어1의 data 설정      #플레이어1과 상대될 플레이어2를 아직 모르므로 "unknown"
      Client.Data.append(player1)                        #플레이어1 data를 추가

      stack = stack_Setting()
      Client.Field.append(stack)               #비어있는 필드 배열에 0값을 넣어준다.

      Client.image.append({'check1':0,'check2':0, 'length_x':range(5),'length_y':range(4)})
      Client.Data[myloc]['imloc']=int(Controll.imloc)

      data = {'locnum' : myloc }         #자신의 플레이어 번호와, data를 넘겨준다

      while (Controll.joinnum == 1) :
         pass
      return render(request, 'Screen/Select_Character.html', data)   
                                                #플레이어 1이 들어왔을 때(2명중 처음 들어온 플레이어)
def goto_SelectCard(request, locnum):
   myloc = int(locnum)                        #플레이어의 데이터를 받아온다.
   char=int(request.POST['characternum'])
   if (char ==1 ):
      Izreal_Setting(myloc)
   elif (char ==2 ):
      Xvii_Setting(myloc)
   else:
      Piz_Setting(myloc)
   Client.Data[myloc]['Readcard'] =0
   Client.Data[myloc]['CardSelect']=[11,11,11]
   Client.Data[myloc]['wait']=3
   enemyloc = int(Client.Data[myloc]['enemyloc'])
   if(myloc < Client.Data[enemyloc]['myloc']):
         play1=Client.Data[myloc]['settingcard']['profile']
         play2="game/WHO8.png"
   else:
      play2=Client.Data[myloc]['settingcard']['profile']
      play1="game/WHO4.png"   
   data={'locnum': myloc, 'player1' : play1, 'player2' : play2, 'wait':Client.Data[myloc]['wait']}
   return render(request, 'Screen/Characterloading.html', data)

def goto_cardend(request, locnum):
   myloc = int(locnum)
   enemyloc = int(Client.Data[myloc]['enemyloc'])
   Client.Data[myloc]['wait']+=1

   if(Client.Data[myloc]['wait']>3 and Client.Data[enemyloc]['wait']==3):
      if(myloc < Client.Data[enemyloc]['myloc']):
         play1=Client.Data[myloc]['settingcard']['profile']
         play2="game/WHO8.png"
      else:
         play2=Client.Data[myloc]['settingcard']['profile']
         play1="game/WHO4.png"   
      data={'locnum': myloc, 'player1' : play1, 'player2' : play2,'wait':Client.Data[myloc]['wait']}
      return render(request, 'Screen/Characterloading.html', data)
   elif(Client.Data[myloc]['wait']>3 and Client.Data[enemyloc]['wait']!=3):
      Client.Data[myloc]['wait']=0
      if(myloc < Client.Data[enemyloc]['myloc']):
         play1=Client.Data[myloc]['settingcard']['profile']
         play2=Client.Data[enemyloc]['settingcard']['profile']
      else:
         play2=Client.Data[myloc]['settingcard']['profile']
         play1=Client.Data[enemyloc]['settingcard']['profile']   
      data={'locnum': myloc, 'player1' : play1, 'player2' : play2}
      return render(request, 'Screen/Characterloading.html', data)
   else:
      setim=Setimage(myloc)
      data = { 'data' : setim, 'locnum' : myloc, 'card' : Client.Data[myloc]['settingcard'],
               'ErrorCode' : Client.Data[myloc]['Error']}
      return render(request, 'Screen/SelectCard.html', data)


def goto_PlayScreen(request, locnum) :                  #카드 선택 후 올바른 카드 선택 했는지 확인 하고 플레이 셋팅 

   myloc = int(locnum)
   enemyloc = Client.Data[myloc]['enemyloc']
   location = Client.Data[myloc]['imloc']

   First = request.POST['firstcard']               #선택한 첫번째 카드를 가져온다.
   Second = request.POST['secondcard']               #선택한 두번째 카드를 가져온다.
   Third = request.POST['thirdcard']               #선택한 두번째 카드를 가져온다.

   Client.Data[myloc]['Error'] = CardCheck(Client.Data[myloc],First, Second, Third)
   if (Client.Data[myloc]['Error'] == 0) :            
         CardSelect = [First, Second, Third]
   else:
      data = { 'data' : Setimage(myloc), 'locnum' : myloc, 'card' : Client.Data[myloc]['settingcard'], 'ErrorCode' : Client.Data[myloc]['Error'] }
      return render(request, 'Screen/SelectCard.html', data)

   Client.Data[myloc]['CardSelect'] = CardSelect
   Client.Data[myloc]['Readcard'] = 1
   data={'myloc': myloc}
   return render(request, 'Screen/selectloading.html', data)

def goto_selectend(request, locnum):
   myloc=int(locnum)
   setim=Setimage(myloc)
   data = {'data' : setim, 'myloc' : myloc, 'round': Client.Data[myloc]['Readcard']} 
   return render(request, 'Screen/PlayScreen.html', data)   #상대의 카드를 확인하고 처음 자기 위치를 보여준다.


def Loop_play(request, locnum):
   myloc = int(locnum)
   enemyloc = Client.Data[myloc]['enemyloc']
   location = Client.Data[myloc]['imloc']
   Client.Field[Client.Data[myloc]['fieldloc']]['stack1']+=1


   while(not ((Client.Field[Client.Data[myloc]['fieldloc']]['stack1'])%2 ==0)):
      pass

   if(Client.Data[myloc]['HP'] <= 0 and Client.Data[enemyloc]['HP'] <= 0) :
      data = {'data' : Client.image[location], 'myloc' : myloc}
      return render(request, 'Screen/DrawScreen.html', data)
   elif (Client.Data[myloc]['HP'] <= 0 and Client.Data[enemyloc]['HP'] > 0) :      #hp상태를 확인하여 승패를 가린다.
      data = {'data' : Client.image[location], 'myloc' : myloc}
      return render(request, 'Screen/LoseScreen.html', data)
   elif(Client.Data[myloc]['HP'] > 0 and Client.Data[enemyloc]['HP'] <= 0) :      
      data = {'data' : Client.image[location], 'myloc' : myloc}
      return render(request, 'Screen/WinScreen.html', data)

   
   elif(Client.Data[myloc]['Readcard'] < 4):                              #첫번째 , 두번째, 세번째 카드 실행 
      waiting = Client.Field[Client.Data[myloc]['fieldloc']]['stack2']
      cardn =int(Client.Data[myloc]['Readcard'])-1
      for i in range(3000000):
         pass
      PatternPlaying(Client.Data[myloc], Client.Data[enemyloc], Client.Data[myloc]['CardSelect'][cardn], waiting)
      
      Client.Data[myloc]['Readcard'] +=1
      Setimage(myloc)
      while(not ((waiting % 2 == 0)) ): #상대편의 카드 사용이 끝날때까지 대기.
         pass
      
      data = {'data' : Client.image[location], 'myloc' : myloc, 'round': Client.Data[myloc]['Readcard']}
      return render(request, 'Screen/PlayScreen.html', data)

   else:                              #세번째 카드가 실행되고 승패가 갈리지 않았을 경우 다시 카드 선택지로 간다.

      
      Client.Field[Client.Data[myloc]['fieldloc']]['stack4']+=1

      

      Client.Data[myloc]['Readcard'] =0
      setim=Client.image[location]
      data = { 'data' : setim, 'locnum' : myloc, 'card' : Client.Data[myloc]['settingcard'] }
      return render(request, 'Screen/SelectCard.html', data)

