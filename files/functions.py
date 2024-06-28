from utilities import *
from colorama import *
from random import randint

def asklifes(language):  #-> lifes: int
    while True:
        lifes: int = 0
        animation1(language['asklifes'])
        input1 = fixtext(input())
        try:
            if 1 <= int(input1) <= 5:
                lifes = input1
        except ValueError: pass
        if input1 == 'r' or input1 == 'random':
            lifes = randint(1,5)
        if 1 <= lifes <= 5: break
        else: animation2(language['errorvaltxt'])
    animation2(f'{language['answerlifes']}: {lifes}\n')
    return lifes

def askplayers(language):  #-> totplayers: int
    return inputint(language['askplayers'], 1, 4)

def initgame(language, totplayers, lifes):  #-> players: list
    init(autoreset=True)
    just_fix_windows_console()
    global bot
    #sigarette(0), manette(1), birra(2), coltellino(3), vetrino(4), polarizzatore(5), telefono(6), oggTot(7)
    #solo per bot: conoscenza[]
    Player1 = [input(f'{language['askname']} Player1: '), lifes, [0, 0, 0, 0, 0, 0, 0, 0]]
    players = [Player1]
    bot = ['Bot', lifes, [0, 0, 0, 0, 0, 0, 0, 0], []]
    if totplayers == 1:
        players.append(bot)
    if totplayers >= 2:
        Player2 = [input(f'{language['askname']} Player2: '), lifes, [0, 0, 0, 0, 0, 0, 0, 0]]
        players.append(Player2)
    if totplayers >= 3:
        Player3 = [input(f'{language['askname']} Player3: '), lifes, [0, 0, 0, 0, 0, 0, 0, 0]]
        players.append(Player3)
    if totplayers == 4:
        Player4 = [input(f'{language['askname']} Player4: '), lifes, [0, 0, 0, 0, 0, 0, 0, 0]]
        players.append(Player4)
    return players

def checkifdead(language, players, turns):  #-> players: list
    if players[turns[0]][1] < 1:
        animation1(f'{Fore.RED}{players[turns[0]][0]} {language['isdead']}\n')
        players.remove(players[turns[0]])
    if players[turns[1]][1] < 1:
        animation1(f'{Fore.RED}{players[turns[1]][0]} {language['isdead']}\n')
        players.remove(players[turns[1]])
    return players

def regenprojectiles(language, players):  #-> iprojectile, projectiles
    global bot
    animation1(language['projregen'])
    for letter in list('...'):
        animation1(letter)
    print()
    while True:
        projectiles = []
        iprojectile = [0, 0, 0, 1, 0, 0, randint(3, 12)]
        players[1][3] = []
        for num2 in range(iprojectile[6]):
            projectiles.append(randint(0, 1))
            if bot in players: players[1][3].append(0)
            if projectiles[num2] == 0:
                iprojectile[2] += 1
            else:
                iprojectile[1] += 1
        iprojectile[0] = iprojectile[1] + iprojectile[2]
        if iprojectile[1] > (1/4) * iprojectile[0] and iprojectile[2] > (1/4) * iprojectile[0] and iprojectile[0] == iprojectile[6]: break
    animation2(f'{Back.GREEN}{language['falseproj']}: {iprojectile[2]}; {Back.YELLOW}{language['trueproj']}: '
               f'{iprojectile[1]}; {Back.BLUE}{language['totproj']}: {iprojectile[0]}\n')
    return iprojectile, projectiles

