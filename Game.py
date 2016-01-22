import pygame,sys,random, pygame.gfxdraw, math
from pygame.locals import *
pygame.init()
pygame.font.init()
pygame.mixer.init(frequency=4410, size=-16, channels=2, buffer=65536)
class Minigames:
    @staticmethod
    def KingOfTheLadder():
        books=["spider eyes 4","broken clay 4","grey wool 4","sparkle 4","360 no scope 4","fiery hair 4","explosive mine 4","randomness 4","witch farm 4","service bat 4"]
        Player.money=Player.money-100
        alive=True
        clock = pygame.time.Clock()
        frame=0
        score=0
        lane=1
        difficulty=9
        rocks=[[],[],[]]
        while alive:
            clock.tick(30)
            lane=Battle.Menu(lane)
            frame=frame+1
            screen.fill((0,0,0))
            Draw.Entity("wall",(0,-832+((score*4)%832)),[0,0,0,0],True,False)
            Draw.Entity("wall",(0,((score*4)%832)),[0,0,0,0],True,False)
            for x in range(1,4):
                for i in range(-1,24):
                    Draw.Entity("ladder",(32*x,32*i+((score*4)%32)),[0,0,0,0],True,False)
            if frame==5:
                if score/80.0==score/80 and difficulty>1:
                    difficulty=difficulty-1
                frame=0
                score=score+1
                if random.randint(0,difficulty*2)==0:
                    rocks[random.randint(0,2)].append({"place":-32,"speed":random.randint(1,abs(difficulty-9))++random.randint(2,6)})
                if rocks==[[],[],[]]:
                    rocks[random.randint(0,2)].append({"place":-32,"speed":random.randint(1,abs(difficulty-9))+random.randint(2,6)})
            Draw.Entity("climb"+str(score%2),(lane*32+32,374),[0,0,0,0],True,False)
            for i in range(0,3):
                x=0
                while x<len(rocks[i]):
                    Draw.Entity("rock",(i*32+32,rocks[i][x]["place"]),[0,0,0,0],True,False)
                    if rocks[i][x]["place"]-12<374 and rocks[i][x]["place"]-12>330 and i==lane:
                        alive=False
                    if rocks[i][x]["place"]-32<374 and rocks[i][x]["place"]-32>330 and i==lane:
                        alive=False
                    rocks[i][x]["place"]=rocks[i][x]["place"]+rocks[i][x]["speed"]
                    if rocks[i][x]["place"]>840:
                        del rocks[i][x]
                        x=0
                    else:
                        x=x+1
            Text.Write("Score: "+str(score/2)+" "*abs(len(str(score))-4),(210,20),color=(250,250,250),name="",update=False)
            Text.Write("Difficulty: "+`abs(difficulty-9)`,(460,20),color=(250,250,250),name="",update=False)
            Text.Write("Highest Score: "+str(Player.ran[28]),(460,650),color=(250,250,250),name="",update=False)
            pygame.display.update()
        if score/2>Player.ran[28]:
            text=""
            holder=score/2
            holder=holder-(holder%50)
            if holder>500:
                holder=500
            while holder>Player.ran:
                Player.inentory.append(books[holder/50])
                text=text+Player.party[0].name.title()+" Won a "+books[holder/50]+" Book! "
                holder=holder-50
            Player.ran[28]=score/2
        pygame.time.wait(2000)
        screen.fill((0,0,0))
        Text.Write("You Scored: "+str(score/2)+" "*abs(len(str(score))-4),(270,310),color=(250,250,250))
        dpress=True
        while dpress:
            for event in pygame.event.get():
                if event.type==KEYDOWN:
                    if event.key==K_d:
                        dpress=False
        Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0),False)
        Draw.Entity(Player.party[0].name,(6*64,4*64),[0,Player.direct*64,64,64],True,False) 
        if text!="":
            Text.Textbox(text,"game")
    @staticmethod
    def EnchantWars():
        prizes=["boulderfist 4","uhc kill 4","brown wool 4","gilitter 4","triforce 4","optimism 4","cloud glitch 4","free millbee 4","german efficency 4"]
        prize=random.choice(prizes)
        level={"knockback":0,"smite":1,"respiration":2,"feather falling":3,"unbreaking":4,"efficiency":5,"sharpness":6,"infinity":7,"fortune":8,"silk touch":9}
        books=["knockback","smite","respiration","feather falling","unbreaking","efficiency","sharpness","infinity","fortune","silk touch"]
        book=random.choice(books)
        enemybook=random.choice(books)
        Text.Textbox("Welcome to Enchant Wars! Your enchanted book is... "+book.title()+"! What would you like to bet?","guudeland",False)
        pygame.time.wait(100)
        run=True
        while run:
            options=["50","100","250","500"]
            var=Menu.Base(620,185,options,200,False)
            pygame.display.update()
            pygame.time.wait(15)
            if var!="pass" and var!=-1:
                if  Player.money<int(options[var]):
                    Text.Textbox(Player.party[0].name.title()+" Dont Have Enough Money For That!","game")
                else:
                    Player.money=Player.money-int(options[var])
                    Text.Textbox("The opponent enchanted... "+enemybook.title()+"!","guudeland")
                    if level[book]>level[enemybook]:
                        Text.Textbox(Player.party[0].name.title()+" Won "+str(int(options[var])*3)+"G!","guudeland")
                    if level[book]<level[enemybook]:
                        Text.Textbox(Player.party[0].name.title()+" Lost "+options[var]+"G. Take a "+prize.title()+" Book!","guudeland")
                        Player.inventory.append(prize)
                    if level[book]==level[enemybook]:
                        Text.Textbox("It Was a Tie! Take a "+prize.title()+" Book!","guudeland")
                        Player.inventory.append(prize)
                        Player.money=Player.money+int(options[var])
                    run=False
                        
    @staticmethod
    def Cards():
        Player.money=Player.money-300
        game=True
        state=0
        card=0
        clock=pygame.time.Clock()
        x=[66,216,366,516,666]
        cards=["none","none","none","book","money"]
        books=["contagious laugh 4","redstone 4","pink wool 4","lullaby 4","meditate 4","dyslexia 4","detnator 4","summon melon 4","villager farm 4"]
        random.shuffle(cards)
        while game:
            if state==0:
                Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0),False)
                Draw.Entity(Player.party[0].name,(6*64,4*64),[0,Player.direct*64,64,64],True,False) 
                for i in range(0,150):
                    Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0),False)
                    Draw.Entity(Player.party[0].name,(6*64,4*64),[0,Player.direct*64,64,64],True,False) 
                    Draw.Entity("card",(366,50),[0,0,0,0],True,False)
                    Draw.Entity("card",(i+366,50),[0,0,0,0],True,False)
                    Draw.Entity("card",(i*2+366,50),[0,0,0,0],True,False)
                    Draw.Entity("card",(366-i,50),[0,0,0,0],True,False)
                    Draw.Entity("card",(366-i*2,50),[0,0,0,0],True)
                    clock.tick(100)
                state=1
            if state==1:
                clock.tick(30)
                card=Battle.Menu(card,4)
                Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0),False)
                Draw.Entity(Player.party[0].name,(6*64,4*64),[0,Player.direct*64,64,64],True,False) 
                pressed=pygame.key.get_pressed()
                pygame.event.pump()
                if pressed[K_d]:
                    state=2
                for i in x:
                    Draw.Entity("card",(i,50),[0,0,0,0],True,False)
                Draw.Entity("outline",(x[card],50),[0,0,0,0],True,False)
                pygame.display.update()
            if state==2:
                Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0),False)
                Draw.Entity(Player.party[0].name,(6*64,4*64),[0,Player.direct*64,64,64],True,False)  
                Draw.Entity("card"+cards[card],(366,300),[0,0,0,0],True)
                pygame.time.wait(1000)
                if cards[card]=="book":
                    book=random.choice(books)
                    Text.Textbox(Player.party[0].name.title()+" Won An Ability Book! "+Player.party[0].name.title()+" Received a "+book.title()+" Book!","game")
                    Player.inventory.append(book)
                if cards[card]=="money":
                    Player.money=Player.money+1000
                    Text.Textbox(Player.party[0].name.title()+" Won 1000$!","game")
                if cards[card]=="none":
                    Text.Textbox(" The Card Is Blank... Better Luck Next Time!","game")
                game=False
#Inworld/ Player Data
class Save:
    @staticmethod
    #Load Write
    def Write():
        ## Ran ##
        save = open("Files/Save/Ran.txt", "w")
        for i in Player.ran:
            save.write(str(i)+"\n")
        ## World ##
        save = open("Files/Save/World.txt", "w")
        save.write(Player.worldname+"\n")
        save.write(str(Player.x)+"\n")
        save.write(str(Player.y)+"\n")
        save.write(str(Player.direct)+"\n")
        save.write(str(Player.money)+"\n")
        save.close()
        ## Inventory ##
        save = open("Files/Save/Inventory.txt", "w")
        for i in range(0,len(Player.inventory)):
            save.write(str(Player.inventory[i])+"\n")
        save.close()
        ## Settings ##
        save = open("Files/Save/Options.txt", "w")
        save.write(str(Player.textspeed)+"\n")
        save.write(str(Player.small)+"\n")
        save.write(str(Player.battlespeed)+"\n")
        save.write(str(Music.volume)+"\n")
        ## Maps ##
        save = open("Files/Save/Maps.txt", "w")
        for i in range(0,len(Map.locations)):
            save.write(str(Map.locations[i].location)+"\n")
        save.close()
        ## Players ##
        save = open("Files/Save/Players.txt", "w")
        for i in range(0,len(Player.party)):
            save.write(str(Player.party[i].name)+"\n")
            levels=""
            for x in range(0,8):
                levels=levels+str(Player.party[i].abilitylevel[x])+" "
            save.write(str(levels)+"\n")
            for x in range(0,3):
                save.write(str(Player.party[i].battleabilities[x])+"\n")
            save.write(str(Player.party[i].lvl)+" "+str(Player.party[i].xp)+" "+str(Player.party[i].gain)+" "+str(Player.party[i].nextlvl)+"\n")
            save.write(str(Player.party[i].weapon)+"\n")
        save.close()
        Text.Textbox("Game Saved.","game")
    @staticmethod
    #Loads Save
    def Load():
        ## Ran ##
        lines=[line.strip() for line in open("Files/Save/Ran.txt")]
        for i in range(0,len(lines)):
            Player.ran[i]=int(lines[i])
        if Player.ran[5]==1:
            Draw.images["tb"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/tree.png"),(64,64))
        ## World ##
        lines=[line.strip() for line in open("Files/Save/World.txt")]
        Player.worldname=lines[0]
        Player.x=int(lines[1])
        Player.y=int(lines[2])
        Player.direct=int(lines[3])
        Player.money=int(lines[4])
        Player.world,Player.events=World.FileToWorld(Player.worldname)
    ## Inventory ##
        Player.inventory=[line.strip() for line in open("Files/Save/Inventory.txt")]
    ## Settings ##
        lines=[line.strip() for line in open("Files/Save/Options.txt")]
        Player.textspeed=int(lines[0])
        if lines[1]=="False":
            Player.small=False
        else:
            Player.small=True
        Player.battlespeed=float(lines[2])
        Music.volume=int(lines[3])
        Music.ChangeSong(Player.worldname)
    ## Maps ##
        fi=[line.strip() for line in open("Files/Save/Maps.txt")]
        Map.locations=[Map(location) for location in fi]
    ## Players ##
        fi=[line.strip() for line in open("Files/Save/Players.txt")]
        amount=len(fi)/7
        counter=0
        Player.party=[]
        while amount>counter:
            start=counter*7
            Player.party.append(PartyMember.Create(PartyMember.FromFile(fi[start].title())))
            l=fi[start+1].split()
            Player.party[counter].abilitylevel=[int(i) for i in l]
            Player.party[counter].battleabilities=[fi[start+2],fi[start+3],fi[start+4]]
            xp=fi[start+5].split()
            for i in range(0,4):
                if i !=2:
                    xp[i]=int(xp[i])
                else:
                    xp[i]=float(xp[i])
            Player.party[counter].lvl=xp[0]
            Player.party[counter].xp=xp[1]
            Player.party[counter].gain=xp[2]
            Player.party[counter].nextlvl=xp[3]
            Player.party[counter].weapon=fi[start+6]
            Player.party[counter].update()
            counter=counter+1
    @staticmethod
    # Creates New Save
    def New():
        screen.fill((0,0,0))
        Text.Textbox("Welcome to Mindcrack : The Quest. Controls: D to Confirm, S to cancel, and Arrow Keys to move around. Our story begins 5 years ago, when King Poose gathered the 5 great warriors of the land, Aureylian the Cleric, Etho the Engineer, Vechs the Evil Mastermind, Coestar the Fighter and Guude, the leader of them all. Together, they stopped the plans of The Dark One, who threatened the land with mass destruction. They sealed him up in King Poose's prison, never to be seen again. Now the great king has summon their leader to his castle.","game",False)
        Map.Add("lord bajs temple")
        Map.Add("king pooses castle")
        Player.party=[PartyMember.Create(PartyMember.FromFile("Guude"))]
        World.LoadWorld("pooses throne",4,6)
        Save.Write()
class Map:
    locations=[]
    x=10
    xdir=0
    ydir=0
    y=90
    def __init__(self,location):
        self.location=location
        xy={"nebris ice castle":(100,200),"bling tower":(620,300),"coe mountain":(720,150),"e-team base":(40,500),"mesa":(50,430),"docms liquid assimilator":(300,300),"shop town":(675,640),"guudeland":(750,650),"barn":(750,250),"king pooses castle":(331,458),"lord bajs temple":(600,550),"aureylians rainbow castle":(460,120)}
        icon={"bling tower":"bling tower","coe mountain":"coe mountain","e-team base":"e-team base","mesa":"mesa","docms liquid assimilator":"doc water","shop town":"shop","guudeland":"guudeland","barn":"barnicon","king pooses castle":"sand","lord bajs temple":"baj","aureylians rainbow castle":"rainbow"}
        self.icon=icon[location]
        worldxy={"bling tower":(7,13),"coe mountain":(15,25),"e-team base":(9,7),"mesa":(15,25),"docms liquid assimilator":(21,10),"guudeland":(8,15),"shop town":(8,15),"barn":(8,15),"king pooses castle":(12,8),"lord bajs temple":(5,12),"aureylians rainbow castle":(11,19)}
        self.x,self.y=xy[location]
        self.worldx,self.worldy=worldxy[location]
    @staticmethod
    #Adds Map
    def Add(item):
        Map.locations.append(Map(item))
    @staticmethod
    #Shows Map, train
    def World():
        clock = pygame.time.Clock()
        run=1
        while run==1:
            clock.tick(60)
            dpress=False
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==KEYDOWN:
                    if event.key==K_d:
                        dpress=True
                    if event.key==K_s:
                        Draw.Fade(20,90)
                        run=0
                    if event.key==K_UP:
                        Map.ydir=-3
                    if event.key==K_DOWN:
                        Map.ydir=3
                    if event.key==K_RIGHT:
                        Map.xdir=3
                    if event.key==K_LEFT:
                        Map.xdir=-3
                if event.type==KEYUP:
                    if event.key in [K_LEFT,K_RIGHT]:
                        Map.xdir=0
                    if event.key in [K_UP,K_DOWN]:
                        Map.ydir=0
            screen.fill((255,255,255))
            Draw.Entity("world",(0,80),[0,0,0,0],True,False)
            if Map.x<0 and Map.xdir==-2:
                Map.xdir=0
            if Map.x>798 and Map.xdir==2:
                Map.xdir=0
            if Map.y<80 and Map.ydir==-2:
                Map.ydir=0
            if Map.y>672 and Map.ydir==2:
                Map.ydir=0
            Map.x=Map.x+Map.xdir
            Map.y=Map.y+Map.ydir
            for i in range(0,len(Map.locations)):
                Draw.Entity(Map.locations[i].icon,(Map.locations[i].x,Map.locations[i].y),[0,0,0,0],True,False)
                Draw.Entity("place",(Map.x,Map.y),[0,0,0,0],True,False)
                if Map.x<Map.locations[i].x+20 and Map.x>Map.locations[i].x-20:
                    if Map.y<Map.locations[i].y+20 and Map.y>Map.locations[i].y-20:
                        Draw.Entity(Map.locations[i].icon,(5,20),[0,0,0,0],True,False)
                        Text.Write(Map.locations[i].location.title(),(85,23),(0,0,0),"",False)
                        if dpress:
                            Draw.CutScene(2) #Train Cutscene
                            run=0
                            World.LoadWorld(Map.locations[i].location,Map.locations[i].worldx,Map.locations[i].worldy)
                            if Map.locations[i].location=="docms liquid assimilator" and Player.ran[30]==0:
                                Events.Call(104)
                                Player.ran[30]=1
            pygame.display.update()
class BattleText:
    coords={}
    list=[]
    font=pygame.font.Font("Files/font.ttf",24)
    coords["member0"]=[30,513]
    coords["member1"]=[294,513]
    coords["member2"]=[558,513]
    coords["enemy0"]=[20,280]
    coords["enemy1"]=[190,280]
    coords["enemy2"]=[360,280]
    coords["enemy3"]=[520,280]
    coords["enemy4"]=[690,280]
    def __init__(self,position,word,plusy=0):
        self.age=1
        self.position=self.coords[position]
        self.position=[self.position[0],self.position[1]-plusy]
        self.word=self.font.render(word,1,(120,120,120))
    #updates battletext
    def Update(self):
        self.age=self.age+2
        Draw.Entity(self.word,(self.position[0],self.position[1]-self.age),[0,0,0,0],False,False)
        if self.age>=90:
            return True
        else:
            return False
class Player:
    ind=[0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]
    ran=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    money=1500
    frame=0
    time=0
    walk=125
    inventory=["potato on a stick"]
    worldname="outside"
    @staticmethod
    #Rearrange Party
    def Move(first,second):
        hold=Player.party[first]
        Player.party[first]=Player.party[second]
        Player.party[second]=hold
    textspeed=-2
    small=False
    battlespeed=0.01
    index=BattleText.list
    world=""
    SelectedPlayer=0
    Dcooldown=10
    events=""
    name="pyro"
    spot=0
    x=0
    y=0
    direct=0
    Current=""
    speed=150
    @staticmethod
    #Handles Drawing World, Calling Events and Walking
    def Inworld():
        clock = pygame.time.Clock()
        clock.tick(60)
        if Player.Current=="menu":
            var=Menu.Base(600,0,["Party","Save","Inventory","Options","Tutorial"],230)
            if var==-1:
                Player.Current="inworld"
                Menu.state=0
            if var==0:
                Player.Current="party"
                Menu.state=0
            if var==1:
                Save.Write()
            if var==2:
                Player.Current="inventory"
                Menu.state=0
            if var==3:
                Player.Current="options"
                Menu.state=0
            if var==4:
                Player.Current="tutorial"
                Menu.state=0
        elif Player.Current=="inventory":
            var=Menu.Base(550,0,["All","Items","Books","Weapons","Key Items","G:"+str(Player.money)],270)
            if var!=-1 and var!="pass":
                Menu.state=1
                if var==0:
                    Player.Current="allin"
                if var==1:
                    Player.Current="specin"
                    Player.spot="item"
                if var==2:
                    Player.Current="specin"
                    Player.spot="book"
                if var==3:
                    Player.Current="specin"
                    Player.spot="weapon"
                if var==4:
                    Player.Current="specin"
                    Player.spot="key"
                if var==5:
                    Menu.state=0
            if var==-1:
                Player.Current="menu"
                Menu.state=2
        elif Player.Current=="specin":
            inv=Menu.Section(Player.spot)
            if len(inv)>0:
                Menu.Inventory(inv)
            else:
                Menu.state=0
                Player.Current="inventory"
                Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0),False)
                Draw.Entity(Player.party[0].name,(6*64,4*64),[0,Player.direct*64,64,64],True,False)
        elif Player.Current=="allin":
            Menu.Inventory(Player.inventory)
        elif Player.Current=="party":
            names=[]
            for i in range(0,len(Player.party)):
                names.append(Player.party[i].name.title())
                names[i]="         "+names[i]
            var=Menu.Base(400,0,names,400,False,70,20,False,True)
            for i in range(0,len(Player.party)):
                Draw.Entity(Player.party[i].name+"face",(450,i*70),[0,0,0,0],True,False)
            pygame.display.update()
            if var!=-1 and var!="pass":
                Player.SelectedMember=var
                Player.Current="party2"
                Menu.state=0
            if var==-1:
                Player.Current="menu"
                Menu.state=0
                Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0),False)
                Draw.Entity(Player.party[0].name,(6*64,4*64),[0,Player.direct*64,64,64],True,False)
        elif Player.Current=="party2":
            if Player.SelectedMember==0:
                x=5
            else:
                x=Player.SelectedMember*70-65
            var=Menu.Base(180,x,["Stats","Abilities","Move"],220)
            if var==2:
                Player.Current="move"
                Menu.state=0
            if var==1:
                Player.Current="ability"
                Menu.state=0
            if var==0:
                Player.Current="stats"
            if var==-1:
                Player.Current="party"
                Menu.state=Player.SelectedMember
        elif Player.Current=="stats":
            a=["","","","",""]
            a[0]="    "+Player.party[Player.SelectedMember].name.title()+" "*abs(len(Player.party[Player.SelectedMember].name)-16)+"Level: "+`Player.party[Player.SelectedMember].lvl`
            a[1]="    "+"HP: "+`Player.party[Player.SelectedMember].currenthp`+"/"+`Player.party[Player.SelectedMember].hp`+"      "+"Attack: "+`Player.party[Player.SelectedMember].attack`
            a[2]="    "+"Speed: "+`int(Player.party[Player.SelectedMember].speed)`+"       "+"Evade: "+`int(Player.party[Player.SelectedMember].evade)`
            a[3]="    "+"XP:            "+`Player.party[Player.SelectedMember].xp`+"/"+`Player.party[Player.SelectedMember].nextlvl`
            a[4]="    "+"Weapon:       "+Player.party[Player.SelectedMember].weapon.title()
            var=Menu.Base(10,10,a,830)
            if var!="pass":
                Player.Current="party"
                Menu.state=Player.SelectedMember
        elif Player.Current=="ability":
            Draw.Entity(pygame.transform.scale(Draw.images["playerbox"],(820,250)),(5,5),[0,0,0,0],False,False)
            a=[]
            for i in range(0,8):
                if Player.party[Player.SelectedMember].abilitylevel[i]!=0:
                    if Player.party[Player.SelectedMember].abilities[i] in Player.party[Player.SelectedMember].battleabilities:
                        a.append(Player.party[Player.SelectedMember].abilities[i]+" "*abs(len(Player.party[Player.SelectedMember].abilities[i])-20)+"Selected  ")
                    else:
                        a.append(Player.party[Player.SelectedMember].abilities[i]+" "*abs(len(Player.party[Player.SelectedMember].abilities[i])-20)+"          ")
            var=Menu.Base(6,250,a,830,False,55,50,False)
            Text.Write(Player.party[Player.SelectedMember].abilities[Menu.state]+" "*abs(len(Player.party[Player.SelectedMember].abilities[Menu.state])-19)+"Level:"+`Player.party[Player.SelectedMember].abilitylevel[Menu.state]`+"  "+"Cooldown:"+`abilities.AbilityCool[Player.party[Player.SelectedMember].abilities[Menu.state]]`,(35,25),color=(100,100,100),name="",update=False,size=27)
            ret=abilities.Description(Player.party[Player.SelectedMember].abilities[Menu.state],Player.party[Player.SelectedMember])
            Text.Write(ret[0],(40,60),(100,100,100),"",False,"small")
            Text.Write(ret[1],(40,90),(100,100,100),"",False,"small")
            Text.Write(ret[2],(40,120),(100,100,100),"",True,"small")
            Text.Write(ret[3],(40,120),(100,100,100),"",True,"small")
            if var==-1:
                Menu.state=Player.SelectedMember
                Player.Current="party"
                Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0),False)
                Draw.Entity(Player.party[0].name,(6*64,4*64),(0,Player.direct*64,64,64),True,False)
            if var!=-1 and var!="pass":
                if not Player.party[Player.SelectedMember].abilities[var] in Player.party[Player.SelectedMember].battleabilities:
                    Player.Current="ability2"
                    Menu.state=0
                    Player.SelectedAbility=var
        elif Player.Current=="ability2":
            var=Menu.Base(300,Player.SelectedAbility*40+80,Player.party[Player.SelectedMember].battleabilities,500)
            if var==-1:
                Menu.state=Player.SelectedMember
                Player.Current="ability"
                Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0),False)
                Draw.Entity(Player.party[0].name,(6*64,4*64),(0,Player.direct*64,64,64),True,False)
            if var!=-1 and var!="pass":
                Player.Current="ability"
                Menu.state=0
                Player.party[Player.SelectedMember].battleabilities[var]=Player.party[Player.SelectedMember].abilities[Player.SelectedAbility]
        elif Player.Current=="move":
            names=[]
            for i in range(0,len(Player.party)):
                names.append(Player.party[i].name.title())
                names[i]="         "+names[i]
            var=Menu.Base(400,0,names,400,False,70,20,False,True)
            for i in range(0,len(Player.party)):
                Draw.Entity(Player.party[i].name+"face",(450,i*70),[0,0,0,0],True,False)
            pygame.display.update()
            if var!=-1 and var!="pass":
                Player.Move(Player.SelectedMember,var)
                Player.Current="party"
                Menu.state=0
            if var==-1:
                Player.Current="party"
                Menu.state=0
        elif Player.Current=="tutorial":
            var=Menu.Base(500,0,["In Battle","Out of Battle"],300)
            if var==-1:
                Player.Current="menu"
                Menu.state=4
            if var==0:
                Player.Current="battle"
            if var==1:
                Text.Textbox("Out of battle, you can move around using the arrow keys, use D to confirm or interact, and S to cancel. You can buy weapons and books at shops using gold you have won in battle. You can also play mini games to win prizes, mainly at Guudeland. You can also find chests that have prizes around the map and in hidden areas. ","game")
        elif Player.Current=="battle":
            var=Menu.Base(450,0,["Basics","Statuses","Abilties","Enemies","Weapons","Experience"],350)
            if var==-1:
                Player.Current="tutorial"
                Menu.state=0
            if var==0:
                Text.Textbox("The battle system is fairly simple at its core, but can get very complicated when making strategies. First off, the combat is timed based and you have 3 Mindcrackers fighting at a time. As time goes by, you will gain PP. Different characters have different speeds, meaning they gain PP faster or slower. With PP you can use skills, being attack(1 PP), confidence +(which we will get to later)(1 PP), or use a skill specific to the person(3 PP). Confidence is a value that goes down over battle and is indicated by the darkness of a players face. If your confidence gets to low, you'll miss a lot. Next, you have abilities. Each player has 8 of these that will be unlocked while leveling up, however you can only have 3 selected at a time. They do not cost PP, however do run on a separate cooldown. You want to use these as soon as possible so they can start cooling down again, however sometimes its better to wait for the right moment. Finally, you can run, but it will return you to the first area of the game. Well that was a lot! Now your ready to get started. If you want more information, read the next tutorial on statuses!","game")
            if var==1:
                Text.Textbox("Statuses are very important to battle. Quite a few abilities and special skills will inflict a status on you or the opponent. One of the most important things about statuses is you can only have one at a time. So, you can use a positive status to overwrite a negitive one, or vice-versa on a enemy. Statuses will naturally end if you give them time, but you generally want to end them quickly. Here are the statuses: [Stat Up/Down: can be speed, evasivness or attack (it will say in the status bar)] [Sleep: cant use skills or abilities until end of cooldown or you take damage] [Encouraged: Highly increases critical hit chance and resets confidence] [Confused: Will attack a random foe or ally] [Posion: -1/16 of HP every turn] [Regeneration: +1/16 of HP every turn] [Paralyzed: Cant use skills] [Ability-Lock: Cant use abilties] [Fire: -1/16 of HP + 1/8 of all damage you do] [Precision: Every attack hits] [Wither: -1/16 first turn, every turn damage doubles] [Shielded: damage directed to another pool of HP]. So, thats statuses! Make sure to use them wisely and be aware of what your enemies can do with them.","game")
            if var==2:
                Text.Textbox("Abilties, along side stats, are what make different party members unique. Abilities have lots of different types of effects, and all characters have 8. You can switch between those eight, but you can only have 3 selected at a time. When choosing abilities, you have to consider what role you want this member to play and how he/Aureylian will compliement the other party members and there abilities. Also, each ability has 4 levels, which you can buy books in stores to upgrade. Be warned though, level 4 books cant by bought, only found or won. Abilties also have cooldowns to consider. Some abilities allow you to use other peoples abilities, which is really useful. I'll give you an example of a strategy you may use with the party members you start with:","game")
            if var==3:
                Text.Textbox("Enemies all work differently, so lets go over some basics. Most enemies have a basic attack and a skill, but some are different. There are also many different types of AI, which decides when they decide to do different things and which party member they will attack. Most enemies attack whoever has the most aggro, a hidden number that tracks who has done the most damage to the enemy and is has a 1/6 chance of being reset every turn. Enemies also have stats like party members, so some will preform better than others. Thats pretty much it for enemies, so be careful!","game")
            if var==4:
                Text.Textbox("Each party member has a weapon type, and can equip weapons that fall under that category. Weapons affect your stats, increasing some while decreasing others. The weapon you choose is important based on the abilities and role the player has. For example, if you have Millbee set up to be a healer, you would want to give him a weapon that increases his speed so he can heal more often instead of something that would increase his attack, because he wont use that as much. Also, different types of weapons are more effective against different enemies. It works like this: Physical is good on Energy, Energy is good on Magic and Magic is good on Physical. In game, this mostly means Sword>Gun>Wand>Sword, because these are the weapons most enemies will have. Its like rock paper scissors, and it doesnt go backwards. So if you have wand attacking a sword, you will do extra damage, but a sword attacking a wand will still do normal. Its only 1.3 damage, but you should still watch out for it. Thats it for weapons! Good luck!","game")
            if var==5:
                Text.Textbox("Experience is required to level up and get stronger. You get XP for beating an enemy. You also gain more experience from fighting with people you have not used as much. This is to allow you to use all the party members instead of just 3. As you use a party member, your gain will start to go down. For every battle their not in, this hidden cooldown will go up. So make sure to switch out your party and get a feel for all the different mindcrackers and their play style!","game")
        elif Player.Current=="options":
            var=Menu.Base(500,0,["Text Speed","Battle Speed","Volume","Screen"],300)
            if var==-1:
                Player.Current="menu"
                Menu.state=3
            if var==0:
                Player.Current="text"
                Menu.state=Player.textspeed
            if var==1:
                Player.Current="battles"
                if Player.battlespeed==0.01:
                    Menu.state=1
                if Player.battlespeed==0.02:
                    Menu.state=0
                if Player.battlespeed==0.007:
                    Menu.state=2
            if var==2:
                Player.Current="music"
                Menu.state=Music.volume/2
            if var==3:
                Player.Current="screen"
                Menu.state=0
        elif Player.Current=="screen":
            var=Menu.Base(600,0,["Large","Small","Full"],200)
            if var==0:
                Player.small=False
                screen=pygame.display.set_mode((832,704))
                Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0),False)
                Draw.Entity(Player.party[0].name,(6*64,4*64),(0,Player.direct*64,64,64),True,False)
            if var==1:
                Player.small=True
                screen=pygame.display.set_mode((416,352))
                Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0),False)
                Draw.Entity(Player.party[0].name,(6*64,4*64),(0,Player.direct*64,64,64),True,False)
            if var==2:
                Player.small=False
                screen=pygame.display.set_mode((832,704),pygame.FULLSCREEN)
                Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0),False)
                Draw.Entity(Player.party[0].name,(6*64,4*64),(0,Player.direct*64,64,64),True,False)
            if var==-1:
                Player.Current="options"
        elif Player.Current=="music":
            var=Menu.Base(600,0,["0","1","2","3","4","5"],200)
            if var!=-1 and var!="pass":
                Music.ChangeVolume(var*2)
            if var==-1:
                Player.Current="options"
                Menu.state=2
        elif Player.Current=="text":
            var=Menu.Base(600,0,["Fast","Middle","Slow"],200)
            if var!=-1 and var!="pass":
                Player.textspeed=var
            if var==-1:
                Player.Current="options"
                Menu.state=0
        elif Player.Current=="battles":
            var=Menu.Base(600,0,["Fast","Middle","Slow"],200)
            if var==0:
                Player.battlespeed=0.02
            if var==1:
                Player.battlespeed=0.01
            if var==2:
                Player.battlespeed=0.007
            if var==-1:
                Player.Current="options"
                Menu.state=1
        else:
            for i in range(0,len(Player.party)):
                if Player.party[i].currenthp!=0:
                    Player.party[i].currenthp=Player.party[i].currenthp+(math.ceil(Player.party[i].hp/64.0))
                    if Player.party[i].currenthp>Player.party[i].hp:
                        Player.party[i].currenthp=Player.party[i].hp
            Player.time=Player.time+1
            if Player.time%8==0:
                Player.frame=Player.frame+1
                Player.frame=Player.frame%8
            Draw.Tiles(Player.x,Player.y,Player.world,Player.events,[0,0],False)
            direction=[(0,1),(-1,0),(1,0),(0,-1)]
            shiftx,shifty=direction[Player.direct]
            Draw.Entity(Player.party[0].name,(6*64,4*64),[0,Player.direct*64,64,64])
            clock.tick(60)
            pressed=pygame.key.get_pressed()
            pygame.event.pump()
            if pressed[K_UP]:
                Player.direct=3
                Player.move=True
            elif pressed[K_DOWN]:
                Player.direct=0
                Player.move=True
            elif pressed[K_LEFT]:
                Player.direct=1
                Player.move=True
            elif pressed[K_RIGHT]:
                Player.direct=2
                Player.move=True
            else:
                Player.move=False
            if pressed[K_d] and Player.Dcooldown==0:
                if Events.Test(Player.x+(shiftx),Player.y+(shifty),"D"):
                    Player.Dcooldown=10
                else:
                    Player.Dcooldown=10
                    Player.Current="menu"
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.KEYUP:
                    if event.key in [pygame.K_LEFT,pygame.K_RIGHT,pygame.K_DOWN,pygame.K_UP]:
                        Player.move=False
            if Player.Dcooldown!=0:
                Player.Dcooldown=Player.Dcooldown-1
            if Player.move:
                Player.x,Player.y,events=Draw.Walk(Player.x,Player.y,Player.direct,Player.world,Player.events,World.collisionlist,Player.party[0].name,False,Player.speed)
                if events:
                    Events.Test(Player.x,Player.y,"Walk")
