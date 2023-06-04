import random, os, time, getpass, json  



################################### HLAVNÍ MENU ###################################

continue_in_game = "New Game-1\nLoad Game-2\nQuit-3"
menu_choose = ""
damager = 0
run = 0
dodge = 0


def menu():    
    while True:
        global continue_in_game,menu_choose,money_lost
        os.system("cls") 
        global menu_choose 
        print(continue_in_game)

        try:
            menu_choose = input("> ")
        except ValueError:
            continue #zopakuje akci inputu a printu jestliže je špatně zadaný input
        if "0" in continue_in_game: 
            if menu_choose == "0":        
                break
        if menu_choose == "1":  
            global money,xp_gain,xp_need_max, level 
            global as_crit, as_luck, ma_crit, ma_luck
            global wa_crit, wa_luck, ar_crit
            global ar_luck, armor_list, order_list
            global armor0_list,weapon_list,weapon0_list,inventory
            global armor_input_global,weapon_input_global
            global odlozene_itemy,items_damage,items_armor,items_health
            global inventory_equip,level_point
            global armor_upgrade, crits_upgrade, health_upgrade, damage_upgrade, luck_upgrade

            inventory_equip={
                "chestplate":"none",
                "helmet":"none",
                "chausses":"none",
                "boots":"none",
                "gloves":"none",
                "weapon":"none"
                            }

            level_point =0
            items_armor=0
            items_health=0
            items_damage =0
            odlozene_itemy = {}
            weapon_input_global = 0    
            armor_input_global = 0
            inventory = {}
            weapon_list=[]
            weapon0_list=[]
            armor0_list = []
            order_list=[]
            armor_list = []
            xp_gain = 0
            xp_need_max = 100          
            money = 2000
            level = 0
            money_lost = 0
            as_crit = 9
            as_luck = 5
            ma_crit=1
            ma_luck=7
            wa_crit=2
            wa_luck=1
            ar_crit=4
            ar_luck=3
            armor_upgrade=0
            damage_upgrade=0
            health_upgrade=0
            luck_upgrade=0
            crits_upgrade=0
            

            break #ukončí smyčku while True 
        if menu_choose == "3":
            exit()
            
menu()

