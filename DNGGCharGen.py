from tkinter import *
import random
DNGGRaces = ['Random', 'Argonian', 'Breton', 'Dark Elf',
               'High Elf', 'Imperial', 'Khajiit', 'Nord', 'Redguard', 'Orc', 'Wood Elf']
DNGGStones = ['Random', 'Apprentice', 'Atronach', 'Lady', 'Lord', 'Lover',
                'Mage', 'Ritual', 'Serpent', 'Shadow', 'Steed', 'Thief', 'Tower', 'Warrior']
DNGGClasses = ['Random','Brave Warrior','Poor Rogue','Elemental Mage','Talented Summoner','Shady Assassin','Noble Knight','Kind Monk','Proud Paladin','Sneaky Nightblade','Wretch(No Class)']
# Divines, remake for starting divines.
DNGGDivines = ['Random', 'Akatosh', 'Arkay', 'Auriel','Dibella', 'Julianos',
                 'Kynareth', 'Mara', 'Stendarr', 'Syrabane', 'Talos', 'Zenithar']
DNGGDaedra = ['Random','Azura','Boethiah','Clavicus Vile','Hermaeus Mora','Hircine','Jyggalag','Malacath','Mehrunes Dagon','Mephala','Meridia','Molag Bal','Namira','Nocturnal','Peryite','Sanguine','Sheogorath','Vaermina']
#Separator Classes
DNGGWarriorClasses = ['Brave Warrior','Noble Knight','Proud Paladin']
DNGGMageClasses = ['Elemental Mage','Talented Summoner','Kind Monk']
DNGGRogueClasses = ['Poor Rogue','Shady Assassin','Sneaky Nightblade']
#Separator Stones
DNGGWarriorStones = ['Lord','Lady','Warrior','Steed']
DNGGMageStones = ['Apprentice','Atronach','Ritual']
DNGGRogueStones = ['Thief','Lover','Serpent','Shadow','Tower']
#Separator Races
DNGGWarriorRaces = ['Redguard','Nord','Orc','Dark Elf']
DNGGMageRaces = ['Breton','Imperial','High Elf','Dark Elf']
DNGGRogueRaces = ['Argonian','Khajiit','Wood Elf','Dark Elf']
#NG+ Options
NGText = ['Companions Complete', 'Thieves Guild Complete', 'Brotherhood Complete', 'Killed Alduin',
              'Killed Miraak', 'Owned Home', 'Cleared Labyrinthian', 'Full Daedric Armor', 'Cleared Wyrmstooth', 'Drank Skooma']

def disableAll(list, vars):
    for i in list:
        vars[list.index(i)].set(0)
        i.config(state="disabled")
        

def enableAll(list):
    for i in list:
        i.config(state="normal")


def changeState(a, vars):
    if (a[0].cget('state') == 'disabled'):
        enableAll(a)
    elif (a[0].cget('state') == 'normal'):
        disableAll(a, vars)


def getData(option, list):
    retData = 'Random'
    if (option != 'Random'):
        return option
    else:
        while (retData == 'Random'):
            retData = random.choice(list)
    return retData


def setDivineMenu(window, option, strVariable):
    window.divineMenu.destroy()
    if option == 0:
        window.divineMenu = OptionMenu(window, strVariable, *DNGGDivines)
    else:
        window.divineMenu = OptionMenu(window, strVariable, *DNGGDaedra)
    window.divineMenu.place(x=300, y=200)