def genoggetti(language, players):  #-> players: list
    for player in players:
        for a in range(2):
            player[2][7] = player[2][0] + player[2][1] + player[2][2] + player[2][3] + player[2][4] + player[2][5] + player[2][6]
            if player[2][7] == 8:
                animation2(f'{player[0]} ha raggiunto il limite di 8 oggetti!')
                break
            else:
                r = randint(1, 7)
                if r == 1:
                    animation2(f'{player[0]} {language['recieved']} {language['getcigarettes']}')
                    player[2][0] += 1
                elif r == 2:
                    animation2(f'{player[0]} {language['recieved']} {language['gethandcuffs']}')
                    player[2][1] += 1
                elif r == 3:
                    animation2(f'{player[0]} {language['recieved']} {language['getbeer']}')
                    player[2][2] += 1
                elif r == 4:
                    animation2(f'{player[0]} {language['recieved']} {language['gethandsaw']}')
                    player[2][3] += 1
                elif r == 5:
                    animation2(f'{player[0]} {language['recieved']} {language['getglass']}')
                    player[2][4] += 1
                elif r == 6:
                    animation2(f'{player[0]} {language['recieved']} {language['getinverter']}')
                    player[2][5] += 1
                elif r == 7:
                    animation2(f'{player[0]} {language['recieved']} {language['getphone']}')
                    player[2][6] += 1
    print()
    return players

def ctrlturni(language, players, iprojectile, turns):  #-> iprojectile: list, turns: list
    if iprojectile[5] == 2:
        animation2(f'{language['removehandcuffs1']} {players[turns[1]][0]}\n')
        iprojectile[5] = 1
    else:
        if iprojectile[5] == 1:
            animation2(f'{language['removehandcuffs2']} {players[turns[1]][0]}\n')
            iprojectile[5] = 0
        if len(players) == 2:
            if turns[0] == 0: turns = [1,0]
            else: turns = [0,1]
        elif len(players) == 3:
            if turns[0] == 0: turns = [1,2]
            elif turns[0] == 1: turns = [2,0]
            else: turns = [0,1]
        elif len(players) == 4: 
            if turns[0] == 0: turns = [1,2]
            elif turns[0] == 1: turns = [2,3]
            elif turns[0] == 2: turns = [3,0]
            else: turns = [0,1]
    return iprojectile, turns


def usasigarette(language, players, turns, time=0):
    if players[turns[0]][2][0] > 0:
        players[turns[0]][2][0] -= 1
        players[turns[0]][1] += 1
        animation2(f"{language['+1life']} {players[turns[0]][0]}\n{language['nowhas']} {players[turns[0]][1]} {language['lifes']}", time)
        sleep(time)
    else:
        animation2(language['errortxtcig'])
    return players


def usamanette(language, players, turns, iprojectile, time=0):
    if players[turns[0]][2][1] > 0:
        if iprojectile[5] > 0:
            animation2(language['nousehandcuffs'])
        else:
            players[turns[0]][2][1] -= 1
            iprojectile[5] = 2
            animation2(f'{language['handcuffsuse']} {players[turns[1]][0]}')
            sleep(time)
    else:
        animation2(language['errortxtcuffs'])
    return players, iprojectile


def usabirra(language, players, turns, iprojectile, projectiles, time=0):
    if players[turns[0]][2][2] > 0:
        if projectiles[iprojectile[4]] == 1:
            animation2(f'{Back.RED}{language['expelledreal']}')
        else:
            animation2(f'{Back.CYAN}{language['expelledfake']}')
        iprojectile[0] -= 1
        iprojectile[4] += 1
        players[turns[0]][2][2] -= 1
        sleep(time)
    else:
        animation2(language['errortxtbeer'])
    return players, iprojectile, projectiles


def usacoltellino(language, players, turns, iprojectile, time=0):
    if players[turns[0]][2][3] > 0:
        if iprojectile[3] == 2:
            animation2(language['nousesaw'])
        else:
            players[turns[0]][2][3] -= 1
            iprojectile[3] = 2
            animation2(language['usesaw'])
            sleep(time)
    else:
        animation2(language['errortxtsaw'])
    return players, iprojectile


def usavetrino(language, players, turns, iprojectile, projectiles, time=0):
    if players[turns[0]][2][4] > 0:
        players[turns[0]][2][4] -= 1
        if projectiles[iprojectile[4]] == 0:
            animation2(f"{Back.GREEN} {language['selectedreal']}")
        else:
            animation2(f"{Back.YELLOW} {language['selectedfake']}")
        sleep(time)
    else:
        animation2(language['errortxtglass'])
    return players