#Battle System, Battle Information and Battle AI
class Battle:
    xpvalue={"sethbot":22,"sethwing":22,"wilson":28,"mesa deed trap":26,"instant damage potion":24,"posion potion":24,"skeleton horse":20,"tumbleweed":16,"lizard":18,"fish":10,"sea monster":21,"kamyu the hidden":18,"dinnerbone the destroyer":20,"codewarrior the instigator":18,"davion":30,"chipmonk":8,"flame venom spider":9,"derp bat":6,"scarecrow":14,"treebeard":16,"sapling":3,"bandit":6,"bandit leader":10,"runaway dog":5,"baby spider":6,"florb":7}
    run=False
    mine=0
    @staticmethod
    def Menu(state,i=2):
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN and event.key==pygame.K_RIGHT and state<i:
                state=state+1
            if event.type==pygame.KEYDOWN and event.key==pygame.K_LEFT and state>0:
                state=state-1
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        return state
    @staticmethod
    #Does all the other stuff with battles (music, end text)
    def Run(enemy,song="Battle1"):
        Music.ChangeByName(song)
        Music.current=song
        Draw.Fade(30,100)
        ret=Battle.Battle(enemy,Player.party)
        Battle.run=False
        Player.move=False
        Music.ChangeSong(Player.worldname)
        Draw.Entity(Player.party[0].name,(6*64,4*64),[0,Player.direct*64,64,64],True,False)
        return ret
    @staticmethod
    #Runs the Battle System
    def Battle(enemy,members):
        enemywait=["none","none","none","none","none"]
        for i in range(0,5):
            try:
                enemywait[i]=random.randint(0,int(enemy[i].currentspeed*10))/10.0
            except:
                pass
        for i in range(0,len(enemy)):
            if enemy[i]!="none":
                enemy[i].num=i
        useally=False
        Battle.mine=0
        caster=0
        xp=0
        enemycount=0
        SelectedPerson=0
        firstenemy=0
        lastenemy=0
        user=0
        end="attack"
        BattleMenu=0
        SelectedMember=0
        SelectedMenu=0
        persondir=1
        SelectedPerson=0
        wait=[1,1,1]
        for i in range(0,3):
            wait[i]=random.randint(0,int(members[i].currentspeed*10))/10.0
            members[i].update()
        hold=0
        maxhold=6
        ability="nouse"
        #Starts Members
        for i in range(0,3):
            members[i].BattleStart()
        Battle.run=True
        player=0
        text=""
        for i in range(0,len(enemy)):
            if enemy[i]!="none":
                text=text+enemy[i].name.title()+" Attacked! "
        Text.Textbox(text,"game")
        while Battle.run:
            if SelectedPerson<0:
                SelectedPerson=0
            Draw.Fill((255,255,255))
            clock.tick(30)
            heal=(10,10,10)
            pressed=pygame.key.get_pressed()
            pygame.event.pump()
            skills=["nouse","nouse","nouse"]
            for i in range(0,len(enemy)):
                if enemy[i]!="none":
                    if enemy[i].currenthp<1:
                        xp=xp+Battle.xpvalue[enemy[i].name]
                        enemy[i]="none"
                        enemywait[i]="none"
                if enemy[i]!="none":
                    enemy[i].addBuffs()
                    change=enemy[i].AI(members,enemy,i)
                    if change!="none":
                        enemy=change
                    Draw.Entity("enemyplate",(170*i+40,340),[0,0,0,0], True, False)
                    Draw.Entity(enemy[i].name,(170*i+40,330),[0,0,0,0], True, False)
                    Draw.Entity("enemybox",(170*i,200),[0,0,0,0], True, False)
                    Text.Write("HP:"+`enemy[i].currenthp`,(170*i+15,210),(10,10,10), "", False)
                    Text.Write(enemy[i].status[0].title(),(170*i+15,250),(10,10,10), enemy[i].status[0], False,19)
                    Text.Write("HP:"+`enemy[i].currenthp`,(170*i+15,210),(10,10,10), "", False)
                    if enemy[i].status[0]!="none":
                        Text.Write(`enemy[i].status[1]`,(170*i+15,275),(10,10,10), enemy[i].status[0], False,19)            
                    if BattleMenu==4:
                        Draw.Entity("surround",(170*SelectedPerson-10,190),[0,0,0,0], True, False)
            dead=0
            while enemy[dead]=="none": 
                dead=dead+1
                if dead==5:
                    Battle.run=False
                    BattleText.list=[]
                    Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0))
                    Player.Dcooldown=10
                    say="The enemy has been defeated! "
                    for i in range(0,3):
                        say=say+members[i].GainXP(int(math.ceil(xp*members[i].gain)))
                        if members[i].gain>=0.2:
                            members[i].gain=members[i].gain-0.1
                    for i in range(3,len(members)):
                        if members[i].gain<0.9:
                            members[i].gain=members[i].gain+0.1
                    return say
            for i in range(0,len(enemy)):
                if enemy[i]!="none":
                    enemycount=enemycount+1
                    lastenemy=i
            for i in range(len(enemy)-1,-1,-1):
                if enemy[i]!="none":
                    firstenemy=i
            for i in range(0,3):
                if members[i].currenthp<1:
                    members[i].currenthp=0
                    members[i].pp=0
                    if members[i].status[0]!="downed":
                        BattleText.list.append(BattleText("member"+str(i),"Downed"))
                    members[i].status=["downed","X",1]
                    members[i].confidence=100
                else:
                    members[i].addBuffs()
                    wait[i]=wait[i]-Player.battlespeed
                    wait[i]=round(wait[i],2)
                    if wait[i]<=0:
                        members[i].Countdown(1)
                        if members[i].hidden=="World Tour" and random.randint(0,100)==1:
                            members[i].pp=members[i].pp+3
                            BattleText.list.append(BattleText("member"+str(i),"World Tour"))
                        if members[i].hidden=="Adorable" and random.randint(0,100)==1:
                            for x in range(0,3):
                                if members[x].currenthp==0:
                                    members[x].currenthp=1
                                    members[x].status=["none",0]
                                BattleText.list.append(BattleText("member"+str(i),"Adorable"))
                        if members[i].hidden=="Nervous" and random.randint(0,100)==1:
                            members[i].status=["fast",6,1.5]
                            BattleText.list.append(BattleText("member"+str(i),"Nervous"))
                        if members[i].hidden=="Battle Scream" and random.randint(0,100)==1:
                            members[i].status=["attack +",6,1.5]
                            BattleText.list.append(BattleText("member"+str(i),"Battle Scream"))
                        if members[i].hidden=="Egg Attack" and random.randint(0,100)==1:
                            tre=random.randint(0,len(enemy)-1)
                            while enemy[tre]=="none":
                                tre=random.randint(0,len(enemy)-1)
                            enemy[tre].currenthp=int(enemy[tre].hp/2)
                            BattleText.list.append(BattleText("member"+str(i),"Egg Attack"))
                            BattleText.list.append(BattleText("enemy"+str(tre),"Half Health"))
                        multi=2-members[i].weaponspeed
                        wait[i]=float(members[i].currentspeed*multi)
                        if members[i].confidence<100:
                            members[i].confidence=members[i].confidence+random.randint(0,4)
                        if members[i].confidence>30:
                            members[i].confidence=100
            for i in range(0,5):
                if enemywait[i]!="none":
                    enemywait[i]=enemywait[i]-Player.battlespeed
                    enemywait[i]=round(enemywait[i],2)
                    if enemywait[i]==0 and enemy[i]!="none":
                        enemy[i].Countdown(1)
                        try:
                            enemywait[i]=enemy[i].currentspeed
                        except:
                            pass           
            for i in range(0,3):
                Draw.Entity("playerbox",(i*264+10,460),[0,0,0,0],True,False)
                Text.Write(members[i].name.title(),(i*264+95,480),(0,0,0),members[i].name,False)
                if members[i].currenthp<members[i].hp/4:
                    heal=(200,0,0)
                elif members[i].currenthp<members[i].hp/2:
                    heal=(200,170,0)
                else:
                    heal=(10,10,10)
                Text.Write(`members[i].currenthp`+"/"+`members[i].hp`+" HP",(i*264+25,530),heal,"",False)
                Text.Write(`members[i].pp`+" PP",(i*264+25,560),(10,10,10),"",False)
                Text.Write("Status:",(i*264+80,600),(10,10,10),(10,10,10),False)
                if members[i].status[0]!="none" and members[i].status[0]!="downed":
                    Text.Write(members[i].status[0].title()+":"+`members[i].status[1]`,(i*264+35,640),(10,10,10),members[i].status[0],False,19)
                else:
                    Text.Write(members[i].status[0].title(),(i*264+35,640),(10,10,10),members[i].status[0],False,19)
            if hold!=0:
                hold=hold-1
            if BattleMenu==0:
                SelectedMember=Battle.Menu(SelectedMember)
                Draw.Entity(members[SelectedMember].name+"face",(SelectedMember*264+10,455),[0,0,0,0],True,False)
                if pressed[K_d] and members[SelectedMember].status[0]!="downed":
                        BattleMenu=1
                        hold=maxhold
                        SelectedMenu=0
            if BattleMenu==1:
                if members[SelectedMember].currenthp<0:
                    BattleMenu=0
                if members[SelectedMember].status[0]=="paralyzed" or members[SelectedMember].status[0]=="sleep":
                    skillcolor=(190,100,100)
                else:
                    skillcolor=(0,0,0)
                if members[SelectedMember].status[0]=="ability-lock" or members[SelectedMember].status[0]=="sleep":
                    abilitycolor=(190,100,100)
                else:
                    abilitycolor=(0,0,0)
                Draw.Entity("menubox",(10,10),[0,0,0,0], True, False)
                Text.Write("Skills",(90,120),skillcolor,"",False)
                Text.Write("Abilities",(354,120),abilitycolor,"",False)
                Text.Write("Run",(618,120),(0,0,0),"",False)
                Text.Write(members[SelectedMember].name.title(),(30,30),(0,0,0),members[SelectedMember].name,False)
                Draw.Entity("pointer",(264*SelectedMenu+40,110),[0,0,0,0],True,False)
                Draw.Entity(members[SelectedMember].name+"face",(SelectedMember*264+10,455),[0,0,0,0],True,False)
                SelectedMenu=Battle.Menu(SelectedMenu)
                if pressed[K_d] and hold==0:
                    if SelectedMenu==0 and members[SelectedMember].status[0]!="paralyzed" and members[SelectedMember].status[0]!="sleep":
                        BattleMenu=2
                        hold=maxhold
                        SelectedMenu=0
                    if SelectedMenu==1 and members[SelectedMember].status[0]!="ability-lock" and members[SelectedMember].status[0]!="sleep":
                        BattleMenu=3
                        SelectedMenu=0
                        hold=maxhold
                    if SelectedMenu==2:
                        for i in range(0,3):
                            members[i].currenthp=1
                        World.LoadWorld("pooses throne",4,6)
                        break
                if pressed[K_s] and hold==0:
                    BattleMenu=0
            if BattleMenu==2:
                if members[SelectedMember].currenthp<0:
                    BattleMenu=0
                Draw.Entity("menubox",(10,10),[0,0,0,0], True, False)
                for i in range(0,3):
                    if members[SelectedMember].pp>i:
                        skills[i]=""
                    else:
                        skills[i]="nouse"
                Text.Write("Attack",(90,120),(0,0,0),skills[0],False)
                Text.Write("Confidence +",(324,120),(0,0,0),skills[0],False)
                Text.Write(members[SelectedMember].skill,(618,120),(0,0,0),skills[2],False)
                Draw.Entity("pointer",(264*SelectedMenu+40,110),[0,0,0,0],True,False)
                Text.Write(members[SelectedMember].name.title(),(30,30),(0,0,0),members[SelectedMember].name,False)
                Draw.Entity(members[SelectedMember].name+"face",(SelectedMember*264+10,455),[0,0,0,0],True,False)
                SelectedMenu=Battle.Menu(SelectedMenu)
                if pressed[K_d] and hold==0:
                    hold=maxhold
                    if SelectedMenu==0 and members[SelectedMember].pp>=1:
                        BattleMenu=4
                        user=SelectedMember
                        end="attack"
                        hold=maxhold
                        SelectedPerson=0
                    if SelectedMenu==1 and members[SelectedMember].pp>=1:
                        BattleMenu=5
                        user=SelectedMember
                        end="confidence"
                        hold=maxhold
                        player=0
                    if SelectedMenu==2 and members[SelectedMember].pp>=3:
                        if abilities.type[members[SelectedMember].skill]=="team":
                            BattleMenu=5
                            end="ability"
                            user=SelectedMember
                            ability=members[SelectedMember].skill
                if pressed[K_s] and hold==0:
                    BattleMenu=1
                    SelectedMenu=0
                    useally=False
                    hold=maxhold
            if BattleMenu==3:
                if members[SelectedMember].currenthp<0:
                    BattleMenu=0
                Draw.Entity("menubox",(10,10),[0,0,0,0], True, False)
                for i in range(0,3):
                    if members[SelectedMember].abilitiescool[i]>0 and not useally:
                        ability="nouse"
                    else:
                        ability="normal"
                    Text.Write(members[SelectedMember].battleabilities[i]+":"+str(members[SelectedMember].abilitiescool[i]),(255*i+45,120),(10,10,10),ability,False,19)
                Text.Write(members[SelectedMember].name.title(),(30,30),(0,0,0),members[SelectedMember].name,False)
                Draw.Entity("pointer",(255*SelectedMenu+20,115),[0,0,0,0],True,False)
                Draw.Entity(members[SelectedMember].name+"face",(SelectedMember*264+10,455),[0,0,0,0],True,False)
                SelectedMenu=Battle.Menu(SelectedMenu)
                if pressed[K_d] and hold==0:
                    if members[SelectedMember].abilitiescool[SelectedMenu]==0 or useally:
                        hold=maxhold
                        ability=members[SelectedMember].battleabilities[SelectedMenu]
                        if abilities.type[ability]=="team":
                            BattleMenu=5
                            end="ability"
                            player=0
                            user=SelectedMember
                            place=SelectedMenu
                            SelectedMenu=0
                        if abilities.type[ability]=="enemy":
                            BattleMenu=4
                            end="ability"
                            person=0
                            user=SelectedMember
                            place=SelectedMenu
                            SelectedMenu=0
                        if abilities.type[ability]=="run":
                            BattleMenu=1
                            hold=maxhold
                            abilities.Run(SelectedMember,ability,members,enemy,"none")
                            if useally and abilities.AbilityCool[ability]!="skill":
                                members[caster].abilitiescool[castera]=abilities.AbilityCool[ability]
                            elif abilities.AbilityCool[ability]!="skill":
                                members[SelectedMember].abilitiescool[SelectedMenu]=abilities.AbilityCool[ability]
                            useally=False
                        if abilities.type[ability]=="ally":
                            BattleMenu=5
                            useally=True
                            caster=SelectedMember
                            castera=SelectedMenu
                            end="ally"
                if pressed[K_s] and hold==0:
                    BattleMenu=1
                    hold=maxhold
                    SelectedMenu=0
                    useally=False
            if BattleMenu==4:
                while enemy[SelectedPerson]=="none":
                    SelectedPerson=SelectedPerson+persondir
                newperson=Battle.Menu(SelectedPerson,enemycount)
                if newperson<=lastenemy and newperson>=firstenemy and newperson>SelectedPerson:
                    persondir=1
                    SelectedPerson=SelectedPerson+persondir
                elif newperson<=lastenemy and newperson>=firstenemy and newperson<SelectedPerson:
                    persondir=-1
                    SelectedPerson=SelectedPerson+persondir
                while enemy[SelectedPerson]=="none":
                    SelectedPerson=SelectedPerson+persondir
                if pressed[K_d] and hold==0:
                    if end=="attack":
                        if members[SelectedMember].status[0]!="confused":
                            members[user].Attack(enemy[SelectedPerson],SelectedPerson)
                        else:
                            if random.randint(0,2)==1:
                                target=random.randint(0,2)
                                members[user].Attack(members[target],target)
                            else:
                                confuse=random.randint(0,4)
                                while enemy[confuse]=="none":
                                    confuse=random.randint(0,4)
                                members[user].Attack(enemy[confuse],confuse)
                        members[user].pp=members[SelectedMember].pp-1
                    if end=="ability":
                        abilities.Run(user,ability,members,enemy,SelectedPerson)
                        if useally and abilities.AbilityCool[ability]!="skill":
                            members[caster].abilitiescool[castera]=abilities.AbilityCool[ability]
                        elif abilities.AbilityCool[ability]!="skill":
                            members[user].abilitiescool[place]=abilities.AbilityCool[ability]
                        useally=False
                    SelectedPerson=0
                    persondir=1
                    hold=maxhold
                    BattleMenu=1
                if pressed[K_s] and hold==0:
                    useally=False
                    BattleMenu=2
                    SelectedPerson=0
                Draw.Entity(members[SelectedMember].name+"face",(SelectedMember*264+10,455),[0,0,0,0],True,False)
            if BattleMenu==5:
                Draw.Entity(members[player].name+"face",(player*264+10,455),[0,0,0,0],True,False)
                player=Battle.Menu(player)
                if pressed[K_d] and hold==0:
                    if end=="confidence":
                        members[player].confidence=0
                        members[user].pp=members[user].pp-1
                        BattleMenu=1
                        hold=maxhold
                        SelectedMenu=0
                        BattleText.list.append(BattleText("member"+str(player),"Confidence +"))
                        player=0
                    if end=="ability":
                        abilities.Run(user,ability,members,enemy,player)
                        if useally and abilities.AbilityCool[ability]!="skill":
                            members[caster].abilitiescool[castera]=abilities.AbilityCool[ability]
                        elif abilities.AbilityCool[ability]!="skill":
                            members[user].abilitiescool[place]=abilities.AbilityCool[ability]
                        useally=False
                        BattleMenu=1
                        hold=maxhold
                        SelectedMenu=0
                        player=0
                    if end=="ally":
                        BattleMenu=3
                        SelectedMember=player
                        hold=maxhold
                if pressed[K_s] and hold==0:
                    useally=False
                    BattleMenu=2
            if BattleMenu!=5:
                Draw.Box(members[SelectedMember].confidence*10,(SelectedMember*264+10,455,64,64))
            else:
                Draw.Box(members[player].confidence*10,(player*264+10,455,64,64))
            index=BattleText.list
            i=0
            while i<len(BattleText.list):
                kill=BattleText.list[i].Update()
                if kill:
                    index.pop(i)
                i=i+1
            Draw.Entity("none",(0,0))
            BattleText.list=index
            if members[0].status[0]=="downed" and members[2].status[0]=="downed" and members[1].status[0]=="downed":
                Text.Textbox("Your party has been defeated!","game",False)
                for i in range(0,len(members)):
                    members[i].currenthp=1
                World.LoadWorld("pooses throne",4,6)
                Battle.run=False
                Player.move=False
                Music.ChangeSong(Player.worldname)
                break
#Makes Enemies and Functions for Effects on Them
class Enemy:
    def __init__(self,name,HPvalue,SPEEDvalue,ATTACKvalue,EVADEvalue,level,status,type,skill="none"):
        self.name=name
        self.aggro=[0,0,0]
        self.type=type
        self.HPvalue=HPvalue
        self.speed=SPEEDvalue
        self.ATTACKvalue=ATTACKvalue
        self.lvl=level+3
        if self.name=="runaway dog":
            self.lvl=self.lvl-3
        self.hp=int(self.HPvalue*float(self.lvl))
        self.currenthp=self.hp
        self.currentspeed=2
        self.attack=int(self.ATTACKvalue*float(self.lvl)+5)
        self.currentattack=self.attack
        self.evade=abs(SPEEDvalue-10)+(EVADEvalue*5)/3
        self.skill=skill
        self.pp=0
        self.oldpp=0
        self.wait=False
        self.status=status
    #Does Damage to Enemy
    def addBuffs(self):
        if self.status[0]=="fast":
            self.currentspeed=self.speed/self.status[2]
        if self.status[0]=="slow":
            self.currentspeed=self.speed*self.status[2]
        if self.status[0]=="attack +" or self.status[0]=="attack -":
            self.currentattack=self.attack*self.status[2]
        if self.status[0]=="evade +":
            self.currentevade=self.evade*self.status[2]
    def DoDamage(self,amount,enemy,enemynum):
        chance=1
        damage=1
        critical=False
        effective=False
        if self.status[0]=="encouraged":
            chance=75
        if random.randint(1,100)<=chance:
            critical=True
            damage=1.5+round(random.random(),1)
        if abilities.typea[self.type]==enemy.type:
            effective=True
            damage=damage*1.3
        enemy.TakeDamage(int(amount*damage),enemynum,critical,effective)
        if self.status[0]=="fire":
            self.TakeDamage(int(amount/8),enemynum,False)
    def TakeDamage(self,damage,enemynum,critical=False,effective=False):
        if critical:
            BattleText.list.append(BattleText("enemy"+str(abs(enemynum)),"Critical",28))
        elif effective:
            BattleText.list.append(BattleText("enemy"+str(abs(enemynum)),abilities.typea[abilities.typea[self.type]].title()+" Hit",28))
        if critical and effective:
            BattleText.list.append(BattleText("enemy"+str(abs(enemynum)),abilities.typea[abilities.typea[self.type]].title()+" Hit",48))
        if self.status[0]=="shield":
            self.status[1]=self.status[1]-damage
            damage=0
            if self.status[1]<=0:
                damage=abs(self.status[1])
                self.currenthp=self.currenthp-damage
                self.status[0]="none"
        else:
            self.currenthp=self.currenthp-damage
        BattleText.list.append(BattleText("enemy"+str(abs(enemynum)),"-"+str(int(damage))+" HP"))
    def Attack(self,enemy,enemynum,times=1):
        if enemy.evade<random.randint(0,100) or self.status[0]=="precision":
            self.DoDamage(int(self.currentattack/10)*times,enemy,enemynum)
            if enemy.hidden=="Ninja" and random.randint(0,100)==1:
                self.DoDamage(int(enemy.currentattack/10),self.num,False,False)
                BattleText.list.append(BattleText("member"+str(enemynum),"Ninja",28))
            if enemy.hidden=="Spooky Ghost" and random.randint(0,100)==1:
                self.status=["paralyzed",5,1]
                BattleText.list.append(BattleText("member"+str(enemynum),"Spooky Ghost",28))
        else:
            BattleText.list.append(BattleText("member"+str(abs(enemynum)),"Missed"))
    def removeBuffs(self):
        self.currentattack=self.attack
        self.currentevade=self.evade
        self.currentspeed=self.speed
    def Countdown(self,time=1):
        self.pp=self.pp+time
        if self.status[0]=="posion":
            self.currenthp=self.currenthp-int(self.hp/16*self.status[2])
        if self.status[0]=="wither":
            self.currenthp=self.currenthp-int(self.hp/32*self.status[2])
            self.status[2]=self.status[2]+1
        if self.status[0]=="regen":
            self.currenthp=self.currenthp+int(self.hp/16*self.status[2])
            if  self.currenthp>self.hp:
                self.currenthp=self.hp
        if self.status[0]!="shield":
            self.status[1]=self.status[1]-1
        if self.status[1]==0:
            self.removeBuffs()
            self.status=["none",0,0]
        if random.randint(1,2)==1 or random.randint(1,2)==1:
            self.aggro=[0,0,0]
    def AI(self,members,enemy,place):
        if self.status[0]!="paralyzed" and self.status[0]!="sleep":
            if self.name=="redstone bug":
                if self.pp>1:
                    self.status=["precision",1,1]
                    target=Enemy.Target(self,members)
                    self.Attack(members[target],target)
                    self.pp=self.pp-1
            if self.name=="world reset":
                buff=["regen","attack +","fast","shield","encouraged"]
                nerf=["posion","sleep","wither","fire","confused","slow","attack -"]
            if self.name=="posion potion":
                if self.pp>2:
                    for i in range(0,3):
                        if random.randint(1,10)!=1:
                            members[i].status=["posion",6,1]
                            BattleText.list.append(BattleText("member"+str(i),"Posioned"))
                        else:
                            BattleText.list.append(BattleText("member"+str(i),"Failed"))
                    self.currenthp=0
            if self.name=="sethwing":
                if self.pp>0:
                    target=Enemy.Target(self,members,"weak")
                    self.Attack(members[target],target)
                    self.pp=self.pp-1
            if self.name=="sethbot":
                target=Enemy.Target(self,members)
                if self.pp>0:
                    if random.randint(0,4)!=2:
                        self.Attack(members[target],target)
                        self.pp=self.pp-1
                    else:
                        members[target].status=["paralyzed",4,1]
                        BattleText.list.append(BattleText("member"+str(target),"Paralyzed"))
            if self.name=="wilson":
                # Gets sick, cures, steak to heal, flower to encourage, slow hits hard
                if self.status[0]=="posion" and random.randint(2,3)==3 and self.oldpp!=self.pp:
                    self.status=["none",0]
                    BattleText.list.append(BattleText("enemy"+str(self.num),"Golden Apple"))
                if self.oldpp!=self.pp and random.randint(0,3)==0:
                    self.status=["posion",8,1.5]
                    BattleText.list.append(BattleText("enemy"+str(self.num),"Sick"))
                if self.pp>0:
                    target=Enemy.Target(self,members)
                    choice=random.randint(0,8)
                    if choice<4:
                        self.Attack(members[target],target)
                    elif choice<6:
                        self.status=["encouraged",4,1]
                        BattleText.list.append(BattleText("enemy"+str(self.num),"Flower"))
                    else:
                        self.currenthp=self.currenthp+25
                        if self.currenthp>self.hp:
                            self.currenthp=self.hp
                        BattleText.list.append(BattleText("enemy"+str(self.num),"Steak"))
                    self.pp=self.pp-1
            if self.name=="mesa deed trap":
                if self.wait==False:
                    self.status=["attack +",12,2]
                    self.wait=True
                if self.pp>0:
                    target=Enemy.Target(self,members)
                    self.Attack(members[target],target)
                    self.pp=self.pp-1          
            if self.name=="instant damage potion":
                if self.pp>2:
                    for i in range(0,3):
                        if random.randint(1,10)!=1:
                            self.Attack(members[i],i,4)
                            BattleText.list.append(BattleText("member"+str(i),"Instant Damage",48))
                        else:
                            BattleText.list.append(BattleText("member"+str(i),"Failed"))
                    self.currenthp=0
            if self.name=="lizard":
                if self.pp>0:
                    if random.randint(0,9)!=1:
                        target=Enemy.Target(self,members)
                        self.Attack(members[target],target)
                        self.pp=self.pp-1
                    else:
                        for i in range(0,2):
                            members[i].status=["posion",6,1.5]
                            BattleText.list.append(BattleText("member"+str(i),"Posion"))
                        self.status=["shield",50,1]
            if self.name=="skeleton horse":
                if self.pp>0 and self.wait==False:
                    self.wait=True
                    for i in range(0,3):
                        members[i].status=["confused",5,1]
                        BattleText.list.append(BattleText("member"+str(i),"Confused"))
                    self.pp=self.pp-1
                if self.pp>0:
                    target=Enemy.Target(self,members)
                    if random.randint(1,5)!=4:
                        self.Attack(members[target],target)
                        self.pp=self.pp-1
                    else:
                        members[target].status=["confused",10,1]
                        BattleText.list.append(BattleText("member"+str(target),"Confused"))
                        self.pp=self.pp-1
            if self.name=="sea monster":
                target=Enemy.Target(self,members)
                run=random.randint(0,9)
                if self.pp>0:
                    if run==0:
                        health=[members[0].currenthp,members[1].currenthp,members[2].currenthp]
                        hit=[members[0].currenthp,members[1].currenthp,members[2].currenthp]
                        hit.sort()
                        if hit[0]!=0:
                            target=health.index(hit[0])
                        elif hit[1]!=0:
                            target=health.index(hit[1])
                        else:
                            target=health.index(hit[2])
                        members[target].status=["aggro",6,1]
                    elif run==1:
                        self.status=["regen",7,2]
                    else:
                        self.Attack(members[target],target)
                    self.pp=self.pp-1
            if self.name=="fish":
                target=Enemy.Target(self,members)
                if self.pp>0:
                    self.Attack(members[target],target)
                    self.pp=self.pp-1
            if self.name=="davion":
                move=random.randint(0,7)
                target=Enemy.Target(self,members)
                if self.pp>0:
                    if move==1:
                        members[target].status=["wither",5,1]
                        BattleText.list.append(BattleText("member"+str(target),"Black Wool"))
                    elif move==2:
                        members[target].status=["fire",5,1]
                        BattleText.list.append(BattleText("member"+str(target),"Red Wool"))
                    elif move==3:
                        members[target].status=["posion",5,1]
                        BattleText.list.append(BattleText("member"+str(target),"Lime Green Wool"))
                    else:
                        self.Attack(members[target],target)
                    self.pp=self.pp-1
            if self.name=="dinnerbone the destroyer":
                if self.pp>0 and self.oldpp!=self.pp and random.randint(0,1)==1:
                    target=Enemy.Target(self,members)
                    self.Attack(members[target],target)
                    self.pp=self.pp-1
                if self.pp>1:
                    target=Enemy.Target(self,members)
                    members[target].confidence=100
                    self.pp=self.pp-2
                    BattleText.list.append(BattleText("enemy"+str(self.num),"Upside Down"))
            if self.name=="codewarrior the instigator":
                if self.pp>0:
                    if random.randint(0,1)==0:
                        target=Enemy.Target(self,members)
                        self.Attack(members[target],target)
                        self.pp=self.pp-1
                    else:
                        for i in range(0,3):
                            members[i].status=["fire",7,1]
                            BattleText.list.append(BattleText("member"+str(i),"Burned"))
                            self.pp=self.pp-1
            if self.name=="kamyu the hidden":
                if self.oldpp!=self.pp and random.randint(0,2)==2:
                    self.wait=True
                if self.pp>0 and not self.wait:
                    target=Enemy.Target(self,members)
                    self.Attack(members[target],target)
                    self.pp=self.pp-1
                if self.pp>2:
                    self.currenthp=self.currenthp+20
                    if self.currenthp>self.hp:
                        self.currenthp=self.hp
                    BattleText.list.append(BattleText("enemy"+str(self.num),"Ran EXE"))
                    self.pp=self.pp-3
                    self.wait=False
            if self.name=="chipmonk":
                if self.oldpp!=self.pp and random.randint(0,2)==2:
                    self.wait=True
                if self.pp>0 and not self.wait:
                    target=Enemy.Target(self,members)
                    self.Attack(members[target],target)
                    self.pp=self.pp-1
                if self.pp>2:
                    self.status=["fast",4,1.5]
                    self.pp=self.pp-2
                    BattleText.list.append(BattleText("enemy"+str(self.num),"Fast"))
                    self.wait=False
            if self.name=="derp bat":
                if self.pp>0:
                    target=Enemy.Target(self,members)
                    self.Attack(members[target],target)
                    self.pp=self.pp-1
            if self.name=="flame venom spider":
                if self.pp>0:
                    target=Enemy.Target(self,members)
                    self.Attack(members[target],target)
                    self.pp=self.pp-1
                    if random.randint(0,3)==1:
                        members[target].status=["fire",random.randint(1,7),1]
                        BattleText.list.append(BattleText("member"+str(target),"Burned",28))
            if self.name=="scarecrow":
                if self.pp>0 and self.status[0]!="paralyzed":
                    attack=random.randint(0,6)
                    if attack==0:
                        for i in range(0,3):
                            members[i].status=["sleep",4,1]
                            BattleText.list.append(BattleText("member"+str(i),"Asleep"))
                    elif attack==1:
                        for i in range(0,3):
                            members[i].status=["paralyzed",4,1]
                            BattleText.list.append(BattleText("member"+str(i),"Paralyzed"))
                    elif attack==2:
                        for i in range(0,3):
                            members[i].status=["ability-lock",4,1]
                            BattleText.list.append(BattleText("member"+str(i),"Ability-Lock"))
                    else:
                        target=Enemy.Target(self,members)
                        self.Attack(members[target],target)
                    self.pp=self.pp-1
            if self.name=="treebeard":
                if self.oldpp!=self.pp and random.randint(0,2)==2:
                    self.wait=True
                if not self.wait and self.pp>=1 and self.status[0]!="paralyzed" and self.status[0]!="sleep":
                    target=Enemy.Target(self,members)
                    self.Attack(members[target],target)
                    self.pp=self.pp-1
                if self.wait and self.pp>=2 and self.status[0]!="paralyzed" and self.status[0]!="sleep":
                    self.wait=False
                    act=random.randint(0,2)
                    if act==0:
                        for i in range(0,3):
                            self.Attack(members[i],i)
                        self.pp=self.pp-3
                    if act==1:
                        for i in range(0,len(enemy)):
                            if random.randint(0,3)==1 and enemy[i]=="none":
                                BattleText.list.append(BattleText("enemy"+str(i),"Growth"))
                                enemy[i]=Enemy("sapling",1,3,2,0,5,["none",0,0],"physical")
                        self.pp=self.pp-3
                        return enemy
                    if act==2:
                        hp=0
                        for i in range(0,len(enemy)):
                            if enemy[i]!="none":
                                if enemy[i].name=="sapling":
                                    BattleText.list.append(BattleText("enemy"+str(i),"Eaten"))
                                    hp=hp+enemy[i].currenthp
                                    enemy[i].currenthp=0
                        if hp>0:
                            BattleText.list.append(BattleText("enemy"+str(place),"+"+str(hp)))
                        self.currenthp=self.currenthp+hp
                        self.pp=self.pp-3
                        if self.currenthp>self.hp:
                            self.currenthp=self.hp
            if self.name=="runaway dog":
                if self.pp>=1 and self.status[0]!="paralyzed":
                    target=Enemy.Target(self,members)
                    self.Attack(members[target],target)
                    self.pp=self.pp-1
            if self.name=="bandit":
                leader=False
                for i in range(0,len(enemy)):
                    try:
                        if enemy[i].name=="bandit leader":
                            leader=i
                            self.wait=True
                    except:
                        pass
                if self.oldpp!=self.pp and random.randint(1,4)==1 and self.status[0]!="paralyzed":
                    self.wait=True
                if self.pp>=1 and not self.wait and self.status[0]!="paralyzed":
                    target=Enemy.Target(self,members)
                    self.Attack(members[target],target)
                    self.pp=self.pp-1
                if self.pp>=2 and self.status[0]!="paralyzed" and self.wait:
                    self.wait=False
                    if leader==False:
                        abilities.Run(place,self.skill,enemy,members,place,"enemy")
                    else:
                        abilities.Run(place,self.skill,enemy,members,leader,"enemy")
                    self.pp=self.pp+1
            if self.name=="bandit leader":
                if self.pp>=1 and self.status[0]!="paralyzed":
                    target=Enemy.Target(self,members)
                    self.Attack(members[target],target)
                    self.pp=self.pp-1
            if self.name=="baby spider":
                if self.pp>0:
                    target=Enemy.Target(self,members)
                    if random.randint(0,5)!=5:
                        self.Attack(members[target],target)
                        self.pp=self.pp-1
                    else:
                        members[target].status=["posion",3,1]
            if self.name=="florb":
                if self.pp>1:
                    if random.randint(0,5)!=5:
                        target=Enemy.Target(self,members)
                        self.Attack(members[target],target)
                        self.pp=self.pp-1
                    else:
                        for i in range(0,len(enemy)):
                            if random.randint(0,3)==1 and enemy[i]=="none":
                                BattleText.list.append(BattleText("enemy"+str(i),"Split"))
                                enemy[i]=Enemy("florb",2,2,2,2,5,["none",0,0],"magical","none")
                                self.pp=self.pp-1
                        self.oldpp=self.pp
                        return enemy
            self.oldpp=self.pp
        return "none"
    @staticmethod
    def Target(user,members,ai="basic"):
        if user.status[0]=="confused":
            return random.randint(0,2)
        for i in range(0,3):
            if members[i].status[0]=="aggro":
                return i
        people=[2,0,1,2,0]
        if ai=="basic":
            for i in range(1,4):
                if user.aggro[people[i]]>user.aggro[people[i+1]] and user.aggro[people[i]]>user.aggro[people[i-1]]:
                    return people[i]
        if ai=="weak":
            hp=[members[0].currenthp,members[1].currenthp,members[2].currenthp]
            sortable=[members[0].currenthp,members[1].currenthp,members[2].currenthp]
            sortable.sort()
            if sortable[0]!=0:
                return hp.index(sortable[0])
            elif sortable[1]!=0:
                return hp.index(sortable[1])
            elif sortable[2]!=0:
                return hp.index(sortable[2])
        return random.randint(0,2)