def buildResp(race, Sclass, stone, divine, optionVariables, NGVariables, evilCheck):
    labelNameList = ['Race: ', 'Class: ', 'Stone: ', 'Divine: ']
    dataList = [race, Sclass, stone,  divine]
    labelList = []
    response = Tk()
    response.title("DNGG Character")
    response.geometry("400x400")
    dataList[0] = getData(race,DNGGRaces)
    #Get class based on option 0
    if(optionVariables[0]):
        if dataList[0] == "Dark Elf":
            dataList[1] = getData(Sclass,DNGGClasses)
        elif dataList[0] in DNGGWarriorRaces:
            tempList = DNGGWarriorClasses
            tempList.append(random.choice(DNGGMageClasses))
            tempList.append(random.choice(DNGGRogueClasses))
            dataList[1] = getData(Sclass,tempList)
        elif dataList[0] in DNGGMageRaces:
            tempList = DNGGMageClasses
            tempList.append(random.choice(DNGGWarriorClasses))
            tempList.append(random.choice(DNGGRogueClasses))
            dataList[1] = getData(Sclass,tempList)
        elif dataList[0] in DNGGRogueRaces:
            tempList = DNGGRogueClasses
            tempList.append(random.choice(DNGGWarriorClasses))
            tempList.append(random.choice(DNGGMageClasses))
            dataList[1] = getData(Sclass,tempList)
    else:
        dataList[1] = getData(Sclass,DNGGClasses)
    #Get stone based on option 1
    if(optionVariables[1]):
        if dataList[1] in DNGGWarriorClasses:
            dataList[2] = getData(stone,DNGGWarriorStones)
        elif dataList[1] in DNGGMageClasses:
            dataList[2] = getData(stone,DNGGMageStones)
        elif dataList[1] in DNGGRogueClasses:
            dataList[2] = getData(stone,DNGGRogueStones)
        else:
            dataList[2] = getData(stone,DNGGStones)
    else:
        dataList[2] = getData(stone,DNGGStones)
    
    #Get Divine based on Evil
    if(evilCheck):
        dataList[3] = getData(divine,DNGGDaedra)
    else:
        dataList[3] = getData(divine,DNGGDivines)
    
    NGGold = 0
    for i in NGVariables:
        if(i.get()):
            NGGold = NGGold + 100
    if(NGGold != 0):
        NGLabel = Label(response,text=f'Gain {NGGold} gold from NG+!\n I will add more options to this if I get some input.')
        NGLabel.place(x=5,y=275)
    charLabel = Label(response, text="Character:", font=(
        "Times New Romans", 18), fg="black")
    charLabel.place(x=5, y=5)
    for s in range(len(labelNameList)):
        labelList.append(
            Label(response, text=f'{labelNameList[s]}{dataList[s]}'))
        labelList[s].place(x=5, y=(s*25)+50)
    response.mainloop()


def initialConfig():
    window = Tk()

    window.title("DNGG Character Randomizer")
    window.geometry("500x400")
    canvas = Canvas()

    canvas.create_line(175, 50, 175, 325, width=3)
    canvas.pack()

    # NG+ Items
    CheckList = []
    CheckListVars = []
    for i in range(10):
        CheckListVars.append(IntVar())
        CheckList.append(Checkbutton(window, text=NGText[i], variable=CheckListVars[i]))
        CheckList[i].place(x=5, y=(i*30)+60)
    disableAll(CheckList, CheckListVars)
    ngBtn = Button(window, text="New Game+?", fg="black",
                   font=("New Times Romans", 16), command=lambda: changeState(CheckList,CheckListVars))
    ngBtn.place(x=5, y=5)
    canvas.pack()

    # Randomizer Items
    rdmLabel = Label(window, text="Randomizer Items:",
                     fg='black', font=('Times New Romans', 18))
    rdmLabel.place(x=200, y=5)
    # Race Menu
    race = StringVar()
    race.set('Random')
    raceMenu = OptionMenu(window, race, *DNGGRaces)
    raceLabel = Label(window, text="Race:", fg="black")
    # Stone Menu
    stone = StringVar()
    stone.set('Random')
    stoneMenu = OptionMenu(window, stone, *DNGGStones)
    stoneLabel = Label(window, text="Stone:", fg="black")
    # Class Menu
    Sclass = StringVar()
    Sclass.set('Random')
    classMenu = OptionMenu(window, Sclass, *DNGGClasses)
    classLabel = Label(window, text="Class:", fg="black")
    # Divine Menu
    divine = StringVar()
    divine.set('Random')
    window.divineMenu = OptionMenu(window, divine, *DNGGDivines)
    divineLabel = Label(window, text="Divine:", fg="black")
    # Menu Placement:
    raceLabel.place(x=250, y=55)
    raceMenu.place(x=300, y=50)
    classLabel.place(x=250, y=105)
    classMenu.place(x=300, y=100)
    stoneLabel.place(x=250, y=155)
    stoneMenu.place(x=300, y=150)
    divineLabel.place(x=250, y=205)
    window.divineMenu.place(x=300, y=200)

    RaceandClass = IntVar()
    mtchRaBtn = Checkbutton(window, text="Match Race and Class", fg="black", variable=RaceandClass)
    mtchRaBtn.place(x=250, y=250)
    ClassandStone = IntVar()
    mtchClBtn = Checkbutton(window, text="Match Class and Stone", fg="black", variable=ClassandStone)
    mtchClBtn.place(x=250, y=275)
    evilCheck = IntVar()
    evil = Checkbutton(window, text="Evil?", fg="black", command=lambda: setDivineMenu(window, evilCheck.get(), divine), variable=evilCheck)
    evil.place(x=400, y=205)
    btnSubmit = Button(window, text="Randomize", fg="black",
                       command=lambda: buildResp(race.get(),Sclass.get(),stone.get(),divine.get(),[RaceandClass.get(),ClassandStone.get()], CheckListVars, evilCheck.get()))
    btnSubmit.place(x=250, y=350)

    window.mainloop()


initialConfig()
