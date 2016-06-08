from .Gameplaylib import Client

def Setimage(MYLOC):                     #플레이어 데이터를 보고 html에 그릴 image를 setting 해준다.
   location=Client.Data[MYLOC]['imloc']

   if(MYLOC < Client.Data[MYLOC]['enemyloc']):               #player1의 이미지들을 구성 

      if((Client.Data[MYLOC]['character'] == 1) and (Client.Data[MYLOC]['Readcard'] <=1)): #카드 골랐을 때만 셋팅    
                                                #이즈리얼을 선택 하였을 경우 html에 그릴 image를 설정한다.
         Client.image[location]['character1'] ="game/izreal.png"
         Client.image[location]['firstcard1'] = imagelist.Izreal[int(Client.Data[MYLOC]['CardSelect'][0])-1]
         Client.image[location]['secondcard1'] = imagelist.Izreal[int(Client.Data[MYLOC]['CardSelect'][1])-1]
         Client.image[location]['thirdcard1'] = imagelist.Izreal[int(Client.Data[MYLOC]['CardSelect'][2])-1]
                                          
      elif((Client.Data[MYLOC]['character'] == 2) and (Client.Data[MYLOC]['Readcard'] <=1)):            
                                                   #바이를 선택 하였을 경우 html에 그릴 image를 설정한다.
         Client.image[location]['character1'] ="game/xvi.png"
         Client.image[location]['firstcard1'] = imagelist.Xvii[int(Client.Data[MYLOC]['CardSelect'][0])-1]
         Client.image[location]['secondcard1'] = imagelist.Xvii[int(Client.Data[MYLOC]['CardSelect'][1])-1]
         Client.image[location]['thirdcard1'] = imagelist.Xvii[int(Client.Data[MYLOC]['CardSelect'][2])-1]

      elif((Client.Data[MYLOC]['character'] == 3) and (Client.Data[MYLOC]['Readcard'] <=1)):            
                                                   #피즈를 선택 하였을 경우 html에 그릴 image를 설정한다.
         Client.image[location]['character1'] ="game/piz.png"
         Client.image[location]['firstcard1'] = imagelist.Piz[int(Client.Data[MYLOC]['CardSelect'][0])-1]
         Client.image[location]['secondcard1'] = imagelist.Piz[int(Client.Data[MYLOC]['CardSelect'][1])-1]
         Client.image[location]['thirdcard1'] = imagelist.Piz[int(Client.Data[MYLOC]['CardSelect'][2])-1]

      Client.image[location]['HP1']=Client.Data[MYLOC]['HP']      #그외에 들어갈 html을 그릴 값들을 설정
      Client.image[location]['MP1']=Client.Data[MYLOC]['MP']
      Client.image[location]['tile']=imagelist.Izreal[11]
      Client.image[location]['Position_x1']=Client.Data[MYLOC]['Position'][0]
      Client.image[location]['Position_y1']=Client.Data[MYLOC]['Position'][1]
      if(Client.Data[MYLOC]['Error'] ==0):
         Client.image[location]['check1'] +=1
      else:
         return Client.image[location]
   else:                                          #player2의 이미지들을 구성    

      if((Client.Data[MYLOC]['character'] == 1) and (Client.Data[MYLOC]['Readcard'] <=1)):            
                                                 #이즈리얼을 선택 하였을 경우 html에 그릴 image를 설정한다.
         Client.image[location]['character2'] = "game/izreal.png"
         Client.image[location]['firstcard2'] = imagelist.Izreal[int(Client.Data[MYLOC]['CardSelect'][0])-1]
         Client.image[location]['secondcard2'] = imagelist.Izreal[int(Client.Data[MYLOC]['CardSelect'][1])-1]
         Client.image[location]['thirdcard2'] = imagelist.Izreal[int(Client.Data[MYLOC]['CardSelect'][2])-1]

      elif((Client.Data[MYLOC]['character'] == 2) and (Client.Data[MYLOC]['Readcard'] <=1)):         
                                                   #바이를 선택 하였을 경우 html에 그릴 image를 설정한다.
         Client.image[location]['character2'] ="game/xvi.png"
         Client.image[location]['firstcard2'] = imagelist.Xvii[int(Client.Data[MYLOC]['CardSelect'][0])-1]
         Client.image[location]['secondcard2'] = imagelist.Xvii[int(Client.Data[MYLOC]['CardSelect'][1])-1]
         Client.image[location]['thirdcard2'] = imagelist.Xvii[int(Client.Data[MYLOC]['CardSelect'][2])-1]

      elif((Client.Data[MYLOC]['character'] == 3) and (Client.Data[MYLOC]['Readcard'] <=1)):            
                                                   #피즈를 선택 하였을 경우 html에 그릴 image를 설정한다.
         Client.image[location]['character2'] ="game/piz.png"
         Client.image[location]['firstcard2'] = imagelist.Piz[int(Client.Data[MYLOC]['CardSelect'][0])-1]
         Client.image[location]['secondcard2'] = imagelist.Piz[int(Client.Data[MYLOC]['CardSelect'][1])-1]
         Client.image[location]['thirdcard2'] = imagelist.Piz[int(Client.Data[MYLOC]['CardSelect'][2])-1]

      Client.image[location]['HP2']=Client.Data[MYLOC]['HP']      #그외에 들어갈 html을 그릴 값들을 설정
      Client.image[location]['MP2']=Client.Data[MYLOC]['MP']
      Client.image[location]['tile']=imagelist.Izreal[11]
      Client.image[location]['Position_x2']=Client.Data[MYLOC]['Position'][0]
      Client.image[location]['Position_y2']=Client.Data[MYLOC]['Position'][1]
      if(Client.Data[MYLOC]['Error'] ==0):
         Client.image[location]['check2'] +=1
      else:
         return Client.image[location]

   while(not ((Client.image[location]['check1'] + Client.image[location]['check2'])%2)==0):
      pass

   if( (Client.image[location]['Position_x2'] == Client.image[location]['Position_x1']) and (Client.image[location]['Position_y1'] == Client.image[location]['Position_y2']) ):
      Client.image[location]['PositionCheck'] = True
   else:
      Client.image[location]['PositionCheck'] = False
   return Client.image[location]

class imagelist:                                       #각 캐릭터에 속한 image 리스트 
   
   Izreal=["game/IZ_MOVE1.png","game/IZ_MOVE2.png","game/IZ_MOVE3.png","game/IZ_MOVE4.png","game/IZ_MOVE5.png",      #이즈
         "game/IZ_SKILL1.png","game/IZ_SKILL2.png","game/IZ_SKILL3.png","game/IZ_SKILL4.png","game/MpPlus.png",
         "game/xbox.png","game/tile.png"]

   Piz=["game/PIZ_MOVE1.png","game/PIZ_MOVE2.png","game/PIZ_MOVE3.png","game/PIZ_MOVE4.png","game/PIZ_MOVE5.png",         #피즈
         "game/PIZ_SKILL1.png","game/PIZ_SKILL2.png","game/PIZ_SKILL3.png","game/PIZ_SKILL4.png","game/MpPlus.png",
         "game/xbox.png"]

   Xvii=["game/VI_MOVE1.png","game/VI_MOVE2.png","game/VI_MOVE3.png","game/VI_MOVE4.png","game/VI_MOVE5.png",         #바이
         "game/VI_SKILL1.png","game/VI_SKILL2.png","game/VI_SKILL3.png","game/VI_SKILL4.png","game/MpPlus.png",
         "game/xbox.png"]