def usapolarizzatore(language, players, turns, iprojectile, projectiles, time=0):
    if players[turns[0]][2][5] > 0:
        players[turns[0]][2][5] -= 1
        if projectiles[iprojectile[4]] == 1:
            projectiles[iprojectile[4]] = 0
        else:
            projectiles[iprojectile[4]] = 1
        animation2(language['inverted'])
        sleep(time)
    else:
        animation2(language['errortxtinverter'])
    return players, projectiles


def usatelefono(language, players, turns, projectiles, iprojectile, time=0):
    global bot
    if players[turns[0]][2][6] > 0:
        players[turns[0]][2][6] -= 1
        r = randint(iprojectile[4], iprojectile[6] - 1)
        if projectiles[r] == 1:
            animation2(f'{Back.YELLOW}{language['theproj']} {r + 1} {language['isreal']}')
        else:
            animation2(f'{Back.GREEN}{language['theproj']} {r + 1} {language['isfake']}')
        if bot in players: players[1][3][r] = 1
        sleep(time)
    else:
        animation2(language['errortxtphone'])
    return players


def usafucileiopieno(language, players, turns, iprojectile):
    iprojectile[4] += 1
    iprojectile[0] -= 1
    players[turns[0]][1] -= iprojectile[3]
    if iprojectile[3] == 1:
        animation2(f'{Back.RED}-{iprojectile[3]} {language['-1lifefor']} {language['u']}{Style.RESET_ALL}\n{language['endofturn']}\n')
    else:
        animation2(f'{Back.RED}-{iprojectile[3]} {language['-2lifesfor']} {language['u']}{Style.RESET_ALL}\n{language['endofturn']}\n')
    iprojectile[3] = 1
    return players, iprojectile


def usafucileiovuoto(language, iprojectile):
    iprojectile[4] += 1
    iprojectile[0] -= 1
    animation2(f'{Back.CYAN}{language['wasemptyproj']}')
    iprojectile[3] = 1
    return iprojectile


def usafucilenemicopieno(language, players, turns, iprojectile):
    iprojectile[4] += 1
    iprojectile[0] -= 1
    players[turns[1]][1] -= iprojectile[3]
    if iprojectile[3] == 1:
        animation2(f'{Back.RED}-{iprojectile[3]} {language['-1lifefor']} {players[turns[1]][0]}{Style.RESET_ALL}\n{language['endofturn']}\n')
    else:
        animation2(f'{Back.RED}-{iprojectile[3]} {language['-2lifesfor']} {players[turns[1]][0]}{Style.RESET_ALL}\n{language['endofturn']}\n')
    iprojectile[3] = 1
    return players, iprojectile


def usafucilenemicovuoto(language, iprojectile):
    iprojectile[4] += 1
    iprojectile[0] -= 1
    animation2(f'{Back.CYAN}{language['wasemptyproj']}{Style.RESET_ALL}\n{language['endofturn']}\n')
    iprojectile[3] = 1
    return iprojectile