def while_menu():

    ################################### LIST CHARAKTERŮ ###################################
   
    
    global continue_in_game
    while menu_choose == "1":     
        if "0"in menu_choose: #objeví se později v kódu 
            if menu_choose == "0":
                break    
        os.system('cls')
        characters =  ["Warrior","Mage","Archer","Assassin"]
        charactersprint = ("Warrior\nMage\nArcher\nAssassin")

        ################################### VÝBĚR CHARAKTERŮ ###################################

        print(charactersprint,"\n\nPlease Choose one character ")
        global characterchoose
        characterchoose=input("> ").lower().title().strip()

        while characterchoose not in characters:
            os.system("cls")
            print(charactersprint)
            characterchoose=input("\nPLEASE CHOOSE ONE CHARACTER: ").lower().title().strip() #není-li input v characteru 
        print("Your character has been successfuly selected")
        time.sleep(1.5)
        os.system('cls')
  

        def dodge(): #funkce pro úhyb 
            global dodge           
            dodge = 1      
       
    ################################### TVOŘENÍ FUNKCE PRO CHARAKTERY ###################################

        def assassin():
            global stats, money, money_lost, xp_gain, xp_need_max, level, items_damage, items_armor, items_health    
            global armor_upgrade, crits_upgrade, health_upgrade, damage_upgrade, luck_upgrade  
            global ma_luck, ma_crit, wa_luck, wa_crit, ar_luck, ar_crit, as_luck, as_crit   

            if run == 0:
                print(f"     {characterchoose}\n\nBASE STATS:\narmor: 15\ndamage: 25-30\nhealth: 315\nluck: 5%\ncrits: 9%")    
            stats = {
                "armor":15,"damage":random.randint(25,30),"health":315,"luck":random.randint(1,100),"crits":random.randint(1,100),"golds":0,"xp":0,"level":0
                    }            
    
            stats["xp"] = xp_gain #zapsání xp do statů     
            stats["armor"]+=armor_upgrade #přidá Armor z vylepšení statů
            stats["health"]+=health_upgrade #přidá životy z vylepšení statů
            stats["damage"]+= damage_upgrade #přidá damage z vylepšení statů
            as_luck += luck_upgrade
            as_crit += crits_upgrade


            if xp_gain >= xp_need_max: #postup do dalšího levelu
                xp_gain -= xp_need_max #zbytek xp které se dají do dalšího levelu
                xp_need_max = (xp_need_max/100 * 17)+xp_need_max #zvyšování maximálních xp
                xp_need_max = round(xp_need_max,1)
                level +=1 #přičtení levelu
            stats["level"] = level #zapsání levelu do statů   

            ########## PENÍZE A HP ##########

            stats["golds"]=money #přičtení peněz      

            ########## PŘIČTENÍ HEALTH A ARMORU Z ITEMŮ ##########
        
            stats["health"] += items_health
            stats["armor"] += items_armor

            stats["health"] -= damager #odečítání HP

    ########## ŠANCE NA KRITICKÝ ÚTOK ##########

            if stats["crits"] <=as_crit:
                stats["damage"] *=1.75
                

    ########## ŠANCE NA ÚHYB ##########

            if stats["luck"]<=as_luck:
                dodge() 

    ########## PŘIČTENÍ DAMAGE Z ITEMŮ ##########

            stats["damage"] += items_damage

        def warrior():
            global stats, money, money_lost, xp_gain, xp_need_max, level, items_damage, items_armor, items_health
            global armor_upgrade, crits_upgrade, health_upgrade, damage_upgrade, luck_upgrade
            global ma_luck, ma_crit, wa_luck, wa_crit, ar_luck, ar_crit, as_luck, as_crit

            if run == 0:
                print(f"     {characterchoose}\n\nBASE STATS:\narmor: 40\ndamage: 16-22\nhealth: 430\nluck: 1%\ncrits: 2%")
            stats = {
                "armor":40,"damage":random.randint(16,22),"health":430,"luck":random.randint(1,100),"crits":random.randint(1,100),"golds":0,"xp":0,"level":0
                    } 
            
            stats["xp"] = xp_gain
            stats["armor"]+=armor_upgrade
            stats["health"]+=health_upgrade
            stats["damage"]+= damage_upgrade
            wa_luck += luck_upgrade
            wa_crit += crits_upgrade
            
            if xp_gain >= xp_need_max:
                xp_gain -= xp_need_max
                xp_need_max = (xp_need_max/100 * 17)+xp_need_max
                xp_need_max = round(xp_need_max,1)
                level +=1
            stats["level"] = level           

            stats["golds"]=money #přičtení peněz   

            ########## PŘIČTENÍ HEALTH A ARMORU Z ITEMŮ ##########
        
            stats["health"] += items_health
            stats["armor"] += items_armor      
            
            stats["health"] -= damager #odečítání HP

        ########## ŠANCE NA KRITICKÝ ÚTOK ##########
            
            if stats["crits"] <=wa_crit:
                stats["damage"] *=1.75
                

        ########## ŠANCE NA ÚHYB ##########

            if stats["luck"]<=wa_luck:             
                dodge()


        ########## PŘIČTENÍ DAMAGE Z ITEMŮ ##########

            stats["damage"] += items_damage         

        def archer():
            global stats, money, money_lost, xp_gain, xp_need_max, level, items_damage, items_armor, items_health
            global armor_upgrade, crits_upgrade, health_upgrade, damage_upgrade, luck_upgrade
            global ma_luck, ma_crit, wa_luck, wa_crit, ar_luck, ar_crit, as_luck, as_crit

            if run == 0:
                print(f"     {characterchoose}\n\nBASE STATS:\narmor: 13\ndamage: 28-35\nhealth: 300\nluck: 3%\ncrits: 4%")
            stats = {
                "armor":13,"damage":random.randint(28,35),"health":300,"luck":random.randint(1,100),"crits":random.randint(1,100),"golds":0,"xp":0,"level":0
                    }  
                        
            ########## PŘIDÁVÁNÍ XP ##########

            stats["xp"] = xp_gain
            stats["armor"]+=armor_upgrade
            stats["health"]+=health_upgrade
            stats["damage"]+= damage_upgrade
            ar_luck += luck_upgrade
            ar_crit += crits_upgrade


            if xp_gain >= xp_need_max:
                xp_gain -= xp_need_max
                xp_need_max = (xp_need_max/100 * 17)+xp_need_max
                xp_need_max = round(xp_need_max,1)
                level +=1

            stats["level"] = level           
            
            stats["golds"]=money #přičtení peněz  

            ########## PŘIČTENÍ HEALTH A ARMORU Z ITEMŮ ##########
        
            stats["health"] += items_health
            stats["armor"] += items_armor

            
            stats["health"] -= damager #odečítání HP

        ########## ŠANCE NA KRITICKÝ ÚTOK ##########

            if stats["crits"] <=ar_crit:
                stats["damage"] *=1.75
                
        ########## ŠANCE NA ÚHYB ##########

            if stats["luck"]<=ar_luck:                
                dodge()
            
        ########## PŘIČTENÍ DAMAGE Z ITEMŮ ##########

            stats["damage"] += items_damage             


        def mage():        
            global stats, money, money_lost, xp_gain, xp_need_max, level, items_damage, items_armor, items_health, level_point
            global armor_upgrade, crits_upgrade, health_upgrade, damage_upgrade, luck_upgrade
            global ma_luck, ma_crit, wa_luck, wa_crit, ar_luck, ar_crit, as_luck, as_crit 

            if run == 0:
                print(f"     {characterchoose}\n\nBASE STATS:\narmor: 12\ndamage: 28-33\nhealth: 325\nluck: 7%\ncrits: 1%")
            stats = {
                "armor":12,"damage":random.randint(28,33),"health":325,"luck":random.randint(1,100),"crits":random.randint(1,100),"golds":0,"xp":0,"level":10
                    }                                               
                        
            stats["xp"] = xp_gain    
            stats["armor"]+=armor_upgrade
            stats["health"]+=health_upgrade
            stats["damage"]+= damage_upgrade  
            ma_luck += luck_upgrade
            ma_crit += crits_upgrade


            if xp_gain >= xp_need_max:
                xp_gain -= xp_need_max
                xp_need_max = (xp_need_max/100 * 17)+xp_need_max
                xp_need_max = round(xp_need_max,1)
                level +=1
                level_point +=1

            stats["level"] = level                

            stats["golds"]=money #přičtení peněz    

            ########## PŘIČTENÍ HEALTH A ARMORU Z ITEMŮ ##########
        
            stats["health"] += items_health
            stats["armor"] += items_armor
            
            stats["health"] -= damager #odečítání HP

        ################################### ŠANCE NA KRITICKÝ ÚTOK ################################### 
        
            if stats["crits"] == ma_crit:
                stats["damage"] *=1.75            

        ################################### ŠANCE NA ÚHYB ###################################

            if stats["luck"]<=ma_luck:
                dodge()  

        ########## PŘIČTENÍ DAMAGE Z ITEMŮ ##########

            stats["damage"] += items_damage             
              
        ########## IF KTERÝ MĚNÍ PRINT VE FUNKCI CHARAKTERU ##########     

        global run
        if run != 0:
            run -= run

        ################################### VÝBĚR FUNKCE PODLE POSTAVY ###################################

        while True:
            global functiondir
            functiondir = {
                "Mage":mage,"Warrior":warrior,"Archer":archer,"Assassin":assassin
                }
            
            ########## FUNKCE KTERÁ JE VHODNÁ K POSTAVĚ ##########

            functiondir[characterchoose]() #funkce například assassin()
            
            stats["golds"] = 0

            ################################### PO VYBRÁNÍ CHARAKTERU ###################################

            continue_in_game = "Continue-0\nNew Game-1\nLoad Game-2\nQuit-3"            
            
            print("\nContinue-1\nBack-2")   
            try:     
                continue_game = int(input("> "))
                if continue_game == 1:
                    break
                if continue_game == 2:
                    while_menu()
                else:
                    os.system("cls")
                    continue
            except ValueError:    
                os.system("cls")        
                continue
            
        break
            
    ################################### ARMOR A ZBRANĚ (HNUSNÉ BALANCOVÁNÍ KVŮLI LEVELU) ###################################

    global armor, weapon, stejny_damage
    stejny_damage = stats["damage"]

    def armor_type():
        global armor
        for x in range(1):
            armor = {
                        "chestplate":{"Clashmogs Chestplate":[random.randint(2,4)+random.randint(2,3)*(1+stats["level"]+round(stats["level"]/2))-(stats["level"]/2) , random.randint(25,45)+random.randint(25,45)*(1+stats["level"]+round(stats["level"]))-(stats["level"]*0.2) , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)], #1. je armor 2. jsou HP a 3. je cena
                                    "Moonfire Chestplate":[random.randint(4,6)+random.randint(4,6)*(1+stats["level"]+round(stats["level"]/2))-(stats["level"]/2) , random.randint(15,22)+random.randint(10,20)*(1+stats["level"]+round(stats["level"]))-(stats["level"]*0.2) , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)],
                                    "Plate of Life":[random.randint(7,10)+random.randint(6,8)*(1+stats["level"]+round(stats["level"]/2))-(stats["level"]/2) , random.randint(3,5)+random.randint(3,5)*(1+stats["level"]+round(stats["level"]))-(stats["level"]*0.2) , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)],
                                    "Farloyle Bamboo Plate":[random.randint(8,11)+random.randint(8,11)*(1+stats["level"]+round(stats["level"]/2))-(stats["level"]/2) , 0 , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)],
                                    "Thawed Heartplate":[random.randint(4,5)+random.randint(2,5)*(1+stats["level"]+round(stats["level"]/2))-(stats["level"]/2) , random.randint(20,25)+random.randint(20,25)*(1+stats["level"]+round(stats["level"]))-(stats["level"]*0.2) , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)]
                                    },

                        "chausses":{"Clashmogs Chausses":[round((random.randint(2,4)+random.randint(2,3)*(1+stats["level"]+round(stats["level"]/2))-(stats["level"]/2))*0.65,1) , round((random.randint(25,45)+random.randint(25,45)*(1+stats["level"]+round(stats["level"]))-(stats["level"]*0.2))*0.65,1) , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)], #1. je armor 2. jsou HP a 3. je cena
                                    "Moonfire Chausses":[round((random.randint(4,6)+random.randint(4,6)*(1+stats["level"]+round(stats["level"]/2))-(stats["level"]/2))*0.65,1) , round((random.randint(15,22)+random.randint(10,20)*(1+stats["level"]+round(stats["level"]))-(stats["level"]*0.2))*0.65) , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)],
                                    "Chausses of Life":[round((random.randint(7,10)+random.randint(6,8)*(1+stats["level"]+round(stats["level"]/2))-(stats["level"]/2))*0.65,1) , round((random.randint(3,5)+random.randint(3,5)*(1+stats["level"]+round(stats["level"]))-(stats["level"]*0.2))*0.65,1) , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)],
                                    "Farloyle Bamboo Chausses":[round((random.randint(8,11)+random.randint(8,11)*(1+stats["level"]+round(stats["level"]/2))-(stats["level"]/2))*0.65,1) , 0 , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)],
                                    "Thawed Heartchausses":[round((random.randint(4,5)+random.randint(2,5)*(1+stats["level"]+round(stats["level"]/2))-(stats["level"]/2))*0.65,1) , round((random.randint(20,25)+random.randint(20,25)*(1+stats["level"]+round(stats["level"]))-(stats["level"]*0.2))*0.65,1) , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)]
                                    },

                        "helmet":{"Clashmogs Helmet":[round((random.randint(2,4)+random.randint(2,3)*(1+stats["level"]+round(stats["level"]/2))-(stats["level"]/2))*0.5,1) , round((random.randint(25,45)+random.randint(25,45)*(1+stats["level"]+round(stats["level"]))-(stats["level"]*0.2))*0.5,1) , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)], #1. je armor 2. jsou HP a 3. je cena
                                "Moonfire Helmet":[round((random.randint(4,6)+random.randint(4,6)*(1+stats["level"]+round(stats["level"]/2))-(stats["level"]/2))*0.5,1) , round((random.randint(15,22)+random.randint(10,20)*(1+stats["level"]+round(stats["level"]))-(stats["level"]*0.2))*0.5) , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4),1],
                                "Helmet of Life":[round((random.randint(7,10)+random.randint(6,8)*(1+stats["level"]+round(stats["level"]/2))-(stats["level"]/2))*0.5,1) , round((random.randint(3,5)+random.randint(3,5)*(1+stats["level"]+round(stats["level"]))-(stats["level"]*0.2))*0.5,1) , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)], 
                                "Farloyle Bamboo Helmet":[round((random.randint(8,11)+random.randint(8,11)*(1+stats["level"]+round(stats["level"]/2))-(stats["level"]/2))*0.5,1) , 0 , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)],
                                "Thawed Heart Helmet":[round((random.randint(4,5)+random.randint(2,5)*(1+stats["level"]+round(stats["level"]/2))-(stats["level"]/2))*0.5,1) , round((random.randint(20,25)+random.randint(20,25)*(1+stats["level"]+round(stats["level"]))-(stats["level"]*0.2))*0.5,1) , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)]
                                    },

                        "boots":{"Clashmogs Boots":[round((random.randint(2,4)+random.randint(2,3)*(1+stats["level"]+round(stats["level"]/2))-(stats["level"]/2))*0.4,1) , round((random.randint(25,45)+random.randint(25,45)*(1+stats["level"]+round(stats["level"]))-(stats["level"]*0.2))*0.4,1) , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)], #1. je armor 2. jsou HP a 3. je cena
                                "Moonfire Boots":[round((random.randint(4,6)+random.randint(4,6)*(1+stats["level"]+round(stats["level"]/2))-(stats["level"]/2))*0.4,1) , round((random.randint(15,22)+random.randint(10,20)*(1+stats["level"]+round(stats["level"]))-(stats["level"]*0.2))*0.4) , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)],
                                "Boots of Life":[round((random.randint(7,10)+random.randint(6,8)*(1+stats["level"]+round(stats["level"]/2))-(stats["level"]/2))*0.4,1) , round((random.randint(3,5)+random.randint(3,5)*(1+stats["level"]+round(stats["level"]))-(stats["level"]*0.2))*0.4,1) , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)],
                                "Farloyle Bamboo Boots":[round((random.randint(8,11)+random.randint(8,11)*(1+stats["level"]+round(stats["level"]/2))-(stats["level"]/2))*0.4,1) , 0 , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)],
                                "Thawed Heart Boots":[round((random.randint(4,5)+random.randint(2,5)*(1+stats["level"]+round(stats["level"]/2))-(stats["level"]/2))*0.4,1),round((random.randint(20,25)+random.randint(20,25)*(1+stats["level"]+round(stats["level"]))-(stats["level"]*0.2))*0.4,1),random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)]
                                    },

                        "gloves":{"Clashmogs Gloves":[round((random.randint(2,4)+random.randint(2,3)*(1+stats["level"]+round(stats["level"]/2))-(stats["level"]/2))*0.4,1) , round((random.randint(25,45)+random.randint(25,45)*(1+stats["level"]+round(stats["level"]))-(stats["level"]*0.2))*0.4,1) , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)], #1. je armor 2. jsou HP a 3. je cena
                                "Moonfire Gloves":[round((random.randint(4,6)+random.randint(4,6)*(1+stats["level"]+round(stats["level"]/2))-(stats["level"]/2))*0.4,1) , round((random.randint(15,22)+random.randint(10,20)*(1+stats["level"]+round(stats["level"]))-(stats["level"]*0.2))*0.4) , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)],
                                "Gloves of Life":[round((random.randint(7,10)+random.randint(6,8)*(1+stats["level"]+round(stats["level"]/2))-(stats["level"]/2))*0.4,1) , round((random.randint(3,5)+random.randint(3,5)*(1+stats["level"]+round(stats["level"]))-(stats["level"]*0.2))*0.4,1) , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)],
                                "Farloyle Bamboo Gloves":[round((random.randint(8,11)+random.randint(8,11)*(1+stats["level"]+round(stats["level"]/2))-(stats["level"]/2))*0.3,1) , 0 , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)],
                                "Thawed Heart Gloves":[round((random.randint(4,5)+random.randint(2,5)*(1+stats["level"]+round(stats["level"]/2))-(stats["level"]/2))*0.4,1) , round((random.randint(20,25)+random.randint(20,25)*(1+stats["level"]+round(stats["level"]))-(stats["level"]*0.2))*0.4,1) , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)]
                                    }
                        }     

    def weapon_type():  
        global weapon   
        for x in range(1):    
            weapon = {
                        "Warrior":{"White Cleaver":[random.randint(6,8)+random.randint(5,6)*(1+stats["level"]+round(stats["level"]/2))-(stats["level"]/2) , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)],
                                "Blades of Fire":[random.randint(7,8)+random.randint(6,7)*(1+stats["level"]+round(stats["level"]/2))-(stats["level"]/2) , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)],
                                "Ice Mallet":[random.randint(5,7)+random.randint(6,7)*(1+stats["level"]+round(stats["level"]/2))-(stats["level"]/2) , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)],
                                "Titanic Slayer":[random.randint(3,4)+random.randint(3,4)*(stats["level"]*stats["level"]*0.075+round(stats["health"]*0.0085)) , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)], #scaluje s max HP čím víc HP, tím větší DMG 2. je cena             
                                    },

                        "Mage":{"Rabadons Staff":[random.randint(8,10)+random.randint(7,9)*(1+stats["level"]+round(stats["level"]*0.6))-(stats["level"]*0.35) , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)],
                                "Ice Wand":[random.randint(7,10)+random.randint(7,9)*(1+stats["level"]+round(stats["level"]/2))-(stats["level"]/2) , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)],
                                "Futens Echo":[random.randint(9,13)+random.randint(7,13)*(1+stats["level"]+round(stats["level"]/2))-(stats["level"]/2) , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)],
                                "Demonic Tooth":[random.randint(6,8)*stats["level"]*0.01+random.randint(4,5)*(stats["level"]*stats["level"]*0.075+round(stats["health"]*0.0025)) , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)],  #scaluje s max HP a Levelem čím víc HP a LVL, tím větší DMG 2. je cena                         
                                    },

                        "Archer":{"Bow of Glory":[random.randint(10,11)+random.randint(9,10)*(1+stats["level"]+round(stats["level"]*0.6))-(stats["level"]*0.55) , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)],
                                "Serpents Crossbow":[random.randint(8,9)+random.randint(8,9)*(1+stats["level"]+round(stats["level"]*0.6))-(stats["level"]*0.45) , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)],
                                "Dragon Slayer":[random.randint(8,12)+random.randint(8,12)*(1+stats["level"]+round(stats["level"]*0.55))-(stats["level"]/2) , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)],
                                "Mortal Longbow":[random.randint(9,14)+random.randint(9,14)*(1+stats["level"])*0.02+random.randint(5,6)*(stats["level"]*stats["level"]*0.065+round(stats["health"]*0.0015)) , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)], #scaluje s max HP a Levelem čím víc HP a LVL, tím větší DMG 2. je cena                         
                                    },

                        "Assassin":{"Dark Dagger":[random.randint(8,9)+random.randint(8,9)*(1+stats["level"]+round(stats["level"]*0.6))-(stats["level"]*0.55) , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)],
                                    "Nocturnal Claw":[random.randint(6,9)+random.randint(6,7)*(1+stats["level"]+round(stats["level"]*0.6))-(stats["level"]*0.45) , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)],
                                    "Last Eclipse":[random.randint(7,11)+random.randint(7,11)*(1+stats["level"]+round(stats["level"]*0.55))-(stats["level"]/2) , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)],
                                    "Wauters Rageblade":[random.randint(8,12)+(random.randint(8,12)*as_crit*0.35)*0.2-1+stats["level"]/2+random.randint(6,8)*(stats["level"]*stats["level"]*0.045+round(stats["health"]*0.001)) , random.randint(60,100)+random.randint(50,90)*(stats["level"]-stats["level"]*0.4)], #scaluje s max HP,levelem a critem čím víc HP,LVL a critu, tím větší DMG 2. je cena                          
                                    }            

                    }