#Holds Effects of Different Abilities
class abilities:
    typea={}
    typea["physical"]="energy"
    typea["energy"]="magical"
    typea["magical"]="physical"
    type={
        "None":"dontrun",
        #Guude
        "Evade +":"team",
        "Contagious Laugh":"enemy",
        "Spider Eyes":"team",
        "Boulderfist":"enemy",
        "Service Bat":"run",
        "Controversy":"run",
        "Never Nude":"team",
        "Golden Throw":"enemy",
        "All Alone":"enemy",
        #Pyro
        "Heal":"team",
        "Tackle":"enemy",
        "Imperssionate":"ally",
        "Green Shell":"enemy",
        "Game Theory":"enemy",
        "Meditate":"run",
        "360 No Scope":"enemy",
        "Triforce":"run",
        "Final Smash":"run",
        #OMGChad
        "Shield":"team",
        "Newcomer":"enemy",
        "Waffles Claw":"run",
        "Collab":"ally",
        "Recap":"enemy",
        "Magic Trick":"enemy",
        "Dyslexia":"run",
        "Fiery Hair":"run",
        "Optimism":"run",
        #Millbee
        "Aggro":"team",
        "Chocolate Knees":"team",
        "Orange Wool":"run",
        "Rainbow Explosion":"run",
        "Dadbee Aid": "enemy",
        "Free Millbee":"run",
        "Date Through":"enemy",
        "Randomness":"run",
        "Summon Melon":"run",
        #Aurey
        "Regen":"team",
        "Pink Enchant":"run",
        "RUDE!":"run",
        "Compliment":"team",
        "Lullaby":"enemy",
        "Sparkle":"run",
        "Glitter":"team",
        "Christmas":"enemy",
        "Rainbow Swirl":"team",
        #Docm
        "Attack +":"team",
        "Doc Block":"enemy",
        "Alright Guys":"run",
        "Carrot Stick":"team",
        "German Efficency":"team",
        "Witch Farm":"run",
        "Villager Farm":"run",
        "Nerfed":"run",
        "Breaking Bedrock":"enemy",
        #Etho
        "Fast":"team",
        "Get Snacks":"run",
        "Redstone":"enemy",
        "Broken Clay":"enemy",
        "UHC Kill":"enemy",
        "General Spaz":"run",
        "BREACH!":"enemy",
        "Anvil Drop":"enemy",
        "Death Games":"enemy",
        #Sethbling
        "Encourage":"team",
        "Sockem":"enemy",
        "Health Pack":"team",
        "Cloud Glitch":"team",
        "Zombie Raid":"run",
        "Redstone Challenge":"enemy",
        "Explosive Mine":"run",
        "Detnator":"run",
        "Lightning Missile":"enemy",
        #Vechs
        "Revive":"team",
        "White Wool":"team",
        "Lime Wool":"enemy",
        "Pink Wool":"run",
        "Grey Wool":"run",
        "Brown Wool":"team",
        "Red Wool":"enemy",
        "Black Wool":"enemy",
        "Victory Monument":"run"
        }
    AbilityCool={
        "":0,
        #Guude
        "Evade +":"skill",
        "Contagious Laugh":9,
        "Spider Eyes":13,
        "Boulderfist":7,
        "Service Bat":12,
        "Controversy":10,
        "Never Nude":7,
        "Golden Throw":6,
        "All Alone":7,
        #Pyro
        "Heal":"skill",
        "Imperssionate":13,
        "Tackle":8,
        "Green Shell":8,
        "Game Theory":12,
        "Meditate":8,
        "360 No Scope":5,
        "Triforce":10,
        "Final Smash":15,
        #Chad
        "Shield":"skill",
        "Newcomer":7,
        "Waffles Claw":9,
        "Collab":11,
        "Recap":4,
        "Magic Trick":7,
        "Dyslexia":10,
        "Fiery Hair":14,
        "Optimism":16,
        #Aurey
        "Regen":"skill",
        "Pink Enchant":7,
        "RUDE!":5,
        "Compliment":10,
        "Lullaby":10,
        "Sparkle":12,
        "Glitter":13,
        "Christmas":6,
        "Rainbow Swirl":9,
        #Millbee
        "Aggro":"skill",
        "Chocolate Knees":10,
        "Orange Wool":5,
        "Rainbow Explosion":10,
        "Dadbee Aid":6,
        "Free Millbee":11,
        "Date Through":5,
        "Randomness":9,
        "Summon Melon":10,
        #Docm
        "Attack +":"skill",
        "Doc Block":6,
        "Alright Guys":7,
        "Carrot Stick":14,
        "German Efficency":12,
        "Witch Farm":7,
        "Villager Farm":7,
        "Nerfed":13,
        "Breaking Bedrock":15,
        #Etho
        "Fast":"skill",
        "Get Snacks":8,
        "Redstone":6,
        "Broken Clay":6,
        "UHC Kill":7,
        "General Spaz":9,
        "BREACH!":10,
        "Anvil Drop":10,
        "Death Games":7,
        #Sethbling
        "Encourage":"skill",
        "Sockem":7,
        "Health Pack":8,
        "Cloud Glitch":10,
        "Zombie Raid":7,
        "Redstone Challenge":6,
        "Explosive Mine":6,
        "Detnator":12,
        "Lightning Missile":9,
        #Vechs
        "Revive":"skill",
        "White Wool":6,
        "Lime Wool":7,
        "Pink Wool":12,
        "Grey Wool":13,
        "Brown Wool":9,
        "Red Wool":7,
        "Black Wool":7,
        "Victory Monument":11
        }
    AbilityLevels={}
    ## Guudes Abilities ##
    AbilityLevels["Spider Eyes1"]=[13,80]
    AbilityLevels["Spider Eyes2"]=[12,70]
    AbilityLevels["Spider Eyes3"]=[12,60]
    AbilityLevels["Spider Eyes4"]=[11,50]
    AbilityLevels["Boulderfist1"]=[7,3]
    AbilityLevels["Boulderfist2"]=[7,4]
    AbilityLevels["Boulderfist3"]=[7,5]
    AbilityLevels["Boulderfist4"]=[6,5]
    AbilityLevels["Service Bat1"]=[12,8,70]
    AbilityLevels["Service Bat2"]=[13,6,80]
    AbilityLevels["Service Bat3"]=[13,4,80]
    AbilityLevels["Service Bat4"]=[14,2,70]
    AbilityLevels["Contagious Laugh1"]=[9,3,80]
    AbilityLevels["Contagious Laugh2"]=[9,4,80]
    AbilityLevels["Contagious Laugh3"]=[9,4,100]
    AbilityLevels["Contagious Laugh4"]=[8,5,100]
    AbilityLevels["Controversy1"]=[10]
    AbilityLevels["Controversy2"]=[9]
    AbilityLevels["Controversy3"]=[8]
    AbilityLevels["Controversy4"]=[7]
    AbilityLevels["Never Nude1"]=[7,10]
    AbilityLevels["Never Nude2"]=[7,20]
    AbilityLevels["Never Nude3"]=[7,30]
    AbilityLevels["Never Nude4"]=[7,40]
    AbilityLevels["Golden Throw1"]=[6,1]
    AbilityLevels["Golden Throw2"]=[6,1.5]
    AbilityLevels["Golden Throw3"]=[5,1.5]
    AbilityLevels["Golden Throw4"]=[5,2]
    AbilityLevels["All Alone1"]=[7,50,200]
    AbilityLevels["All Alone2"]=[7,40,200]
    AbilityLevels["All Alone3"]=[6,40,230]
    AbilityLevels["All Alone4"]=[6,30,230]
    ## Pyros Abilities ##
    AbilityLevels["Tackle1"]=[8]
    AbilityLevels["Tackle2"]=[8]
    AbilityLevels["Tackle3"]=[7]
    AbilityLevels["Tackle4"]=[6]
    AbilityLevels["Imperssionate1"]=[13]
    AbilityLevels["Imperssionate2"]=[12]
    AbilityLevels["Imperssionate3"]=[11]
    AbilityLevels["Imperssionate4"]=[10]
    AbilityLevels["Green Shell1"]=[8,60]
    AbilityLevels["Green Shell2"]=[8,70]
    AbilityLevels["Green Shell3"]=[7,70]
    AbilityLevels["Green Shell4"]=[6,70]
    AbilityLevels["Game Theory1"]=[12,8,50]
    AbilityLevels["Game Theory2"]=[12,8,60]
    AbilityLevels["Game Theory3"]=[12,4,50]
    AbilityLevels["Game Theory4"]=[12,4,60]
    AbilityLevels["Meditate1"]=[8,1]
    AbilityLevels["Meditate2"]=[8,2]
    AbilityLevels["Meditate3"]=[7,1]
    AbilityLevels["Meditate4"]=[7,2]
    AbilityLevels["360 No Scope1"]=[5,20]
    AbilityLevels["360 No Scope2"]=[5,25]
    AbilityLevels["360 No Scope3"]=[4,30]
    AbilityLevels["360 No Scope4"]=[4,35]
    AbilityLevels["Triforce1"]=[10,60]
    AbilityLevels["Triforce2"]=[10,70]
    AbilityLevels["Triforce3"]=[10,80]
    AbilityLevels["Triforce4"]=[9,80]
    AbilityLevels["Final Smash1"]=[15,60]
    AbilityLevels["Final Smash2"]=[15,80]
    AbilityLevels["Final Smash3"]=[14,80]
    AbilityLevels["Final Smash4"]=[14,100]
    ## Chads Abilities ##
    AbilityLevels["Newcomer1"]=[7,85]
    AbilityLevels["Newcomer2"]=[7,90]
    AbilityLevels["Newcomer3"]=[6,90]
    AbilityLevels["Newcomer4"]=[6,95]
    AbilityLevels["Waffles Claw1"]=[9]
    AbilityLevels["Waffles Claw2"]=[8]
    AbilityLevels["Waffles Claw3"]=[8]
    AbilityLevels["Waffles Claw4"]=[7]
    AbilityLevels["Collab1"]=[11]
    AbilityLevels["Collab2"]=[10]
    AbilityLevels["Collab3"]=[10]
    AbilityLevels["Collab4"]=[9]
    AbilityLevels["Recap1"]=[4]
    AbilityLevels["Recap2"]=[3]
    AbilityLevels["Recap3"]=[3]
    AbilityLevels["Recap4"]=[2]
    AbilityLevels["Magic Trick1"]=[7,0]
    AbilityLevels["Magic Trick2"]=[7,10]
    AbilityLevels["Magic Trick3"]=[7,20]
    AbilityLevels["Magic Trick4"]=[6,25]
    AbilityLevels["Dyslexia1"]=[10]
    AbilityLevels["Dyslexia2"]=[10]
    AbilityLevels["Dyslexia3"]=[9]
    AbilityLevels["Dyslexia4"]=[8]
    AbilityLevels["Fiery Hair1"]=[14,60]
    AbilityLevels["Fiery Hair2"]=[14,70]
    AbilityLevels["Fiery Hair3"]=[13,70]
    AbilityLevels["Fiery Hair4"]=[13,75]
    AbilityLevels["Optimism1"]=[16,30]
    AbilityLevels["Optimism2"]=[15,40]
    AbilityLevels["Optimism3"]=[14,40]
    AbilityLevels["Optimism4"]=[14,50]
    ## Millbees Abilities ##
    AbilityLevels["Chocolate Knees1"]=[10]
    AbilityLevels["Chocolate Knees2"]=[9]
    AbilityLevels["Chocolate Knees3"]=[8]
    AbilityLevels["Chocolate Knees4"]=[8]
    AbilityLevels["Orange Wool1"]=[5,4]
    AbilityLevels["Orange Wool2"]=[5,4]
    AbilityLevels["Orange Wool3"]=[4,3]
    AbilityLevels["Orange Wool4"]=[4,2]
    AbilityLevels["Rainbow Explosion1"]=[10]
    AbilityLevels["Rainbow Explosion2"]=[9]
    AbilityLevels["Rainbow Explosion3"]=[9]
    AbilityLevels["Rainbow Explosion4"]=[8]
    AbilityLevels["Dadbee Aid1"]=[6]
    AbilityLevels["Dadbee Aid2"]=[6]
    AbilityLevels["Dadbee Aid3"]=[5]
    AbilityLevels["Dadbee Aid4"]=[4]
    AbilityLevels["Free Millbee1"]=[11,70]
    AbilityLevels["Free Millbee2"]=[11,80]
    AbilityLevels["Free Millbee3"]=[10,80]
    AbilityLevels["Free Millbee4"]=[9,80]
    AbilityLevels["Date Through1"]=[5,1.5]
    AbilityLevels["Date Through2"]=[5,2]
    AbilityLevels["Date Through3"]=[4,1.5]
    AbilityLevels["Date Through4"]=[4,2]
    AbilityLevels["Randomness1"]=[9,1]
    AbilityLevels["Randomness2"]=[9,2]
    AbilityLevels["Randomness3"]=[9,3]
    AbilityLevels["Randomness4"]=[9,4]
    AbilityLevels["Summon Melon1"]=[10,80]
    AbilityLevels["Summon Melon2"]=[9,80]
    AbilityLevels["Summon Melon3"]=[8,80]
    AbilityLevels["Summon Melon4"]=[8,100]
    ## Aureys Abilities ##
    AbilityLevels["Pink Enchant1"]=[7,80]
    AbilityLevels["Pink Enchant2"]=[7,90]
    AbilityLevels["Pink Enchant3"]=[6,90]
    AbilityLevels["Pink Enchant4"]=[6,100]
    AbilityLevels["RUDE!1"]=[5,80]
    AbilityLevels["RUDE!2"]=[4,80]
    AbilityLevels["RUDE!3"]=[4,90]
    AbilityLevels["RUDE!4"]=[3,90]
    AbilityLevels["Compliment1"]=[10]
    AbilityLevels["Compliment2"]=[9]
    AbilityLevels["Compliment3"]=[8]
    AbilityLevels["Compliment4"]=[8]
    AbilityLevels["Lullaby1"]=[10,4]
    AbilityLevels["Lullaby2"]=[10,5]
    AbilityLevels["Lullaby3"]=[9,5]
    AbilityLevels["Lullaby4"]=[9,6]
    AbilityLevels["Sparkle1"]=[12]
    AbilityLevels["Sparkle2"]=[11]
    AbilityLevels["Sparkle3"]=[10]
    AbilityLevels["Sparkle4"]=[9]
    AbilityLevels["Glitter1"]=[13]
    AbilityLevels["Glitter2"]=[12]
    AbilityLevels["Glitter3"]=[11]
    AbilityLevels["Glitter4"]=[10]
    AbilityLevels["Christmas1"]=[6,50]
    AbilityLevels["Christmas2"]=[6,60]
    AbilityLevels["Christmas3"]=[6,70]
    AbilityLevels["Christmas4"]=[5,70]
    AbilityLevels["Rainbow Swirl1"]=[9,0]
    AbilityLevels["Rainbow Swirl2"]=[9,1]
    AbilityLevels["Rainbow Swirl3"]=[8,1]
    AbilityLevels["Rainbow Swirl4"]=[7,2]
    ## Docms Abilities ##
    AbilityLevels["Doc Block1"]=[6,2]
    AbilityLevels["Doc Block2"]=[6,3]
    AbilityLevels["Doc Block3"]=[5,2]
    AbilityLevels["Doc Block4"]=[5,3]
    AbilityLevels["Alright Guys1"]=[7,1]
    AbilityLevels["Alright Guys2"]=[7,2]
    AbilityLevels["Alright Guys3"]=[7,2]
    AbilityLevels["Alright Guys4"]=[6,2]
    AbilityLevels["Carrot Stick1"]=[14,60]
    AbilityLevels["Carrot Stick2"]=[14,70]
    AbilityLevels["Carrot Stick3"]=[13,70]
    AbilityLevels["Carrot Stick4"]=[13,70]
    AbilityLevels["German Efficency1"]=[12,50]
    AbilityLevels["German Efficency2"]=[12,60]
    AbilityLevels["German Efficency3"]=[12,70]
    AbilityLevels["German Efficency4"]=[11,70]
    AbilityLevels["Witch Farm1"]=[7,1]
    AbilityLevels["Witch Farm2"]=[7,1.5]
    AbilityLevels["Witch Farm3"]=[7,1.5]
    AbilityLevels["Witch Farm4"]=[6,1.5]
    AbilityLevels["Villager Farm1"]=[7,1.5]
    AbilityLevels["Villager Farm2"]=[7,2]
    AbilityLevels["Villager Farm3"]=[7,2]
    AbilityLevels["Villager Farm4"]=[6,2]
    AbilityLevels["Nerfed1"]=[13,70]
    AbilityLevels["Nerfed2"]=[13,60]
    AbilityLevels["Nerfed3"]=[12,60]
    AbilityLevels["Nerfed4"]=[12,50]
    AbilityLevels["Breaking Bedrock1"]=[15,1]
    AbilityLevels["Breaking Bedrock2"]=[14,1]
    AbilityLevels["Breaking Bedrock3"]=[14,2]
    AbilityLevels["Breaking Bedrock4"]=[13,2]
    ## Ethos Abilities ##
    AbilityLevels["Get Snacks1"]=[8,60]
    AbilityLevels["Get Snacks2"]=[7,60]
    AbilityLevels["Get Snacks3"]=[7,70]
    AbilityLevels["Get Snacks4"]=[7,75]
    AbilityLevels["Redstone1"]=[6,4]
    AbilityLevels["Redstone2"]=[6,3]
    AbilityLevels["Redstone3"]=[5,3]
    AbilityLevels["Redstone4"]=[5,2]
    AbilityLevels["Broken Clay1"]=[6,0]
    AbilityLevels["Broken Clay2"]=[6,1]
    AbilityLevels["Broken Clay3"]=[5,1]
    AbilityLevels["Broken Clay4"]=[5,2]
    AbilityLevels["UHC Kill1"]=[7,4]
    AbilityLevels["UHC Kill2"]=[7,5]
    AbilityLevels["UHC Kill3"]=[6,5]
    AbilityLevels["UHC Kill4"]=[6,6]
    AbilityLevels["General Spaz1"]=[9,60]
    AbilityLevels["General Spaz2"]=[9,65]
    AbilityLevels["General Spaz3"]=[8,65]
    AbilityLevels["General Spaz4"]=[8,70]
    AbilityLevels["BREACH!1"]=[10,40]
    AbilityLevels["BREACH!2"]=[10,50]
    AbilityLevels["BREACH!3"]=[9,50]
    AbilityLevels["BREACH!4"]=[9,60]
    AbilityLevels["Anvil Drop1"]=[10,25]
    AbilityLevels["Anvil Drop2"]=[10,30]
    AbilityLevels["Anvil Drop3"]=[9,35]
    AbilityLevels["Anvil Drop4"]=[9,40]
    AbilityLevels["Death Games1"]=[7,5]
    AbilityLevels["Death Games2"]=[7,6]
    AbilityLevels["Death Games3"]=[6,6]
    AbilityLevels["Death Games4"]=[6,7]
    ## Sethbling Abilities ##
    AbilityLevels["Sockem1"]=[7]
    AbilityLevels["Sockem2"]=[7]
    AbilityLevels["Sockem3"]=[6]
    AbilityLevels["Sockem4"]=[6]
    AbilityLevels["Health Pack1"]=[8,0.5]
    AbilityLevels["Health Pack2"]=[7,1]
    AbilityLevels["Health Pack3"]=[7,1]
    AbilityLevels["Health Pack4"]=[7,2]
    AbilityLevels["Cloud Glitch1"]=[10,8]
    AbilityLevels["Cloud Glitch2"]=[9,8]
    AbilityLevels["Cloud Glitch3"]=[9,4]
    AbilityLevels["Cloud Glitch4"]=[8,4]
    AbilityLevels["Zombie Raid1"]=[7,80]
    AbilityLevels["Zombie Raid2"]=[7,90]
    AbilityLevels["Zombie Raid3"]=[6,90]
    AbilityLevels["Zombie Raid4"]=[6,100]
    AbilityLevels["Redstone Challenge1"]=[6,4]
    AbilityLevels["Redstone Challenge2"]=[6,5]
    AbilityLevels["Redstone Challenge3"]=[6,6]
    AbilityLevels["Redstone Challenge4"]=[5,6]
    AbilityLevels["Explosive Mine1"]=[6,50]
    AbilityLevels["Explosive Mine2"]=[6,60]
    AbilityLevels["Explosive Mine3"]=[6,70]
    AbilityLevels["Explosive Mine4"]=[5,80]
    AbilityLevels["Detnator1"]=[12]
    AbilityLevels["Detnator2"]=[11]
    AbilityLevels["Detnator3"]=[11]
    AbilityLevels["Detnator4"]=[10]
    AbilityLevels["Lightning Missile1"]=[9,5]
    AbilityLevels["Lightning Missile2"]=[9,6]
    AbilityLevels["Lightning Missile3"]=[8,6]
    AbilityLevels["Lightning Missile4"]=[8,7]
    ## Vechs Abilities ##
    AbilityLevels["White Wool1"]=[6]
    AbilityLevels["White Wool2"]=[6]
    AbilityLevels["White Wool3"]=[5]
    AbilityLevels["White Wool4"]=[5]
    AbilityLevels["Lime Wool1"]=[7,6]
    AbilityLevels["Lime Wool2"]=[7,7]
    AbilityLevels["Lime Wool3"]=[6,7]
    AbilityLevels["Lime Wool4"]=[6,8]
    AbilityLevels["Pink Wool1"]=[12]
    AbilityLevels["Pink Wool2"]=[11]
    AbilityLevels["Pink Wool3"]=[11]
    AbilityLevels["Pink Wool4"]=[10]
    AbilityLevels["Grey Wool1"]=[13]
    AbilityLevels["Grey Wool2"]=[12]
    AbilityLevels["Grey Wool3"]=[12]
    AbilityLevels["Grey Wool4"]=[11]
    AbilityLevels["Brown Wool1"]=[9,1]
    AbilityLevels["Brown Wool2"]=[9,2]
    AbilityLevels["Brown Wool3"]=[8,2]
    AbilityLevels["Brown Wool4"]=[8,3]
    AbilityLevels["Red Wool1"]=[7,4]
    AbilityLevels["Red Wool2"]=[7,5]
    AbilityLevels["Red Wool3"]=[6,5]
    AbilityLevels["Red Wool4"]=[6,6]
    AbilityLevels["Black Wool1"]=[7,5]
    AbilityLevels["Black Wool2"]=[6,5]
    AbilityLevels["Black Wool3"]=[6,5]
    AbilityLevels["Black Wool4"]=[6,6]
    AbilityLevels["Victory Monument1"]=[11,70]
    AbilityLevels["Victory Monument2"]=[10,70]
    AbilityLevels["Victory Monument3"]=[10,80]
    AbilityLevels["Victory Monument4"]=[10,85]
    @staticmethod
    def Description(ability,user):
        ret=["","","",""]
        ## Guudes Abilities ##
        if ability=="Spider Eyes":
            stats=abilities.AbilityLevels["Spider Eyes"+str(user.abilitylevel[1])]
            ret[0]="Sets an allies ability cooldowns to 0,"
            ret[1]="but has a "+`stats[1]`+"% chance of posioning Guude."
        if ability=="Contagious Laugh":
            stats=abilities.AbilityLevels["Contagious Laugh"+str(user.abilitylevel[0])]
            ret[0]="Paralyzes an enemy for "+`stats[1]`+" turns with"
            ret[1]="a "+`stats[2]`+"% chance of missing."
        if ability=="Boulderfist":
            stats=abilities.AbilityLevels["Boulderfist"+str(user.abilitylevel[2])]
            ret[0]="Attack with a crushing rock, slowing the "
            ret[1]="enemy for "+`stats[1]`+" turns"
        if ability=="Service Bat":
            stats=abilities.AbilityLevels["Service Bat"+str(user.abilitylevel[3])]
            ret[0]="A Secret Service Bat acts as a shield,"
            ret[1]="Taking 1/"+`stats[1]`+" damage of your max HP, with"
            ret[2]="a "+`stats[2]`+"% accuracy."
        if ability=="Controversy":
            ret[0]="Gives Guude the status Aggro for 6 turns."
        if ability=="Never Nude":
            ret[0]="Gives Guude a random, positive status."
        if ability=="Golden Throw":
            stats=abilities.AbilityLevels["Golden Throw"+str(user.abilitylevel[6])]
            ret[0]="Does damage "+`stats[1]`+" times the opponents level."
        if ability=="All Alone":
            stats=abilities.AbilityLevels["All Alone"+str(user.abilitylevel[7])]
            ret[0]="Takes "+`stats[1]`+"HP from all allies to deal"
            ret[1]=`stats[2]`+" damage to an enemy."
        ## Omgchads Abilities ##
        if ability=="Newcomer":
            stats=abilities.AbilityLevels["Newcomer"+str(user.abilitylevel[0])]
            ret[0]="Hit for double damage with a "+`stats[1]`+"% accuracy."
        if ability=="Waffles Claw":
            stats=abilities.AbilityLevels["Waffles Claw"+str(user.abilitylevel[1])]
            ret[0]="Hits all enemies once."
        if ability=="Collab":
            stats=abilities.AbilityLevels["Collab"+str(user.abilitylevel[2])]
            ret[0]="Allows Chad to use an allies ability."
        if ability=="Recap":
            stats=abilities.AbilityLevels["Recap"+str(user.abilitylevel[3])]
            ret[0]="Copy an opponents status, and steals it"
            ret[1]="from them."
        if ability=="Magic Trick":
            ret[0]="Perform a magic trick, having several "
            ret[1]="possible effects."
        if ability=="Dyslexia":
            ret[0]="Hits a random foe, but 3 times as hard."
        if ability=="Fiery Hair":
            stats=abilities.AbilityLevels["Fiery Hair"+str(user.abilitylevel[6])]
            ret[0]="Has a "+`stats[1]`+"% chance of burning for each "
            ret[1]="opponent."
        if ability=="Optimism":
            stats=abilities.AbilityLevels["Optimism"+str(user.abilitylevel[7])]
            ret[0]="Has a "+`stats[1]`+"% chance of fully healing and a "
            ret[1]=`stats[1]`+"% chance of encouraging for each ally."
        ## Pyros Abilities ##
        if ability=="Tackle":
            ret[0]="Hit for double damage."
        if ability=="Imperssionate":
            ret[0]="Allows you to use an allies ability."
        if ability=="Green Shell":
            stats=abilities.AbilityLevels["Green Shell"+str(user.abilitylevel[2])]
            ret[0]="Does 1/4 of an enemies HP with a "
            ret[1]=`stats[1]`+"% accuracy."
        if ability=="Game Theory":
            stats=abilities.AbilityLevels["Game Theory"+str(user.abilitylevel[3])]
            ret[0]="Fully heal yourself, while dealing"
            ret[1]="1/"+`stats[1]`+" of the HP you were healed to an"
            ret[2]="enemy. "+`stats[2]`+"% accuaracy."
        if ability=="Meditate":
            stats=abilities.AbilityLevels["Meditate"+str(user.abilitylevel[4])]
            ret[0]="Gain between "+`stats[1]`+"-"+`stats[1]+2`+" PP."
        if ability=="360 No Scope":
            stats=abilities.AbilityLevels["360 No Scope"+str(user.abilitylevel[5])]
            ret[0]="Normal attack, low accuracy at "+`stats[1]`+"% but"
            ret[1]="encourages."
        if ability=="Triforce":
            stats=abilities.AbilityLevels["Triforce"+str(user.abilitylevel[6])]
            ret[0]="Has a "+`stats[1]`+"% chance of giving Attack +"
            ret[1]="for each ally."
        if ability=="Final Smash":
            stats=abilities.AbilityLevels["Final Smash"+str(user.abilitylevel[7])]
            ret[0]="Do "+`stats[1]`+" damage to all enemies."
        ## Millbees Abilities ##
        if ability=="Chocolate Knees":
            ret[0]="Fully heal an ally, but take 1/4 of the HP"
            ret[1]="as damage."
        if ability=="Orange Wool":
            stats=abilities.AbilityLevels["Orange Wool"+str(user.abilitylevel[1])]
            ret[0]="Fully heal yourself, but paralyze yourself"
            ret[1]="For "+`stats[1]`+" turns."
        if ability=="Rainbow Explosion":
            ret[0]="Hits all opponents once."
        if ability=="Dadbee Aid":
            ret[0]="Normal attack, if enemy HP is higher, does"
            ret[1]="4 times the damage."
        if ability=="Free Millbee":
            stats=abilities.AbilityLevels["Free Millbee"+str(user.abilitylevel[4])]
            ret[0]="Get fully healed and encouraged with"
            ret[1]=`stats[1]`+"% accuracy."
        if ability=="Date Through":
            ret[0]="Does more damage the higher Millbee's"
            ret[1]="confidence, all enemies hidden aggro maxed."
        if ability=="Randomness":
            ret[0]="Gives Millbee a random status."
        if ability=="Summon Melon":
            stats=abilities.AbilityLevels["Summon Melon"+str(user.abilitylevel[7])]
            ret[0]="Heals all allies "+`stats[1]`+" HP."
        ## Aureylians Abilities ##
        if ability=="Pink Enchant":
            stats=abilities.AbilityLevels["Pink Enchant"+str(user.abilitylevel[0])]
            ret[0]="Fully heals a random ally with"
            ret[1]=`stats[1]`+"% accuracy."
        if ability=="RUDE!":
            stats=abilities.AbilityLevels["RUDE!"+str(user.abilitylevel[1])]
            ret[0]="Has a "+`stats[1]`+"% chance of clearing"
            ret[1]="enemy statuses."
        if ability=="Compliment":
            ret[0]="Encourages an ally."
        if ability=="Lullaby":
            stats=abilities.AbilityLevels["Lullaby"+str(user.abilitylevel[3])]
            ret[0]="Puts an enemy to sleep for"
            ret[1]=`stats[1]`+" turns."
        if ability=="Sparkle":
            ret[0]="Heals all allies 1/2 health."
        if ability=="Glitter":
            ret[0]="Fully heals an ally of choice."
        if ability=="Christmas":
            stats=abilities.AbilityLevels["Christmas"+str(user.abilitylevel[6])]
            ret[0]="Hits an enemy 1-25 times with a"
            ret[1]=`stats[1]`+"% chance each hit."
        if ability=="Rainbow Swirl":
            stats=abilities.AbilityLevels["Rainbow Swirl"+str(user.abilitylevel[7])]
            ret[0]="Heals all allies "+`stats[1]`+"-7/7 health."
        ## Docms Abilities ##
        if ability=="Doc Block":
            stats=abilities.AbilityLevels["Doc Block"+str(user.abilitylevel[0])]
            ret[0]="Inflicts confusion for "+`stats[1]`+" turns while "
            ret[1]="attacking."
        if ability=="Alright Guys":
            stats=abilities.AbilityLevels["Alright Guys"+str(user.abilitylevel[1])]
            ret[0]="Gives "+`stats[1]`+" PP to each party member."
        if ability=="Carrot Stick":
            stats=abilities.AbilityLevels["Carrot Stick"+str(user.abilitylevel[2])]
            ret[0]="Has a "+`stats[1]`+"% chance of setting an allies"
            ret[1]="ability cooldowns to 0."
        if ability=="German Efficency":
            stats=abilities.AbilityLevels["German Efficency"+str(user.abilitylevel[3])]
            ret[0]="Doubles the length of an allies current"
            ret[1]="status with "+`stats[1]`+"% accuracy."
        if ability=="Witch Farm":
            ret[0]="Inflicts posion on all enemies for"
            ret[1]="4 turns."
        if ability=="Villager Farm":
            ret[0]="Lags enemies, inflicting posion on"
            ret[1]="all enemies for 4 turns."
        if ability=="Nerfed":
            stats=abilities.AbilityLevels["Nerfed"+str(user.abilitylevel[6])]
            ret[0]="Gives Attack + to all allies with a"
            ret[1]=`stats[1]`+"% chance of lowering your"
            ret[2]="attack."
        if ability=="Breaking Bedrock":
            stats=abilities.AbilityLevels["Breaking Bedrock"+str(user.abilitylevel[7])]
            ret[0]="Has a "+`stats[1]`+"% chance of OHKOing an enemy."
        ## Etho's Abilities ##
        if ability=="Get Snacks":
            stats=abilities.AbilityLevels["Get Snacks"+str(user.abilitylevel[0])]
            ret[0]="Has a "+`stats[1]`+"% chance of encouraging all"
            ret[1]="allies."
        if ability=="Redstone":
            ret[0]="Does more damage the longer a status"
            ret[1]="you currently have."
        if ability=="Broken Clay":
            stats=abilities.AbilityLevels["Broken Clay"+str(user.abilitylevel[2])]
            ret[0]="Hits "+`stats[1]`+"-4 times."
        if ability=="UHC Kill":
            stats=abilities.AbilityLevels["UHC Kill"+str(user.abilitylevel[3])]
            ret[0]="Hits and gives you regen for "+`stats[1]`+" turns."
        if ability=="General Spaz":
            stats=abilities.AbilityLevels["General Spaz"+str(user.abilitylevel[4])]
            ret[0]="Hits all opponents 1-3 times with "+`stats[1]`+"%"
            ret[1]="accuracy."
        if ability=="BREACH!":
            ret[0]="Huge EXPLOSION! May back fire and hit"
            ret[1]="yourself."
        if ability=="Anvil Drop":
            ret[0]="Massive damage, high chance of missing."
        if ability=="Death Games":
            stats=abilities.AbilityLevels["Death Games"+str(user.abilitylevel[7])]
            ret[0]="Hits and gives enemy posion for "+`stats[1]`+" turns."
        ## Sethbling Abilities ##
        if ability=="Sockem":
            ret[0]="Hits 1-4 times."
        if ability=="Health Pack":
            stats=abilities.AbilityLevels["Health Pack"+str(user.abilitylevel[1])]
            ret[0]="Heals ally level times "+`stats[1]`+" HP."
        if ability=="Cloud Glitch":
            ret[0]="Summons a cloud to act as a shield for an"
            ret[1]="ally."
        if ability=="Zombie Raid":
            stats=abilities.AbilityLevels["Cloud Glitch"+str(user.abilitylevel[3])]
            ret[0]="Has a "+`stats[1]`+"% chance of hitting all enemies."
        if ability=="Redstone Challenge":
            stats=abilities.AbilityLevels["Redstone Challenge"+str(user.abilitylevel[4])]
            ret[0]="Paralyzes an enemy for "+`stats[1]`+" turns."
        if ability=="Explosive Mine":
            stats=abilities.AbilityLevels["Explosive Mine"+str(user.abilitylevel[5])]
            ret[0]="Activated with detnator to do "+`stats[1]`+" damage"
            ret[1]="to each enemy. Stacks."
        if ability=="Detnator":
            ret[0]="Activates all mines layed by Sethbling."
        if ability=="Lightning Missile":
            stats=abilities.AbilityLevels["Lightning Missile"+str(user.abilitylevel[7])]
            ret[0]="Always hits, gives you precision for "+`stats[1]`+" turns."
        ## Vechs Abilities ##
        if ability=="White Wool":
            stats=abilities.AbilityLevels["White Wool"+str(user.abilitylevel[0])]
            ret[0]="Heals 1/4 of an allies HP."
        if ability=="Lime Wool":
            stats=abilities.AbilityLevels["Lime Wool"+str(user.abilitylevel[1])]
            ret[0]="Posions enemy for "+`stats[1]`+" turns."
        if ability=="Pink Wool":
            stats=abilities.AbilityLevels["Pink Wool"+str(user.abilitylevel[2])]
            ret[0]="Maxes all allies and your own confidence."
        if ability=="Grey Wool":
            stats=abilities.AbilityLevels["Grey Wool"+str(user.abilitylevel[3])]
            ret[0]="Clears all enemy statuses."
        if ability=="Brown Wool":
            stats=abilities.AbilityLevels["Brown Wool"+str(user.abilitylevel[4])]
            ret[0]="Gives an ally "+`stats[1]`+" PP."
        if ability=="Red Wool":
            stats=abilities.AbilityLevels["Red Wool"+str(user.abilitylevel[5])]
            ret[0]="Burns an enemy for "+`stats[1]`+" turns."
        if ability=="Black Wool":
            stats=abilities.AbilityLevels["Black Wool"+str(user.abilitylevel[6])]
            ret[0]="Withers an enemy for "+`stats[1]`+" turns."
        if ability=="Victory Monument":
            stats=abilities.AbilityLevels["Victory Monument"+str(user.abilitylevel[7])]
            ret[0]="Raises all allies speed with "+`stats[1]`+"%"
            ret[1]="accuracy."
        return ret
    @staticmethod
    def Run(user,ability,members,enemy,target,type="member"):
        if ability=="Regen":
            members[user].pp=members[user].pp-3
            members[target].status=["regen",5,1]
            BattleText.list.append(BattleText(type+str(target),"Regen"))
        if ability=="Heal":
            BattleText.list.append(BattleText(type+str(target),"+"+str(int(members[target].hp/4.0))+" HP"))
            members[user].pp=members[user].pp-3
            if members[target].currenthp>0:
                members[target].currenthp=members[target].currenthp+int(members[target].hp/4.0)
            if members[target].currenthp>members[target].hp:
                members[target].currenthp=members[target].hp
        if ability=="Evade +":
            members[user].pp=members[user].pp-3
            members[target].status=["evade +",6,1]
            BattleText.list.append(BattleText(type+str(target),"Evade +"))
        if ability=="Shield":
            members[user].pp=members[user].pp-3
            if members[target].status[0]=="shield":
                members[target].status=["shield",members[target].status[1]+int(members[target].hp/4),1]
            else:
                members[target].status=["shield",int(members[target].hp/4),1]
            BattleText.list.append(BattleText(type+str(target),"Shielded"))
        if ability=="Aggro":
            members[user].pp=members[user].pp-3
            members[target].status=["aggro",6,1]
            BattleText.list.append(BattleText(type+str(target),"Aggro"))
        if ability=="Fast":
            members[user].pp=members[user].pp-3
            members[target].status=["fast",6,1]
            BattleText.list.append(BattleText(type+str(target),"Fast"))
        if ability=="Attack +":
            members[user].pp=members[user].pp-3
            members[target].status=["attack +",6,1]
            BattleText.list.append(BattleText(type+str(target),"Attack +"))
        if ability=="Encourage":
            members[user].pp=members[user].pp-3
            members[target].status=["encouraged",6,1]
            BattleText.list.append(BattleText(type+str(target),"Encouraged"))
        if ability=="Revive":
            if random.randint(0,100)<20:
                members[target].currenthp=1
                members[target].status=["none",0]
                self.pp=self.pp-3
                BattleText.list.append(BattleText(type+str(target),"Revived"))
            else:
                BattleText.list.append(BattleText(type+str(target),"Failed"))
        ## Guudes Abilities ##
        if ability=="Spider Eyes":
            stats=abilities.AbilityLevels["Spider Eyes"+str(members[user].abilitylevel[1])]
            if random.randint(1,100)<stats[1]:
                members[user].status=["posion",5,1]
                BattleText.list.append(BattleText("member"+str(user),"Posioned",28))
            for i in range(0,3):
                if members[target].battleabilities[i]!="Spider Eyes" and members[target].battleabilities[i]!="None":
                    members[target].abilitiescool[i]=0
                elif members[target].battleabilities[i]=="none":
                    members[target].abilitiescool[i]="X"
            BattleText.list.append(BattleText("member"+str(target),"Cooldowns=0"))
        if ability=="Contagious Laugh":
            stats=abilities.AbilityLevels["Contagious Laugh"+str(members[user].abilitylevel[0])]
            if random.randint(0,100)<stats[2]:
                BattleText.list.append(BattleText("enemy"+str(target),"Paralyzed"))
                enemy[target].status=["paralyzed",stats[1],1]
            else:
                BattleText.list.append(BattleText("enemy"+str(target),"Failed"))
        if ability=="Boulderfist":
            stats=abilities.AbilityLevels["Boulderfist"+str(members[user].abilitylevel[2])]
            members[user].Attack(enemy[target],target)
            BattleText.list.append(BattleText("enemy"+str(target),"Slowed",28))
            enemy[target].status=["slow",stats[1],1.5]
        if ability=="Service Bat":
            stats=abilities.AbilityLevels["Service Bat"+str(members[user].abilitylevel[3])]
            for i in range(0,3):
                if random.randint(0,100)<stats[2]:
                    if members[i].status[0]=="shield":
                        members[i].status[1]=members[i].status[1]+int(members[i].hp/stats[1])
                    else:
                        members[i].status=["shield",int(members[i].hp/stats[1]),1]
                    BattleText.list.append(BattleText("member"+str(i),"Shielded",28))
                else:
                    BattleText.list.append(BattleText("member"+str(i),"Failed"))
        if ability=="Controversy":
            if random.randint(0,100)<90:
                members[user].status=["aggro",6,1]
                BattleText.list.append(BattleText("member"+str(user),"Aggro +"))
            else:
                BattleText.list.append(BattleText("member"+str(user),"Failed"))
        if ability=="Never Nude":
            status=["precision","fast","attack +","regen","encouraged"]
            amount=[0,30,50,80,90,999]
            stats=abilities.AbilityLevels["Never Nude"+str(members[user].abilitylevel[5])]
            level=random.randint(stats[1],100)
            for i in range(0,5):
                if level>amount[i]:
                    members[target].status=[status[i],5,1.5]
                    if i==4:
                        members[target].status[2]=1
                    if level<amount[i+1]:
                        BattleText.list.append(BattleText("member"+str(target),status[i].title()))
        if ability=="Golden Throw":
            stats=abilities.AbilityLevels["Golden Throw"+str(members[user].abilitylevel[6])]
            members[user].DoDamage(enemy[target].lvl*(stats[1]+round(random.random(),1)),enemy[target],target)
        if ability=="All Alone":
            stats=abilities.AbilityLevels["All Alone"+str(members[user].abilitylevel[7])]
            for i in range(0,3):
                if i!=user:
                    members[i].TakeDamage(stats[1],i,False,False)
            members[user].DoDamage(stats[2],enemy[target],target)
        ## Chads Abilities ##
        if ability=="Newcomer":
            stats=abilities.AbilityLevels["Newcomer"+str(members[user].abilitylevel[0])]
            if random.randint(0,100)<stats[1]:
                members[user].Attack(enemy[target],target,2)
            else:
                BattleText.list.append(BattleText("enemy"+str(target),"Failed"))
        if ability=="Waffles Claw":
            for i in range(0,len(enemy)):
                if enemy[i]!="none":
                    members[user].Attack(enemy[i],i)
        if ability=="Recap":
            members[user].status=enemy[target].status
            enemy[target].status=["none",0]
            BattleText.list.append(BattleText("member"+str(user),members[user].status[0].title()))
        if ability=="Magic Trick":
            stats=abilities.AbilityLevels["Magic Trick"+str(members[user].abilitylevel[4])]
            chance=random.randint(0,100)
            chance=chance+stats[1]
            if chance<30:
                enemy[target].status=["confused",10,1]
                BattleText.list.append(BattleText("enemy"+str(target),"Confused"))
            elif chance<60:
                enemy[target].status=["paralyzed",7,1]
                BattleText.list.append(BattleText("enemy"+str(target),"Paralyzed"))
            elif chance<90:
                members[user].status=["encouraged",6,1]
                BattleText.list.append(BattleText("member"+str(user),"Encouraged"))
            else:
                enemy[target].currenthp=int(enemy[target].currenthp/2)
                BattleText.list.append(BattleText("enemy"+str(target),"Sawed In Half"))
        if ability=="Dyslexia":
            run=True
            while run:
                rand=random.randint(0,4)
                if enemy[rand]!="none":
                    members[user].Attack(enemy[rand],rand,3)
                    run=False
        if ability=="Fiery Hair":
            stats=abilities.AbilityLevels["Fiery Hair"+str(members[user].abilitylevel[6])]
            for i in range(0,5):
                if enemy[i]!="none":
                    if random.randint(0,100)<stats[1]:
                        enemy[i].status=["fire",7,1]
                        BattleText.list.append(BattleText("enemy"+str(i),"Burned"))
                    else:
                        BattleText.list.append(BattleText("enemy"+str(i),"Failed"))
        if ability=="Optimism":
            stats=abilities.AbilityLevels["Fiery Hair"+str(members[user].abilitylevel[7])]
            for i in range(0,3):
                if members[i].currenthp!=0:
                    if random.randint(1,100)<stats[1]:
                        members[i].currenthp=members[i].hp
                        BattleText.list.append(BattleText("member"+str(i),"Healed"))
                    else:
                        BattleText.list.append(BattleText("member"+str(i),"Failed"))
                    if random.randint(1,100)<stats[1]:
                        members[i].status=["encouraged",8,1]
                        BattleText.list.append(BattleText("member"+str(i),"Encouraged",28))
                    else:
                        BattleText.list.append(BattleText("member"+str(i),"Failed",28))
        ## Pyros Abilities ##
        if ability=="Tackle":
            members[user].Attack(enemy[target],target,2)
        if ability=="Green Shell":
            stats=abilities.AbilityLevels["Green Shell"+str(members[user].abilitylevel[2])]
            if random.randint(0,100)<stats[1]:
                damage=int(enemy[target].currenthp/4)
                members[user].DoDamage(damage,enemy[target],target)
            else:
                BattleText.list.append(BattleText("enemy"+str(target),"Failed"))
        if ability=="Game Theory":
            stats=abilities.AbilityLevels["Game Theory"+str(members[user].abilitylevel[3])]
            if stats[2]>random.randint(0,100):
                damage=int(((members[user].hp-(members[user].currenthp))/stats[1]))
                members[user].currenthp=members[user].hp
                members[user].DoDamage(damage,enemy[target],target)
            else:
                BattleText.list.append(BattleText("enemy"+str(target),"Failed"))
        if ability=="Meditate":
            stats=abilities.AbilityLevels["Meditate"+str(members[user].abilitylevel[4])]
            gain=random.randint(0,2)+stats[1]
            members[user].pp=members[user].pp+gain
            BattleText.list.append(BattleText("member"+str(user),"+"+str(gain)+" PP"))
        if ability=="360 No Scope":
            stats=abilities.AbilityLevels["360 No Scope"+str(members[user].abilitylevel[5])]
            if random.randint(0,100)<stats[1]:
                members[user].status=["precision",6,1]
                members[user].Attack(enemy[target],target,1)
                members[user].status=["encouraged",6,1]
                BattleText.list.append(BattleText("member"+str(user),"Montage Clip",28))
            else:
                BattleText.list.append(BattleText("enemy"+str(target),"Failed"))  
        if ability=="Triforce":
            stats=abilities.AbilityLevels["Triforce"+str(members[user].abilitylevel[6])]
            for i in range(0,3):
                if random.randint(0,100)<stats[1]:
                    members[i].status=["attack +",5,1]
                    BattleText.list.append(BattleText("member"+str(i),"Attack +"))
                else:
                    BattleText.list.append(BattleText("member"+str(i),"Failed"))
        if ability=="Final Smash":
            stats=abilities.AbilityLevels["Final Smash"+str(members[user].abilitylevel[7])]
            for i in range(0,len(enemy)):
                if enemy[i]!="none":
                    members[user].DoDamage(stats[1],enemy[i],i)
        ## Millbees Abilities ##
        if ability=="Chocolate Knees":
            hp=(members[target].hp-members[target].currenthp)/4
            if members[target].currenthp>0:
                members[target].currenthp=members[target].hp
                members[user].currenthp=members[user].currenthp-hp
        if ability=="Orange Wool":
            stats=abilities.AbilityLevels["Orange Wool"+str(members[user].abilitylevel[1])]
            members[user].currenthp=members[user].hp
            members[user].status=["paralyzed",stats[1],1]
            BattleText.list.append(BattleText("member"+str(user),"Paralyzed"))
            BattleText.list.append(BattleText("member"+str(user),"Healed",28))
        if ability=="Rainbow Explosion":
            for i in range(0,len(enemy)):
                if enemy[i]!="none":
                    members[user].Attack(enemy[i],i)
        if ability=="Dadbee Aid":
            if enemy[target].currenthp>members[user].currenthp:
                members[user].Attack(enemy[target],target,4)
            else:
                members[user].Attack(enemy[target],target)
        if ability=="Free Millbee":
            stats=abilities.AbilityLevels["Free Millbee"+str(members[user].abilitylevel[4])]
            if random.randint(0,100)<stats[1]:
                BattleText.list.append(BattleText("member"+str(user),"Encouraged"))
                BattleText.list.append(BattleText("member"+str(user),"Healed",28))
                members[user].status=["encouraged",3,1]
                members[user].currenthp=members[user].hp
            else:
                BattleText.list.append(BattleText("member"+str(user),"Failed"))
        if ability=="Date Through":
            stats=abilities.AbilityLevels["Date Through"+str(members[user].abilitylevel[5])]
            stats[1]=stats[1]*(abs(members[user].confidence-100)/100.0)
            members[user].Attack(enemy[target],target,stats[1])
            for i in range(0,len(enemy)):
                if enemy[i]!="none":
                    enemy[i].aggro[user]=9999
        if ability=="Randomness":
            stats=abilities.AbilityLevels["Randomness"+str(members[user].abilitylevel[6])]
            if stats[1]==1:
                members[user].status=["encouraged",4,1]
                BattleText.list.append(BattleText("member"+str(user),"Encouraged")) 
            if stats[1]==2:
                members[user].status=["aggro",4,1]
                BattleText.list.append(BattleText("member"+str(user),"Aggro"))
            if stats[1]==3:
                members[user].status=["regen",4,1]
                BattleText.list.append(BattleText("member"+str(user),"Regen"))
            if stats[1]==4:
                members[user].status=["evade +",4,1]
                BattleText.list.append(BattleText("member"+str(user),"Evade +"))
        if ability=="Summon Melon":
            stats=abilities.AbilityLevels["Summon Melon"+str(members[user].abilitylevel[7])]
            for i in range(0,3):
                if members[i].currenthp>0:
                    members[i].currenthp=members[i].currenthp+stats[1]
                    BattleText.list.append(BattleText("member"+str(i),"+"+`stats[1]`+" HP"))
                if members[i].currenthp>members[i].hp:
                    members[i].currenthp=members[i].hp
        ## Aureys Abilities ##
        if ability=="Pink Enchant":
            stats=abilities.AbilityLevels["Pink Enchant"+str(members[user].abilitylevel[0])]
            if random.randint(0,100)<stats[1]:
                choice=random.randint(0,2)
                if members[choice].currenthp!=0:
                    members[choice].currenthp=members[choice].hp
                    BattleText.list.append(BattleText("member"+str(choice),"Fully Healed"))
            else:
                BattleText.list.append(BattleText("member"+str(user),"Failed"))
        if ability=="RUDE!":
            stats=abilities.AbilityLevels["RUDE!"+str(members[user].abilitylevel[1])]
            if random.randint(0,100)<stats[1]:
                for i in range(0,len(enemy)):
                    if enemy[i]!="none":
                        enemy[i].status=["none",0,0]
                        BattleText.list.append(BattleText("enemy"+str(i),"Cleared"))
            else:
                BattleText.list.append(BattleText("member"+str(user),"Failed"))
        if ability=="Compliment":
            members[target].status=["encouraged",8,0]
            BattleText.list.append(BattleText("member"+str(target),"Encouraged"))
        if ability=="Lullaby":
            stats=abilities.AbilityLevels["Lullaby"+str(members[user].abilitylevel[3])]
            enemy[target].status=["sleep",stats[1],0]
            BattleText.list.append(BattleText("enemy"+str(target),"Asleep"))
        if ability=="Sparkle":
            for i in range(0,3):
                if members[i].currenthp!=0:
                    members[i].currenthp=members[i].currenthp+int(members[i].hp/2)
                    if members[i].currenthp>members[i].hp:
                        members[i].currenthp=members[i].hp
                        BattleText.list.append(BattleText("member"+str(i),"Healed"))
        if ability=="Glitter":
            if members[target].currenthp!=0:
                members[target].currenthp=members[target].hp
                BattleText.list.append(BattleText("member"+str(target),"Fully Healed"))
        if ability=="Christmas":
            stats=abilities.AbilityLevels["Christmas"+str(members[user].abilitylevel[6])]
            chance=stats[1]
            damage=1
            run=True
            while run:
                if chance<random.randint(0,100):
                    damage=damage+1
                    chance=chance-1
                else:
                    run=False
            if damage>25:
                damage=25
            members[user].Attack(enemy[target],target,damage)
            BattleText.list.append(BattleText("enemy"+str(target),"      x"+str(damage)))
        if ability=="Rainbow Swirl":
            stats=abilities.AbilityLevels["Rainbow Swirl"+str(members[user].abilitylevel[7])]
            for i in range(0,3):
                if members[i].cuurenthp!=0:
                    heal=int((members[i].hp/7)*random.randint(stats[1],7))
                    members[i].currenthp=members[i].currenthp+heal
                    if members[i].currenthp>members[i].hp:
                        members[i].currenthp=members[i].hp
                    BattleText.list.append(BattleText("member"+str(i),"+"+str(heal)+" HP"))
        ## Docms Abilities ##
        if ability=="Doc Block":
            stats=abilities.AbilityLevels["Doc Block"+str(members[user].abilitylevel[0])]
            enemy[target].status=["confused",stats[1],1]
            members[user].Attack(enemy[target],target)
            BattleText.list.append(BattleText("enemy"+str(target),"Confused",24))
        if ability=="Alright Guys":
            stats=abilities.AbilityLevels["Alright Guys"+str(members[user].abilitylevel[1])]
            for i in range(0,3):
                members[i].pp=members[i].pp+stats[1]
                BattleText.list.append(BattleText("member"+str(i),"+"+`stats[1]`+" PP"))
        if ability=="Carrot Stick":
            stats=abilities.AbilityLevels["Carrot Stick"+str(members[user].abilitylevel[2])]
            if random.randint(0,100)<stats[1]:
                BattleText.list.append(BattleText("member"+str(target),"Cooldowns = 0"))
                for i in range(0,3):
                    if members[target].battleabilities[i]!="Carrot Stick" and members[target].battleabilities[i]!="None":
                        members[target].abilitiescool[i]=0
                    elif members[target].battleabilities[i]=="none":
                        members[target].abilitiescool[i]="X"
            else:
                BattleText.list.append(BattleText("member"+str(target),"Failed"))
        if ability=="German Efficency":
            stats=abilities.AbilityLevels["German Efficency"+str(members[user].abilitylevel[3])]
            try:
                members[target].status=[members[target].status[0],members[target].status[1]*2,members[target].status[2]]
            except:
                members[target].status=[members[target].status[0],members[target].status[1]*2]
            BattleText.list.append(BattleText("member"+str(target),"Doubled Status"))
        if ability=="Witch Farm":
            stats=abilities.AbilityLevels["Witch Farm"+str(members[user].abilitylevel[4])]
            for i in range(0,len(enemy)):
                if enemy[i]!="none":
                    if random.randint(2,10)!=10:
                        enemy[i].status=["posion",4,stats[1]]
                        BattleText.list.append(BattleText("enemy"+str(i),"Posioned"))
                    else:
                        BattleText.list.append(BattleText("enemy"+str(i),"Failed"))
        if ability=="Villager Farm":
            stats=abilities.AbilityLevels["Villager Farm"+str(members[user].abilitylevel[5])]
            for i in range(0,len(enemy)):
                if enemy[i]!="none":
                    if random.randint(2,10)!=10:
                        enemy[i].status=["slow",4,stats[1]]
                        BattleText.list.append(BattleText("enemy"+str(i),"Slowed"))
                    else:
                        BattleText.list.append(BattleText("enemy"+str(i),"Failed"))
        if ability=="Nerfed":
            stats=abilities.AbilityLevels["Nerfed"+str(members[user].abilitylevel[6])]
            for i in range(0,2):
                if i!=user:
                    members[i].status=["attack +",5,1]
                    BattleText.list.append(BattleText("member"+str(i),"Attack +"))
                else:
                    if random.randint(1,100)<stats[1]:
                        members[i].status=["attack -",5,0.5]
                        BattleText.list.append(BattleText("member"+str(i),"Attack -"))
        if ability=="Breaking Bedrock":
            stats=abilities.AbilityLevels["Breaking Bedrock"+str(members[user].abilitylevel[7])]
            if random.randint(1,100)<=stats[1]:
                BattleText.list.append(BattleText("enemy"+str(target),"OHKO!"))
                enemy[target].currenthp=0
            else:
                BattleText.list.append(BattleText("enemy"+str(target),"Failed"))
        ## Ethos Abilities ##
        if ability=="Get Snacks":
            stats=abilities.AbilityLevels["Get Snacks"+str(members[user].abilitylevel[0])]
            for i in range(0,3):
                if i!=user:
                    if random.randint(1,100)<stats[1]:
                        members[i].status=["encouraged",4,1]
                        BattleText.list.append(BattleText("member"+str(i),"Encouraged"))
                    else:
                        BattleText.list.append(BattleText("member"+str(i),"Failed"))
        if ability=="Redstone":
            stats=abilities.AbilityLevels["Redstone"+str(members[user].abilitylevel[1])]
            members[user].Attack(enemy[target],target,int(members[user].status[1]/stats[1]))
        if ability=="Broken Clay":
            stats=abilities.AbilityLevels["Broken Clay"+str(members[user].abilitylevel[2])]
            members[user].Attack(enemy[target],target,random.randint(stats[1],4))
        if ability=="UHC Kill":
            stats=abilities.AbilityLevels["UHC Kill"+str(members[user].abilitylevel[3])]
            members[user].Attack(enemy[target],target)
            members[user].status=["regen",stats[1],1]
            BattleText.list.append(BattleText("member"+str(user),"Regen",28))
        if ability=="General Spaz":
            stats=abilities.AbilityLevels["General Spaz"+str(members[user].abilitylevel[4])]
            for i in range(0,len(enemy)):
                if enemy[i]!="none":
                    if random.randint(1,100)<stats[1]:
                        members[user].Attack(enemy[i],i,random.randint(0,3))
                    else:
                        BattleText.list.append(BattleText("enemy"+str(i),"Failed"))
        if ability=="BREACH!":
            stats=abilities.AbilityLevels["BREACH!"+str(members[user].abilitylevel[5])]
            if random.randint(1,100)<stats[1]:
                members[user].Attack(enemy[target],target,4)
            else:
                members[user].TakeDamage((members[user].attack/10)*3,user)
        if ability=="Anvil Drop":
            stats=abilities.AbilityLevels["Anvil Drop"+str(members[user].abilitylevel[6])]
            if random.randint(1,100)<stats[1]:
                members[user].Attack(enemy[target],target,4)
            else:
                BattleText.list.append(BattleText("enemy"+str(target),"Missed"))
        if ability=="Death Games":
            stats=abilities.AbilityLevels["Death Games"+str(members[user].abilitylevel[7])]
            members[user].Attack(enemy[target],target)
            enemy[target].status=["posion",stats[1],1.5]
            BattleText.list.append(BattleText("enemy"+str(target),"Posioned",28))
        ## Sethblings Abilities ##
        if ability=="Sockem":
            run=True
            damage=1
            chance=50
            while run:
                if random.randint(0,100)<chance and damage!=4:
                    chance=int(chance/2)
                    damage=damage+1
                else:
                    run=False
            members[user].Attack(enemy[target],target,damage)
        if ability=="Health Pack":
            stats=abilities.AbilityLevels["Health Pack"+str(members[user].abilitylevel[1])]
            members[target].currenthp=members[target].currenthp+int(members[target].lvl*stats[1])
            BattleText.list.append(BattleText("member"+str(target),"+"+`int(members[target].lvl*stats[1])`+" HP"))
        if ability=="Cloud Glitch":
            stats=abilities.AbilityLevels["Cloud Glitch"+str(members[user].abilitylevel[2])]
            members[target].status=["shield",int(members[target].hp/stats[1]),1]
            BattleText.list.append(BattleText("member"+str(target),"Shielded"))
        if ability=="Zombie Raid":
            stats=abilities.AbilityLevels["Zombie Raid"+str(members[user].abilitylevel[3])]
            for i in range(0,len(enemy)):
                if enemy[i]!="none":
                    if random.randint(1,100)<stats[1]:
                        members[user].Attack(enemy[i],i)
                    else:
                        BattleText.list.append(BattleText("enemy"+str(i),"Missed"))
        if ability=="Redstone Challenge":
            stats=abilities.AbilityLevels["Redstone Challenge"+str(members[user].abilitylevel[4])]
            enemy[target].status=["paralyzed",stats[1],1]
            BattleText.list.append(BattleText("enemy"+str(target),"Paralyzed"))
        if ability=="Explosive Mine":
            stats=abilities.AbilityLevels["Explosive Mine"+str(members[user].abilitylevel[5])]
            Battle.mine=Battle.mine+1
            BattleText.list.append(BattleText("member"+str(user),"Mine Planted"))
        if ability=="Detnator":
            stats=abilities.AbilityLevels["Explosive Mine"+str(members[user].abilitylevel[6])]
            for i in range(0,len(enemy)):
                if enemy[i]!="none":
                    enemy[i].TakeDamage(stats[1]*Battle.mine,i)
            Battle.mine=0
        if ability=="Lightning Missile":
            stats=abilities.AbilityLevels["Death Games"+str(members[user].abilitylevel[7])]
            members[user].status=["precision",stats[1],1]
            members[user].Attack(enemy[target],target)
        ## Vechs Abilities ##
        if ability=="White Wool":
            if members[target].currenthp>0:
                members[target].currenthp=members[target].currenthp+members[target].hp/4
            if members[target].currenthp>members[target].hp:
                members[target].currenthp=members[target].hp
            BattleText.list.append(BattleText("member"+str(target),"+"+`members[target].hp/4`+" HP"))
        if ability=="Lime Wool":
            stats=abilities.AbilityLevels["Lime Wool"+str(members[user].abilitylevel[1])]
            if random.randint(1,100)<90:
                enemy[target].status=["posion",stats[1],1.5]
                BattleText.list.append(BattleText("enemy"+str(target),"Posioned"))
            else:
                BattleText.list.append(BattleText("enemy"+str(target),"Failed"))
        if ability=="Pink Wool":
            stats=abilities.AbilityLevels["Pink Wool"+str(members[user].abilitylevel[2])]
            for i in range(0,3):
                members[i].confidence=0
                BattleText.list.append(BattleText("member"+str(i),"Confidence Maxed"))
        if ability=="Grey Wool":
            stats=abilities.AbilityLevels["Grey Wool"+str(members[user].abilitylevel[3])]
            for i in range(0,3):
                members[i].status=["none",0]
                BattleText.list.append(BattleText("member"+str(i),"Status Cleared"))
        if ability=="Brown Wool":
            stats=abilities.AbilityLevels["Brown Wool"+str(members[user].abilitylevel[4])]
            members[target].pp=members[target].pp+stats[1]
            BattleText.list.append(BattleText("member"+str(target),"+"+`stats[1]`+" PP"))
        if ability=="Red Wool":
            stats=abilities.AbilityLevels["Red Wool"+str(members[user].abilitylevel[5])]
            enemy[target].status=["fire",stats[1],1]
            BattleText.list.append(BattleText("enemy"+str(target),"Burned",28))
            members[user].Attack(members[target],target)
        if ability=="Black Wool":
            stats=abilities.AbilityLevels["Black Wool"+str(members[user].abilitylevel[6])]
            BattleText.list.append(BattleText("enemy"+str(target),"Withered"))
            enemy[target].status=["wither",stats[1],1]
        if ability=="Victory Monument":
            stats=abilities.AbilityLevels["Victory Monument"+str(members[user].abilitylevel[7])]
            for i in range(0,3):
                if random.randint(1,100)<stats[1]:
                    members[i].status=["fast",6,1.5]
                    BattleText.list.append(BattleText("member"+str(i),"Fast"))
                else:
                    BattleText.list.append(BattleText("member"+str(i),"Failed"))