def botgameplay(language, players, turns, iprojectile, projectiles):  #-> player: list, iprojectile: list
    if players[turns[0]][0] == 'Bot':
        animation1(f'{Back.BLUE}{language['turnofbot']} {players[1][1]}{language['lifes']}):\n')
        while 1:
            if players[1][2][0] > 0:
                animation1(language['botusedcig'])
                players = usasigarette(language, players, turns, 1)
            for a in range(randint(0,2)):
                if randint(0,100) <= 60 and players[1][2][1] > 0 and iprojectile[5] != 1:
                    animation1(language['botusedcuffs'])
                    players, iprojectile = usamanette(language, players, turns, iprojectile, 1)
                if randint(0,100) <= 50 and players[1][2][2] > 0:
                    animation1(language['botusedbeer'])
                    players, iprojectile, projectiles = usabirra(language, players, turns, iprojectile, projectiles, 1)
                    if controllo(projectiles, iprojectile) == 1: break
                if randint(0,100) <= 10 and players[1][2][3] > 0 and iprojectile[3] != 2:
                    animation1(language['botusedsaw'])
                    players, iprojectile = usacoltellino(language, players, turns, iprojectile, 1)
                if randint(0,100) <= 80 and players[1][2][4] > 0 and players[1][3][iprojectile[4]] != 1:
                    animation1(language['botusedlens'])
                    players = usavetrino(language, players, turns, iprojectile, projectiles, 1)
                if randint(0,100) <= 10 and players[1][2][5] > 0:
                    animation1(language['botusedinverter'])
                    players, projectiles = usapolarizzatore(language, players, turns, iprojectile, projectiles, 1)
                if randint(0,100) <= 80 and players[1][2][6] > 0:
                    animation1(language['botusedphone'])
                    players = usatelefono(language, players, turns, projectiles, iprojectile, 1)
            else:
                if players[1][3][iprojectile[4]] == 1:
                    if players[1][2][5] > 0 and projectiles[iprojectile[4]] == 0:
                        animation1(language['botusedinverter'])
                        players, projectiles = usapolarizzatore(language, players, turns, iprojectile, projectiles, 1)
                    if players[1][2][3] > 0 and iprojectile[3] != 2 and projectiles[iprojectile[4]] == 1:
                        animation1(language['botusedcig'])
                        players, iprojectile = usacoltellino(language, players, turns, iprojectile, 1)
                    if projectiles[iprojectile[4]] == 0:
                        animation1(language['botusedgunhimself'])
                        iprojectile = usafucileiovuoto(language, iprojectile)
                        if controllo(projectiles, iprojectile) == 1: break
                        continue
                    else:
                        animation1(f'{language['botusedgunenemy']}{players[turns[1]][0]}: ')
                        players, iprojectile = usafucilenemicopieno(language, players, turns, iprojectile)
                        break
                elif randint(0,100) <= 20:
                    if projectiles[iprojectile[4]] == 1:
                        animation1(language['botusedgunhimself'])
                        players, iprojectile = usafucileiopieno(language, players, turns, iprojectile)
                        break
                    else:
                        animation1(language['botusedgunhimself'])
                        iprojectile = usafucileiovuoto(language, iprojectile)
                        if controllo(projectiles, iprojectile) == 1: break
                        continue
                else:
                    if projectiles[iprojectile[4]] == 1:
                        animation1(f'{language['botusedgunenemy']} {players[turns[1]][0]}: ')
                        players, iprojectile = usafucilenemicopieno(language, players, turns, iprojectile)
                        break
                    else:
                        animation1(f'{language['botusedgunenemy']} {players[turns[1]][0]}: ')
                        iprojectile = usafucilenemicovuoto(language, iprojectile)
                        break
            break
        return players, iprojectile