################################### VYTVOŘENÍ FUNKCE OBCHODŮ ###################################

    def armorsmith():
        global armor_list,order_list,armor0_list,selected_armor,armor_input,armor_input_global,armor,money,inventory
        armor_type()

        while True:
            os.system('cls')
            armor_list=[]
            armor0_list=[]
            order = 0

            for x in range(6):
                armor0 = random.choice(list(armor.keys())) #vybere část zbroje například: chestplate
                armor1 =list(armor[armor0].keys())[random.randint(0,4)] #z dané části zbroje vybere konkrétní zbroj                
                order+=1  
                order_list.append(order)                              
                armor_list.append(armor1)  #přidání do listu konkrétní zbroj
                armor0_list.append(armor0) #přidání do listu část zbroje                           
                
            while True:            
                os.system('cls')
                for x in range (len(armor_list)):
                    print(f"{armor_list[x]}-{order_list[x]}")    

                try:
                    armor_input=int(input("\nBack-0\n> "))
                    if armor_input == 0:
                        os.system('cls')
                        break 

                    if armor_input >=1 and armor_input <=6:                       
                        armor_input -=1  
                        armor_input_global = armor_input
                        selected_armor = armor[armor0_list[armor_input]][armor_list[armor_input]] #postupně se dostane k hodnotě zbroje (armor - část zbroje - konkrétní zbroj- hodnoty)
                        os.system('cls')

                        while True:  
                            os.system('cls')                
                            print(f"     {armor_list[armor_input]}\n\nMy Money: {money}\nArmor: {selected_armor[0]}\nHealth: {selected_armor[1]}\nPrice: {selected_armor[2]}\n\nBack-0\nBuy-1 ") #print hodnot zbroje                           
                            buy=input("> ")
                            
                            if buy == "0":
                                os.system('cls')
                                break      

                            if buy == "1":
                                if money >=selected_armor[2]:
                                    if armor_list[armor_input] in inventory:
                                        print("\nWARNING! THIS ITEM IS ALREADY IN INVENTORY.\n\nIF YOU WANT TO CONTINUE IN PURCHASE YOUR ITEM IN INVENTORY WILL BE REMOVED WITHOUT GETTING MONEY")  
                                        print("Do you want to continue in purchase\n\nYES-1\nNO-2")
                                        yes_no = input("> ").lower().strip()

                                        if yes_no == "1":
                                            money-=selected_armor[2]
                                            inventory_armor()
                                            continue
                                        else:
                                            continue

                                    else:
                                        money-=selected_armor[2]
                                        inventory_armor()
                                        continue 
                                else:                                    
                                    print("YOU DON'T HAVE ENOUGH MONEY!")
                                    time.sleep(1)                                                                
                                    continue
                                
                            else:
                                os.system('cls')
                                continue

                except ValueError:
                    os.system('cls')
                    continue
            
            break
  
    def weaponsmith():
        global weapon_list, order_list, weapon0_list, characterchoose, selected_weapon, weapon_input, weapon, money, inventory
        weapon_type()
        while True:
            os.system('cls')
            weapon_list=[]            
            order = 0
            for x in range(6):
                
                weapon1 =random.choice(list(weapon[characterchoose])) #vybere zbraň z dictionary podle daného characteru například: Mage a vybere Demonic Tooth
                print(weapon1)           
                order+=1  
                order_list.append(order)                              
                weapon_list.append(weapon1) #přidá do listu zbraň z weapon1                                        
                
            while True:            
                os.system('cls')
                for x in range (len(weapon_list)):
                    print(f"{weapon_list[x]}-{order_list[x]}") #napíše všech 6 zbraní a číslo pořadí  

                try:
                    weapon_input=int(input("\nBack-0\n> "))

                    if weapon_input == 0:
                        os.system('cls')
                        break 

                    if weapon_input >=1 and weapon_input <=6:                       
                        weapon_input -=1  
                        selected_weapon = weapon[characterchoose][weapon_list[weapon_input]] #dostane se k hodnotám zbraně například: damage
                        os.system('cls')   
                        while True:  
                            os.system('cls')                
                            print(f"     {weapon_list[weapon_input]}\n\nMy Money: {money}\nDamage: {selected_weapon[0]}\nPrice: {selected_weapon[1]}\n\nBack-0\nBuy-1 ") #print hodnot zbraně
                            buy=input("> ")

                            if buy == "0":
                                os.system('cls')
                                break        

                            if buy == "1":
                                if money >=selected_weapon[1]:
                                    if weapon_list[weapon_input] in inventory:
                                        print("\nWARNING! THIS ITEM IS ALREADY IN INVENTORY.\n\nIF YOU WANT TO CONTINUE IN PURCHASE YOUR ITEM IN INVENTORY WILL BE REMOVED WITHOUT GETTING MONEY")  
                                        print("Do you want to continue in purchase\n\nYES-1\nNO-2")
                                        yes_no = input("> ").lower().strip()

                                        if yes_no == "1":
                                            money-=selected_weapon[1]
                                            inventory_weapon()
                                            continue
                                        else:
                                            continue

                                    else:
                                        money-=selected_weapon[1]
                                        inventory_weapon()
                                        continue
                                else:                                    
                                    print("YOU DON'T HAVE ENOUGH MONEY!")
                                    time.sleep(1)                                                                
                                    continue
                                                          
                            else:
                                os.system('cls')
                                continue

                except ValueError:
                    os.system('cls')
                    continue
            
            break


    def inventory_armor():
        global selected_armor,inventory,armor_list,armor_input_global                     
        inventory[armor_list[armor_input_global]]=[selected_armor[0],selected_armor[1],selected_armor[2]]              
          

    def inventory_weapon():
        global selected_weapon,inventory,weapon_input_global,weapon_list
        inventory[weapon_list[weapon_input]]=[selected_weapon[0],selected_weapon[1]]        


    def inventory():
        while True:
            global inventory, money, odlozene_itemy, inventory_equip, weapon, armor, items_damage,items_armor, items_health, stejny_damage
            os.system('cls')            
            print("Equiped:\n")   

            for key,value in inventory_equip.items():
                print(f"{key}: {value}")

            pozice = 0
            print("\nInventory:\n")

            for key,value in inventory.items():
                pozice+=1                     
                print(f"{key}-{pozice}")
    	        

            try:
                vyber = int(input(f"\nBack-0\nUnequip-100\n> "))
            except ValueError:
                continue

            if vyber >0 and vyber <= pozice:
                vyber-=1
                os.system('cls') 
                vyber_itemu=list(inventory)[vyber]    
                    
                print(f"{vyber_itemu}:")
                armor_type()
                weapon_type()
                if vyber_itemu in weapon[characterchoose]:                    
                    print(f"\nDamage: {list(inventory[vyber_itemu])[0]}\nSell Price: {(list(inventory[vyber_itemu])[1])/2}")      

                else:                    
                    print(f"\nArmor: {list(inventory[vyber_itemu])[0]}\nHealth: {list(inventory[vyber_itemu])[1]}\nSell Price: {(list(inventory[vyber_itemu])[2])/2}")                   

                print(f"\nEquip-1\nSell-2\nBack-0")
                try:
                    vyber_pokracovani=int(input("> "))
                except ValueError:
                    continue
                
                if vyber_pokracovani == 2:                
                    if vyber_itemu in weapon[characterchoose]:                        
                        money+=((list(inventory[vyber_itemu])[1])/2)                        

                    else:                        
                        money+=((list(inventory[vyber_itemu])[2])/2)                        

                    inventory.pop(vyber_itemu)
                    continue
                
                if vyber_pokracovani == 1:
                    if vyber_itemu in weapon[characterchoose]:
                        items_damage = list(inventory[vyber_itemu])[0]                         
                        if inventory_equip["weapon"] == "none":
                            inventory_equip["weapon"] = vyber_itemu
                        else:
                            continue
                        stejny_damage += items_damage
                        odlozene_itemy[vyber_itemu]=[list(inventory[vyber_itemu])[0],list(inventory[vyber_itemu])[1]]
                        inventory.pop(vyber_itemu)
                        
                    
                    for x in range(len(armor)):                        
                        finalni_armor=list(armor.keys())[x] #jedná se o část armoru jako je chestplate               
                        armor_vyber = armor[list(armor.keys())[x]] #jedná se o konkrétní části v dic. armoru jako je clashmog atd.

                        if vyber_itemu in armor_vyber:   
                            items_armor = list(inventory[vyber_itemu])[0]    
                            items_health = list(inventory[vyber_itemu])[1]        
                            if inventory_equip[finalni_armor] == "none":       
                                inventory_equip[finalni_armor] = vyber_itemu
                            else:
                                continue
                            odlozene_itemy[vyber_itemu]=[list(inventory[vyber_itemu])[0],list(inventory[vyber_itemu])[1],list(inventory[vyber_itemu])[2]]
                            inventory.pop(vyber_itemu)
                    continue                    


            if vyber == 0:
                break

            if vyber == 100:
                while True:                    
                    os.system('cls')
                    print("Equiped:\n\n")
                    try:         
                        for key,value in inventory_equip.items():
                            print(f"{key}: {value}")               
                        co_oddelat=str(input("\nWHAT DO YOU WANT TO UNEQUIP:\nChestplate\nHelmet\nChausses\nBoots\nGloves\nWeapon\n\nBack-0\n> ")).lower()

                        if co_oddelat == "0":
                            break
                        for x in range(1):
                            for x in range(len(armor)): 
                                armor_vyber = armor[list(armor.keys())[x]]
                                if inventory_equip[co_oddelat] in armor_vyber:                          
                                    inventory[inventory_equip[co_oddelat]]=[list(odlozene_itemy[inventory_equip[co_oddelat]])[0],list(odlozene_itemy[inventory_equip[co_oddelat]])[1],list(odlozene_itemy[inventory_equip[co_oddelat]])[2]]
                                    

                            if inventory_equip[co_oddelat] in weapon[characterchoose]:
                                stejny_damage -= items_damage
                                inventory[inventory_equip[co_oddelat]]=[list(odlozene_itemy[inventory_equip[co_oddelat]])[0],list(odlozene_itemy[inventory_equip[co_oddelat]])[1]]      
                                items_damage -=list(odlozene_itemy[inventory_equip[co_oddelat]])[0]
                                
                            else:
                                continue

                        inventory_equip[co_oddelat]="none"
                        
                    except KeyError:
                        continue
            else:
                continue   

    def staty():
        while True:               
            global stats,xp_gain,xp_need_max,money,ma_luck,ma_crit, level_point, stejny_damage
            global armor_upgrade, crits_upgrade, health_upgrade, damage_upgrade, luck_upgrade
                 
            os.system('cls')
            crits_upgrade =0
            luck_upgrade=0
            order1=0
            order2=0          

            print(f"My Stats:\n\nAvailable Points: {level_point}\nLevel: {stats['level']}\nCurrent XP: {xp_gain}\nMax XP: {xp_need_max}\nMoney: {money}\n")
            

            for key,value in stats.items():
                if order2 < 3:
                    order2+=1
                    if key != "damage":
                        print(f"{key.title()}:{value}")
                    else:
                        print(f"Damage: {stejny_damage}")

            luck_chooser=[characterchoose[:2].lower()+"_luck"][0] 
            crit_chooser=[characterchoose[:2].lower()+"_crit"][0]       
            print(f"Dodge Chance: {globals()[luck_chooser]}")
            print(f"Crit Chance: {globals()[crit_chooser]}")

            print("\nUpgrade something:\n")
            for key in stats:
                if order1 <5:
                    order1 +=1                                       
                    print(f"{key}-{order1}")   
                    
                             
            try:
                upgrade_choose=int(input("\nBack-0\n> "))
                
                if upgrade_choose ==0:
                        break
                if level_point >0:   
                    if upgrade_choose <6 and upgrade_choose >0:
                        level_point -=1                    
                        upgrade_choose -=1
                        vyber_upgradu=[list(stats)[upgrade_choose].lower()+"_upgrade"][0]                       
                        vysledny_pridavek = {0:0.5, 1:0.5, 2:2.5, 3:40, 4:0.25}    

                        globals()[vyber_upgradu] +=vysledny_pridavek[upgrade_choose]      
                        functiondir[characterchoose]() 

                        if  globals()[luck_chooser] >65:
                            globals()[luck_chooser]=65                                                       
                            level_point+=1
                            continue
                        if globals()[crit_chooser] >65:                             
                            globals()[crit_chooser]=65  
                            level_point+=1                            
                            continue         
                        if upgrade_choose == 1:
                            stejny_damage +=0.5
            except:
                continue
            
    ################################### ZADÁVÁNÍ JMÉNA ###################################

    for x in range(1):
        global name_of_character
        run +=1 #přičte číslo tak aby nefungoval print ve funkci charakteru

        if menu_choose == "0":            
            break
        os.system("cls")
        name_of_character = input("Nickname: ")
        while len(name_of_character) >25:
            os.system('cls')
            print("Max name length is 25 characters!\n")
            name_of_character = input("Nickname: ")
                         
            
        os.system('cls')
        while " " in name_of_character:
            print("Cannot contain spaces") #jestliže obsahuje mezeru vypíše znova input
            name_of_character = input("Nickname: ")
            os.system("cls")
        break
    
    ################################### TVOŘENÍ FUNKCE ###################################  
    
    def damage():   
        
        ########## MŮJ DAMAGE ##########   

        global enemystats,basestats,damager

        if not(stats["health"]<=0):   
            my_damage = {"damage dealt":0} 
            time.sleep(0.25)
            my_damage["damage dealt"]= stats["damage"]*(100/(100+enemystats["armor"]))
            my_damage["damage dealt"]=round(my_damage["damage dealt"],1)
                    
        else:
            my_damage["damage"] = 0  


        if enemystats["luck"] <=round(1.5*(2+dungeonpick+dungeonpick/2)):
            my_damage["damage dealt"] = 0
            print("ENEMY DODGE")

        ########## ENEMY STATY ##########   

        enemystats["damage"]=random.randint(basestats["damagefull"],basestats["damagefull2"])
        enemystats["luck"]=random.randint(1,100)
        enemystats["crits"]=random.randint(1,100)        
        enemystats["health"] = enemystats["health"]-my_damage["damage dealt"] 
        enemystats["health"]=round(enemystats["health"],1)
              
        
        ########## ENEMY DAMAGE ##########

        if not(enemystats["health"]<=0):            
            time.sleep(0.25)
            global enemy_damage,dodge

            enemy_damage = {"damage": 0}        
            enemy_damage["damage"] = enemystats["damage"]*(100/(100+stats["armor"]))

            if enemystats["crits"] <=(1.5*(1+dungeonpick+dungeonpick+dungeonpick/2)):
                enemy_damage["damage"] *= 1.75

            enemy_damage["damage"] = round(enemy_damage["damage"],1)
            
            if dodge == 1:
                enemy_damage["damage"] -= enemy_damage["damage"]
                dodge -= dodge
                print("DODGE")
            
            damager += enemy_damage["damage"]

        else:            
            enemy_damage["damage"]=0  

    ########## MOJE STATY ##########

        stats["crits"]=random.randint(1,100)
        stats["luck"]=random.randint(1,100)
        stats["health"] = stats["health"] - enemy_damage["damage"]
        stats["health"] = round(stats["health"],1)        

        
        for x in zip(my_damage.items(),enemy_damage.items()):
            print(f"Damage Dealt: {my_damage['damage dealt']}\t           Enemy Damage Dealt: {enemy_damage['damage']}")
            
    def enemy():
        
        ########## DUNGEONY A ENEMY V NICH ########## 
        
        global enemystats,money_lost, stejny_damage, name_of_character
        dungeon={
        1:["Skeleton","Grubr","Viper","Clog","Stonie"],
        2: ["Slime","Eiktros","Head Grabber","Brontin","Rhytin"],
        3: ["Nightmare","Trindym","Raudr","Undimald","Katalysich"],
        4: ["Thrafstiras","Fobe","Alonistis","Polyov","Fotia"],
        5: ["Osteoth","Kataran","Thanatos","Belanthona","Ka-Ko"],
        6: ["Potrin","Ooze","Surden","Kardo","Rendunt"],
        7: ["Fader","Louk","Vinre","Wauter","Krblin"],
        8: ["Stog","Dark Mage","Vit-Star","Uter","Lamel"],
        9: ["Kordin","Panthon","Tapius","Vugonk","Treivn"],
        10: ["Wuju","Nalfite","Frundle","Kasiopei","Kei-za"]
        }     
        
    ################################### CELÁ FUNKCE STATŮ ENEMY (HNUS) ###################################

        while True: 
            list_of_stats = []
            os.system("cls")  
            for x in range(5): #kolik dungeonů je
                x+=1                        
                print(f"Dungeon-{x:1} Dungeon-{x+5:1}") #napíše pod sebe dungeony do dvou sloupců

            print("\nGame Menu-0")     
            try: #při špatném inputu
                global dungeonpick
                dungeonpick=int(input("> "))                  
            except ValueError:                
                continue #při špatném inputu opakuje akci
            if dungeonpick == 0:                
                in_game_menu() 
                break #ukončí smyčku
            elif dungeonpick <=10 and dungeonpick >0: 
                enemy = random.choice(dungeon[dungeonpick])
                global randomstats,basestats,enemystats

                randomstats= {  #základní staty pro všechny dungeony 
                    "armor0":15,
                    "armor1":23,
                    "damage0":22,
                    "damage1":28,
                    "health0":285,
                    "health1":400,
                    "gold0":15,
                    "gold1":22,
                    "xp0":8,
                    "xp1":15
                            }
            
                ########## SOUČET VÍCE STATŮ ABY BYLY DVA ##########

                basestats={  #základní staty pro daný dungeon
                    "armorfull":randomstats["armor0"]+(randomstats["armor0"]*(dungeonpick-1)*dungeonpick), 
                    "armorfull2":randomstats["armor1"]+(randomstats["armor1"]*(dungeonpick-1)*dungeonpick),
                    "damagefull":randomstats["damage0"]+(randomstats["damage0"]*(dungeonpick-1)*dungeonpick),
                    "damagefull2":randomstats["damage1"]+(randomstats["damage1"]*(dungeonpick-1)*dungeonpick),
                    "healthfull":randomstats["health0"]+(randomstats["health0"]*(dungeonpick-1)*dungeonpick),
                    "healthfull2":randomstats["health1"]+(randomstats["health1"]*(dungeonpick-1)*dungeonpick),
                    "goldfull":randomstats["gold0"]+(randomstats["gold1"]*(dungeonpick-1)*dungeonpick),
                    "goldfull2":randomstats["gold1"]+(randomstats["gold1"]*(dungeonpick-1)*dungeonpick),
                    "xpfull":randomstats["xp0"]+(randomstats["xp0"]*(dungeonpick-1)*dungeonpick),
                    "xpfull2":randomstats["xp1"]+(randomstats["xp1"]*(dungeonpick-1)*dungeonpick)
                        }
                
                ########## POUŽITÍ DVOU STATŮ JAKO RANDOM INTERVAL ##########
                
                enemystats = { #náhodný výběr z rozmezí 
                    "armor":random.randint(basestats["armorfull"],basestats["armorfull2"]),
                    "damage":random.randint(basestats["damagefull"],basestats["damagefull2"]),
                    "health":random.randint(basestats["healthfull"],basestats["healthfull2"]),
                    "luck":random.randint(1,100),
                    "crits":random.randint(1,100),
                    "golds":random.randint(basestats["goldfull"],basestats["goldfull2"]),
                    "xp":random.randint(basestats["xpfull"],basestats["xpfull2"])
                    }
                

                ########## NÁHODNÉ VĚTY ##########

                random_quote_me = ""
                random_quote_enemy =""
                

                quote_enemy = {
                    1:f"{enemy} robbed you while you were unconscious.",
                    2:f"{enemy} threatened you to give {enemy} money.",
                    3:f"{enemy} spit on you and left. ",
                    4:f"You begged for mercy and gave {enemy} money.",
                    5:f"{enemy} robbed you while you were unconscious.",
                    6:f"{enemy} threatened you to give {enemy} money.",                    
                    7:f"{enemy} robbed you while you were unconscious.",
                    8:f"{enemy} threatened you to give {enemy} money.",
                    9:f"{enemy} robbed you while you were unconscious.",
                    10:f"{enemy} threatened you to give {enemy} money."                  
                    }
                
                quote_me = {
                    1:f"You robbed {enemy} while it was unconscious.",
                    2:f"You totaly destroyed {enemy} and took some golds.",
                    3:f"{enemy} ran away and you get nothing",
                    4:f"You robbed {enemy} while it was unconscious.",
                    5:f"You totaly destroyed {enemy} and took some golds.",
                    6:f"You robbed {enemy} while it was unconscious.",
                    7:f"You totaly destroyed {enemy} and took some golds.",
                    8:f"You robbed {enemy} while it was unconscious.",
                    9:f"You totaly destroyed {enemy} and took some golds.",
                    10:f"You robbed {enemy} while it was unconscious."                    
                    }

                        
                ################################### DOKUD NIKDO NENÍ MRTVÝ ###################################
                
                timer = 0.5
                global money,money_lost,xp_gain                
                while not (enemystats["health"] <=0 or stats["health"] <=0):  
                 
                    
                    enemystats1 = { 
                        "armor":enemystats["armor"],
                        "damage":[randomstats["damage0"]+(randomstats["damage0"]*(dungeonpick-1)*dungeonpick),randomstats["damage1"]+(randomstats["damage1"]*(dungeonpick-1)*dungeonpick)],
                        "health":enemystats["health"]                  
                            }
                
                    stats1 = {
                        "armor":stats["armor"],
                        "damage":stats["damage"],
                        "health":stats["health"]
                            }   
                    
                    functiondir[characterchoose]()
                    os.system("cls")                      
                    print(f"{name_of_character}:                        {enemy}:\n")                   

                    for (key1, value1), (key2, value2) in zip(stats1.items(), enemystats1.items()):
                        if key2 != "damage":
                            print(f"{key1.title()}: {value1}\t                   {key2.title()}: {value2}")
                        else:
                            print(f"Damage: {value1}\t                   Damage: {value2[0]}-{value2[1]}")                    
                    damage()# funkce damage pro mě i enemy
                    time.sleep(timer)
                    timer = round(timer,1)                    
                    if timer >0:
                        timer-=0.1                                                                     
                    os.system("cls")                      
                        
                    ########## PROHRA ##########

                    if stats["health"] <= 0 and enemystats["health"] > 0:
                        
                        print("You lose")                        
                        
                        random_quote_enemy=random.choice(list(quote_enemy.values())) #výběr náhodné věty

                        if random_quote_enemy == quote_enemy[3]:
                            print(random_quote_enemy)                            
                            break
                        
                        if not (money <=0): #jestliže moje peníze nejsou 0 a méně 
                                                       
                            money_lost = money*0.03                            
                            if money_lost < 1: #jestliže peníze, které ztratím jsou menší než 1, ztratí se 1 
                                money_lost =1  
                            money-=round(money_lost) #odečtení peněz                            
                            money_lost = round(money_lost)
                           
                            print(f"{random_quote_enemy}\nYou lost {money_lost} golds.")
                        elif money <=0: #jestliže moje peníze jsou menší nebo rovny 0 (žádná ztráta)
                            print("Odin had mercy and you lost nothing.")                       
                    
                    ########## VÝHRA ##########

                    if stats["health"] >0 and enemystats["health"] <= 0:                                              
                        print("You won")                        
                        
                        random_quote_me=random.choice(list(quote_me.values())) #výběr náhodné věty

                        if random_quote_me == quote_me[3]:
                            print(random_quote_me)                            
                            break            
                        
                        xp_gain += enemystats["xp"]    

                        money += enemystats["golds"] #přičtení peněz                         
                        print(f"{random_quote_me}\nYou earned {enemystats['golds']} golds and {enemystats['xp']} XP.") 
                    
                getpass.getpass("Press ENTER to continue: ") 
                global damager
                damager -= damager #změní daný damage na negativní (takže se při odečítání přičte)            
                functiondir[characterchoose]()
                os.system("cls")
    

    ################################### FUNKCE IN GAME MENU ###################################

    def in_game_menu():

    ########## MENU VE HŘE ##########
        while True:
            global in_game_menu_choose
            os.system("cls")
            print("Dungeons-1\nInventory-2\nStats-3\nSwordsmith-4\nArmorsmith-5\nMain Menu-6")

            try: #při špatném inputu
                in_game_menu_choose=input("> ")
            except ValueError:                
                continue                
            if in_game_menu_choose == "1":                                
                enemy() #vrátí mě do výběrů dungeonů
            if in_game_menu_choose == "2":
                inventory()                  
            if in_game_menu_choose == "3":
                staty()              
            if in_game_menu_choose == "6":
                menu() #vrátí mě do menu 
                while_menu()        
            if in_game_menu_choose == "5":
                armorsmith()       
            if in_game_menu_choose == "4":
                weaponsmith()

    ########## SPOUŠTĚNÍ DALŠÍCH FUNCKÍ ##########   

    in_game_menu()

while_menu()