#Makes a Party Member Functions for Effects on Them
class PartyMember:
    @staticmethod
    def HaveMember(member):
        a=[]
        for i in range(0,len(Player.party)):
            a.append(Player.party[i].name)
        if member in a:
            return True
        else:
            return False
    weapontoattack={"pink wand":0.7,"rapier":0.8,"basic staff":1.2,"sythe":1.3,"basic wand":1.0,"basic sword":1.0,"basic gun":1.0,"claymore":1.2,"ameythyst":1.6}
    weapontospeed={"pink wand":1.2,"rapier":1.2,"basic staff":0.9,"sythe":0.8,"basic wand":1.0,"basic sword":1.0,"basic gun":1.0,"claymore":1.0,"ameythyst":1.0}
    weapontoblock={"pink wand":0.9,"rapier":0.9,"basic staff":1.1,"sythe":1.1,"basic wand":1.0,"basic sword":1.0,"basic gun":1.0,"claymore":1.1,"ameythyst":0.7}
    weapontoevade={"pink wand":1.1,"rapier":1.5,"basic staff":1.1,"sythe":0.7,"basic wand":1.0,"basic sword":1.0,"basic gun":1.0,"claymore":0.5,"ameythyst":0.9}
    weapontype={"pink wand":"magical","rapier":"physical","basic staff":"magical","sythe":"physical","basic wand":"magical","basic sword":"physical","basic gun":"physical","claymore":"physical","ameythystRaindrops":"physical"}
    #Loads Party Member From File
    @staticmethod
    def FromFile(name):
        lines=[line.strip() for line in open("Files/Members/"+name+".txt")]
        for i in range(1,5):
            lines[i]=float(lines[i])
        lines[5]=int(lines[5])
        holder=lines[6]
        holder=holder.split()
        for i in range(0,len(holder)):
            holder[i]=holder[i].replace("#"," ")
        lines[6]=holder
        holder=lines[7]
        holder=holder.split()
        holder=[int(i) for i in holder]
        lines[7]=holder
        return lines
    def __init__(self,name,HPvalue,SPEEDvalue,ATTACKvalue,EVADEvalue,level,abilities,uabilities,skill,hidden,type,weapon="basic"):
        if weapon=="basic" and type=="physical":
            weapon="basic sword"
        if weapon=="basic" and type=="magical":
            weapon="basic wand"
        if weapon=="basic" and type=="energy":
            weapon="basic gun"
        self.xp=0
        self.lvl=level
        self.hidden=hidden
        self.gain=1
        self.nextlvl=10
        for i in range(5,level+1):
            self.nextlvl=int(self.nextlvl*1.1)
        self.weapon=weapon
        self.weaponspeed=PartyMember.weapontospeed[self.weapon]
        self.weaponattack=PartyMember.weapontoattack[self.weapon]
        self.weaponblock=PartyMember.weapontoblock[self.weapon]
        self.weaponevade=PartyMember.weapontoevade[self.weapon]
        self.confidence=0
        self.status=["none",0]
        self.abilitiescooldown=[0,0,0]
        self.pp=0
        self.abilitylevel=[0,0,0,0,0,0,0,0]
        self.type=type
        self.name=name
        self.HPvalue=HPvalue
        self.speed=SPEEDvalue
        self.ATTACKvalue=ATTACKvalue
        self.EVADEvalue=EVADEvalue
        self.hp=int((self.HPvalue*float(self.lvl)+5)*self.weaponblock)
        self.attack=int((self.ATTACKvalue*float(self.lvl)+5)*self.weaponattack)
        self.evade=((abs(self.speed-10)+(self.EVADEvalue*5))*self.weaponevade)/3
        self.abilities=abilities
        self.unlocklvl=uabilities
        self.currenthp=self.hp
        self.currentspeed=self.speed
        self.currentattack=self.attack
        self.battleabilities=[self.abilities[0],self.abilities[1],"None"]
        self.abilitiescool=[0,0,"X"]
        self.skill=skill
        self.number=0
    @staticmethod
    #Creates a PartyMember object
    def Create(lines):
        person=PartyMember(lines[0],lines[1],lines[2],lines[3],lines[4],lines[5],lines[6],lines[7],lines[8],lines[9],lines[10])
        return person
    #Take Damage
    def TakeDamage(self,damage,enemynum,critical=False,effective=False):
        if self.hidden!="Death Swap" or random.randint(1,100)!=1:
            if critical:
                BattleText.list.append(BattleText("member"+str(abs(enemynum)),"Critical",28))
            elif effective:
                BattleText.list.append(BattleText("member"+str(abs(enemynum)),abilities.typea[abilities.typea[self.type]].title()+" Hit",28))
            if critical and effective:
                BattleText.list.append(BattleText("member"+str(abs(enemynum)),abilities.typea[abilities.typea[self.type]].title()+" Hit",48))
            if self.status[0]=="shield":
                self.status[1]=self.status[1]-damage
                damage=0
                if self.status[1]<=0:
                    damage=abs(self.status[1])
                    self.currenthp=self.currenthp-damage
                    self.status[0]="none"
            else:
                self.currenthp=self.currenthp-damage
            if self.status[0]=="sleep":
                self.status=["none",0,0]
            BattleText.list.append(BattleText("member"+str(self.number),"-"+str(int(damage))+" HP"))
        else:
            BattleText.list.append(BattleText("member"+str(abs(enemynum)),"Death Swap"))
    def DoDamage(self,amount,enemy,enemynum):
        chance=5
        damage=1*self.weaponattack
        effective=False
        critical=False
        if self.status[0]=="encouraged":
            chance=60
        if random.randint(1,100)<=chance:
            critical=True
            damage=1.5+round(random.random(),1)
        if random.randint(0,100)==1 and self.hidden=="Lord Baj":
            critical=True
            damage=1.5+round(random.random(),1)
            BattleText.list.append(BattleText("member"+str(self.number),"Lord Baj"))
        if abilities.typea[self.type]==enemy.type:
            effective=True
            damage=damage*1.3
        try:
            enemy.aggro[self.number]=enemy.aggro[self.number]+amount*damage
        except:
            pass
        enemy.TakeDamage(int(amount*damage),enemynum,critical,effective)
        if self.status[0]=="fire":
            self.TakeDamage(int(amount/8),enemynum,False)
    #Damages Enemy
    def Attack(self,enemy,enemynum,times=1):
        if enemy.evade<random.randint(0,100) or self.status[0]=="precision":
            if self.confidence<30:
                self.DoDamage(int(self.currentattack/10.0)*times,enemy,enemynum)
            else:
                if random.randint(1,2)!=2:
                    self.DoDamage(int(self.currentattack/10.0)*times,enemy,enemynum)
                else:
                    BattleText.list.append(BattleText("enemy"+str(enemynum),"Missed"))
        else:
            BattleText.list.append(BattleText("enemy"+str(enemynum),"Missed"))
    def removeBuffs(self):
        self.currentattack=self.attack
        self.currentevade=self.evade
        self.currentspeed=self.speed
    def addBuffs(self):
        if self.status[0]=="fast" or self.status[0]=="slow":
            self.currentspeed=self.speed/self.status[2]
        if self.status[0]=="attack +" or self.status[0]=="attack -":
            self.currentattack=self.attack*self.status[2]
        if self.status[0]=="evade +" or self.status[0]=="evade -":
            self.currentevade=self.evade*self.status[2]
        if self.status[0]=="encouraged":
            self.confidence=0
    #Recalculates Stats
    def update(self):
        self.weaponspeed=PartyMember.weapontospeed[self.weapon]
        self.weaponattack=PartyMember.weapontoattack[self.weapon]
        self.weaponblock=PartyMember.weapontoblock[self.weapon]
        self.weaponevade=PartyMember.weapontoevade[self.weapon]
        self.hp=int((self.HPvalue*float(self.lvl)+5)*self.weaponblock)
        if self.currenthp>self.hp:
            self.currenthp=self.hp
        self.currenthp=int(self.currenthp)
        self.currentattack=int(self.currentattack)
        self.attack=int((self.ATTACKvalue*float(self.lvl)+5)*self.weaponattack)
        self.evade=((abs(self.speed-10)+(self.EVADEvalue*5))*self.weaponevade)/3
        for i in range(0,8):
            if self.lvl>=self.unlocklvl[i] and self.abilitylevel[i]==0:
                self.abilitylevel[i]=1
        try:
            num=Player.party.index(self)
            self.number=num
        except:
            pass
    #Prepares for Battle
    def BattleStart(self):
        self.currentspeed=self.speed
        self.currentattack=self.attack
        self.status=["none",0,0]
        self.pp=0
        self.confidence=0
        for i in range(0,3):
            if self.battleabilities[i]!="None":
                self.abilitiescool[i]=random.randint(0,abilities.AbilityCool[self.battleabilities[i]])
            else:
                self.abilitiescool[i]="X"
    #Levels Up Party Member
    def GainXP(self,xp):
        ret=""
        self.xp=self.xp+xp
        Player.money=Player.money+xp*5
        while self.xp>=self.nextlvl:
            lis=self.LevelUp()
            ret=ret+lis+" "
        return self.name.title()+" gained "+str(xp)+" XP! "+ret
    def LevelUp(self):
        ret=["","",""]
        if self.lvl<50:
            self.xp=self.xp-self.nextlvl
            self.nextlvl=int(self.nextlvl*1.1)
            self.lvl=self.lvl+1
            try:
                ability=self.unlocklvl.index(self.lvl)
                ret[2]=" "+self.name.title()+" has learned the ability "+self.abilities[ability]+"! "
            except:
                pass
            self.update()
            if self.name[-1]!="s":
                ret[0]=self.name.title()+" grew to level "+str(self.lvl)+"! "+self.name.title()+"s HP increase to "+`self.hp`+"!"
                ret[1]=" "+self.name.title()+"s attack increase to "+`self.attack`+"!"
            else:
                ret[0]=self.name.title()+" grew to level "+str(self.lvl)+"! "+self.name.title()+"' HP increase to "+`self.hp`+"!"
                ret[1]=" "+self.name.title()+"' attack increase to "+`self.attack`+"!"
        else:
            if self.name[-1]!="s":
                ret[0]=self.name.title()+"s level is maxed!"
            else:
                ret[0]=self.name.title()+"' level is maxed!"
        return ret[0]+ret[1]+ret[2]
    #Handles Ability Cooldown And PP Calculation
    def Countdown(self,time):
        self.pp=self.pp+time
        for i in range(0,3):
            if self.abilitiescool[i]!="X":
                self.abilitiescool[i]=self.abilitiescool[i]-1
                if self.abilitiescool[i]<0:
                    self.abilitiescool[i]=0
        if self.status[0]=="posion":
            self.currenthp=self.currenthp-int(self.hp/16*self.status[2])
        if self.status[0]=="fire":
            self.currenthp=self.currenthp-int(self.hp/16*self.status[2])
        if self.status[0]=="regen":
            self.currenthp=self.currenthp+int(self.hp/16*self.status[2])
            if  self.currenthp>self.hp:
                self.currenthp=self.hp
        if self.status[0]=="wither":
            self.currenthp=self.currenthp-int(self.hp/32*self.status[2])
            self.status[2]=self.status[2]+1
        if self.status[0]!="shield":
            self.status[1]=self.status[1]-1
        if self.status[1]==0:
            self.removeBuffs()
            self.status=["none",0,0]
#Handles All the Music
class Music:
    volume=2
    song={}
    song["king pooses castle"]="Town"
    song["prison"]="Caverns"
    song["noprison"]="Caverns"
    song["pooses throne"]="Town"
    song["poose hall"]="Town"
    song["poose bar"]="Town"
    song["king pooses castle"]="Town"
    song["king pooses castlenoad"]="Town"
    song["lord bajs temple"]="Bajers"
    song["bajers"]="Bajers"
    song["bajers1"]="Bajers"
    song["bajers2"]="Bajers"
    song["bajers3"]="Bajers"
    song["bajers town"]="Bajers"
    song["barn"]="Bajers"
    song["barn in"]="Bajers"
    song["baj forest"]="Forest"
    song["baj templeopen"]="Temple"
    song["baj templein"]="Temple"
    song["baj cave"]="Caverns"
    song["aureylians rainbow castle"]="Aurey"
    song["aureylians room"]="Aurey"
    song["aureylian room"]="Aurey"
    song["aurey hall"]="Aurey"
    song["vechs1"]="Vechs"
    song["vechs2"]="Vechs"
    song["vechs3"]="Vechs"
    song["vechs4"]="Vechs"
    song["vechs5"]="Vechs"
    song["vechs6"]="Vechs"
    song["portal"]="Vechs"
    song["docms liquid assimilator"]="Docm"
    song["mesa"]="Mesa"
    song["mesa1"]="Mesa"
    song["e-team base"]="Mesa"
    song["etho mesa"]="Mesa"
    song["etho nomesa"]="Mesa"
    song["etho center"]="Mesa"
    song["coe mountain"]="Coe"
    song["coe1"]="Coe"
    song["coe2"]="Coe"
    song["coe top"]="Coe"
    song["bling tower"]="Bling"
    song["bling inside"]="Bling"
    song["bling noseth"]="Bling"
    song["bling under"]="Bling"
    song["nebris inside"]="Nebris"
    song["nebris' ice castle"]="Nebris"
    current="bob"
    @staticmethod
    #Changes Song to Song Matching World
    def ChangeSong(world=Player.worldname):
        if Music.current!=Music.song[world]:
            pygame.mixer.music.load("Files/Music/"+Music.song[world]+".wav")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(Music.volume/10.0)
            Music.current=Music.song[world]
    @staticmethod
    def ChangeByName(name,extension=".wav"):
        pygame.mixer.music.load("Files/Music/"+name+extension)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(Music.volume/10.0)
        Music.current=name
    @staticmethod
    def ChangeVolume(volume):
        Music.volume=volume
        pygame.mixer.music.set_volume(Music.volume/10.0)
#Handles Setting World Data
class World:
    collisionlist=["sn","sy","gh","cyw","cyp","cyb","cyu","cyl","oc","mw","id","do","pw","ps","czh","cad","cae","caj","cao","cay","czd","czi","sky","rw","ww","wa","bk","tb","td","wh","sw","bl","tr","ic","sf","bw","td","qw","qp","qt"]
    @staticmethod
    #Get World Info From File
    def FileToWorld(file):
        lines=[line.strip() for line in open("Files/Maps/"+file+".txt")]
        lines=[line.split() for line in lines]
        events=[line.strip() for line in open("Files/Maps/"+file+"events.txt")]
        events=[line.split() for line in events]
        return lines,events
    @staticmethod
    #Loads World Info Into World and Transition
    def LoadWorld(world,x,y):
        Draw.Fade(20,90)
        Player.worldname=world
        Player.x,Player.y=(x,y)
        Player.world,Player.events=World.FileToWorld(world)
        Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0),False)
        Draw.Entity(Player.party[0].name,(6*64,4*64),(0,Player.direct*64,64,64))
        Draw.Fade(120,20)
        Music.ChangeSong(world)