def playergameplay(language, players, turns,  iprojectile, projectiles):  #->
    animation2(f"{Back.BLUE}{language['turnof']} {players[turns[0]][0]}\n{Style.RESET_ALL}{language['uhave']}")
    if players[turns[0]][2][0] == 1:
        animation2(f"- {players[turns[0]][2][0]} {language['ipackofcig']}")
    elif players[turns[0]][2][0] > 1:
        animation2(f"- {players[turns[0]][2][0]} {language['ipacksofcig']}")
    if players[turns[0]][2][1] == 1:
        animation2(f"- {players[turns[0]][2][1]} {language['ipairhandcuff']}")
    elif players[turns[0]][2][1] > 1:
        animation2(f"- {players[turns[0]][2][1]} {language['ipairshandcuffs']}")
    if players[turns[0]][2][2] == 1:
        animation2(f"- {players[turns[0]][2][2]} {language['ibeer']}")
    elif players[turns[0]][2][2] > 1:
        animation2(f"- {players[turns[0]][2][2]} {language['ibeers']}")
    if players[turns[0]][2][3] == 1:
        animation2(f"- {players[turns[0]][2][3]} {language['ihandsaw']}")
    elif players[turns[0]][2][3] > 1:
        animation2(f"- {players[turns[0]][2][3]} {language['ihandsaws']}")
    if players[turns[0]][2][4] == 1:
        animation2(f"- {players[turns[0]][2][4]} {language['i1lens']}")
    elif players[turns[0]][2][4] > 1:
        animation2(f"- {players[turns[0]][2][4]} {language['imorelens']}")
    if players[turns[0]][2][5] == 1:
        animation2(f"- {players[turns[0]][2][5]} {language['iinverter']}")
    elif players[turns[0]][2][5] > 1:
        animation2(f"- {players[turns[0]][2][5]} {language['iinverters']}")
    if players[turns[0]][2][6] == 1:
        animation2(f"- {players[turns[0]][2][6]} {language['iphone']}")
    elif players[turns[0]][2][6] > 1:
        animation2(f"- {players[turns[0]][2][6]} {language['iphones']}")
    if players[turns[0]][1] == 1:
        animation2(f"- {players[turns[0]][1]} {language['life']}")
    elif players[turns[0]][1] > 1:
        animation2(f"- {players[turns[0]][1]} {language['lifes']}")
    while 1:
        animation2(language['whatuwantuse'])
        if players[turns[0]][2][0] > 0: animation1(language['cigarettsor'])
        if players[turns[0]][2][1] > 0: animation1(language['handcuffsor'])
        if players[turns[0]][2][2] > 0: animation1(language['beeror'])
        if players[turns[0]][2][3] > 0: animation1(language['sawor'])
        if players[turns[0]][2][4] > 0: animation1(language['lensor'])
        if players[turns[0]][2][5] > 0: animation1(language['inverteror'])
        if players[turns[0]][2][6] > 0: animation1(language['phoneor'])
        animation1(language['Gun'] + ': ')
        input2 = fixtext(input())
        if input2 == language['cig']:
            players = usasigarette(language, players, turns)
        elif input2 == language['cuffs']:
            players, iprojectile = usamanette(language, players, turns, iprojectile)
        elif input2 == language['beer']:
            players, iprojectile, projectiles = usabirra(language, players, turns, iprojectile, projectiles)
            if controllo(projectiles, iprojectile) == 1: break
        elif input2 == language['saw']:
            players, iprojectile = usacoltellino(language, players, turns, iprojectile)
        elif input2 == language['lens']:
            players = usavetrino(language, players, turns, iprojectile, projectiles)
        elif input2 == language['inv']:
            players, projectiles = usapolarizzatore(language, players, turns, iprojectile, projectiles)
        elif input2 == language['phone']:
            players = usatelefono(language, players, turns, projectiles, iprojectile)
        elif input2 == language['gun']:
            while True:
                animation1(f'{language['gunask']} {players[turns[1]][0]}({language['Enemy']})? ')
                input3 = fixtext(input())
                if input3 == language['i'] or input3 == language['enemy'] or input3 == fixtext(players[turns[1]][0]):
                    break
                else:
                    animation2(language['errortypetxt'])
            if input3.lower().strip() == language['i']:
                if projectiles[iprojectile[4]] == 1:
                    players, iprojectile = usafucileiopieno(language, players, turns, iprojectile)
                    break
                else:
                    iprojectile = usafucileiovuoto(language, iprojectile)
                    if controllo(projectiles, iprojectile) == 1: break
            else:
                if projectiles[iprojectile[4]] == 1:
                    players, iprojectile = usafucilenemicopieno(language, players, turns, iprojectile)
                    break
                else:
                    iprojectile= usafucilenemicovuoto(language, iprojectile)
                    break
        else:
            animation2(language['errortypetxt'])
    return players, iprojectile, projectiles