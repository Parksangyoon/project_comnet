class SkillBook:
    
    damage=[15, 50, 50, 30, 25, 30, 40, 40, 30, 30]
    UsingMP=[15, 50, 50, 30, 25, 20, 50, 50, 30, 30]

    attackrange = [
    [[-1,-1],[0,-1],[1,-1],[-1,0],[0,0],[1,0],[-1,1],[0,1],[1,1]],  #Skill[0]   789456123  <-숫자 키패드의 모양을 통해 공격범위를 표현한 것
    [[0,0],[-1,1],[0,1],[1,1]],                                     #Skill[1]   5123
    [[0,0],[-1,-1],[0,-1],[1,-1]],                                  #Skill[2]   5789
    [[-1,-1],[1,-1],[0,0],[-1,1],[1,1]],                            #Skill[3]   79513
    [[0,-1],[-1,0],[0,0],[1,0],[0,1]],                              #Skill[4]   84562                             #Skill[5]   84562
    [[-1,0],[0,0],[1,0]],                                           #Skill[5]   456
    [[-1,-1],[-1,0],[-1,1],[0,0],[1,-1],[1,0],[1,1]],               #Skill[6]   7415963
    [[-1,-1],[0,-1],[1,-1],[0,0],[-1,1],[0,1],[1,1]],               #Skill[7]   7895123
    [[-1,-1],[0,-1],[1,-1],[-1,0],[0,0],[0,1]],                     #Skill[8]   789456 
    [[0,-1],[1,-1],[0,0],[1,0],[0,1],[1,1]]                         #Skill[9]   895623
    ]             
               
    Skill=  [[attackrange[0],damage[0],UsingMP[0]],[attackrange[1],damage[1],UsingMP[1]],[attackrange[2],damage[2],UsingMP[2]],
            [attackrange[3],damage[3],UsingMP[3]],[attackrange[4],damage[4],UsingMP[4]],[attackrange[5],damage[5],UsingMP[5]],
            [attackrange[6],damage[6],UsingMP[6]],[attackrange[7],damage[7],UsingMP[7]],[attackrange[8],damage[8],UsingMP[8]],
            [attackrange[9],damage[9],UsingMP[9]]]
        
    