#Render Code
class Draw:
    global screen
    screen = pygame.display.set_mode((832,704))
    images={}
    #faces
    images["bookface"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/book.png").convert_alpha(),(64,64))
    images["wilsonface"]=pygame.transform.scale(pygame.image.load("Files/Art/face/wilson.png").convert_alpha(),(64,64))
    images["1st bajface"]=pygame.transform.scale(pygame.image.load("Files/Art/face/baj.png").convert_alpha(),(64,64))
    images["carlface"]=pygame.transform.scale(pygame.image.load("Files/Art/face/carl.png").convert_alpha(),(64,64))
    images["graceface"]=pygame.transform.scale(pygame.image.load("Files/Art/face/grace.png").convert_alpha(),(64,64))
    images["2nd bajface"]=pygame.transform.flip(pygame.transform.scale(pygame.image.load("Files/Art/face/baj.png").convert_alpha(),(64,64)),True,False)
    images["graveface"]=pygame.transform.scale(pygame.image.load("Files/Art/face/grave.png").convert_alpha(),(64,64))
    images["signface"]=pygame.transform.scale(pygame.image.load("Files/Art/events/sign.png").convert_alpha(),(64,64))
    images["bandit leaderface"]=pygame.image.load("Files/Art/face/bandit_leader.png").convert_alpha()
    images["banditface"]=pygame.image.load("Files/Art/face/bandit.png").convert_alpha()
    images["gameface"]=pygame.image.load("Files/Art/face/game.png").convert_alpha()
    images["guudeface"]=pygame.image.load("Files/Art/face/guude.png").convert_alpha()
    images["guudelandface"]=pygame.image.load("Files/Art/face/guude.png").convert_alpha()
    images["docmface"]=pygame.image.load("Files/Art/face/docm.png").convert_alpha()
    images["pyroface"]=pygame.image.load("Files/Art/face/pyro.png").convert_alpha()
    images["pauseface"]=pygame.image.load("Files/Art/face/pause.png").convert_alpha()
    images["pauseUnpauseLPface"]=pygame.image.load("Files/Art/face/pause.png").convert_alpha()
    images["vintagebeefface"]=pygame.image.load("Files/Art/face/beef.png").convert_alpha()
    images["coestarface"]=pygame.image.load("Files/Art/face/coestar.png").convert_alpha()
    images["pauseUnpauseYTface"]=pygame.image.load("Files/Art/face/pause.png").convert_alpha()
    images["pauseUnpauseHDface"]=pygame.image.load("Files/Art/face/pause.png").convert_alpha()
    images["pauseUnpauseFBface"]=pygame.image.load("Files/Art/face/pause.png").convert_alpha()
    images["pauseUnpause420face"]=pygame.image.load("Files/Art/face/pause.png").convert_alpha()
    images["pauseUnpausesface"]=pygame.image.load("Files/Art/face/pause.png").convert_alpha()
    images["millbeeface"]=pygame.image.load("Files/Art/face/millbee.png").convert_alpha()
    images["ethoface"]=pygame.image.load("Files/Art/face/etho.png").convert_alpha()
    images["aureylianface"]=pygame.image.load("Files/Art/face/aureylian.png").convert_alpha()
    images["omgchadface"]=pygame.image.load("Files/Art/face/omgchad.png").convert_alpha()
    images["drewface"]=pygame.image.load("Files/Art/face/drew.png").convert_alpha()
    images["adlingtonface"]=pygame.image.load("Files/Art/face/adlingtont.png").convert_alpha()
    images["vechsface"]=pygame.image.load("Files/Art/face/vechs.png").convert_alpha()
    images["davionface"]=pygame.image.load("Files/Art/face/vechs.png").convert_alpha()
    images["sethblingface"]=pygame.image.load("Files/Art/face/sethbling.png").convert_alpha()
    images["sheepface"]=pygame.image.load("Files/Art/face/sheep.png").convert_alpha()
    images["cowface"]=pygame.image.load("Files/Art/face/cow.png").convert_alpha()
    images["anderzelface"]=pygame.image.load("Files/Art/face/anderzel.png").convert_alpha()
    images["???face"]=pygame.image.load("Files/Art/face/question.png").convert_alpha()
    #enemies
    images["banditleader"]=pygame.image.load("Files/Art/enemies/banditleader.png").convert_alpha()
    images["bandit leader"]=pygame.image.load("Files/Art/enemies/banditleader.png").convert_alpha()
    images["bandit"]=pygame.image.load("Files/Art/enemies/bandit.png").convert_alpha()
    images["florb"]=pygame.transform.scale(pygame.image.load("Files/Art/enemies/florb.png").convert_alpha(),(64,64))
    images["treebeard"]=pygame.transform.scale(pygame.image.load("Files/Art/enemies/treebeard.png").convert_alpha(),(64,64))
    images["sapling"]=pygame.transform.scale(pygame.image.load("Files/Art/enemies/sapling.png").convert_alpha(),(64,64))
    images["baby spider"]=pygame.transform.scale(pygame.image.load("Files/Art/enemies/baby spider.png").convert_alpha(),(64,64))
    images["runaway dog"]=pygame.image.load("Files/Art/enemies/runaway dog.png").convert_alpha()
    images["chipmonk"]=pygame.transform.scale(pygame.image.load("Files/Art/enemies/chipmonk.png").convert_alpha(),(64,64))
    images["derp bat"]=pygame.transform.scale(pygame.image.load("Files/Art/enemies/derp bat.png").convert_alpha(),(64,64))
    images["flame venom spider"]=pygame.transform.scale(pygame.image.load("Files/Art/enemies/flame venom spider.png").convert_alpha(),(64,64))
    images["codewarrior the instigator"]=pygame.transform.scale(pygame.image.load("Files/Art/events/codewarrior.png").convert_alpha(),(64,64))
    images["dinnerbone the destroyer"]=pygame.transform.scale(pygame.image.load("Files/Art/events/dinnerbone.png").convert_alpha(),(64,64))
    images["kamyu the hidden"]=pygame.transform.scale(pygame.image.load("Files/Art/events/kamyu.png").convert_alpha(),(64,64))
    images["davion"]=pygame.transform.scale(pygame.image.load("Files/Art/enemies/davion.png").convert_alpha(),(64,64))
    images["sea monster"]=pygame.transform.scale(pygame.image.load("Files/Art/enemies/sea monster.png").convert_alpha(),(64,64))
    images["fish"]=pygame.transform.scale(pygame.image.load("Files/Art/enemies/fish.png").convert_alpha(),(64,64))
    images["lizard"]=pygame.transform.scale(pygame.image.load("Files/Art/enemies/lizard.png").convert_alpha(),(64,64))
    images["skeleton horse"]=pygame.transform.scale(pygame.image.load("Files/Art/enemies/skeleton horse.png").convert_alpha(),(64,64))
    images["tumbleweed"]=pygame.transform.scale(pygame.image.load("Files/Art/enemies/tumbleweed.png").convert_alpha(),(64,64))
    images["mesa deed trap"]=pygame.transform.scale(pygame.image.load("Files/Art/enemies/mesa deed.png").convert_alpha(),(64,64))
    images["wilson"]=pygame.transform.scale(pygame.image.load("Files/Art/enemies/wilson.png").convert_alpha(),(64,64))
    images["posion potion"]=pygame.transform.scale(pygame.image.load("Files/Art/enemies/posion potion.png").convert_alpha(),(64,64))
    images["instant damage potion"]=pygame.transform.scale(pygame.image.load("Files/Art/enemies/instant damage potion.png").convert_alpha(),(64,64))
    images["sethbot"]=pygame.transform.scale(pygame.image.load("Files/Art/enemies/sethbot.png").convert_alpha(),(64,64))
    images["sethwing"]=pygame.transform.scale(pygame.image.load("Files/Art/enemies/sethwing.png").convert_alpha(),(64,64))
    images["redstone bug"]=pygame.transform.scale(pygame.image.load("Files/Art/enemies/redstone bug.png").convert_alpha(),(64,64))
    #party members
    images["omgchad"]=pygame.transform.scale(pygame.image.load("Files/Art/inworld/omgchadfull.png").convert_alpha(),(256,256))
    images["docm"]=pygame.transform.scale(pygame.image.load("Files/Art/inworld/docmfull.png").convert_alpha(),(256,256))
    images["guude"]=pygame.transform.scale(pygame.image.load("Files/Art/inworld/guudefull.png").convert_alpha(),(256,256))
    images["pyro"]=pygame.transform.scale(pygame.image.load("Files/Art/inworld/pyrofull.png").convert_alpha(),(256,256))
    images["millbee"]=pygame.transform.scale(pygame.image.load("Files/Art/inworld/millbeefull.png").convert_alpha(),(256,256))
    images["aureylian"]=pygame.transform.scale(pygame.image.load("Files/Art/inworld/aureyfull.png").convert_alpha(),(256,256))
    images["etho"]=pygame.transform.scale(pygame.image.load("Files/Art/inworld/ethofull.png").convert_alpha(),(256,256))
    images["vechs"]=pygame.transform.scale(pygame.image.load("Files/Art/inworld/vechsfull.png").convert_alpha(),(256,256))
    images["sethbling"]=pygame.transform.scale(pygame.image.load("Files/Art/inworld/sethblingfull.png").convert_alpha(),(256,256))
    #tiles
    for i in range(0,8):
        images["s"+str(i)]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/s"+str(i)+".png"),(64,64))
    images["ie"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/ice.png"),(64,64))
    images["sy"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/snowtop.png"),(64,64))
    images["sn"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/snow.png"),(64,64))
    images["bc"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/blingstairs.png"),(64,64))
    images["bd"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/barndoor.png"),(64,64))
    images["bd"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/barndoor.png"),(64,64))
    images["gh"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/grasshill.png"),(64,64))
    images["bw"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/blackwall.png"),(64,64))
    images["bdl"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/barndoorleft.png"),(64,64))
    images["bdr"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/barndoorright.png"),(64,64))
    images["pw"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/pinkwall.png"),(64,64))
    images["ps"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/pinksign.png"),(64,64))
    images["pt"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/pinktile.png"),(64,64))
    images["pd"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/pinkdoor.png"),(64,64))
    images["do"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/trapdoor.png"),(64,64))
    images["sky"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/sky.png"),(64,64))
    images["clo"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/cloud/cloud.png"),(64,64))
    images["rcl"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/cloud/rcloud.png"),(64,64))
    images["lcl"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/cloud/lcloud.png"),(64,64))
    images["ucl"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/cloud/ucloud.png"),(64,64))
    images["dcl"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/cloud/dcloud.png"),(64,64))
    images["urc"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/cloud/urcloud.png"),(64,64))
    images["ulc"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/cloud/ulcloud.png"),(64,64))
    images["drc"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/cloud/drcloud.png"),(64,64))
    images["dlc"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/cloud/dlcloud.png"),(64,64))
    images["scl"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/cloud/smallcloud.png"),(64,64))
    images["dr"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/dirt.png"),(64,64))
    images["wb"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/bridge.png"),(64,64))
    images["bf"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/blackfloor.png"),(64,64))
    images["bs"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/blackstairs.png"),(64,64))
    images["bsr"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/blackstairsright.png"),(64,64))
    images["cnn"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/carpet/carpet.png"),(64,64))
    images["cun"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/carpet/carpetu.png"),(64,64))
    images["cdn"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/carpet/carpetd.png"),(64,64))
    images["cln"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/carpet/carpetl.png"),(64,64))
    images["crn"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/carpet/carpetr.png"),(64,64))
    images["cul"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/carpet/carpetul.png"),(64,64))
    images["cur"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/carpet/carpetur.png"),(64,64))
    images["cdr"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/carpet/carpetdr.png"),(64,64))
    images["cdl"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/carpet/carpetdl.png"),(64,64))
    images["ic"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/ice.png").convert_alpha(),(64,64))
    images["tr"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/tree.png").convert_alpha(),(64,64))
    images["tb"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/treebeard.png").convert_alpha(),(64,64))
    images["td"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/treedark.png").convert_alpha(),(64,64))
    images["bl"]=pygame.image.load("Files/Art/tiles/black.png").convert_alpha()
    images["nn"]=pygame.image.load("Files/Art/tiles/black.png").convert_alpha()
    images["gr"]=pygame.image.load("Files/Art/tiles/grass.png").convert_alpha()
    images["gd"]=pygame.image.load("Files/Art/tiles/grassdark.png").convert_alpha()
    images["wh"]=pygame.image.load("Files/Art/tiles/white.png").convert_alpha()
    images["sa"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/sand.png").convert_alpha(),(64,64))
    images["rd"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/rockdoor.png").convert_alpha(),(64,64))
    images["sal"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/sandlight.png").convert_alpha(),(64,64))
    images["ss"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/sandstairs.png").convert_alpha(),(64,64))
    images["ssl"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/sandstairsleft.png").convert_alpha(),(64,64))
    images["sf"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/sandfish.png").convert_alpha(),(64,64))
    images["sd"]=pygame.image.load("Files/Art/tiles/sanddoor.png").convert_alpha()
    images["se"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/sandentrance.png").convert_alpha(),(64,64))
    images["rw"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/rockwall.png").convert_alpha(),(64,64))
    images["ro"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/rock.png").convert_alpha(),(64,64))
    images["ru"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/rockup.png").convert_alpha(),(64,64))
    images["sw"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/sandwall.png").convert_alpha(),(64,64))
    images["qs"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/quartzstairs.png").convert_alpha(),(64,64))
    images["qscl"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/quartzstairscornerleft.png").convert_alpha(),(64,64))
    images["qscr"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/quartzstairscornerright.png").convert_alpha(),(64,64))
    images["qd"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/quartzdoor.png").convert_alpha(),(64,64))
    images["qr"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/quartz.png").convert_alpha(),(64,64))
    images["bk"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/bookshelf.png").convert_alpha(),(64,64))
    images["qp"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/quartzpillar.png").convert_alpha(),(64,64))
    images["qw"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/quartzwall.png").convert_alpha(),(64,64))
    images["qt"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/quartztop.png").convert_alpha(),(64,64))
    images["wa"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/water.png").convert_alpha(),(64,64))
    images["shl"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/smalllhouse.png").convert_alpha(),(64,64))
    images["shr"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/smallrhouse.png").convert_alpha(),(64,64))
    images["lhlu"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/luhouse.png").convert_alpha(),(64,64))
    images["lhld"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/ldhouse.png").convert_alpha(),(64,64))
    images["lhru"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/ruhouse.png").convert_alpha(),(64,64))
    images["lhrd"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/rdhouse.png").convert_alpha(),(64,64))
    images["qsr"]=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("Files/Art/tiles/quartzstairs.png").convert_alpha(),(64,64)),90)
    images["qsl"]=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("Files/Art/tiles/quartzstairs.png").convert_alpha(),(64,64)),270)
    images["qtr"]=pygame.transform.flip(pygame.transform.scale(pygame.image.load("Files/Art/tiles/quartzstairsstart.png").convert_alpha(),(64,64)),True,False)
    images["qtl"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/quartzstairsstart.png").convert_alpha(),(64,64))
    images["qel"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/quartzstairsend.png").convert_alpha(),(64,64))
    images["qer"]=pygame.transform.flip(pygame.transform.scale(pygame.image.load("Files/Art/tiles/quartzstairsend.png").convert_alpha(),(64,64)),True,False)
    images["qwl"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/quartzwallleft.png").convert_alpha(),(64,64))
    images["qwr"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/quartzwallright.png").convert_alpha(),(64,64))
    images["bk"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/bookshelf.png").convert_alpha(),(64,64))
    images["ww"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/woodwall.png").convert_alpha(),(64,64))
    images["su"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/sandup.png").convert_alpha(),(64,64))
    images["fl"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/woodfloor.png").convert_alpha(),(64,64))
    images["caa"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/castle/castlea.png").convert_alpha(),(64,64))
    images["cab"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/castle/castleb.png").convert_alpha(),(64,64))
    images["cac"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/castle/castlec.png").convert_alpha(),(64,64))
    images["cad"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/castle/castled.png").convert_alpha(),(64,64))
    images["cae"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/castle/castlee.png").convert_alpha(),(64,64))
    images["caf"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/castle/castlef.png").convert_alpha(),(64,64))
    images["cag"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/castle/castleg.png").convert_alpha(),(64,64))
    images["cah"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/castle/castleh.png").convert_alpha(),(64,64))
    images["cai"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/castle/castlei.png").convert_alpha(),(64,64))
    images["caj"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/castle/castlej.png").convert_alpha(),(64,64))
    images["cak"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/castle/castlek.png").convert_alpha(),(64,64))
    images["cal"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/castle/castlel.png").convert_alpha(),(64,64))
    images["cam"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/castle/castlem.png").convert_alpha(),(64,64))
    images["can"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/castle/castlen.png").convert_alpha(),(64,64))
    images["cao"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/castle/castleo.png").convert_alpha(),(64,64))
    images["cap"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/castle/castlep.png").convert_alpha(),(64,64))
    images["caq"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/castle/castleq.png").convert_alpha(),(64,64))
    images["car"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/castle/castler.png").convert_alpha(),(64,64))
    images["cas"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/castle/castles.png").convert_alpha(),(64,64))
    images["cat"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/castle/castlet.png").convert_alpha(),(64,64))
    images["cau"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/castle/castleu.png").convert_alpha(),(64,64))
    images["cav"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/castle/castlev.png").convert_alpha(),(64,64))
    images["caw"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/castle/castlew.png").convert_alpha(),(64,64))
    images["cax"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/castle/castlex.png").convert_alpha(),(64,64))
    images["cay"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/castle/castley.png").convert_alpha(),(64,64))
    images["caz"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/castle/castlez.png").convert_alpha(),(64,64))
    images["cza"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/castle/castleza.png").convert_alpha(),(64,64))
    images["czb"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/castle/castlezb.png").convert_alpha(),(64,64))
    images["czc"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/castle/castlezc.png").convert_alpha(),(64,64))
    images["czd"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/castle/castlezd.png").convert_alpha(),(64,64))
    images["cze"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/castle/castleze.png").convert_alpha(),(64,64))
    images["czf"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/castle/castlezf.png").convert_alpha(),(64,64))
    images["czg"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/castle/castlezg.png").convert_alpha(),(64,64))
    images["czh"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/castle/castlezh.png").convert_alpha(),(64,64))
    images["czi"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/castle/castlezi.png").convert_alpha(),(64,64))
    images["go"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/gold.png").convert_alpha(),(64,64))
    images["pl"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/planks.png").convert_alpha(),(64,64))
    images["st"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/stone.png").convert_alpha(),(64,64))
    images["sc"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/crackedstonebricks.png").convert_alpha(),(64,64))
    images["sb"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/stonebricks.png").convert_alpha(),(64,64))
    images["sx"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/stonewall.png").convert_alpha(),(64,64))
    images["ssd"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/stairs.png").convert_alpha(),(64,64))
    images["ssr"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/stairsright.png").convert_alpha(),(64,64))
    images["ssc"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/stairscenter.png").convert_alpha(),(64,64))
    images["ssle"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/stairsleft.png").convert_alpha(),(64,64))
    images["gl"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/glowstone.png").convert_alpha(),(64,64))
    images["oc"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/ocean.png").convert_alpha(),(64,64))
    images["mw"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/metalwall.png").convert_alpha(),(64,64))
    images["pa"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/plaster.png").convert_alpha(),(64,64))
    images["id"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/irondoor.png").convert_alpha(),(64,64))
    images["cyw"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/claywhite.png").convert_alpha(),(64,64))
    images["cyr"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/clayred.png").convert_alpha(),(64,64))
    images["cyo"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/clayorange.png").convert_alpha(),(64,64))
    images["cyp"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/clayporange.png").convert_alpha(),(64,64))
    images["cyy"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/clayyellow.png").convert_alpha(),(64,64))
    images["cyh"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/clayhard.png").convert_alpha(),(64,64))
    images["cyl"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/claylight.png").convert_alpha(),(64,64))
    images["cyb"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/claywall.png").convert_alpha(),(64,64))
    images["cyu"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/claybutter.png").convert_alpha(),(64,64))
    images["xa"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/portala.png").convert_alpha(),(64,64))
    images["xb"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/portalb.png").convert_alpha(),(64,64))
    images["xc"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/portalc.png").convert_alpha(),(64,64))
    images["xd"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/portald.png").convert_alpha(),(64,64))
    images["xe"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/portale.png").convert_alpha(),(64,64))
    images["xf"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/portalf.png").convert_alpha(),(64,64))
    images["ob"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/obsidian.png").convert_alpha(),(64,64))
    images["nr"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/netherrack.png").convert_alpha(),(64,64))
    images["ga"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/gravel.png").convert_alpha(),(64,64))
    images["bb"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/whitebrick.png").convert_alpha(),(64,64))
    #events
    images["beef"]=pygame.transform.scale(pygame.image.load("Files/Art/events/steak.png").convert_alpha(),(64,64))
    images["beef"]=pygame.transform.scale(pygame.image.load("Files/Art/events/mutton.png").convert_alpha(),(64,64))
    images["beef"]=pygame.transform.scale(pygame.image.load("Files/Art/events/pork.png").convert_alpha(),(64,64))
    images["beef"]=pygame.transform.scale(pygame.image.load("Files/Art/events/beef.png").convert_alpha(),(64,64))
    images["coestar"]=pygame.transform.scale(pygame.image.load("Files/Art/events/coestar.png").convert_alpha(),(64,64))
    images["stonehouselu"]=pygame.transform.scale(pygame.image.load("Files/Art/events/stonehouselu.png").convert_alpha(),(64,64))
    images["stonehouseld"]=pygame.transform.scale(pygame.image.load("Files/Art/events/stonehouseld.png").convert_alpha(),(64,64))
    images["stonehouserd"]=pygame.transform.scale(pygame.image.load("Files/Art/events/stonehouserd.png").convert_alpha(),(64,64))
    images["stonehouseru"]=pygame.transform.scale(pygame.image.load("Files/Art/events/stonehouseru.png").convert_alpha(),(64,64))
    images["crattop"]=pygame.transform.scale(pygame.image.load("Files/Art/events/crafting top.png").convert_alpha(),(64,64))
    images["craft"]=pygame.transform.scale(pygame.image.load("Files/Art/events/crafting table.png").convert_alpha(),(64,64))
    images["mesadeed"]=pygame.transform.scale(pygame.image.load("Files/Art/events/mesadeed.png").convert_alpha(),(64,64))
    images["barnright"]=pygame.transform.scale(pygame.image.load("Files/Art/events/barnright.png").convert_alpha(),(64,64))
    images["wfencev"]=pygame.transform.scale(pygame.image.load("Files/Art/events/whitefencev.png").convert_alpha(),(64,64))
    images["barnleft"]=pygame.transform.scale(pygame.image.load("Files/Art/events/barnleft.png").convert_alpha(),(64,64))
    images["barn"]=pygame.transform.scale(pygame.image.load("Files/Art/events/barn.png").convert_alpha(),(64,64))
    images["barnroof"]=pygame.transform.scale(pygame.image.load("Files/Art/events/barnroof.png").convert_alpha(),(64,64))
    images["barnroofright"]=pygame.transform.scale(pygame.image.load("Files/Art/events/barnroofright.png").convert_alpha(),(64,64))
    images["barnroofleft"]=pygame.transform.scale(pygame.image.load("Files/Art/events/barnroofleft.png").convert_alpha(),(64,64))
    images["sidead"]=pygame.transform.scale(pygame.image.load("Files/Art/events/sidead.png").convert_alpha(),(64,64))
    images["othersidead"]=pygame.transform.flip(pygame.transform.scale(pygame.image.load("Files/Art/events/sidead.png").convert_alpha(),(64,64)),True,False)
    images["topbed"]=pygame.transform.scale(pygame.image.load("Files/Art/events/topbed.png").convert_alpha(),(64,64))
    images["bottombed"]=pygame.transform.scale(pygame.image.load("Files/Art/events/bottombed.png").convert_alpha(),(64,64))
    images["drew"]=pygame.transform.scale(pygame.image.load("Files/Art/events/drew.png").convert_alpha(),(64,64))
    images["grace"]=pygame.transform.scale(pygame.image.load("Files/Art/events/grace.png").convert_alpha(),(64,64))
    images["carl"]=pygame.transform.scale(pygame.image.load("Files/Art/events/carl.png").convert_alpha(),(64,64))
    images["crate"]=pygame.transform.scale(pygame.image.load("Files/Art/events/crate.png").convert_alpha(),(64,64))
    images["bobby"]=pygame.transform.scale(pygame.image.load("Files/Art/events/bajersshop.png").convert_alpha(),(64,64))
    images["goldbaj"]=pygame.transform.scale(pygame.image.load("Files/Art/events/goldbaj.png").convert_alpha(),(64,64))
    images["sidead"]=pygame.transform.scale(pygame.image.load("Files/Art/events/sidead.png").convert_alpha(),(64,64))
    images["wheat"]=pygame.image.load("Files/Art/events/wheat.png").convert_alpha()
    images["adback"]=pygame.transform.scale(pygame.image.load("Files/Art/events/adback.png").convert_alpha(),(64,64))
    images["carrot"]=pygame.transform.scale(pygame.image.load("Files/Art/events/carrot.png").convert_alpha(),(64,64))
    images["sheep"]=pygame.transform.scale(pygame.image.load("Files/Art/events/sheep.png").convert_alpha(),(64,64))
    images["cow"]=pygame.transform.scale(pygame.image.load("Files/Art/events/cow.png").convert_alpha(),(64,64))
    images["chicken"]=pygame.transform.scale(pygame.image.load("Files/Art/events/chicken.png").convert_alpha(),(64,64))
    images["chickent"]=pygame.transform.scale(pygame.image.load("Files/Art/events/chickent.png").convert_alpha(),(64,64))
    images["pig"]=pygame.transform.scale(pygame.image.load("Files/Art/events/pig.png").convert_alpha(),(64,64))
    images["smallwhea"]=pygame.transform.scale(pygame.image.load("Files/Art/events/smallwheat.png").convert_alpha(),(64,64))
    images["wfence"]=pygame.transform.scale(pygame.image.load("Files/Art/events/whitefence.png").convert_alpha(),(64,64))
    images["siderunaway dog"]=pygame.transform.scale(pygame.image.load("Files/Art/cutscenes/runaway dogside.png").convert_alpha(),(64,64))
    images["none"]=pygame.image.load("Files/Art/events/none.png").convert_alpha()
    images["load"]=pygame.image.load("Files/Art/cutscenes/load.png").convert_alpha()
    images["logo"]=pygame.image.load("Files/Art/events/logo.png").convert_alpha()
    images["pauseu"]=pygame.image.load("Files/Art/events/pauseu.png").convert_alpha()
    images["train"]=pygame.image.load("Files/Art/events/train.png").convert_alpha()
    images["vrail"]=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("Files/Art/events/rail.png").convert_alpha(),(64,64)),90)
    images["rail"]=pygame.transform.scale(pygame.image.load("Files/Art/events/rail.png").convert_alpha(),(64,64))
    images["track"]=pygame.transform.scale(pygame.image.load("Files/Art/events/track.png").convert_alpha(),(64,64))
    images["trainback"]=pygame.image.load("Files/Art/events/trainback.png").convert_alpha()
    images["pausel"]=pygame.image.load("Files/Art/events/pausel.png").convert_alpha()
    images["pauser"]=pygame.image.load("Files/Art/events/pauser.png").convert_alpha()
    images["millbeef"]=pygame.image.load("Files/Art/events/millbee.png").convert_alpha()
    images["train1"]=pygame.image.load("Files/Art/cutscenes/train1.png").convert_alpha()
    images["train2"]=pygame.image.load("Files/Art/cutscenes/train2.png").convert_alpha()
    images["bars"]=pygame.transform.scale(pygame.image.load("Files/Art/events/bars.png").convert_alpha(),(64,64))
    images["celldoor"]=pygame.transform.scale(pygame.image.load("Files/Art/events/celldoor.png").convert_alpha(),(64,64))
    images["sign"]=pygame.transform.scale(pygame.image.load("Files/Art/events/sign.png").convert_alpha(),(64,64))
    images["arrowd"]=pygame.transform.scale(pygame.image.load("Files/Art/events/arrow.png").convert_alpha(),(64,64))
    images["arrowu"]=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("Files/Art/events/arrow.png").convert_alpha(),(64,64)),180)
    images["arrowl"]=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("Files/Art/events/arrow.png").convert_alpha(),(64,64)),270)
    images["arrowr"]=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("Files/Art/events/arrow.png").convert_alpha(),(64,64)),90)
    images["brokendoor"]=pygame.transform.scale(pygame.image.load("Files/Art/events/brokendoor.png").convert_alpha(),(64,64))
    images["table"]=pygame.transform.scale(pygame.image.load("Files/Art/events/table.png").convert_alpha(),(64,64))
    images["tableleft"]=pygame.transform.scale(pygame.image.load("Files/Art/events/tableleft.png").convert_alpha(),(64,64))
    images["tableright"]=pygame.transform.scale(pygame.image.load("Files/Art/events/tableright.png").convert_alpha(),(64,64))
    images["tablemid"]=pygame.transform.scale(pygame.image.load("Files/Art/events/tablemid.png").convert_alpha(),(64,64))
    images["chairfront"]=pygame.transform.scale(pygame.image.load("Files/Art/events/chairfront.png").convert_alpha(),(64,64))
    images["chairback"]=pygame.transform.scale(pygame.image.load("Files/Art/events/chairback.png").convert_alpha(),(64,64))
    images["fencev"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fencev.png").convert_alpha(),(64,64))
    images["fenceh"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fenceh.png").convert_alpha(),(64,64))
    images["chest"]=pygame.transform.scale(pygame.image.load("Files/Art/events/chest.png").convert_alpha(),(64,64))
    images["tree"]=pygame.transform.scale(pygame.image.load("Files/Art/events/tree.png").convert_alpha(),(64,64))
    images["grave"]=pygame.transform.scale(pygame.image.load("Files/Art/events/grave.png").convert_alpha(),(64,64))
    images["scarecrow"]=pygame.transform.scale(pygame.image.load("Files/Art/events/scarecrow.png").convert_alpha(),(64,64))
    images["aureyfront"]=pygame.transform.scale(pygame.image.load("Files/Art/events/aureyfront.png").convert_alpha(),(64,64))
    images["aureyback"]=pygame.transform.scale(pygame.image.load("Files/Art/events/aureyback.png").convert_alpha(),(64,64))
    images["vechsfront"]=pygame.transform.scale(pygame.image.load("Files/Art/events/vechsfront.png").convert_alpha(),(64,64))
    images["kamyu"]=pygame.transform.scale(pygame.image.load("Files/Art/events/kamyu.png").convert_alpha(),(64,64))
    images["dinnerbone"]=pygame.transform.scale(pygame.image.load("Files/Art/events/dinnerbone.png").convert_alpha(),(64,64))
    images["codewarrior"]=pygame.transform.scale(pygame.image.load("Files/Art/events/codewarrior.png").convert_alpha(),(64,64))
    images["anderz"]=pygame.transform.scale(pygame.image.load("Files/Art/events/anderzel.png").convert_alpha(),(64,64))
    images["foura"]=pygame.transform.scale(pygame.image.load("Files/Art/events/foura.png").convert_alpha(),(64,64))
    images["fourb"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fourb.png").convert_alpha(),(64,64))
    images["fourc"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fourc.png").convert_alpha(),(64,64))
    images["fourd"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fourd.png").convert_alpha(),(64,64))
    images["foure"]=pygame.transform.scale(pygame.image.load("Files/Art/events/foure.png").convert_alpha(),(64,64))
    images["fourf"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fourf.png").convert_alpha(),(64,64))
    images["fourg"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fourg.png").convert_alpha(),(64,64))
    images["fourh"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fourh.png").convert_alpha(),(64,64))
    images["fouri"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fouri.png").convert_alpha(),(64,64))
    images["fourj"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fourj.png").convert_alpha(),(64,64))
    images["fourk"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fourk.png").convert_alpha(),(64,64))
    images["fourl"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fourl.png").convert_alpha(),(64,64))
    images["fourm"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fourm.png").convert_alpha(),(64,64))
    images["fourn"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fourn.png").convert_alpha(),(64,64))
    images["fouro"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fouro.png").convert_alpha(),(64,64))
    images["fourp"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fourp.png").convert_alpha(),(64,64))
    images["fourq"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fourq.png").convert_alpha(),(64,64))
    images["fourr"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fourr.png").convert_alpha(),(64,64))
    images["fours"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fours.png").convert_alpha(),(64,64))
    images["fourt"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fourt.png").convert_alpha(),(64,64))
    images["fouru"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fouru.png").convert_alpha(),(64,64))
    images["fourv"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fourv.png").convert_alpha(),(64,64))
    images["fourw"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fourw.png").convert_alpha(),(64,64))
    images["fourx"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fourx.png").convert_alpha(),(64,64))
    images["foury"]=pygame.transform.scale(pygame.image.load("Files/Art/events/foury.png").convert_alpha(),(64,64))
    images["fourz"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fourz.png").convert_alpha(),(64,64))
    images["fouraa"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fouraa.png").convert_alpha(),(64,64))
    images["fourab"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fourab.png").convert_alpha(),(64,64))
    images["fourac"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fourac.png").convert_alpha(),(64,64))
    images["fourad"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fourad.png").convert_alpha(),(64,64))
    images["fourae"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fourae.png").convert_alpha(),(64,64))
    images["fouraf"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fouraf.png").convert_alpha(),(64,64))
    images["fourag"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fourag.png").convert_alpha(),(64,64))
    images["fourah"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fourah.png").convert_alpha(),(64,64))
    images["fourai"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fourai.png").convert_alpha(),(64,64))
    images["fouraj"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fouraj.png").convert_alpha(),(64,64))
    images["fourak"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fourak.png").convert_alpha(),(64,64))
    images["foural"]=pygame.transform.scale(pygame.image.load("Files/Art/events/foural.png").convert_alpha(),(64,64))
    images["fouram"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fouram.png").convert_alpha(),(64,64))
    images["fouran"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fouran.png").convert_alpha(),(64,64))
    images["fourao"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fourao.png").convert_alpha(),(64,64))
    images["fourap"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fourap.png").convert_alpha(),(64,64))
    images["fouraq"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fouraq.png").convert_alpha(),(64,64))
    images["fourar"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fourar.png").convert_alpha(),(64,64))
    images["fouras"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fouras.png").convert_alpha(),(64,64))
    images["fourat"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fourat.png").convert_alpha(),(64,64))
    images["fourau"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fourau.png").convert_alpha(),(64,64))
    images["fourav"]=pygame.transform.scale(pygame.image.load("Files/Art/events/fourav.png").convert_alpha(),(64,64))
    images["wilsona"]=pygame.transform.scale(pygame.image.load("Files/Art/events/wilsona.png").convert_alpha(),(64,64))
    images["wilsonb"]=pygame.transform.scale(pygame.image.load("Files/Art/events/wilsonb.png").convert_alpha(),(64,64))
    images["wilsonc"]=pygame.transform.scale(pygame.image.load("Files/Art/events/wilsonc.png").convert_alpha(),(64,64))
    images["wilsond"]=pygame.transform.scale(pygame.image.load("Files/Art/events/wilsond.png").convert_alpha(),(64,64))
    images["wilsone"]=pygame.transform.scale(pygame.image.load("Files/Art/events/wilsone.png").convert_alpha(),(64,64))
    images["wilsonf"]=pygame.transform.scale(pygame.image.load("Files/Art/events/wilsonf.png").convert_alpha(),(64,64))
    images["wilsong"]=pygame.transform.scale(pygame.image.load("Files/Art/events/wilsong.png").convert_alpha(),(64,64))
    images["wilsonh"]=pygame.transform.scale(pygame.image.load("Files/Art/events/wilsonh.png").convert_alpha(),(64,64))
    images["wilsoni"]=pygame.transform.scale(pygame.image.load("Files/Art/events/wilsoni.png").convert_alpha(),(64,64))
    images["wilsonj"]=pygame.transform.scale(pygame.image.load("Files/Art/events/wilsonj.png").convert_alpha(),(64,64))
    images["wilsonk"]=pygame.transform.scale(pygame.image.load("Files/Art/events/wilsonk.png").convert_alpha(),(64,64))
    images["wilsonl"]=pygame.transform.scale(pygame.image.load("Files/Art/events/wilsonl.png").convert_alpha(),(64,64))
    images["button"]=pygame.transform.scale(pygame.image.load("Files/Art/events/button.png").convert_alpha(),(64,64))
    images["ethoback"]=pygame.transform.scale(pygame.image.load("Files/Art/events/ethoback.png").convert_alpha(),(64,64))
    images["blinga"]=pygame.transform.scale(pygame.image.load("Files/Art/events/blinga.png").convert_alpha(),(64,64))
    images["blingb"]=pygame.transform.scale(pygame.image.load("Files/Art/events/blingb.png").convert_alpha(),(64,64))
    images["blingc"]=pygame.transform.scale(pygame.image.load("Files/Art/events/blingc.png").convert_alpha(),(64,64))
    images["blingd"]=pygame.transform.scale(pygame.image.load("Files/Art/events/blingd.png").convert_alpha(),(64,64))
    images["blinge"]=pygame.transform.scale(pygame.image.load("Files/Art/events/blinge.png").convert_alpha(),(64,64))
    images["blingf"]=pygame.transform.scale(pygame.image.load("Files/Art/events/blingf.png").convert_alpha(),(64,64))
    images["blingg"]=pygame.transform.scale(pygame.image.load("Files/Art/events/blingg.png").convert_alpha(),(64,64))
    images["blingh"]=pygame.transform.scale(pygame.image.load("Files/Art/events/blingh.png").convert_alpha(),(64,64))
    images["blingi"]=pygame.transform.scale(pygame.image.load("Files/Art/events/blingi.png").convert_alpha(),(64,64))
    images["blingj"]=pygame.transform.scale(pygame.image.load("Files/Art/events/blingj.png").convert_alpha(),(64,64))
    images["blingk"]=pygame.transform.scale(pygame.image.load("Files/Art/events/blingk.png").convert_alpha(),(64,64))
    images["blingl"]=pygame.transform.scale(pygame.image.load("Files/Art/events/blingl.png").convert_alpha(),(64,64))
    images["blingm"]=pygame.transform.scale(pygame.image.load("Files/Art/events/blingm.png").convert_alpha(),(64,64))
    images["blingn"]=pygame.transform.scale(pygame.image.load("Files/Art/events/blingn.png").convert_alpha(),(64,64))
    images["blingo"]=pygame.transform.scale(pygame.image.load("Files/Art/events/blingo.png").convert_alpha(),(64,64))
    images["blingp"]=pygame.transform.scale(pygame.image.load("Files/Art/events/blingp.png").convert_alpha(),(64,64))
    images["blingq"]=pygame.transform.scale(pygame.image.load("Files/Art/events/blingq.png").convert_alpha(),(64,64))
    images["blingr"]=pygame.transform.scale(pygame.image.load("Files/Art/events/blingr.png").convert_alpha(),(64,64))
    images["flower1"]=pygame.transform.scale(pygame.image.load("Files/Art/events/flower1.png").convert_alpha(),(64,64))
    images["flower2"]=pygame.transform.scale(pygame.image.load("Files/Art/events/flower2.png").convert_alpha(),(64,64))
    images["flower3"]=pygame.transform.scale(pygame.image.load("Files/Art/events/flower3.png").convert_alpha(),(64,64))
    images["flower4"]=pygame.transform.scale(pygame.image.load("Files/Art/events/flower4.png").convert_alpha(),(64,64))
    images["seth"]=pygame.transform.scale(pygame.image.load("Files/Art/events/seth.png").convert_alpha(),(64,64))
    #menu
    images["credits"]=pygame.image.load("Files/Art/menu/credits.png").convert_alpha()
    images["world"]=pygame.image.load("Files/Art/menu/map.png").convert_alpha()
    images["enemyplate"]=pygame.image.load("Files/Art/menu/enemyplate.png").convert_alpha()
    images["place"]=pygame.image.load("Files/Art/menu/place.png").convert_alpha()
    images["textbox"]=pygame.image.load("Files/Art/menu/textbox.png").convert_alpha()
    images["menubox"]=pygame.image.load("Files/Art/menu/menubox.png").convert_alpha()
    images["pointer"]=pygame.transform.scale(pygame.image.load("Files/Art/menu/pointer.png").convert_alpha(),(32,32))
    images["playerbox"]=pygame.image.load("Files/Art/menu/playerbox.png").convert_alpha()
    images["basebox"]=pygame.transform.scale(pygame.image.load("Files/Art/menu/playerbox.png").convert_alpha(),(200,500))
    images["enemybox"]=pygame.image.load("Files/Art/menu/enemybox.png").convert_alpha()
    images["surround"]=pygame.image.load("Files/Art/menu/surround.png").convert_alpha()
    images["up"]=pygame.transform.scale(pygame.image.load("Files/Art/menu/up.png").convert_alpha(),(40,40))
    images["down"]=pygame.transform.scale(pygame.image.load("Files/Art/menu/down.png").convert_alpha(),(40,40))
    images["equal"]=pygame.transform.scale(pygame.image.load("Files/Art/menu/equal.png").convert_alpha(),(40,40))
    images["heal"]=pygame.transform.scale(pygame.image.load("Files/Art/menu/heal.png").convert_alpha(),(64,64))
    images["revive"]=pygame.transform.scale(pygame.image.load("Files/Art/menu/revive.png").convert_alpha(),(64,64))
    images["key"]=pygame.transform.scale(pygame.image.load("Files/Art/menu/key.png").convert_alpha(),(64,64))
    images["weapon"]=pygame.transform.scale(pygame.image.load("Files/Art/menu/weapon.png").convert_alpha(),(64,64))
    images["book"]=pygame.transform.scale(pygame.image.load("Files/Art/menu/book.png").convert_alpha(),(64,64))
    #icons
    images["sand"]=pygame.image.load("Files/Art/menu/sand.png").convert_alpha()
    images["barnicon"]=pygame.image.load("Files/Art/menu/barn.png").convert_alpha()
    images["rainbow"]=pygame.image.load("Files/Art/menu/rainbow.png").convert_alpha()
    images["baj"]=pygame.image.load("Files/Art/menu/baj.png").convert_alpha()
    images["doc water"]=pygame.image.load("Files/Art/menu/doc water.png").convert_alpha()
    images["guudeland"]=pygame.image.load("Files/Art/menu/guude.png").convert_alpha()
    images["shop"]=pygame.image.load("Files/Art/menu/shop.png").convert_alpha()
    images["mesa"]=pygame.image.load("Files/Art/menu/mesa.png").convert_alpha()
    images["e-team base"]=pygame.image.load("Files/Art/menu/e-team base.png").convert_alpha()
    images["bling tower"]=pygame.image.load("Files/Art/menu/bling tower.png").convert_alpha()
    images["coe mountain"]=pygame.image.load("Files/Art/menu/coe mountain.png").convert_alpha()
    #minigames
    images["climb0"]=pygame.image.load("Files/Art/minigames/climbleft.png").convert_alpha()
    images["climb1"]=pygame.image.load("Files/Art/minigames/climbright.png").convert_alpha()
    images["rock"]=pygame.image.load("Files/Art/minigames/rock.png").convert_alpha()
    images["ladder"]=pygame.image.load("Files/Art/minigames/ladder.png").convert_alpha()
    images["wall"]=pygame.image.load("Files/Art/minigames/wall.png").convert_alpha()
    images["card"]=pygame.image.load("Files/Art/minigames/card.png").convert_alpha()
    images["outline"]=pygame.image.load("Files/Art/minigames/outline.png").convert_alpha()
    images["cardnone"]=pygame.image.load("Files/Art/minigames/cardnone.png").convert_alpha()
    images["cardmoney"]=pygame.image.load("Files/Art/minigames/cardmoney.png").convert_alpha()
    images["cardbook"]=pygame.image.load("Files/Art/minigames/cardbook.png").convert_alpha()
    #Box With Transparency
    @staticmethod
    def Credits():
        pygame.mixer.music.load("Files/Music/Credits.wav")
        pygame.mixer.music.play(1)
        pygame.mixer.music.set_volume(Music.volume/10.0)
        screen.blit(Draw.images["credits"],(0,0))
        pygame.display.update()
        pygame.time.wait(4000)
        for i in range(0,-4551,-1):
            print i
            screen.blit(Draw.images["credits"],(0,i))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.time.wait(10)
        pygame.time.wait(8000)
    def CutScene(run):
        if run==1:
            Music.ChangeByName("millbee")
            for i in range(1,146,5):
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                screen.blit(pygame.transform.scale(pygame.image.load("Files/Videos/prefix00"+`i`+".png"),screen.get_size()),(0,0))
                pygame.display.update()
                pygame.time.wait(240)
            pygame.time.wait(1500)
            Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0),False)
            Draw.Entity(Player.party[0].name,(6*64,4*64),(0,Player.direct*64,64,64),True,False)
        if run==2:
            for i in range(0,7):
                Draw.Entity("load",(0,0),[0,0,0,0],True,False)
                for x in range(0,13):
                    Draw.Entity("track",(x*64,604),[0,0,0,0],True,False)
                Draw.Entity("train1",(0,540),[0,0,0,0],True,False)
                for  x in range(0,len(Player.party)):
                    Draw.Entity(Player.party[x].name,(x*94+10,i*16+500),[i%4*64,0,64,64],True,False)
                pygame.time.wait(150)
                Draw.Entity("train2",(0,540),[0,0,0,0],True,False)
                pygame.display.update() 
                pygame.time.wait(150)
            pygame.time.wait(100)
            Draw.Entity("load",(0,0),[0,0,0,0],True,False)
            for x in range(0,13):
                Draw.Entity("track",(x*64,604),[0,0,0,0],True,False)
            Draw.Entity("train1",(0,540),[0,0,0,0],True,False)
            for  x in range(0,len(Player.party)):
                Draw.Entity(Player.party[x].name,(x*94+10,596),[0,64,64,64],True,False)
            Draw.Entity("train2",(0,540),[0,0,0,0],True,False)
            pygame.display.update()
            pygame.time.wait(1500)
            for i in range(0,-900,-2):
                Draw.Entity("load",(0,0),[0,0,0,0],True,False)
                for x in range(0,13):
                    Draw.Entity("track",(x*64,604),[0,0,0,0],True,False)
                Draw.Entity("train1",(i,540),[0,0,0,0],True,False)
                for  x in range(0,len(Player.party)):
                    Draw.Entity(Player.party[x].name,(x*94+10+i,596),[0,64,64,64],True,False)
                Draw.Entity("train2",(i,540),[0,0,0,0],True,False)
                pygame.display.update()
                pygame.time.wait(3)
            Draw.Fade(20,70)
        if run==3:
            Text.Textbox("Ah, I see the great warrior Guude has finally come. We are in need of your abilities.","pause")
            Text.Textbox("Okay guy, whatcha need?","guude")
            Text.Textbox("The Dark One we imprisoned together, years ago, has escaped. We fear he is hatching a plan.","pause")
            Text.Textbox("No... Not cheaty-","guude")
            Text.Textbox("Yes. We do not speak his name.","pause")
            Text.Textbox("Well shit, man. What a guy.","guude")
            Text.Textbox("I ask you, my old friend, to go, and gather our old group to oppose this new darkness that threatens the land.","pause")
            Text.Textbox("Hold up, you arent coming with me?","guude")
            Text.Textbox("Unfortunately, I am departing on vacation- Or rather a buisness trip in the coming hours. But please, take my newest warrior, Chadwick, with you.","pause")
            for x in range(12,4,-1):
                for i in range(0,4):
                    Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0),False)
                    Draw.Entity(Player.party[0].name,(6*64,4*64),[0,0*64,64,64],True,False)
                    Draw.Entity("omgchad",(7*64,x*64-i*16),[i*64,3*64,64,64])
                    pygame.time.wait(120)
            Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0),False)
            Draw.Entity(Player.party[0].name,(6*64,4*64),[0,2*64,64,64],True,False)
            Draw.Entity("omgchad",(7*64,4*64),[0*64,1*64,64,64])
            pygame.time.wait(2000)
            Text.Textbox("Omgchad Joined The Party!","game")
            Player.party.append(PartyMember.Create(PartyMember.FromFile("Omgchad")))
            for i in range(0,len(Player.party)):
                Player.party[i].update()
            Text.Textbox("Why is his hair so red?","guude")
            Text.Textbox("Also, we have a disciple of dadbee in our prison. Though I would rather keep him locked up, desperate times call for desperate measures. Let's go unlock him.","pause")
            Player.ran[1]=1
        if run==4:
            World.LoadWorld("king pooses castlenoad",7,6)
            Text.Textbox("Help! Help Me!","adlington")
            Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0),False)
            Draw.Entity(Player.party[0].name,(6*64,4*64),[0,Player.direct*64,64,64],True,False)
            Draw.Fade(30,120)
            Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0),False)
            Draw.Entity(Player.party[0].name,(6*64,4*64),[0,Player.direct*64,64,64],True,False)
            Draw.Entity("sidead",(4*64,5*64))
            Draw.Entity("siderunaway dog",(5*64,5*64))
            Text.Textbox("Quick! We've got to help!","omgchad")
            Draw.Entity("sidead",(4*64,5*64))
            Draw.Entity("siderunaway dog",(5*64,5*64))
            Text.Textbox("Haha, foolish dog. We will crush you... HAHA. HYA!","millbee")
            Draw.Entity("sidead",(4*64,5*64))
            Draw.Entity("siderunaway dog",(5*64,5*64))
            text=Battle.Run(["none","none",Enemy("runaway dog",10,3,2,1,5,["none",0,0],"physical"),"none","none"])
            Draw.Entity("sidead",(4*64,5*64))
            Draw.Entity(Player.party[0].name,(6*64,4*64),[0,Player.direct*64,64,64],True,False)
            Text.Textbox(text,"game")
            Draw.Entity("sidead",(4*64,5*64))
            Text.Textbox("Thank you so much! I dont know what I would have done without you!","adlington")
            Draw.Entity("sidead",(4*64,5*64))
            Text.Textbox("YES! FEEL MY WRATH. AH ITS BEEN SO LONG. THE POWER IS FLOWING THROUGH ME.","millbee")
            Draw.Entity("sidead",(4*64,5*64))
            Text.Textbox("Ah, yes. I know! come with me. I can give you rides on my Mindcrack Rail Network. Normally its one AdPense per person, but I'll make an exception for you!","adlington")
            Draw.Entity("sidead",(4*64,5*64))
            Text.Textbox("Sounds great!","omgchad")
            Draw.Entity("sidead",(4*64,5*64))
            Text.Textbox("Where are you guys headed?","adlington")
            Draw.Entity("sidead",(4*64,5*64))
            Text.Textbox("Uh, well, we dont know yet. We're looking for the warriors of the great battle, but they have all split up.","guude")
            Draw.Entity("sidead",(4*64,5*64))
            Text.Textbox("Then how about we head to Lord Baj's temple? You can ask for guidance there.","adlington")
            Draw.Entity("sidead",(4*64,5*64))
            Text.Textbox("Lord Baj's Temple Was Added to Your Map.","game")
            Draw.Entity("sidead",(4*64,5*64))
            Text.Textbox("Talk to me when ever you need to go somewhere.","adlington")
            World.LoadWorld("king pooses castle",7,6)
        if run==5:
            for i in range(0,3):
                Player.direct=3
                Player.x,Player.y,events=Draw.Walk(Player.x,Player.y,Player.direct,Player.world,Player.events,World.collisionlist,Player.party[0].name,False,Player.speed)
            Draw.Fade(10,100)
            Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0),False)
            Draw.Entity(Player.party[0].name,(6*64,4*64),[0,Player.direct*64,64,64],True,False)
            Draw.Entity("bandit",(6*64,3*64))
            pygame.time.wait(2000)
            Text.Textbox("Hehe.. Gotta get out of here before the gaurdian comes back..","bandit",False)
            Text.Textbox("Hey! What are you up to?","omgchad",False)
            Text.Textbox("Shoot! I need to go, but since you've seen me, I'll need to deal with you first..","bandit",False)
            text=Battle.Run(["none",Enemy("bandit",5.5,5,5,5,5,["none",0,0],"energy","Shield"),"none","none","none"])
            Text.Textbox(text+" The Bandit Dropped a Book!","game")
            for x in range(1,3):
                for i in range(0,4):
                    Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0),False)
                    Draw.Entity(Player.party[0].name,(6*64,4*64),[0,3*64,64,64],True,False)
                    Draw.Entity("pyro",(6*64,x*64+i*16),[i*64,0*64,64,64])
                    pygame.time.wait(120)
            Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0),False)
            Draw.Entity(Player.party[0].name,(6*64,4*64),[0,Player.direct*64,64,64],True,False)
            Draw.Entity("pyro",(6*64,3*64),[0*64,0*64,64,64])
            Text.Textbox("Whats going on here?","pyro")
            Draw.Entity("pyro",(6*64,3*64),[0*64,0*64,64,64])
            Text.Textbox("Oh, ahh, this guy was like, im gonna hurt you, and we were like, no, fuck you.","guude")
            Draw.Entity("pyro",(6*64,3*64),[0*64,0*64,64,64])
            Text.Textbox("Are you kidding me? I bet he stole more knowledge from the Baj Libraries.","pyro")
            Draw.Entity("pyro",(6*64,3*64),[0*64,0*64,64,64])
            Text.Textbox("Oh, is this what your looking for?","omgchad")
            Draw.Entity("pyro",(6*64,3*64),[0*64,0*64,64,64])
            Text.Textbox("Did he drop that? Sssiiccckkk!!!! Well thanks, m8! What brings you to Lord Baj's Temple?","pyro")
            Draw.Entity("pyro",(6*64,3*64),[0*64,0*64,64,64])
            Text.Textbox("We're trying to regroup the warriors of the great battle, we came here to ask guidance from Lord Baj.","omgchad")
            Draw.Entity("pyro",(6*64,3*64),[0*64,0*64,64,64])
            Text.Textbox("Ah, a most noble quest. I am the gaurdian of this temple, I will accompany you in.","pyro")
            Draw.Fade(10,80)
            Text.Textbox("Pyro Joined The Party!","game")
            Player.party.append(PartyMember.Create(PartyMember.FromFile("Pyro")))
            for i in range(0,len(Player.party)):
                Player.party[i].update()
            Player.ran[16]=1
            for i in range(0,len(Player.party)):
                Player.party.update[i]
        if run==6:
            for i in range(0,15):
                Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0),False)
                Draw.Entity(Player.party[0].name,(6*64,4*64),[0,3*64,64,64],True,False)
                pygame.display.update()
                pygame.time.wait(200)
                Player.frame=Player.frame+1
                Player.frame=Player.frame%8
            Player.x,Player.y,events=Draw.Walk(Player.x,Player.y,Player.direct,Player.world,Player.events,World.collisionlist,Player.party[0].name,False,Player.speed)
            for i in range(0,5):
                Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0),False)
                Draw.Entity(Player.party[0].name,(6*64,4*64),[0,3*64,64,64],True,False)
                pygame.display.update()
                pygame.time.wait(200)
                Player.frame=Player.frame+1
                Player.frame=Player.frame%8
            Draw.Entity("aureyfront",(6*64,2*64))
            for i in range(0,15):
                Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0),False)
                Draw.Entity(Player.party[0].name,(6*64,4*64),[0,3*64,64,64],True,False)
                Draw.Entity("aureyfront",(6*64,2*64))
                pygame.time.wait(200)
                Player.frame=Player.frame+1
                Player.frame=Player.frame%8
            Text.Textbox("Guude! Its nice to see you, Its been so long! What are you doing here?","aureylian")
            Text.Textbox("Nice to see you too, Aurey. Cheaty Nebris has escaped, Poose thinks he's up to something. We hope to find the others too, we're gonna need all the help we can get.","guude")
            Text.Textbox("I see. I would love to help you stop his shenanigans, but Davion is holding me captive here. If i want to leave, we will have to fight him.","aureylian")
            Text.Textbox("Davion? No worries, who ever he is, we can take him!","omgchad")
            Text.Textbox("Gasp! SPARKELY!","millbee")
            Text.Textbox("I know! Isnt it wonderful! I literally can't even!","aureylian")
            Text.Textbox("Ah... Anyways.. Wait here, we'll take care of him.","omgchad")
            Text.Textbox("No, I'll fight beside you. But I need my wand. It should be at my barn in Farm Land.","aureylian")
            Text.Textbox("Got, it! See you soon.","guude")
            Text.Textbox("Aurey's Barn Was Added to Your Map.","game")
            Map.Add("barn")
        if run==7:
            Draw.Entity("docm",(2*64,7*64),[0*64,0*64,64,64])
            pygame.time.wait(1000)
            for i in range(1,5):
                pygame.time.wait(175)
                Player.frame=Player.frame+1
                Player.frame=Player.frame%8
                Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,-1*i*16))
                Draw.Entity(Player.party[0].name,(6*64,4*64),[i%4*64,0*64,64,64])
                Draw.Entity("docm",(2*64+i*16,7*64-i*16),[i%4*64,2*64,64,64])
            Player.y=Player.y+1
            for i in range(1,5):
                pygame.time.wait(175)
                Player.frame=Player.frame+1
                Player.frame=Player.frame%8
                Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,-1*i*16))
                Draw.Entity(Player.party[0].name,(6*64,4*64),[i%4*64,0*64,64,64])
                Draw.Entity("docm",(3*64+i*16,6*64-i*16),[i%4*64,2*64,64,64])
            Player.y=Player.y+1
            for i in range(1,5):
                pygame.time.wait(175)
                Player.frame=Player.frame+1
                Player.frame=Player.frame%8
                Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,-1*i*16))
                Draw.Entity(Player.party[0].name,(6*64,4*64),[i%4*64,0*64,64,64])
                Draw.Entity("docm",(4*64+i*16,5*64-i*16),[i%4*64,2*64,64,64])
            Draw.Entity("docm",(5*64,4*64),[0*64,2*64,64,64])
            pygame.time.wait(1000)
            Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,-1*i*16))
            Draw.Entity("docm",(5*64,4*64),[0*64,2*64,64,64])
            Draw.Entity(Player.party[0].name,(6*64,4*64),[i%4*64,1*64,64,64])
            pygame.time.wait(2000)
            Text.Textbox("Hey.","docm",False)
            Text.Textbox("AHHH! Holy fucking shit he dun fuck wow I can't no fuck me! Now me damn southern be comin out!","guude",False)
            Text.Textbox("Um. Ya.","docm",False)
            Text.Textbox("Heya, Doc! It's been a while!","aureylian",False)
            Text.Textbox("Aurey! What are you doing here?","docm",False)
            Text.Textbox("We're looking for Etho. He said he was going to come here and work with you.","aureylian",False)
            Text.Textbox("Sorry, he left quite a while ago. We went\ to the Mesa to help the B-team and he decided to stay.","docm",False)
            Text.Textbox("Bananas! I guess we'll have to track him down there.","aureylian",False)
            Text.Textbox("Are you kidding me?","pyro",False)
            Text.Textbox("Why do you guys need him?","docm",False)
            Text.Textbox("Nebris has escaped. King Poose thinks he's planning something big.","aureylian",False)
            Text.Textbox("Sounds serious, but nothing Etho and you can't deal with. I'll help you find him, not much is going on here anyways.","docm",False)
            Text.Textbox("Really? Thanks, Doc!","aureylian",False)
            Text.Textbox("Before we go, I have to tell Anderz I'm leaving. He'll be over by the docks.","docm",False)
            Text.Textbox("Docm Joined The Party!","game")
            Player.party.append(PartyMember.Create(PartyMember.FromFile("Docm")))
            for i in range(0,len(Player.party)):
                Player.party[i].update()
            Player.y=Player.y+1
    @staticmethod
    def Box(i,box):
        if i > 200:
            i=200
        pygame.gfxdraw.box(screen, pygame.Rect(box[0],box[1],box[2],box[3]), (0,0,0,i))
    #Draws Image
    @staticmethod
    def Entity(image,place,rect=[0,0,0,0],fromimages=True,update=True):
        newrect=[rect[0],rect[1],rect[2],rect[3]]
        if fromimages:
            image=Draw.images[image]
        if Player.small:
            image=pygame.transform.scale(image,(image.get_width()/2,image.get_height()/2))
            for i in range(0,4):
                try:
                    newrect[i]=newrect[i]/2
                except:
                    pass
            if newrect[2]==0 and newrect[3]==0:
                newrect[2],newrect[3]=image.get_size()
            nplace=[0,0]
            nplace[0]=place[0]/2
            nplace[1]=place[1]/2
            screen.blit(image,(nplace[0],nplace[1]),(newrect[0],newrect[1],newrect[2],newrect[3]))
        if newrect[2]==0 and newrect[3]==0:
            newrect[2],newrect[3]=image.get_size()
        if not Player.small:
            screen.blit(image,(place[0],place[1]),(newrect[0],newrect[1],newrect[2],newrect[3]))
        if update:
            pygame.display.update()
    @staticmethod
    #Fills Screen
    def Fill(color=(0,0,0)):
        screen.fill(color)
    @staticmethod
    #Fades Screen
    def Fade(start=0,end=255):
        different=end-start
        counter=0
        if different>0:
            for i in range(start,end):
                pygame.gfxdraw.box(screen, pygame.Rect(0,0,900,900), (0,0,0,i))
                pygame.display.update()
                pygame.time.wait(15)
                counter=counter+1
                if counter==8:
                    Player.frame=Player.frame+1
                    Player.frame=Player.frame%8
                    counter=0
        if different<=0:
            for i in range(start,end,-1):
                Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0),False)
                Draw.Entity(Player.party[0].name,(6*64,4*64),(0,Player.direct*64,64,64),True,False)
                pygame.gfxdraw.box(screen, pygame.Rect(0,0,900,900), (0,0,0,i))
                pygame.display.update()
                pygame.time.wait(2)
                counter=counter+1
                if counter==20:
                    Player.frame=Player.frame+1
                    Player.frame=Player.frame%8
                    counter=0
    @staticmethod
    #Updates Tiles
    def Tiles(x,y,world,events,shift,update=True):
        for yer in range(-1, 12):
            for xer in range(-1,14):
                if y+(yer-5)>=0 and x+(xer-7)>=0:
                    try:
                        image=world[y+(yer-5)][x+(xer-7)]
                    except:
                        image="bl"
                else:
                    image="bl"
                if y+(yer-5)>=0 and x+(xer-7)>=0:
                    try:
                        event=events[y+(yer-5)][x+(xer-7)]
                        event=event.replace("-"," ")
                        event=event.split()
                        event=event[1]
                        event=Draw.images[event]
                    except:
                        event=Draw.images["none"]
                else:
                    event=Draw.images["none"]
                if image[-1]=="0":
                    image=image[:len(image)-1]+str(Player.frame)
                image=Draw.images[image]
                if Player.small:
                    event=pygame.transform.scale(event,(32,32))
                    image=pygame.transform.scale(image,(32,32))
                    screen.blit(image,((xer)*32+shift[0]/2,(yer)*32+shift[1]/2))
                    screen.blit(event,((xer)*32+shift[0]/2,(yer)*32+shift[1]/2))
                else:
                    screen.blit(image,((xer)*64+shift[0],(yer)*64+shift[1]))
                    screen.blit(event,((xer)*64+shift[0],(yer)*64+shift[1]))
    @staticmethod
    #Handles Walking Draw Code
    def Walk(x,y,direct,world,events,collision,name,update=True,speed=150):
        direction=[(0,-1),(1,0),(-1,0),(0,1)]
        shiftx,shifty=direction[direct]
        try:
            tile=world[y+(shifty*-1)-1][x+(shiftx*-1)-1]
        except:
            tile="bl"
        Draw.Tiles(x,y,world,events,(0,0),update)
        Draw.Entity(name,(6*64,4*64),[0*64,direct*64,64,64],True,update)
        collide=False
        try:
            event=events[y+(shifty*-1)-1][x+(shiftx*-1)-1]
            event=event.replace("-"," ")
            event=event.split()
            if event[2]=="True":
                collide=True
        except:
            collide=False
        if tile in collision:
            return x,y,False
        if collide:
            return x,y,False
        if x+(shiftx*-1)<1 or y+(shifty*-1)<1:
            return x,y,False
        else:
            for i in range(1,5):
                pygame.time.wait(Player.walk)
                Player.frame=Player.frame+1
                Player.frame=Player.frame%8
                Draw.Tiles(x,y,world,events,(shiftx*i*16,shifty*i*16))
                Draw.Entity(name,(6*64,4*64),[i%4*64,direct*64,64,64])
            return x+(shiftx*-1),y+(shifty*-1),True
#Writing Text on Screen
class Text:
    color={}
    color["nouse"]=(190,100,100)
    color["pyro"]=(50,0,0)
    color["aureylian"]=(255,120,150)
    color["guude"]=(0,240,0)
    color["millbee"]=(255,0,255)
    color["omgchad"]=(235,0,0)
    color["etho"]=(61,64,76)
    color["docm"]=(10,70,3)
    color["vechs"]=(128,0,0)
    color["sethbling"]=(255,178,0)
    color["slow"]=(30,30,150)
    color["fast"]=(255,100,30)
    color["attack +"]=(30,30,150)
    color["attack -"]=(255,100,30)
    color["evade +"]=(30,30,150)
    color["evade -"]=(255,100,30)
    color["aggro"]=(190,0,0)
    color["sleep"]=(0,0,0)
    color["encouraged"]=(255,230,20)
    color["confused"]=(100,255,100)
    color["posion"]=(140,0,255)
    color["paralyzed"]=(255,255,0)
    color["ability-lock"]=(100,100,100)
    color["fire"]=(170,0,0)
    color["precision"]=(0,0,130)
    color["wither"]=(40,0,40)
    color["shield"]=(150,150,250)
    color["regen"]=(255,120,120)
    color["downed"]=(0,0,0)
    font=pygame.font.Font("Files/font.ttf",29)
    small=pygame.font.Font("Files/font.ttf",27)
    myfont=pygame.font.Font("Files/font.ttf",29)
    @staticmethod
    #Basic Write Text on Screen
    def Write(word,place,color=(100,100,100),name="",update=True,size=29):
        try:
            color=Text.color[name]
        except:
            pass
        if size!=29 and size!="small":
            Text.myfont=pygame.font.Font("Files/font.ttf",size)
        if size=="small":
            Text.myfont=Text.small
        Draw.Entity(Text.myfont.render(word,1,color),place,[0,0,0,0],False,update)
        if size!=29:
            Text.myfont=Text.font
    @staticmethod
    #Writes Part of Word
    def WriteLine(word,place):
        for i in range(1,len(word)+1):
            pygame.time.wait(Player.textspeed*10+30)
            Draw.Entity(Text.myfont.render(word[:i],1,(100,100,100)),place,[0,0,0,0],False)
    @staticmethod
    #Draws Clean TextBox
    def ClearBox(name):
        try:
            color=Text.color[name]
        except:
            color=(100,100,100)
        Draw.Entity("textbox",(10,10))
        Draw.Entity(name+"face",(17,5))
        cap = [word[0].upper() + word[1:] for word in name.split()]
        name = " ".join(cap)
        Draw.Entity(Text.myfont.render(name,1,color),(110,33),[0,0,0,0],False)
    @staticmethod
    #Draw a Textbox
    def Textbox(word,name,update=True):
        word=word.split()
        currentline=0
        line1=(20,85)
        line2=(20,130)
        lines=[word[0]]
        for i in range(1,len(word)):
            if len(lines[currentline])+len(word[i])<41:
                lines[currentline]=lines[currentline]+" "+word[i]
            else:
                currentline=currentline+1
                lines.append(word[i])
        Text.ClearBox(name)
        run=len(lines)
        if run==1:
            run=2
        for i in range(1,run):
            Text.ClearBox(name)
            if i==1:
                Text.WriteLine(lines[i-1],line1)
            else:
                Text.Write(lines[i-1],line1)
            try:
                Text.WriteLine(lines[i],line2)
            except:
                pass
            wait=True
            pressed=pygame.key.get_pressed()
            pygame.event.pump()
            while pressed[K_d]==False or wait==True:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type==KEYDOWN and event.key==K_s:
                        i=run-1
                pygame.event.pump()
                pressed=pygame.key.get_pressed()
                wait=False
        if update:
            Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0))
            Draw.Entity(Player.party[0].name,(6*64,4*64),(0,Player.direct*64,64,64))
        Player.Dcooldown=10
#Holds the Data for Events Triggered Inworld
class Events:
    @staticmethod
    #Hardcoded Events
    def Call(event):
        if event==1:
            World.LoadWorld("inside",5,12)
            Player.worldname="inside"
            Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0))
            Draw.Entity(Player.party[0].name,(6*64,4*64),(0,Player.direct*64,64,64))
            Text.Textbox("Hey! You! Dont worry, I'm not with the bandits. I've been in disguise waiting for you. If you want guidance, talk to me","bandit")
            Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0))
            Draw.Entity(Player.party[0].name,(6*64,4*64),(0,Player.direct*64,64,64))
            Player.move=False
        if event==2:
            if Player.ran[5]==0:
                Text.Textbox("This tree looks weird...","guude")
                Text.Textbox("When trees grow, they get bigger. And when they get bigger... I want OJ.","pyro")
                Text.Textbox("Oh no. It's him.","millbee")
                Text.Textbox("Wait... Did that tree just... move?","omgchad")
                foe=["none",Enemy("sapling",1,3,2,0,5,["none",0,0],"physical"),Enemy("treebeard",8,4,5,2,10,["none",0,0],"magical"),Enemy("sapling",1,3,2,0,5,["none",0,0],"physical"),"none"]
                text=Battle.Run(foe,"Battle2")
                Text.Textbox(text,"game")
                Player.ran[5]=1
                Draw.images["tb"]=pygame.transform.scale(pygame.image.load("Files/Art/tiles/tree.png"),(64,64))
        if event==4 and random.randint(0,5)==5:
            foe=["none",Enemy("bandit",5.5,5,5,5,5,["none",0,0],"energy","Shield"),"none","none","none"]
            if random.randint(0,10)==1:
                foe[3]=Enemy("bandit",5.5,5,5,5,5,["shield",15,0],"energy","Shield")
            ret=Battle.Run(foe)
            Draw.Entity(Player.party[0].name,(6*64,4*64),(0,Player.direct*64,64,64))
            Text.Textbox(ret,"game")
            Music.ChangeSong(Player.worldname)
        if event==5:
            Text.Textbox("NO! Hanako.... Im so sorry. Hanako! Its all their fault. They told me to go to 10,000. \"Its not that many\", they said. \"It wont take that long\", they said. Dadbee, Have mercy on me and end my suffering. So many Boobahs. Get them out! OUT OF MY HEAD. Oh. Its you. Guude. You have been shown to me in a vision. You will release me.","millbee")
            Text.Textbox("Is this him? He's out of his fucking mind!","guude")
            Text.Textbox("Dont let his demeanor fool you, he is a very powerful sorcerer.","pause")
            Text.Textbox("Yes. I know what you want. My power. I will aid you. Just free me.","millbee")
            World.LoadWorld("noprison",Player.x,Player.y)
            Text.Textbox("Millbee Joined The Party!","game")
            Player.party.append(PartyMember.Create(PartyMember.FromFile("Millbee")))
            Player.ran[0]=1
            for i in range(0,len(Player.party)):
                Player.party[i].update()
        if event==6:
            Text.Textbox("So this is.. Or was, the cell of the Dark One? Wow. He must be even more powerful.","guude")
            Text.Textbox("You can say that again.","omgchad")
            Text.Textbox("Wow. He must be even more powerful.","guude")
            Text.Textbox("No, thats not..","omgchad")
            Text.Textbox("What Chad?","guude")
            Text.Textbox("Nevermind.","omgchad")
        if event==7:
            World.LoadWorld("poose hall",2,2)
            Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0))
            Draw.Entity(Player.party[0].name,(6*64,4*64),(0,Player.direct*64,64,64))
        if event==8:
            Text.Textbox("Welcome to King Pooses Vacation House! You must be Guude, the king would like to see you. He's right up ahead.","pauseUnpauseLP")
        if event==9:
            Text.Textbox("Welcome to King Pooses Vacation House! You must be Guude, the king would like to see you. He's right up ahead.","pauseUnpauseYT")
        if event==10:
            if Player.ran[1]==0:
                Draw.CutScene(3)
            elif Player.ran[0]==0:
                Text.Textbox("The prison is out the door, then to your right.","pause")
            else:
                Text.Textbox("Good luck on your quest. Peace out girl scouts!","pause")
                for i in Player.party:
                    try:
                        i.currenthp=i.hp
                    except:
                        pass
        if event==11:
            if Player.ran[1]==1:
                World.LoadWorld("poose hall",4,2)
                Player.worldname="poose hall"
                Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0))
                Draw.Entity(Player.party[0].name,(6*64,4*64),(0,Player.direct*64,64,64))
            else:
                Text.Textbox("I've gotta speak to King Poose.","guude")
                Player.direct=3
                Player.x,Player.y,events=Draw.Walk(Player.x,Player.y,Player.direct,Player.world,Player.events,World.collisionlist,Player.party[0].name,False,Player.speed)
        if event==12:
            if Player.ran[0]==0:
                load="prison"
            else:
                load="noprison"
            World.LoadWorld(load,8,4)
            Player.worldname=load
            Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0))
            Draw.Entity(Player.party[0].name,(6*64,4*64),(0,Player.direct*64,64,64))
        if event==13:
            World.LoadWorld("pooses throne",4,13)
            Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0))
            Draw.Entity(Player.party[0].name,(6*64,4*64),(0,Player.direct*64,64,64))
        if event==14:
            if Player.ran[0]==0:
                Text.Textbox("The prison is the other way.","omgchad")
                Player.direct=3
                Player.x,Player.y,events=Draw.Walk(Player.x,Player.y,Player.direct,Player.world,Player.events,World.collisionlist,Player.party[0].name,False,Player.speed)
            else:
                if Player.ran[4]==1:
                    World.LoadWorld("king pooses castle",7,6)
                    Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0))
                    Draw.Entity(Player.party[0].name,(6*64,4*64),(0,Player.direct*64,64,64))
                if Player.ran[4]==0:
                    Draw.CutScene(4)
                    Player.ran[4]=1
        if event==15:
            if Player.ran[0]==0:
                Text.Textbox("The prison is the other way.","omgchad")
                Player.direct=1
                Player.x,Player.y,events=Draw.Walk(Player.x,Player.y,Player.direct,Player.world,Player.events,World.collisionlist,Player.party[0].name,False,Player.speed)
            else:
                World.LoadWorld("poose bar",2,4)
        if event==16:
            Text.Textbox("This place used to be a seperate prison, but we never had enough prisoners anyways, so we turned it into a bar!","pauseUnpauseHD")
        if event==17:
            Text.Textbox("Are we gonna go get some dominos?","pauseUnpauseHD")
            Menu.Shop(["dominos","fish bowl"],[100,180])
        if event==18:
            if Player.ran[2]==0:
                Text.Textbox("Hey. Come here. You dont know meee man, but I know you. I do, I really do. Im not drunk, nope no I'm not, but the fuckin man wont give me another drink. Can you get me one?","pauseUnpause420")
                Player.ran[2]=1
            if Player.ran[3]==0:
                Text.Textbox("You got a drink for me?","pauseUnpause420")
                if "fish bowl" in Player.inventory:
                    del Player.inventory[Player.inventory.index("fish bowl")]
                    Text.Textbox("Oh yes, you are ma hero!","pauseUnpause420")
                    Text.Textbox("PauseUnpause420 took the fish bowl.","game")
                    Text.Textbox("Here, take this. I dunno what it is, but its yours....","pauseUnpause420")
                    Player.inventory.append("newcomer 4")
                    Text.Textbox(Player.party[0].name.title()+" Received a Newcomer 4 Book!","game")
                    Player.ran[3]=1
            if Player.ran[3]==1:
                Text.Textbox("Thank you kind sir, I'm forever in your... debt.. Uhhh. I don't feel so well...","pauseUnpause420")
                Text.Textbox("I swear if you puke on my I will punch you in the face.","guude")
        if event==20:
            World.LoadWorld("poose hall",6,2)
        if event==21:
           Text.Textbox("What can I get you?","pauseUnpauses")
           Menu.Shop(["claymore","potato on a stick","notch apple"],[300,300,1000])
        if event==22:
            if Player.ran[45]!=1:
                Text.Textbox("Where are we off to?","adlington")
                Map.World()
            else:
                Text.Textbox("Where are we off to?","adlington")
                Text.Textbox("Nebris's Ice Castle, up north.","guude")
                Text.Textbox("Sorry, our Mindcrack Rail Network can't travel on ice.","adlington")
                Text.Textbox("Wait, so you can travel to the middle of the ocean and a house on a rainbow, but god forbid you come across ice?","millbee")
                Text.Textbox("Yep. If we could upgrade the train to levitate, we could go, but that would take some command block magic.","adlington")
                Text.Textbox("Dont look at me, that voodoo doesn't exist in survival.","docm")
                Text.Textbox("Etho?","aureylian")
                Text.Textbox("I dont think I can, but I know someone who can. Adlington, we're heading to Bling Tower.","etho")
                Text.Textbox("That I can do.","adlington")
                Text.Textbox("Bling Tower Was Added to Your Map.","game")
                Map.Add("bling tower")
                Player.ran[45]=2
        if event==23:
            Text.Textbox("King Pooses Castle.  Population : 11,000","sign")
        if event==24:
            Text.Textbox("<--------- Bah Grylls Forest <--------- -----------> Bajers Town -----------> ^-------- Lord Baj's Temple --------^","sign")
        if event==25:
            if random.randint(0,10)==1:
                foe=["none",Enemy("runaway dog",10,3,2,1,5,["none",0,0],"physical","none"),"none","none","none"]
                if random.randint(0,10)==1:
                    foe[3]=Enemy("florb",2,2,2,2,5,["none",0,0],"magical","none")
                ret=Battle.Run(foe)
                Draw.Entity(Player.party[0].name,(6*64,4*64),(0,Player.direct*64,64,64))
                Text.Textbox(ret,"game")
                Music.ChangeSong(Player.worldname)
        if event==26:
            World.LoadWorld("baj templeopen",8,7)
            if Player.ran[16]==0:
                Draw.CutScene(5)
        if event==27:
            World.LoadWorld("baj forest",12,8)
        if event==28:
            if Player.ran[6]==0:
                Text.Textbox("I think the temple is up ahead.","omgchad")
                Player.direct=1
                Player.x,Player.y,events=Draw.Walk(Player.x,Player.y,Player.direct,Player.world,Player.events,World.collisionlist,Player.party[0].name,False,Player.speed)
            else:
                World.LoadWorld("bajers",2,4)
        if event==30:
            World.LoadWorld("lord bajs temple",2,3)
        if event==31:
            if random.randint(0,11)==10:
                enemy=random.randint(0,4)
                foe=["none","none","none","none","none"]
                if enemy==0 or enemy==1:
                    foe[2]=Enemy("florb",2,2,2,2,5,["none",0,0],"magical","none")
                if enemy==1:
                    foe[4]=Enemy("florb",2,2,2,2,5,["none",0,0],"magical","none")
                if enemy==2 or enemy==3 or enemy==4:
                    foe[3]=Enemy("baby spider",3,3,4,2,5,["none",0,0],"physical","none")
                if enemy==3:
                    foe[4]==Enemy("florb",2,2,2,2,5,["none",0,0],"magical","none")
                ret=Battle.Run(foe)
                Draw.Entity(Player.party[0].name,(6*64,4*64),(0,Player.direct*64,64,64))
                Text.Textbox(ret,"game")
                Music.ChangeSong(Player.worldname)
        if event==32:
            Text.Textbox("Would You Like to Read 50 Chades Of A?","game",False)
            pygame.time.wait(100)
            while True:
                var=Menu.Base(700,185,["Yes","No"],120,False)
                pygame.display.update()
                if var==0:
                    screen.fill((0,0,0))
                    Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0))
                    Draw.Entity(Player.party[0].name,(6*64,4*64),(0,Player.direct*64,64,64))
                    Text.Textbox("The nigth is dark chilling and hostile in the north of Sweden. A Viking tall and handsome steps out of the shower sriping wett of clean mounting spring water. He reatches for a towle to dry his still driping boddy. The mirror refects a smiling face that say you did a hell of a jobb ther buddy. Some one is shouting softly in the other end of teh home \"Com back here my big boy\" He slowly dry himself of and takes another glance at the mirror. The face looking back just got a big grin on on it and he say \"Time for the second act\" He steps out of the bathroom in is full frontal glory. Slowly walks towards the bedroom with a praude step. When he gets closer to the bedroom the voice once again shouts softly. \"There you are my BIG MAN\" The Viking takes the last few steps with stride. The bed rock like the sea when he leaps in to it for the waith of his boddy. Now we see the blond bomb shell who so sofly shouted at his earlier. She is a beauty like any Swedish girl. She smiles with a confident smile, knowing her lust for Falukorv will be fullfiled. The Viking smiles back tthen starts kissing gently. Breaths become deaper and the kissing becomes more heated. His hands flowing over her boddy like how your hand flow over a car with grate curves. There breaths become deper and quicker. She wispers i want it i want it now. So he reatches over to his nigth stand and grabs the remote. She gently press the Hdmi 1 button. The sweet sound of mindcrackers voices are heard its UHC 13 on the TV. She tells him \"my big man pleas just tell me how it ends\" He answers \"no darling i cant even tell you that. The End","book")
                    Menu.state=0
                    break
                elif var==1 or var==-1:
                    Menu.state=0 
                    break
        if event==33:
            World.LoadWorld("baj templein",6,13)
        if event==34:
            World.LoadWorld("lord bajs temple",5,2)
        if event==35:
            World.LoadWorld("baj cave",5,12)
        if event==36:
            if Player.ran[18]==0:
                Text.Textbox("What are you doing here? You dare challenge me? Haha, I will crush you!","bandit leader")
                foe=["none",Enemy("bandit",5.5,5,5,5,5,["none",0,0],"energy","Shield"),Enemy("bandit leader",4,4,6,2,5,["none",0,0],"energy"),Enemy("bandit",5.5,5,5,5,5,["none",0,0],"energy","Shield"),"none"]
                ret=Battle.Run(foe,"Battle2")
                Draw.Entity(Player.party[0].name,(6*64,4*64),(0,Player.direct*64,64,64))
                Text.Textbox(ret,"game")
                Music.ChangeSong(Player.worldname)
                Player.ran[18]=1
        if event==37:
            if Player.ran[8]==0:
                Text.Textbox("The Chest Contained a Claddagh Ring!","game")
                Player.inventory.append("claddagh ring")
                Player.ran[8]=1
            else:
                Text.Textbox("The Chest is Empty!","game")
        if event==38:
            if Player.ran[9]==0:
                Text.Textbox("The Chest Contained a Pink Enchant 4 Book!","game")
                Player.inventory.append("pink enchant 4")
                Player.ran[9]=1
            else:
                Text.Textbox("The Chest is Empty!","game")
        if event==39:
            Text.Textbox("R.I.P. Snuggles, pet to Arkas, friend to all. Murdered by AnderZEL.","grave")
        if event==40:
            Text.Textbox("R.I.P. Jerry, Wes Wilson never let him into PlayOnCon.","grave")
        if event==41:
            Text.Textbox("R.I.P. Giant Cactus, you will live on in our hearts far after you have dyed.","grave")
        if event==42:
            Text.Textbox("R.I.P. Ferris Mueller, who soared a little to high in the sky.","grave")
        if event==43:
            Text.Textbox("Would You Like to Read Mindcrack History?","game",False)
            pygame.time.wait(100)
            while True:
                var=Menu.Base(700,185,["Yes","No"],120,False)
                pygame.display.update()
                if var==0:
                    screen.fill((0,0,0))
                    Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0))
                    Draw.Entity(Player.party[0].name,(6*64,4*64),(0,Player.direct*64,64,64))
                    Text.Textbox("In the beginning there was peace in the Mindcrack world and a new friend was born into it. His name was BTC also known as Jarool to friends. Jarool had an insteresting past, most notably having fought at the past 3 World Fighting Championships under Kai and his trademark fighter. He learnt many techniques that a mortal shouldn't be allowed to learn however somehow he learnt them, this even impressed King Kai. However one day Jarool changed and used his powers not for good... but for evil. One day on the server generikb's mansion blew up - thankfully we managed to pass it by to the viewers as a charity \"event\" however it was really Jarool. Other events started occurring, Pyro's bookstore burnt down with no explination and things started disappearing. Everyone knew Jarool had become an Evil Karate Master. Sort of like Akuma from Street Fighter except not as cool. The server needed a saviour otherwise it would be doomed to destruction but who could said the server In comes Baj, a former war veteran who fought in the previous two Great Mindcrack Wars - he'd lost his arm and leg in them and opted into the first Minecraft bionics program which gave him extraordinary powers. Baj decided to stand up for Mindcrack and so one of the most epic battles in all of Mindcrack history occurred. It was over in a flash. Jarool lay on the floor and Baj walk on. The next day Guude knighted Baj on behalf of the server and he was known as Lord Baj. Some people refuse to acknowledge this such as Squire Old Man Willy but what does he know.","book")
                    Menu.state=0
                    break
                if var==-1 or var==1:
                    Menu.state=0 
                    break
        if event==44:
            Text.Textbox("\"When Life Gives You Melons\", sounds like a good read.","omgchad")
            Text.Textbox("Its lemons, Chad. When life gives you lemons.","guude")
            Text.Textbox("Oh.","omgchad")
        if event==45:
            Text.Textbox("UHC : The Battle Of Twin Peaks. Written By Seth Bling.","book")
        if event==46:
            Text.Textbox("Love and Grief. Written by Notch.","book")
        if event==47:
            Text.Textbox("Which Book Would You Like to Read?","game",False)
            pygame.time.wait(100)
            while True:
                var=Menu.Base(620,185,["Blue","Red","Yellow"],200,False)
                pygame.display.update()
                pygame.time.wait(15)
                if var==2:
                    World.LoadWorld("baj templechest",Player.x,Player.y)
                    Menu.state=0
                    break
                elif var==1:
                    Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0))
                    Draw.Entity(Player.party[0].name,(6*64,4*64),(0,Player.direct*64,64,64))
                    Text.Textbox("Great wisdom lies in this book. Positivity will guide you to sucess.","pyro")
                    Text.Textbox("Positivity and Matt Damon.","millbee")
                    Menu.state=0
                    break
                elif var==0:
                    Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0))
                    Draw.Entity(Player.party[0].name,(6*64,4*64),(0,Player.direct*64,64,64))
                    Text.Textbox("Under The Dome. Great book, horrible TV show.","guude")
                    Menu.state=0
                    break
        if event==48:
            try:
                wheat=Player.inventory.index("wheat")
                del Player.inventory[wheat]
                Player.ran[11]=1
            except:
                pass
            if Player.ran[11]==0:
                Text.Textbox("Guude. You are the leader of this group. Speak to Lord Baj.","pyro")
                Text.Textbox("Oh, ah, ya. Umm, Hey Baj, I need to know where Aurey, Coe, Vechs and Etho are. So... Guide the way, oh great one.","guude")
                Text.Textbox("...","guude")
                Text.Textbox("....","omgchad")
                Text.Textbox(".....","millbee")
                Text.Textbox("Holy hell, how long is this going to take!","millbee")
                Text.Textbox("It would appear Lord Baj wont talk to you. We may need an offering.","pyro")
                Text.Textbox("Where can we get an offering?","omgchad")
                Text.Textbox("We can head to Bajers, a small town that farms wheat to offer to Lord Baj.","pyro")
                Text.Textbox("Well lets get the fuck out of here then, this place is creepy.","guude")
                Player.ran[6]=1
            if Player.ran[11]==1:
                Text.Textbox("Lord Baj, we offer this up to you!","pyro")
                Text.Textbox("*munch munch* Just a second, hes coming.","2nd baj")
                Text.Textbox("Yes, Squire Pyro. Why do you call me?","1st baj")
                Text.Textbox("These great warriors have came to see you.","pyro")
                Text.Textbox("So ya, were looking for some people.","guude")
                Text.Textbox("Yes. I see. As you search, a girl is calling your name...","1st baj")
                Text.Textbox("Aurey. Where is she?","guude")
                Text.Textbox("She is far from here. She is imprisoned in the sky where she used to fly...","1st baj")
                Text.Textbox("Why are we always so cryptic? She's in her house up in a cloud.","2nd baj")
                Text.Textbox("Quiet! They always said you did nothing, thats not true! You wont shut your mouth!","1st baj")
                Text.Textbox("In a cloud? Got it! Let's go guys!","omgchad")
                Text.Textbox("Lord Baj, I feel I must accompany these warriors on their quest. I ask for your premission and blessing.","pyro")
                Text.Textbox("Squire Pyro, you will go with them. Use your wisdom and skills to help them find the people they search for and defeat the Dark One.","1st baj")
                Text.Textbox("YES! Finally the annoying peice of work is leaving!","2nd baj")
                Text.Textbox("SHUT UP.","1st baj")
                Text.Textbox("Aureylians Rainbow Castle Has Been Added to Your Map!","game")
                Player.ran[11]=2
                Map.Add("aureylians rainbow castle")
            if Player.ran[11]==2:
                Text.Textbox("*munch munch*...*munch munch*...","2nd baj")
        if event==49:
            World.LoadWorld("baj templeopen",8,2)
        if event==50:
            if Player.ran[10]==0:
                Text.Textbox("The Chest Contained a Controversy 4 Book!","game")
                Player.inventory.append("controversy 4")
                Player.ran[10]=1
            else:
                Text.Textbox("The Chest is Empty!","game")
        if event==51:
            if Player.ran[12]==0:
                Text.Textbox("The Chest Contained a Rainbow Explosion 4 Book!","game")
                Player.inventory.append("rainbow explosion 4")
                Player.ran[12]=1
            else:
                Text.Textbox("The Chest is Empty!","game")
        if event==52:
            World.LoadWorld("bajers1")
        if event==53:
            try:
                place=Player.inventory.index("claddagh ring")
                del Player.inventory[place]
                Text.Textbox("Can it be? you found my claddagh ring! It was stolen in the last bandit raid! Here, take this.","drew")
                Player.inventory.append("sythe")
                Text.Textbox(Player.party[0].name.title()+" Recieved a Sythe!","game")
                Player.ran[13]=1
            except:
                if Player.ran[13]==1:
                    Text.Textbox("Thanks for finding my ring!","drew")
                else:
                    Text.Textbox("My claddagh ring was stolen in the last bandit raid. I really wish I still had it.","drew")
        if event==54:
            if Player.ran[14]==0:
                Text.Textbox("Oh god! What is that thing!","millbee")
                Text.Textbox("It certainly is creepy...","omgchad")
                if Player.ran[15]==1:
                    Text.Textbox("Well, they said it comes alive at night. Guess we gotta to wait...","guude")
                    for i in range(0,20):
                        pygame.gfxdraw.box(screen, pygame.Rect(0,0,900,900), (0,0,0,i))
                        pygame.display.update()
                        pygame.time.wait(200)
                    Text.Textbox("Guys, its moving! Attack! BURN IT TO THE GROUND!","millbee")
                    foe=["none","none",Enemy("scarecrow",6,4,4,1,10,["none",0,0],"magical"),"none","none"]
                    ret=Battle.Run(foe,"Battle2")
                    Draw.Entity(Player.party[0].name,(6*64,4*64),(0,Player.direct*64,64,64))
                    Text.Textbox(ret,"game")
                    Music.ChangeSong(Player.worldname)
                    Player.ran[14]=1
                    Player.ran[15]=0
        if event==55:
            Menu.Shop(["spider eyes 2","impersonate 2","claymore","basic staff","rapier"],[700,700,300,400,400])
        if event==56:
            World.LoadWorld("bajers1",3,4)
        if event==57:
            World.LoadWorld("bajers2",3,4)
        if event==58:
            World.LoadWorld("bajers",7,4)
        if event==59:
            World.LoadWorld("bajers",10,4)
        if event==60:
            World.LoadWorld("lord bajs temple",7,3)
        if event==61:
            World.LoadWorld("bajers",14,4)
        if event==62:
            World.LoadWorld("bajers3",4,5)
        if event==63:
            if Player.ran[14]==1:
                if Player.ran[15]==0:
                    Text.Textbox("You did it! Now we can continue to farm for Lord Baj.","carl")
                    Text.Textbox("Great! Give us some.","millbee")
                    Text.Textbox("Right, you guys wanted some wheat to offer. Here.","carl")
                    Player.inventory.append("wheat")
                    Text.Textbox(Player.party[0].name.title()+" Received Wheat!","game")
                    Player.ran[15]=1
                if Player.ran[15]==1:
                    Text.Textbox("We can't thank you enough for what you've done for us.","carl")
            if Player.ran[14]==0:
                if Player.ran[15]==0:
                    Text.Textbox("Hey guy, could we get some wheat to offer up to lord baj?","guude")
                    Text.Textbox("I'm sorry, but we have no way to know you will really offer up the wheat. You might be here to steal from us.","carl")
                    Text.Textbox("Worry not. I will assure the wheat is used properly.","pyro")
                    Text.Textbox("Gaurdian! Well then, I would be happy to give you wheat, but our fields have been being terrorised by a haunted scarecrow that only comes to life during the night. We tried destroying it during the day, but it just put itself back together. If you could kill it, we would be able to give you wheat.","carl")
                    Text.Textbox("Lets go rekt some scarecrow then!","pyro")
                    Player.ran[15]=1
                if Player.ran[15]==1:
                    Text.Textbox("We cant do anything until someone takes care of that scarecrow.","carl")
        if event==64:
            if Player.ran[17]==0:
                Text.Textbox("Our horse is very sick... I dont know if he will make it...","grace")
                try:
                    place=Player.inventory.index("notch apple")
                    del Player.inventory[place]
                    Text.Textbox("Wow, that apples so pretty! Wait.. is that.. For The Horse? Thank you, I'm sure this will help him get better. Take this as my thanks. A girl with red hair gave it to me a few years ago.","grace")
                    Player.inventory.append("hair clip")
                    Text.Textbox(Player.party[0].name.title()+" Received a Hair Clip!","game")
                    Player.ran[17]=1
                except:
                    Text.Textbox("I'm very sorry to hear that.","omgchad")
            else:
                Text.Textbox("My horse is all better now!","grace")
        if event==65:
            World.LoadWorld("baj forest",2,3)
        if event==66:
            World.LoadWorld("aurey hall",8,6)
        if event==67:
            World.LoadWorld("aureylians rainbow castle",11,16)
        if event==68:
            World.LoadWorld("orphanage",10,5)
        if event==70:
            World.LoadWorld("boo room",6,4)
        if event==71:
            Text.Textbox("Boo's Room.","sign")
        if event==72:
            Text.Textbox("Aureylian's Room.","sign")
        if event==73:
            if Player.ran[21]==1:
                World.LoadWorld("aureylians room",1,5)
            else:
                World.LoadWorld("aureylian room",1,5)
                if Player.ran[22]==0:
                    Draw.CutScene(6)
                    Player.ran[22]=1
        if event==74:
            World.LoadWorld("aurey hall",13,3)
        if event==75:
            World.LoadWorld("aurey hall",3,3)
        if event==76:
            Text.Textbox("Of course I'll help you Guude, but I need me wand if you want me to be of any use. Its at a barn in Farm Land.","aureylian")
            if "pink wand" in Player.inventory:
                Text.Textbox("You got it? Great, I'll lead the way. Davion's base is through the trapdoor in the main hall.","aureylian")
                Text.Textbox("Aureylian Joined The Party!","game")
                Player.party.append(PartyMember.Create(PartyMember.FromFile("Aureylian")))
                for i in range(0,len(Player.party)):
                    Player.party[i].update()
                Player.ran[21]=1
                World.LoadWorld("aureylians room",1,3)
        if event==77:
            World.LoadWorld("barn in",7,7)
        if event==78:
            World.LoadWorld("barn",8,4)
        if event==79:
            if Player.ran[19]==0:
                Text.Textbox("The Chest Contained a Pink Wand!","game")
                Player.inventory.append("pink wand")
                Player.ran[19]=1
            else:
                Text.Textbox("The Chest is Empty!","game")
        if event==80:
            if Player.ran[20]==0:
                Text.Textbox("The Chest Contained a Hoe!","game")
                Player.inventory.append("hoe")
                Player.ran[20]=1
            else:
                Text.Textbox("The Chest is Empty!","game")
        if event==81:
            Text.Textbox("Moooo! Wait, no, Baaahhh!","sheep")
            Text.Textbox("You had one job...","guude")
        if event==82:
            Text.Textbox("Moo!","cow")
        if event==83:
            World.LoadWorld("aurey hall",2,4)
        if event==84:
            if Player.ran[23]==0:
                Text.Textbox("It's Locked.","game")
                if PartyMember.HaveMember("aureylian"):
                    Text.Textbox("Here, I can unlock it.","aureylian")
                    Player.ran[23]=1
            else:
                World.LoadWorld("vechs1",5,10)
        if event==85:
            possible=["flame venom spider","derp bat","baby spider","chipmonk"]
            left=[0,1,2,3,4]
            foe=["none","none","none","none","none"]
            if random.randint(0,10)==1:
                foe[2]=random.choice(possible)
                for i in left:
                    if random.randint(1,6)==1:
                        foe[i]=random.choice(possible)
                for i in range(0,5):
                    if foe[i]=="flame venom spider":
                        foe[i]=Enemy("flame venom spider",4,5,5,3,8,["none",0,0],"physical")
                    if foe[i]=="derp bat":
                        foe[i]=Enemy("derp bat",5,7,5,1,9,["none",0,0],"physical")
                    if foe[i]=="baby spider":
                        foe[i]=Enemy("baby spider",3,4,5,2,6,["none",0,0],"physical")
                    if foe[i]=="chipmonk":
                        foe[i]=Enemy("chipmonk",2,1,2,6,8,["none",0,0],"magical")
                Text.Textbox(Battle.Run(foe),"game")
        if event==86:
            World.LoadWorld("aurey hall",8,3)
        if event==87:
            World.LoadWorld("vechs2",5,6)
        if event==88:
            World.LoadWorld("vechs1",5,2)
        if event==89:
            World.LoadWorld("vechs3",1,6)
        if event==90:
            World.LoadWorld("vechs3",9,6)
        if event==91:
            World.LoadWorld("vechs2",1,2)
        if event==92:
            World.LoadWorld("vechs2",9,2)
        if event==93:
            World.LoadWorld("vechs4",2,4)
            if Player.ran[24]==0:
                Text.Textbox(Battle.Run(["none","none",Enemy("kamyu the hidden",9,4,3,2,12,["none",0,0],"magical"),"none","none"],"Battle2"),"game")
                Player.ran[24]=1
        if event==94:
            World.LoadWorld("vechs5",2,5)
            if Player.ran[25]==0:
                Text.Textbox(Battle.Run(["none","none",Enemy("dinnerbone the destroyer",7,3,4,2,12,["none",0,0],"energy"),"none","none"],"Battle2"),"game")
                Player.ran[25]=1
        if event==95:
            World.LoadWorld("vechs6",2,4)
            if Player.ran[26]==0:
                Text.Textbox(Battle.Run(["none","none",Enemy("codewarrior the instigator",6,5,5,5,12,["none",0,0],"physical"),"none","none"],"Battle2"),"game")
                Player.ran[26]=1
        if event==96:
            World.LoadWorld("vechs3",1,2)
        if event==97:
            World.LoadWorld("vechs3",5,2)
        if event==98:
            World.LoadWorld("vechs3",9,2)
        if event==99:
            if Player.ran[27]==0:
                Text.Textbox("Rellykins? What are you doing down here?","davion")
                Text.Textbox("Davion, I'm going with Guude to help him. Please, come with us. We need your help.","aureylian")
                Text.Textbox("Wait, Wha?","millbee")
                Text.Textbox("No Rel Rel. My mission here is to important. You have to stay for when it's ready.","davion")
                Text.Textbox("I need to help, whether you're coming or not.","aureylian")
                Text.Textbox("I can't allow that. I will crush your punny friends and show you the power we strive for! Mwahahaha! Haha! He he! he he..","davion")
                Text.Textbox(Battle.Run(["none",Enemy("derp bat",7,5,5,1,8,["none",0,0],"physical"),Enemy("davion",6,6,4,3,15,["none",0,0],"magical"),Enemy("derp bat",7,5,5,1,8,["none",0,0],"physical"),"none"],"Battle3"),"game")
                Player.ran[27]=1
                Text.Textbox("No.... FINE! GO. But come back...","davion")
                Text.Textbox("I will... Guys, lets go.","aureylian")
                Text.Textbox("Hmm.. Yes. Where are we of to now?","pyro")
                Text.Textbox("Doc's place. His luquid assim-i-la-thingy. He's a friend of Etho.","aureylian")
                Text.Textbox("Sounds like fun. Are there water slides?","millbee")
                Text.Textbox("Years ago, the land of Mindcrack was plagued with heavy rains. Doc created a giant water reserve and a magnetized machine to collect it all and stop the relentless rain.","pyro")
                Text.Textbox("Wait. He had enough water to create an ocean and he didnt make water slides?","millbee")
                Text.Textbox("So you think this Doc will know where Etho is?","guude")
                Text.Textbox("Etho went to his place after the great war. We have to hope he's still there.","aureylian")
                Text.Textbox("Docms Liquid Assimilator Was Added to Your Map.","game")
                Map.Add("docms liquid assimilator")
        if event==100:
            if money>=300:
                Text.Textbox("Let's Play!","guudeland")
                Minigames.Cards()
            else:
                Text.Textbox(Player.party[0].name.title()+" Doesnt Have Enough Money!","game")
        if event==101:
            if money>=100:
                Text.Textbox("Let's Play!","guudeland")
                Minigames.KingOfTheLadder()
            else:
                Text.Textbox(Player.party[0].name.title()+" Doesnt Have Enough Money!","game")
        if event==102:
            if money>=50:
                Text.Textbox("Let's Play!","guudeland")
                Minigames.EnchantWars()
            else:
                Text.Textbox(Player.party[0].name.title()+" Doesnt Have Enough Money!","game")
        if event==103:
            if Player.ran[37]==0:
                Text.Textbox("Anderz! Hey man, I'm heading out for a while.","docm")
                Text.Textbox("Yellolo Doc, Were you of to bud?","anderzel")
                Text.Textbox("Going to find Etho with these guys.","docm")
                Text.Textbox("Okey, talk to you latter.","anderzel")
                Text.Textbox("Wait, What's that?","omgchad")
                Text.Textbox("Oh no!","anderzel")
                Text.Textbox("A sea monster! Hmmm... Should I become Chad the lobster or Mr. Chad the Ice Packer?","omgchad")
                Text.Textbox("I dont care what the fuck you turn into, just kill it!","guude")
                Text.Textbox(Battle.Run(["none",Enemy("fish",3,4,3,1,11,["none",0,0],"physical"),Enemy("sea monster",7,4,4,1,14,["none",0,0],"magical"),Enemy("fish",3,4,3,1,11,["none",0,0],"physical"),"none"],"Battle2"),"game")
                Text.Textbox("Well, that was random.","millbee")
                Text.Textbox("You're one to speak...","guude")
                Text.Textbox("Yes, but with that taken care of we can head to the Mesa!","docm")
                Map.Add("mesa")
                Text.Textbox("The Mesa Was Added to Your Map.","game")
                Player.ran[37]=1
        if event==104:
            Player.direct=0
            Player.x,Player.y,events=Draw.Walk(Player.x,Player.y,Player.direct,Player.world,Player.events,World.collisionlist,Player.party[0].name,False,Player.speed)
            Text.Textbox("Umm, before we go in, you should know...","aureylian")
            Text.Textbox("What is it Aurey?","guude")
            Text.Textbox("Doc doesn't.. Look like you might imagine.","aureylian")
            Text.Textbox("How weird can he be. Does he bite string cheese? Wait, he doesnt stand to wipe, right?","pyro")
            Text.Textbox("I... don't know.","aureylian")
            Text.Textbox("Whhaaa? Isn't that the first thing you ask when you meet someone??","pyro")
            Text.Textbox("Dont worry Aurey, it will be fine.","guude")
            Draw.CutScene(7)
            Player.direct=1
        if event==105:
            if Player.ran[31]==0:
                Text.Textbox("The Chest Contained a Imperssionate 4 Book!","game")
                Player.inventory.append("imperssionate 4")
                Player.ran[31]=1
            else:
                Text.Textbox("The Chest is Empty!","game")
        if event==106:
            if Player.ran[32]==0:
                Text.Textbox("The Chest Contained a Alright Guys 4 Book!","game")
                Player.inventory.append("alright guys 4")
                Player.ran[32]=1
            else:
                Text.Textbox("The Chest is Empty!","game")
        if event==107:
            if Player.ran[33]==0:
                Text.Textbox("The Chest Contained a Compliment 4 Book!","game")
                Player.inventory.append("compliment 4")
                Player.ran[33]=1
            else:
                Text.Textbox("The Chest is Empty!","game")
        if event==108:
            if Player.ran[34]==0:
                Text.Textbox("The Chest Contained a Get Snacks 4 Book!","game")
                Player.inventory.append("get snacks 4")
                Player.ran[34]=1
            else:
                Text.Textbox("The Chest is Empty!","game")
        if event==109:
            if random.randint(0,6)==1:
                if random.randint(0,1)!=0:
                    Text.Textbox(Battle.Run(["none",Enemy("tumbleweed",13,4,3,2,15,["none",0,0],"physical"),Enemy("skeleton horse",5,4,7,1,14,["none",0,0],"energy"),Enemy("tumbleweed",13,4,3,2,15,["none",0,0],"physical"),"none"],"Battle1"),"game")
                else:
                    Text.Textbox(Battle.Run(["none","none",Enemy("lizard",9,4,4,2,15,["none",0,0],"physical"),"none","none"],"Battle1"),"game")
        if event==110:
            if Player.ran[43]==0:
                Text.Textbox("At the E-Team base dealing with the B-Team, be back soon. - Etho","sign")
                Text.Textbox("Hmmm.. Dealing with the B-Team at the \"E-Team Base\"? Wait, is today secret saturday?","guude")
                Text.Textbox("Oh no! I forgot the twix! What will we smoke?","pyro")
                Text.Textbox("No worries Pyro, I've always got extra. I was imprisoned under King Poose after all.","millbee")
                Text.Textbox("Guys. It's Tuesday.","aureylian")
                Text.Textbox("Guess it's been a long session. Hehehe.","guude")
                Text.Textbox("Hehe.. Haha..","millbee")
                Text.Textbox("Ahehehhahaheahahe!","guude")
                Text.Textbox("Aannyyyways, off to the E-Team Base!","omgchad")
                Text.Textbox("E-Team Base Was Added to Your Map.","game")
                Map.Add("e-team base")
                Player.ran[43]=1
            else:
                Text.Textbox("Off to the E-Team Base!","omgchad")
        if event==111:
            World.LoadWorld("mesa",15,16)
        if event==112:
            World.LoadWorld("mesa1",4,4)
        if event==113:
            if Player.ran[35]==0:
                Text.Textbox("The Chest Contained a Carrot Stick 4 Book!","game")
                Player.inventory.append("carrot stick 4")
                Player.ran[35]=1
            else:
                Text.Textbox("The Chest is Empty!","game")
        if event==114:
            if Player.ran[36]==0:
                World.LoadWorld("etho mesa",4,6)
            else:
                World.LoadWorld("etho nomesa",4,6)
        if event==115:
            Text.Textbox(Battle.Run(["none","none",Enemy("mesa deed trap",3,3,7,20,15,["none",0,0],"energy"),"none","none"],"Battle1"),"game")
            World.LoadWorld("etho nomesa",Player.x,Player.y)
        if event==116:
            World.LoadWorld("e-team base",9,2)
        if event==117:
            if Player.ran[38]==0:
                Text.Textbox("Aw! He's suck a cutie!","aureylian")
                Text.Textbox("Defense Mechanism Activated.","wilson")
                Text.Textbox("Oh no.","millbee")
                Text.Textbox(Battle.Run(["none","none",Enemy("wilson",7.5,5,6,0,20,["none",0,0],"energy"),"none","none"]),"game")
                Player.ran[38]=1
        if event==118:
            if Player.ran[39]==0:
                Text.Textbox("LEVEL 4 BOOK: NUMERICALLY, CODE IS EASY","wilson")
                if Menu.Passcode():
                    Text.Textbox(Player.party[0].name.title()+" Received a White Wool 4 Book!","game")
                    Player.inventory.append("white wool 4")
                    Player.ran[39]=1
                else:
                    Text.Textbox("ERROR: Invalid Code.","wilson")
            else:
                Text.Textbox("ERROR: Storage Empty.","wilson")
        if event==119:
            World.LoadWorld("etho nomesa",4,2)
        if event==120:
            World.LoadWorld("etho center",8,12)
        if event==121:
            if Player.ran[41]==0 and Player.ran[40]==1:
                Text.Textbox("Did you bring it?","etho")
                try:
                    hoe=Player.inventory.index("hoe")
                    Text.Textbox("Awesome, the hoe!","etho")
                    Text.Textbox("Wait... A hoe is E to the T to your mom? E to the T to the HO is Etho... Wow, I thought you were kid friendly.","millbee")
                    Text.Textbox("I'll turn of Wilson and leave a dummy of myself here, in case the B-Team comes back.","etho")
                    Text.Textbox("Wow, only a dummy would fall for that dummy.","guude")
                    Text.Textbox("Well we are talking about the B-Team.","docm")
                    Text.Textbox("Hehehehe.","guude")
                    Text.Textbox("Etho Joined The Party!","game")
                    Player.party.append(PartyMember.Create(PartyMember.FromFile("Etho")))
                    for i in range(0,len(Player.party)):
                        Player.party[i].update()
                    Text.Textbox("So.. Were are we going to next?","pyro")
                    Text.Textbox("I guess we should try to find Coe.","guude")
                    Text.Textbox("We should be able to find him at Coe Mountain.","docm")
                    Text.Textbox("How do you know?","omgchad")
                    Text.Textbox("Where else would Coe be but Coe Mountain?","docm")
                    Text.Textbox("Coe Mountain Was Added to Your Map.","game")
                    Player.ran[41]=1
                    Map.Add("coe mountain")
                except:
                    Text.Textbox("You dont have it yet.","etho")
            if Player.ran[40]==0:
                Text.Textbox("Hey! Etho!","aureylian")
                Text.Textbox("Aurey? Doc? Guude? What are you guys doing here?","etho")
                Text.Textbox("We need your help to fight off Nebris again. You free?","guude")
                Text.Textbox("Sure. All I've been doing is taking care of Wilson and watching Seinfeld. Oh, and The Office. The Office is a good show.","etho")
                Text.Textbox("Great! Will Wilson be okay if you come with us?","docm")
                Text.Textbox("Ya.. I just need the key to shut him down. Could you get it for me?","etho")
                Text.Textbox("Where is it?","aureylian")
                Text.Textbox("I'll give you a hint - E to the T to your mom.","etho")
                Player.ran[40]=1
        if event==122:
            possible=["instant damage potion","posion potion","sethwing","sethbot","sethwing","sethbot"]
            left=[0,1,2,3,4]
            foe=["none","none","none","none","none"]
            if random.randint(1,10)==1:
                foe[2]=random.choice(possible)
                for i in left:
                    if random.randint(1,6)==1:
                        foe[i]=random.choice(possible)
                for i in range(0,5):
                    if foe[i]=="instant damage potion":
                        foe[i]=Enemy("instant damage potion",1,5,6,15,["none",0,0],"magical")
                    if foe[i]=="posion potion":
                        foe[i]=Enemy("posion potion",1,5,6,15,["none",0,0],"magical")
                    if foe[i]=="sethwing":
                        foe[i]=Enemy("sethwing",4,3,4,6,14,["none",0,0],"physical")
                    if foe[i]=="sethbot":
                        foe[i]=Enemy("sethbot",5,5,5,5,16,["none",0,0],"energy")
                Text.Textbox(Battle.Run(foe),"game")
        if event==123:
            if Player.ran[42]==0:
                Text.Textbox("Hurry up you nimwit!","???")
                Text.Textbox("Who you callin nimwit?!","???")
                Text.Textbox("Hey Etho! You there?","docm")
                Text.Textbox("Hells blazes! We gotta go Genny!","???")
                Text.Textbox("Etho?","docm")
                Text.Textbox("Ah, Hey! It's Etho here! I'm kinda busy, come back later!","???")
                Text.Textbox("That doesnt sound like Etho..","guude")
                Text.Textbox("Well, I've got a cold, you see! Uh, ya.","???")
                effect = pygame.mixer.Sound('Files/Sounds/ThankYouGuude.wav')
                effect.play()
                Text.Textbox("Thank you Guude! You've almost made it! I'm EthosLab and welcome to my channel!","???")
                Text.Textbox("Bdubs, lets scat! Were already risking a lawsuit from Cat Fancy Home Delivery Service and The Bakery, we can't get caught here!","???")
                Player.ran[42]=1
        if event==124:
            if Player.ran[41]==1 and Player.ran[44]==0:
                print "xp"
        if event==125:
            World.LoadWorld("coe top",6,7)
        if event==126:
            if Player.ran[45]==0:
                Text.Textbox("Hey! It's Coe!","aureylian")
                Text.Textbox("Oh, hey guys.","coestar")
                Text.Textbox("We need your help. Nebris has escaped and is plotting something disastrous.","guude")
                Text.Textbox("How do you want me to help?","coestar")
                Text.Textbox("Well, come fight with us.","guude")
                Text.Textbox("Sorry guys, I gave up fighting a long time ago. After the battle 5 years ago, I settled down here.","coestar")
                Text.Textbox("Okay. This place seems really peaceful, I dont blame you.","aureylian")
                Text.Textbox("Wait! Dont we need this guy to win?","millbee")
                Text.Textbox("I'll give you a big mac if you come with us.","pyro")
                Text.Textbox("Coe, I understand that you want to stay here, but this is bigger than us both.","guude")
                Text.Textbox("How do you know that? Maybe Nebris is trying for a second chance, like me. You know, I've been pretty sucessful since I invented the first bucket with wheels.","coestar")
                Text.Textbox("I guess, I never really thought of that. Okay Coe, I guess we'll go then.","guude")
                Text.Textbox("Where are we off to now?","omgchad")
                Text.Textbox("I guess Nebris's Base, up in the north. Let's finish this.","guude")
                Text.Textbox("What about Vechs?","etho")
                Text.Textbox("We dont have any leads to where he could be, and we know how much time we have left. Besides, like Coe said we dont know there's going to be a fight.","guude")
                Text.Textbox("Even if there is, we can beat him!","omgchad")
                Text.Textbox("...","aureylian")
                Text.Textbox("Alright, lets go!","pyro")
                Player.ran[45]=1
            Text.Textbox("Good luck guys!","coestar")
        if event==127:
            World.LoadWorld("coe mountain",14,1)
        if event==128:
            if Player.ran[46]==1:
                Text.Textbox("Tell Pause to come visit some time!","vintagebeef")
            if Player.ran[46]==0:
                Text.Textbox("Hello, how may I help you? Oh, Etho! How are you son? You and Pause are so busy since he left and joined yip yip and the woodstick bandits, you never come to visit!","vintagebeef")
                Text.Textbox("Etho, is this your dad?","aureylian")
                Text.Textbox("No, my mom.","etho")
                Text.Textbox("Oh. Okay.","aureylian")
                Text.Textbox("Are these your friends? Please come in, I'll get some popsics and make some bifanas. Dont pretend you don't get your Cooking With Etho talent from me.","vintagebeef")
                Text.Textbox("Sorry, we're pretty busy and should be moving on.","etho")
                Text.Textbox("Oh, I understand. I used to adventure like you kids before I lost the use of my legs. Tell Pause to come visit some time!","vintagebeef")
                Text.Textbox("Okay mom.","etho")
                Player.ran[46]=1
        if event==129:
            Text.Textbox("It's Locked.","game")
        if event==130:
            Text.Textbox("Welcome to Bling Tower, what can I do for you?","sethbling")
            Text.Textbox("We are in need of your unrivaled redstone abilties.","aureylian")
            Text.Textbox("Well, rivaled by one.","docm")
            Text.Textbox("Hey, two! dont forget about me!","millbee")
            Text.Textbox("Hahaha! Hehehe!","guude")
            Text.Textbox("What are you laughing at? I'll fire you ass out of my TNT cannon you fuckboy! Look at Pyro, he doesn't know the first thing about redstone!","millbee")
            Text.Textbox("U WAT M8? I'll punish you for that, scrub!","pyro")
            Text.Textbox("Guys! Lets leave the redstone to the professionals!","omgchad")
            Text.Textbox("So what exactly do you need?","sethbling")
            Text.Textbox("We are trying to go to the ice plains in the north, but The Mindcrack Rail Network can't travel there. Can you upgrade the train to help us?","etho")
            Text.Textbox("Sure, I'll need to get my redstone kit from downstairs. We have had a bit of a pest problem, but we should be fine.","sethbling")
            Text.Textbox("Let's go!","omgchad")
            Text.Textbox("Sethbling Joined The Party!","game")
            Player.ran[47]=1
            Player.party.append(PartyMember.Create(PartyMember.FromFile("Sethbling")))
            for i in range(0,len(Player.party)):
                Player.party[i].update()
            World.LoadWorld("bling noseth",Player.x,Player.y)
        if event==131:
            if Player.ran[47]==0:
                World.LoadWorld("bling inside",5,8)
            else:
                World.LoadWorld("bling noseth",4,8)
        if event==132:
            World.LoadWorld("bling tower",7,7)
        if event==133:
            if Player.ran[47]==0:
                Text.Textbox("We should speak to Seth.","etho")
                Player.direct=2
                Player.x,Player.y,events=Draw.Walk(Player.x,Player.y,Player.direct,Player.world,Player.events,World.collisionlist,Player.party[0].name,False,Player.speed)
            else:
                World.LoadWorld("bling under",2,2)
        if event==134:
            World.LoadWorld("bling noseth",2,5)
        if event==135:
            if Player.ran[48]==0:
                Text.Textbox("The Chest Contained a Redstone Tool Kit!","game")
                Player.ran[48]=1
                Text.Textbox("Awesome! Is that all you need?","omgchad")
                Text.Textbox("Yep. I can upgrade it now, but it will take me a minute. Do you guys want me to get you some rooms? It look's like you've had a long journey.","sethbling")
                Text.Textbox("That would be super nice!","docm")
                Draw.Fade(50,150)
                Text.Textbox("Knock Knock Knock.","game","false")
                Text.Textbox("Knock Knock Knock.","game","false")
                Text.Textbox("Can you confirm you are awake?","sethbling","false")
                Text.Textbox("Fuck off Seth.","guude","false")
                Text.Textbox("Get up Guude. we're waiting for you.","aureylian","false")
                World.LoadWorld("bling inside",5,5)
            else:
                Text.Textbox("The Chest is Empty!","game")


        if event==150:
            if Player.ran[50]:
                Text.Textbox("Now Aurey! Finish it with your light magic!","omgchad")
                Text.Textbox("Wait. Maybe... Maybe we shouldn't. Maybe Nebris is right.","aureylian")
                Text.Textbox("Wwhhaa?","pyro")
                Text.Textbox("It's like you said Guude, no matter what happens we will always be together. This land is not Mindcrack, we are Mindcrack. No matter where we go, near or far, we will never lose that.","aureylian")
                Text.Textbox("You're right Aurey. We are Mindcrack. All of us here, all of us around the land, and all of them that cheered us on. Though we are all so different, we've come together.","guude")
                Text.Textbox("We support each other.","omgchad")
                Text.Textbox("We laugh with each other.","millbee")
                Text.Textbox("We do dank memes with each other.","pyro")
                Text.Textbox("We love each other.","aureylian")
                Text.Textbox("We help each other.","docm")
                Text.Textbox("We listen to each other.","etho")
                Text.Textbox("We talk to each other.","sethbling")
                Text.Textbox("We fight for each other.","vechs")
                Text.Textbox("Now, we've found peace and hapiness in each other. Wasn't that really always our quest, for peace? Not just our quest, The Quest.","guude")
            else:
                Text.Textbox("Now Aurey! Finish it with your light magic!","omgchad")
                Text.Textbox("Yes!","aureylian")
                Text.Textbox("No! All my work, gone. I just wanted to be the good guy. What can I do now?","nebris")
                Text.Textbox("Come back with us. We don't need a new world for people to forgive you. We can work this all out.","omgchad")
                Text.Textbox("Think of all you've created Nebris. People have to respect that, even if you cheated.","aureylian")
                Text.Textbox("I never cheated.","nebris")
                Text.Textbox("Hahahaha! Well Meme'd my friend! Oh you're not kidding?","pyro")
                Text.Textbox("I would love to have you at my place Nebris. We both think big.","docm")
                Text.Textbox("Me too! It would be like the good old derping, motherfuckin bread crumb, WHECK :V days.","vechs")
                Text.Textbox("Okay, Doc, that sounds cool.","nebris")
                Text.Textbox("What about me?","vechs")
                Text.Textbox("Never again Vechs. Never again.","nebris")
                Text.Textbox("Well, I guess that's everything sorted out. wow, we kinda saved the world. Thanks for your help, guys!","guude")
                Text.Textbox("It was an honor, Guude! I guess I'm going back to King Poose's army, just in time for fancy fridays! Where is everyone going now?","omgchad")
                Text.Textbox("I must return to dadbee, now that all the fun is over. Thanks for freeing me from prison, by the way.","millbee")
                Text.Textbox("I too must return to my lord. Hopefully he will be satisfied with my preformance, sometimes he's a little twofaced.","pyro")
                Text.Textbox("I'm going to head back to my castle. Unicorns and lost travellers don't feed themselves. Also Boo's coming back soon, I can't wait to see her.","aureylian")
                Text.Textbox("I guess my and Nebris will continue on my next big project. It's exciting to have someone to work with!","docm")
                Text.Textbox("Me and Seth have some plans. Setho is offically in business.","etho")
                Text.Textbox("Guess I'll just derp around and think of fun ways to make you all BURN MUAWHAHHAHA. Also I'm gonna adopt a kitty.","vechs")
                Text.Textbox("What about you, Guude?","aureylian")
                
            Draw.Credits()
        if event==151:
            if Player.ran[49]==1:
                Text.Textbox("Good luck!","pakratt")
            else:
                Text.Textbox("Wow! It's the great heros Guude and Aureylian!","pakratt")
                Text.Textbox("Hey. I don't remember you for the battle, how do you know us?","guude")
                Text.Textbox("I was there, I worked under Etho as a trap engineer. I just got wounded right at the start of the battle. Yet again, the first one out.. One of my traps did get someone though, a guy in a red hat and overalls. Anyways, why are you guys in Guudeland?","pakratt")
                Text.Textbox("Nebris escaped from his prison, we're tracking him down. Aurey though we might win some useful prizes here.","omgchad")
                Text.Textbox("Can I win a fedora?","pyro")
                Text.Textbox("So Nebris has escaped? I told them they should have made the cell out of furnaces... Well, you can definitely win some prizes that will prepare you for your upcoming battle. At current we have 3 games running, King of The Ladder, Enchant Wars and some card game you've never heard of. Good luck!","pakratt")
                Player.ran[49]=1
        if event==152:
            Text.Textbox("The Unicorn Stable is Closed for Construction.","sign")
    @staticmethod
    #Testing What Events Need to be Called
    def Test(x,y,type):
        x=x-1
        y=y-1
        run=False
        try:
            event=Player.events[y][x]
            event=event.replace("-"," ")
            event=event.split()
            if event[0]==type:
                Events.Call(int(event[3]))
                return True
        except:
            return False
class Menu:
    @staticmethod
    def Passcode():
        string=""
        run=True
        while True:
            Text.Write("Enter Code",(150,100),(255,255,255),"",True,80)
            Text.Write(string,(170,180),(255,255,255),"",True,80)
            if len(string)>8:
                return False
            if string=="511925":
                return True
            for event in pygame.event.get():
                if event.type==KEYDOWN:
                    if event.key==K_ESCAPE or event.key==K_d or event.key==K_d:
                        return False
                    if event.key==K_1 and run:
                        string=string+"1"
                        run=False
                    if event.key==K_2 and run:
                        string=string+"2"
                        run=False
                    if event.key==K_3 and run:
                        string=string+"3"
                        run=False
                    if event.key==K_4 and run:
                        string=string+"4"
                        run=False
                    if event.key==K_5 and run:
                        string=string+"5"
                        run=False
                    if event.key==K_6 and run:
                        string=string+"6"
                        run=False
                    if event.key==K_7 and run:
                        string=string+"7"
                        run=False
                    if event.key==K_8 and run:
                        string=string+"8"
                        run=False
                    if event.key==K_9 and run:
                        string=string+"9"
                        run=False
                if event.type==KEYUP:
                    run=True
    def BookShop(level=2):
        ret=[]
        counter=0
        while Player.party[0].abilitylevel[counter]!=0:
            ret.append(Player.party[0].abilities[counter]+" "+str(level))
            ret[-1]=ret[-1].lower()
            counter=counter+1
        return ret
    itemType={"pink wand":["weapon"],"hoe":["key"],"hair clip":["key"],"wheat":["key"],"impersonate 2":["book"],"spider eyes 2":["book"],"rapier":["weapon"],"basic staff":["weapon"],"sythe":["weapon"],"rainbow explosion 4":["book"],"controversy 4":["book"],"pink enchant 4":["book"],"claddagh ring":["key"],"notch apple":["key"],"newcomer 4":["book"],"fish bowl":["heal",20],"dominos":["heal",30],"basic sword":["weapon"],"basic wand":["weapon"],"basic gun":["weapon"],"":["none",0],"claymore":["weapon"],"chicken":["heal",50],"potato on a stick":["revive",1]}
    itemType["contagious laugh 2"]=["book"]
    itemType["contagious laugh 3"]=["book"]
    itemType["contagious laugh 4"]=["book"]
    itemType["spider eyes 2"]=["book"]
    itemType["spider eyes 3"]=["book"]
    itemType["spider eyes 4"]=["book"]
    itemType["boulderfist 2"]=["book"]
    itemType["boulderfist 3"]=["book"]
    itemType["boulderfist 4"]=["book"]
    itemType["service bat 2"]=["book"]
    itemType["service bat 3"]=["book"]
    itemType["service bat 4"]=["book"]
    itemType["controversy 2"]=["book"]
    itemType["controversy 3"]=["book"]
    itemType["controversy 4"]=["book"]
    itemType["never nude 2"]=["book"]
    itemType["never nude 3"]=["book"]
    itemType["never nude 4"]=["book"]
    itemType["golden throw 2"]=["book"]
    itemType["golden throw 3"]=["book"]
    itemType["golden throw 4"]=["book"]
    itemType["all alone 2"]=["book"]
    itemType["all alone 3"]=["book"]
    itemType["all alone 4"]=["book"]
    itemType["newcomer 2"]=["book"]
    itemType["newcomer 3"]=["book"]
    itemType["newcomer 4"]=["book"]
    itemType["waffles claw 2"]=["book"]
    itemType["waffles claw 3"]=["book"]
    itemType["waffles claw 4"]=["book"]
    itemType["collab 2"]=["book"]
    itemType["collab 3"]=["book"]
    itemType["collab 4"]=["book"]
    itemType["recap 2"]=["book"]
    itemType["recap 3"]=["book"]
    itemType["recap 4"]=["book"]
    itemType["magic trick 2"]=["book"]
    itemType["magic trick 3"]=["book"]
    itemType["magic trick 4"]=["book"]
    itemType["dyslexia 2"]=["book"]
    itemType["dyslexia 3"]=["book"]
    itemType["dyslexia 4"]=["book"]
    itemType["fiery hair 2"]=["book"]
    itemType["fiery hair 3"]=["book"]
    itemType["fiery hair 4"]=["book"]
    itemType["optimism 2"]=["book"]
    itemType["optimism 3"]=["book"]
    itemType["optimism 4"]=["book"]
    itemType["chocolate knees 2"]=["book"]
    itemType["chocolate knees 3"]=["book"]
    itemType["chocolate knees 4"]=["book"]
    itemType["orange wool 2"]=["book"]
    itemType["orange wool 3"]=["book"]
    itemType["orange wool 4"]=["book"]
    itemType["rainbow explosion 2"]=["book"]
    itemType["rainbow explosion 3"]=["book"]
    itemType["rainbow explosion 4"]=["book"]
    itemType["dadbee aid 2"]=["book"]
    itemType["dadbee aid 3"]=["book"]
    itemType["dadbee aid 4"]=["book"]
    itemType["free millbee 2"]=["book"]
    itemType["free millbee 3"]=["book"]
    itemType["free millbee 4"]=["book"]
    itemType["date through 2"]=["book"]
    itemType["date through 3"]=["book"]
    itemType["date through 4"]=["book"]
    itemType["randomness 2"]=["book"]
    itemType["randomness 3"]=["book"]
    itemType["randomness 4"]=["book"]
    itemType["summon melon 2"]=["book"]
    itemType["summon melon 3"]=["book"]
    itemType["summon melon 4"]=["book"]
    itemType["imperssionate 2"]=["book"]
    itemType["imperssionate 3"]=["book"]
    itemType["imperssionate 4"]=["book"]
    itemType["tackle 2"]=["book"]
    itemType["tackle 3"]=["book"]
    itemType["tackle 4"]=["book"]
    itemType["green shell 2"]=["book"]
    itemType["green shell 3"]=["book"]
    itemType["green shell 4"]=["book"]
    itemType["game theory 2"]=["book"]
    itemType["game theory 3"]=["book"]
    itemType["game theory 4"]=["book"]
    itemType["meditate 2"]=["book"]
    itemType["meditate 3"]=["book"]
    itemType["meditate 4"]=["book"]
    itemType["360 no scope 2"]=["book"]
    itemType["360 no scope 3"]=["book"]
    itemType["360 no scope 4"]=["book"]
    itemType["triforce 2"]=["book"]
    itemType["triforce 3"]=["book"]
    itemType["triforce 4"]=["book"]
    itemType["final smash 2"]=["book"]
    itemType["final smash 3"]=["book"]
    itemType["final smash 4"]=["book"]
    itemType["pink enchant 2"]=["book"]
    itemType["pink enchant 3"]=["book"]
    itemType["pink enchant 4"]=["book"]
    itemType["rude! 2"]=["book"]
    itemType["rude! 3"]=["book"]
    itemType["rude! 4"]=["book"]
    itemType["compliment 2"]=["book"]
    itemType["compliment 3"]=["book"]
    itemType["compliment 4"]=["book"]
    itemType["lullaby 2"]=["book"]
    itemType["lullaby 3"]=["book"]
    itemType["lullaby 4"]=["book"]
    itemType["sparkle 2"]=["book"]
    itemType["sparkle 3"]=["book"]
    itemType["sparkle 4"]=["book"]
    itemType["glitter 2"]=["book"]
    itemType["glitter 3"]=["book"]
    itemType["glitter 4"]=["book"]
    itemType["christmas 2"]=["book"]
    itemType["christmas 3"]=["book"]
    itemType["christmas 4"]=["book"]
    itemType["rainbow swirl 2"]=["book"]
    itemType["rainbow swirl 3"]=["book"]
    itemType["rainbow swirl 4"]=["book"]
    itemType["doc block 2"]=["book"]
    itemType["doc block 3"]=["book"]
    itemType["doc block 4"]=["book"]
    itemType["alright guys 2"]=["book"]
    itemType["alright guys 3"]=["book"]
    itemType["alright guys 4"]=["book"]
    itemType["carrot stick 2"]=["book"]
    itemType["carrot stick 3"]=["book"]
    itemType["carrot stick 4"]=["book"]
    itemType["german efficiency 2"]=["book"]
    itemType["german efficiency 3"]=["book"]
    itemType["german efficiency 4"]=["book"]
    itemType["witch farm 2"]=["book"]
    itemType["witch farm 3"]=["book"]
    itemType["witch farm 4"]=["book"]
    itemType["villager farm 2"]=["book"]
    itemType["villager farm 3"]=["book"]
    itemType["villager farm 4"]=["book"]
    itemType["nerfed 2"]=["book"]
    itemType["nerfed 3"]=["book"]
    itemType["nerfed 4"]=["book"]
    itemType["breaking bedrock 2"]=["book"]
    itemType["breaking bedrock 3"]=["book"]
    itemType["breaking bedrock 4"]=["book"]
    itemType["get snacks 2"]=["book"]
    itemType["get snacks 3"]=["book"]
    itemType["get snacks 4"]=["book"]
    itemType["redstone 2"]=["book"]
    itemType["redstone 3"]=["book"]
    itemType["redstone 4"]=["book"]
    itemType["broken clay 2"]=["book"]
    itemType["broken clay 3"]=["book"]
    itemType["broken clay 4"]=["book"]
    itemType["uhc kill 2"]=["book"]
    itemType["uhc kill 3"]=["book"]
    itemType["uhc kill 4"]=["book"]
    itemType["general spaz 2"]=["book"]
    itemType["general spaz 3"]=["book"]
    itemType["general spaz 4"]=["book"]
    itemType["breach 2"]=["book"]
    itemType["breach 3"]=["book"]
    itemType["breach 4"]=["book"]
    itemType["anvil drop 2"]=["book"]
    itemType["anvil drop 3"]=["book"]
    itemType["anvil drop 4"]=["book"]
    itemType["death games 2"]=["book"]
    itemType["death games 3"]=["book"]
    itemType["death games 4"]=["book"]
    itemType["white wool 2"]=["book"]
    itemType["white wool 3"]=["book"]
    itemType["white wool 4"]=["book"]
    itemType["lime wool 2"]=["book"]
    itemType["lime wool 3"]=["book"]
    itemType["lime wool 4"]=["book"]
    itemType["pink wool 2"]=["book"]
    itemType["pink wool 3"]=["book"]
    itemType["pink wool 4"]=["book"]
    itemType["grey wool 2"]=["book"]
    itemType["grey wool 3"]=["book"]
    itemType["grey wool 4"]=["book"]
    itemType["brown wool 2"]=["book"]
    itemType["brown wool 3"]=["book"]
    itemType["brown wool 4"]=["book"]
    itemType["red wool 2"]=["book"]
    itemType["red wool 3"]=["book"]
    itemType["red wool 4"]=["book"]
    itemType["black wool 2"]=["book"]
    itemType["black wool 3"]=["book"]
    itemType["black wool 4"]=["book"]
    itemType["victory monument 2"]=["book"]
    itemType["victory monument 3"]=["book"]
    itemType["victory monument 4"]=["book"]
    itemType["sock'em 2"]=["book"]
    itemType["sock'em 3"]=["book"]
    itemType["sock'em 4"]=["book"]
    itemType["health pack 2"]=["book"]
    itemType["health pack 3"]=["book"]
    itemType["health pack 4"]=["book"]
    itemType["cloud glitch 2"]=["book"]
    itemType["cloud glitch 3"]=["book"]
    itemType["cloud glitch 4"]=["book"]
    itemType["zombie raid 2"]=["book"]
    itemType["zombie raid 3"]=["book"]
    itemType["zombie raid 4"]=["book"]
    itemType["redstone challenge 2"]=["book"]
    itemType["redstone challenge 3"]=["book"]
    itemType["redstone challenge 4"]=["book"]
    itemType["explosive mine 2"]=["book"]
    itemType["explosive mine 3"]=["book"]
    itemType["explosive mine 4"]=["book"]
    itemType["detnator 2"]=["book"]
    itemType["detnator 3"]=["book"]
    itemType["detnator 4"]=["book"]
    itemType["lightning missile 2"]=["book"]
    itemType["lightning missile 3"]=["book"]
    itemType["lightning missile 4"]=["book"]
    state=0
    wait=10
    down=0
    hold=0
    @staticmethod
    def Base(x,y,options,length,clear=True,space=70,xshift=20,update=True,color=False):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        Menu.wait=Menu.wait-1
        pygame.event.pump()
        pressed=pygame.key.get_pressed()
        if pressed[K_DOWN] and Menu.state<len(options)-1 and Menu.wait<0:
            Menu.state=Menu.state+1
            Menu.wait=10
        if pressed[K_UP] and Menu.state>0 and Menu.wait<0:
            Menu.state=Menu.state-1
            Menu.wait=10
        Draw.Entity(pygame.transform.scale(Draw.images["playerbox"],(length,len(options)*space+5)),(x,y),[0,0,0,0],False,False)
        Draw.Entity("pointer",(x+xshift,Menu.state*space+y+10),[0,0,0,0],True,False)
        for i in range(0,len(options)):
            if color:
                Text.Write(options[i],(x+xshift+20,y+(i*space)+15),(0,0,0),(options[i].lower()).replace(" ",""),False)
            else:
                Text.Write(options[i],(x+xshift+20,y+(i*space)+15),(0,0,0),"",False)
        if update:
            pygame.display.update()
        if pressed[K_s] and Menu.wait<0:
            if clear:
                Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0),False)
                Draw.Entity(Player.party[0].name,(6*64,4*64),(0,Player.direct*64,64,64),True,False)
            Menu.wait=10
            return -1
        if pressed[K_d] and Menu.wait<0:
            if clear:
                Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0),False)
                Draw.Entity(Player.party[0].name,(6*64,4*64),(0,Player.direct*64,64,64),True,False)
            Menu.wait=10
            return Menu.state
        return "pass"
    @staticmethod
    def Weapon(weapon,cost=0):
        run=True
        while run:
            clock.tick(60)
            names=[]
            for i in range(0,len(Player.party)):
                names.append(" ")
            var=Menu.Base(0,0,names,150,False,80,20,False)
            for i in range(0,len(Player.party)):
                Draw.Entity(Player.party[i].name+"face",(50,i*75+10),[0,0,0,0],True,False)
            Draw.Entity(pygame.transform.scale(Draw.images["playerbox"],(690,320)),(155,0),[0,0,0,0],False,False)
            if PartyMember.weapontype[weapon]==Player.party[Menu.state].type:
                Text.Write(weapon.title(),(530,20),(100,100,100),"",False)
                Text.Write(Player.party[Menu.state].weapon.title(),(190,20),(100,100,100),"",False)
                Text.Write("Attack:  "+`Player.party[Menu.state].weaponattack`+"       "+`PartyMember.weapontoattack[weapon]`,(180,80),(0,0,0),"",False)
                Text.Write("Evade:   "+`Player.party[Menu.state].weaponevade`+"       "+`PartyMember.weapontoevade[weapon]`,(180,140),(0,0,0),"",False)
                Text.Write("Speed:   "+`Player.party[Menu.state].weaponspeed`+"       "+`PartyMember.weapontospeed[weapon]`,(180,200),(0,0,0),"",False)
                Text.Write("Block:   "+`Player.party[Menu.state].weaponblock`+"       "+`PartyMember.weapontoblock[weapon]`,(180,260),(0,0,0),"",False)
                value=0
                if Player.party[Menu.state].weaponattack<PartyMember.weapontoattack[weapon]:
                    value=value-1
                    Draw.Entity("up",(470,72),[0,0,0,0],True,False)
                elif Player.party[Menu.state].weaponattack>PartyMember.weapontoattack[weapon]:
                    value=value+1
                    Draw.Entity("down",(470,72),[0,0,0,0],True,False)
                else:
                    Draw.Entity("equal",(470,72),[0,0,0,0],True,False)
                if Player.party[Menu.state].weaponevade<PartyMember.weapontoevade[weapon]:
                    value=value-1
                    Draw.Entity("up",(470,132),[0,0,0,0],True,False)
                elif Player.party[Menu.state].weaponevade>PartyMember.weapontoevade[weapon]:
                    value=value+1
                    Draw.Entity("down",(470,132),[0,0,0,0],True,False)
                else:
                    Draw.Entity("equal",(470,132),[0,0,0,0],True,False)
                if Player.party[Menu.state].weaponspeed<PartyMember.weapontospeed[weapon]:
                    value=value-1
                    Draw.Entity("up",(470,192),[0,0,0,0],True,False)
                elif Player.party[Menu.state].weaponspeed>PartyMember.weapontospeed[weapon]:
                    value=value+1
                    Draw.Entity("down",(470,192),[0,0,0,0],True,False)
                else:
                    Draw.Entity("equal",(470,192),[0,0,0,0],True,False)
                if Player.party[Menu.state].weaponblock<PartyMember.weapontoblock[weapon]:
                    value=value-1
                    Draw.Entity("up",(470,252),[0,0,0,0],True,False)
                elif Player.party[Menu.state].weaponblock>PartyMember.weapontoblock[weapon]:
                    value=value+1
                    Draw.Entity("down",(470,252),[0,0,0,0],True,False)
                else:
                    Draw.Entity("equal",(470,252),[0,0,0,0],True,False)
                    
                if value==0:
                    Draw.Entity("equal",(470,12),[0,0,0,0],True,False)
                elif value>0:
                    Draw.Entity("down",(470,12),[0,0,0,0],True,False)
                elif value<0:
                    Draw.Entity("up",(470,12),[0,0,0,0],True,False)
                pygame.display.update()
            else:
                Text.Write("       Cant Equip",(300,20))
            if var!=-1 and var!="pass" and PartyMember.weapontype[weapon]==Player.party[Menu.state].type:
                if Player.money>=cost:
                    Player.inventory.append(Player.party[Menu.state].weapon)
                    Player.party[Menu.state].weapon=weapon
                    Player.party[Menu.state].update()
                    if cost==0:
                        del Player.inventory[Player.inventory.index(weapon)]
                    Menu.state=Menu.hold
                    Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0),False)
                    Draw.Entity(Player.party[0].name,(6*64,4*64),(0,Player.direct*64,64,64),True,False)
                    Player.money=Player.money-cost
                else:
                    Text.Textbox("Not Enough Money!","game")
                run=False
            if var==-1:
                Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0),False)
                Draw.Entity(Player.party[0].name,(6*64,4*64),(0,Player.direct*64,64,64),True,False)
                Menu.state=Menu.hold
                run=False
    @staticmethod
    def Item(item):
        stats=Menu.itemType[item]
        run=True
        while run:
            pygame.display.update()
            names=[]
            for i in range(0,len(Player.party)):
                names.append("     "+`Player.party[i].currenthp`+"/"+`Player.party[i].hp`)
            var=Menu.Base(0,0,names,400,False,80,20,False)
            for i in range(0,len(Player.party)):
                Draw.Entity(Player.party[i].name+"face",(50,i*75+10),[0,0,0,0],True,False)
            clock.tick(60)
            if var==-1:
                run=False
            if var!=-1 and var!="pass":
                if stats[0]=="heal":
                    if Player.party[var].currenthp!=0:
                        Player.party[var].currenthp=Player.party[var].currenthp+stats[1]
                        if Player.party[var].currenthp>Player.party[var].hp:
                            Player.party[var].currenthp=Player.party[var].hp
                        Text.Textbox("Healed "+Player.party[var].name.title()+" "+`stats[1]`+" HP!","game")
                    else:
                        Text.Textbox(Player.party[var].name.title()+" can't be healed!","game")
                    del Player.inventory[Player.inventory.index(item)]
                if stats[0]=="revive":
                    if Player.party[var].currenthp==0:
                        Player.party[var].currenthp=stats[1]
                        Text.Textbox(Player.party[var].name.title()+" has been revived.","game")
                    else:
                        Text.Textbox(Player.party[var].name.title()+" is not downed!","game")
                    del Player.inventory[Player.inventory.index(item)]
                Menu.state=Menu.hold
                break
    @staticmethod
    def Book(book):
        book=book.title()
        if book=="Uhc Kill":
            book=="UHC Kill"
        if book=="Rude!":
            book="RUDE!"
        person=-1
        name="".join(book[:-2])
        level=int(book[-1])
        for i in range(0,len(Player.party)):
            if name in Player.party[i].abilities:
                person=i
        if person!=-1:
            place=Player.party[person].abilities.index(name)
            abilities.AbilityCool[name]=abilities.AbilityLevels[name+str(level)][0]
            if Player.party[person].abilitylevel[place]!=0:
                Player.party[person].abilitylevel[place]=level
                del Player.inventory[Player.inventory.index(book.lower())]
    @staticmethod
    def Section(type):
        ret=[]
        for i in range(0,len(Player.inventory)):
            if Menu.itemType[Player.inventory[i]][0]==type:
                ret.append(Player.inventory[i])
            if type=="item":
                if Menu.itemType[Player.inventory[i]][0]=="heal" or Menu.itemType[Player.inventory[i]][0]=="revive":
                    ret.append(Player.inventory[i])
        return ret
    @staticmethod
    def Inventory(inventory):
        display=[]
        newdisplay=[]
        for i in range(0,len(inventory)):
            display.append(inventory[i])
        if len(display)<Menu.down+8:
            display=display[Menu.down:]
        else:
            display=display[Menu.down:Menu.down+8]
        display=[item.title() for item in display]
        for i in range(0,len(display)):
            if display[i]=="Uhc Kill":
                display[i]=="UHC Kill"
        display.append("")
        display=[""]+display
        for i in range(0,len(display)):
            newdisplay.append("     "+display[i])
        var=Menu.Base(300,0,newdisplay,500,clear=True,space=70,xshift=20,update=False)
        for i in range(0,len(display)):
            if display[i]!="":
                Draw.Entity(Menu.itemType[display[i].lower()][0],(340,i*70),[0,0,0,0],True,False)
        if Menu.state==0 and Menu.down!=0:
            Menu.down=Menu.down-1
            Menu.state=Menu.state+1
        elif Menu.state==9 and Menu.down+8!=len(inventory):
            Menu.down=Menu.down+1
            Menu.state=Menu.state-1
        elif Menu.state==len(inventory)+1:
            Menu.state=Menu.state-1
        elif Menu.state==0:
            Menu.state=1
        elif Menu.state==9:
            Menu.state=8
        else:
            pygame.display.update()
        if var==-1:
            Player.Current="inventory"
            Menu.state=0
            Menu.down=0
            Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0),False)
            Draw.Entity(Player.party[0].name,(6*64,4*64),[0,Player.direct*64,64,64],True,False)
        if var!=-1 and var!="pass":
            if Menu.itemType[display[Menu.state].lower()][0]=="heal" or Menu.itemType[display[Menu.state].lower()][0]=="revive":
                Menu.hold=Menu.state
                Menu.state=0
                Menu.Item(display[Menu.hold].lower())
            elif Menu.itemType[display[Menu.state].lower()][0]=="weapon":
                    Menu.hold=Menu.state
                    Menu.state=0
                    Menu.Weapon(display[Menu.hold].lower())
            elif Menu.itemType[display[Menu.state].lower()][0]=="book":
                Menu.Book(display[Menu.state])
    @staticmethod
    def Shop(items,cost):
        clock=pygame.time.Clock()
        while True:
            clock.tick(60)
            display=[]
            for i in range(0,len(items)):
                display.append("     "+items[i].title().ljust(20)+`cost[i]`+"G")
            display=["Money: "+str(Player.money)+"G"]+display
            var=Menu.Base(0,0,display,700,clear=True,space=70,xshift=20,update=False)
            if var!="pass":
                var=var-1
                if var==-1:
                    var="pass"
            for i in range(1,len(items)+1):
                Draw.Entity(Menu.itemType[items[i-1]][0],(50,i*70-2),[0,0,0,0],True,False)
            pygame.display.update()
            if var==-2:
                Menu.state=0
                break
            if var!=-2 and var!="pass":
                Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0),False)
                Draw.Entity(Player.party[0].name,(6*64,4*64),[0,Player.direct*64,64,64],True,False)
                if Menu.itemType[items[var]][0]=="weapon":
                    Menu.state=0
                    Menu.Weapon(items[var],cost[var])
                    Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0),False)
                    Draw.Entity(Player.party[0].name,(6*64,4*64),[0,Player.direct*64,64,64],True,False)
                elif Menu.itemType[items[var]][0]=="heal" or Menu.itemType[items[var]][0]=="revive" or Menu.itemType[items[var]][0]=="book" or Menu.itemType[items[var]][0]=="key":
                    if Player.money>=cost[var]:
                        Player.inventory.append(items[var])
                        Player.money=Player.money-cost[var]
                        Text.Textbox(Player.party[0].name.title()+" Bought a "+items[var].title()+"!","game")
                    else:
                        Text.Textbox("Not Enough Money!","game")
    @staticmethod
    def MainScreen():
        i=0
        clock = pygame.time.Clock()
        new=False
        run=True
        while run:
            Draw.Entity("load",(0,0),[0,0,0,0],True,False)
            clock.tick(60)
            i=i+1
            party=[]
            if new:
                pygame.draw.rect(screen, (90,90,90),(480,530,300,70),3)
            else:
                pygame.draw.rect(screen, (90,90,90),(480,430,300,70),3)
            Text.Write("Load Game",(600,450),(0,0,0),"",False)
            Text.Write(" New Game",(600,550),(0,0,0),"",False)
            Text.Write("This Game is a Fan Made Creation and in no Way Associated with Mindcrack",(3,690),(0,0,0),"",False,15)
            Text.Write("D to Confirm, S to Cancel, Arrow Keys to Move",(3,675),(0,0,0),"",False,15)
            fi=[line.strip() for line in open("Files/Save/Players.txt")]
            for j in range(0,len(fi)/7):
                party.append(fi[j*7])
            for  x in range(0,len(party)):
                Draw.Entity(party[x],(x*90+20,610),[math.floor(i/20)%4*64,0,64,64],True,False)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==KEYDOWN:
                    if event.key==K_DOWN:
                        new=True
                    if event.key==K_UP:
                        new=False
                    if event.key==K_d:
                        if new==False:
                            try:
                                Save.Load()
                                run=False
                            except:
                                Text.Textbox("A save has not yet been created or has been corrupted.","game",False)
                        else:
                            Save.New()
                            run=False
Player.volume=2
pygame.display.set_caption("Mindcrack : The Quest")
pygame.display.set_icon(Draw.images["logo"])
Player.move=False
clock = pygame.time.Clock()
Save.Load()
Map.Add("bling tower")
Map.Add("coe mountain")
World.LoadWorld("aurey hall",5,5)
#Text.Textbox(Battle.Run(["none","none",Enemy("wilson",6,5,6,0,20,["none",0,0],"energy"),"none","none"],"Battle1"),"game")
Draw.Tiles(Player.x,Player.y,Player.world,Player.events,(0,0),False)
Draw.Credits()
while True:
    Player.Inworld()
