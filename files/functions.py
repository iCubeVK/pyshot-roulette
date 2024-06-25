from utilities import *
from colorama import *
from random import randint

def asklifes():  #-> lifes: int
    while True:
        animation1("Inserisci Numero Vite(da 1 a 5), oppure Random: ")
        input1 = fixtext(input())
        if input1 == "random" or input1 == 'r':
            lifes: int = randint(1, 5)
            break
        else:
            try:
                lifes: int = int(input1)
                break
            except TypeError:
                animation2('Input non Valido!')
    animation2(f'Numero vite per player: {lifes}\n')
    return lifes

def askplayers():  #-> totplayers: int
    return inputint('Inserisci Numero Giocatori(da 1 a 4): ', 1, 4)

def initgame(totplayers, lifes):  #-> players: list
    init(autoreset=True)
    just_fix_windows_console()
    global bot
    #sigarette(0), manette(1), birra(2), coltellino(3), vetrino(4), polarizzatore(5), telefono(6), oggTot(7)
    #solo per bot: conoscenza[]
    Player1 = [input('Inserisci il nome di Player1: '), lifes, [0, 0, 0, 0, 0, 0, 0, 0]]
    players = [Player1]
    bot = ['Bot', lifes, [0, 0, 0, 0, 0, 0, 0, 0], []]
    if totplayers == 1:
        players.append(bot)
    if totplayers >= 2:
        Player2 = [input('Inserisci il nome di Player2: '), lifes, [0, 0, 0, 0, 0, 0, 0, 0]]
        players.append(Player2)
    if totplayers >= 3:
        Player3 = [input('Inserisci il nome di Player3: '), lifes, [0, 0, 0, 0, 0, 0, 0, 0]]
        players.append(Player3)
    if totplayers == 4:
        Player4 = [input('Inserisci il nome di Player4: '), lifes, [0, 0, 0, 0, 0, 0, 0, 0]]
        players.append(Player4)
    return players

def checkifdead(players, turns):  #-> players: list
    if players[turns[0]][1] < 1:
        animation1(f'{players[turns[0]][0]} è morto!\n')
        players.remove(players[turns[0]])
    if players[turns[1]][1] < 1:
        animation1(f'{players[turns[1]][0]} è morto!\n')
        players.remove(players[turns[1]])
    return players

def regenprojectiles(players):  #-> iprojectile, projectiles
    global bot
    animation1('Rigenerazione Proiettili')
    animation2('...', 1)
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
        if iprojectile[1] > (1 / 4) * iprojectile[0] and iprojectile[2] > (1 / 4) * iprojectile[0] and iprojectile[0] == iprojectile[6]: break
    animation2(f'{Back.GREEN}Proiettili Vuoti: {iprojectile[2]}; {Back.YELLOW}Proiettili Pieni: {iprojectile[1]}; {Back.BLUE}Proiettili Totali: {iprojectile[0]}\n')
    return iprojectile, projectiles

def genoggetti(players):  #-> players: list
    for player in players:
        for a in range(2):
            player[2][7] = player[2][0] + player[2][1] + player[2][2] + player[2][3] + player[2][4] + player[2][5] + player[2][6]
            if player[2][7] == 8:
                animation2(f'{player[0]} ha raggiunto il limite di 8 oggetti!')
                break
            else:
                r = randint(1, 7)
                if r == 1:
                    animation2(f'{player[0]} ha ricevuto un pacchetto di sigarette')
                    player[2][0] += 1
                elif r == 2:
                    animation2(f'{player[0]} ha ricevuto un paio di manette')
                    player[2][1] += 1
                elif r == 3:
                    animation2(f'{player[0]} ha ricevuto una lattina di birra')
                    player[2][2] += 1
                elif r == 4:
                    animation2(f'{player[0]} ha ricevuto un coltellino')
                    player[2][3] += 1
                elif r == 5:
                    animation2(f'{player[0]} ha ricevuto un vetrino')
                    player[2][4] += 1
                elif r == 6:
                    animation2(f'{player[0]} ha ricevuto un polarizzatore')
                    player[2][5] += 1
                elif r == 7:
                    animation2(f'{player[0]} ha ricevuto un telefono')
                    player[2][6] += 1
    print()
    return players

def ctrlturni(players, iprojectile, turns):  #-> iprojectile: list, turns: list
    if iprojectile[5] == 1:
        animation2(f'Manette verranno rimosse dopo questo turno (a {players[turns[1]][0]})\turns[0]')
        iprojectile[5] = 0
    else:
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


def usasigarette(players, turns, time=0, errortxt='Non hai Sigarette!'):
    if players[turns[0]][2][0] > 0:
        players[turns[0]][2][0] -= 1
        players[turns[0]][1] += 1
        animation2(f"+1 Vita per {players[turns[0]][0]}\nAdesso ha {players[turns[0]][1]} vite", time)
        sleep(time)
    else:
        animation2(errortxt)
    return players


def usamanette(players, turns, iprojectile, time=0, errortxt='Non hai manette!'):
    if players[turns[0]][2][1] > 0:
        if iprojectile[5] == 1:
            animation2(f'Non puoi usare piu di un paio di manette per turno!')
        else:
            players[turns[0]][2][1] -= 1
            iprojectile[5] = 1
            animation2(f'Manette Usate su {players[turns[1]][0]}')
            sleep(time)
    else:
        animation2(errortxt)
    return players, iprojectile


def usabirra(players, turns, iprojectile, projectiles, time=0, errortxt='Non hai Birra!'):
    if players[turns[0]][2][2] > 0:
        if projectiles[iprojectile[4]] == 1:
            animation2(f'{Back.RED}Proiettile espulso Vero')
        else:
            animation2(f'{Back.CYAN}Proiettile espulso Finto')
        iprojectile[0] -= 1
        iprojectile[4] += 1
        players[turns[0]][2][2] -= 1
        sleep(time)
    else:
        animation2(errortxt)
    return players, iprojectile, projectiles


def usacoltellino(players, turns, iprojectile, time=0, errortxt0='Non puoi usare piu di un coltellino per turno!', errortxt1='Non hai Birra!'):
    if players[turns[0]][2][3] > 0:
        if iprojectile[3] == 2:
            animation2(errortxt0)
        else:
            players[turns[0]][2][3] -= 1
            iprojectile[3] = 2
            animation2(f'Coltellino usato (Danno x2 al prossimo utilizzo del fucile)')
            sleep(time)
    else:
        animation2(errortxt1)
    return players, iprojectile


def usavetrino(players, turns, iprojectile, projectiles, time=0, errortxt='Non hai Vetrini!'):
    if players[turns[0]][2][4] > 0:
        players[turns[0]][2][4] -= 1
        if projectiles[iprojectile[4]] == 0:
            animation2(f"{Back.GREEN}Il proiettile selezionato adesso e' vuoto")
        else:
            animation2(f"{Back.YELLOW}Il proiettile selezionato adesso e' pieno")
        sleep(time)
    else:
        animation2(errortxt)
    return players


def usapolarizzatore(players, turns, iprojectile, projectiles, time=0, errortxt='Non hai Polarizzatori!'):
    if players[turns[0]][2][5] > 0:
        players[turns[0]][2][5] -= 1
        if projectiles[iprojectile[4]] == 1:
            projectiles[iprojectile[4]] = 0
        else:
            projectiles[iprojectile[4]] = 1
        animation2(f"Proiettile polarizzato")
        sleep(time)
    else:
        animation2(errortxt)
    return players, projectiles


def usatelefono(players, turns, projectiles, iprojectile, time=0, errortxt="Non hai Telefoni!"):
    global bot
    if players[turns[0]][2][6] > 0:
        players[turns[0]][2][6] -= 1
        r = randint(iprojectile[4], iprojectile[6] - 1)
        if projectiles[r] == 1:
            animation2(f'{Back.YELLOW}Il proiettile {r + 1} è pieno')
        else:
            animation2(f'{Back.GREEN}Il proiettile {r + 1} è vuoto')
        if bot in players: players[1][3][r] = 1
        sleep(time)
    else:
        animation2(errortxt)
    return players


def usafucileiopieno(players, turns, iprojectile):
    iprojectile[4] += 1
    iprojectile[0] -= 1
    players[turns[0]][1] -= iprojectile[3]
    if iprojectile[3] == 1:
        animation2(f'{Back.RED}-{iprojectile[3]} vita per te{Style.RESET_ALL}\nFine turno\n')
    else:
        animation2(f'{Back.RED}-{iprojectile[3]} vite per te{Style.RESET_ALL}\nFine turno\n')
    iprojectile[3] = 1
    return players, iprojectile


def usafucileiovuoto(iprojectile):
    iprojectile[4] += 1
    iprojectile[0] -= 1
    animation2(f'{Back.CYAN}Il proiettile era vuoto')
    iprojectile[3] = 1
    return iprojectile


def usafucilenemicopieno(players, turns, iprojectile):
    iprojectile[4] += 1
    iprojectile[0] -= 1
    players[turns[1]][1] -= iprojectile[3]
    if iprojectile[3] == 1:
        animation2(f'{Back.RED}-{iprojectile[3]} vita per {players[turns[1]][0]}{Style.RESET_ALL}\nFine turno\n')
    else:
        animation2(f'{Back.RED}-{iprojectile[3]} vite per {players[turns[1]][0]}{Style.RESET_ALL}\nFine turno\n')
    iprojectile[3] = 1
    return players, iprojectile


def usafucilenemicovuoto(iprojectile):
    iprojectile[4] += 1
    iprojectile[0] -= 1
    animation2(f'{Back.CYAN}Il proiettile era vuoto{Style.RESET_ALL}\nFine turno\n')
    iprojectile[3] = 1
    return iprojectile


def botgameplay(players, turns, iprojectile, projectiles):  #-> player: list, iprojectile: list
    if players[turns[0]][0] == 'Bot':
        animation1(f'{Back.BLUE}Turno di Bot(Vite: {players[1][1]}):\n')
        while 1:
            if players[1][2][0] > 0:
                animation1('Bot ha usato sigarette: ')
                players = usasigarette(players, turns, 1)
            for a in range(randint(0,2)):
                if randint(0,100) <= 60 and players[1][2][1] > 0 and iprojectile[5] != 1:
                    animation1('Bot ha usato manette: ')
                    players, iprojectile = usamanette(players, turns, iprojectile, 1)
                if randint(0,100) <= 50 and players[1][2][2] > 0:
                    animation1('Bot ha usato birra: ')
                    players, iprojectile, projectiles = usabirra(players, turns, iprojectile, projectiles, 1)
                    if controllo(projectiles, iprojectile) == 1: break
                if randint(0,100) <= 10 and players[1][2][3] > 0 and iprojectile[3] != 2:
                    animation1('Bot ha usato coltellino: ')
                    players, iprojectile = usacoltellino(players, turns, iprojectile, 1)
                if randint(0,100) <= 80 and players[1][2][4] > 0 and players[1][3][iprojectile[4]] != 1:
                    animation1('Bot ha usato vetrino: ')
                    players = usavetrino(players, turns, iprojectile, projectiles, 1)
                if randint(0,100) <= 10 and players[1][2][5] > 0:
                    animation1('Bot ha usato polarizzatore: ')
                    players, projectiles = usapolarizzatore(players, turns, iprojectile, projectiles, 1)
                if randint(0,100) <= 80 and players[1][2][6] > 0:
                    animation1('Bot ha usato telefono: ')
                    players = usatelefono(players, turns, projectiles, iprojectile, 1)
            else:
                if players[1][3][iprojectile[4]] == 1:
                    if players[1][2][5] > 0 and projectiles[iprojectile[4]] == 0:
                        animation1('Bot ha usato polarizzatore: ')
                        players, projectiles = usapolarizzatore(players, turns, iprojectile, projectiles, 1)
                    if players[1][2][3] > 0 and iprojectile[3] != 2 and projectiles[iprojectile[4]] == 1:
                        animation1('Bot ha usato coltellino: ')
                        players, iprojectile = usacoltellino(players, turns, iprojectile, 1)
                    if projectiles[iprojectile[4]] == 0:
                        animation1('Bot ha usato Fucile su se stesso: ')
                        iprojectile = usafucileiovuoto(iprojectile)
                        if controllo(projectiles, iprojectile) == 1: break
                        continue
                    else:
                        animation1(f'Bot ha usato Fucile su {players[turns[1]][0]}: ')
                        players, iprojectile = usafucilenemicopieno(players, turns, iprojectile)
                        break
                elif randint(0,100) <= 20:
                    if projectiles[iprojectile[4]] == 1:
                        animation1(f'Bot ha usato Fucile su se stesso: ')
                        players, iprojectile = usafucileiopieno(players, turns, iprojectile)
                        break
                    else:
                        animation1(f'Bot ha usato Fucile su se stesso: ')
                        iprojectile = usafucileiovuoto(iprojectile)
                        if controllo(projectiles, iprojectile) == 1: break
                        continue
                else:
                    if projectiles[iprojectile[4]] == 1:
                        animation1(f'Bot ha usato Fucile su {players[turns[1]][0]}: ')
                        players, iprojectile = usafucilenemicopieno(players, turns, iprojectile)
                        break
                    else:
                        animation1(f'Bot ha usato Fucile su {players[turns[1]][0]}: ')
                        iprojectile = usafucilenemicovuoto(iprojectile)
                        break
            break
        return players, iprojectile

def playergameplay(players, turns,  iprojectile, projectiles):  #->
    animation2(f"{Back.BLUE}Turno di {players[turns[0]][0]}\n{Style.RESET_ALL}Hai:")
    if players[turns[0]][2][0] == 1:
        animation2(f"- {players[turns[0]][2][0]} pacchetto di sigarette(Rigenerano una vita)")
    elif players[turns[0]][2][0] > 1:
        animation2(f"- {players[turns[0]][2][0]} pacchetti di sigarette(Rigenerano una vita)")
    if players[turns[0]][2][1] == 1:
        animation2(f"- {players[turns[0]][2][1]} paio di manette(Fanno Saltare un turno al nemico/prossimo giocatore)")
    elif players[turns[0]][2][1] > 1:
        animation2(f"- {players[turns[0]][2][1]} paia di manette(Fanno Saltare un turno al nemico/prossimo giocatore)")
    if players[turns[0]][2][2] == 1:
        animation2(f"- {players[turns[0]][2][2]} lattina di birra(Rimuove un proiettile a caso dal fucile)")
    elif players[turns[0]][2][2] > 1:
        animation2(f"- {players[turns[0]][2][2]} lattine di birra(Rimuove un proiettile a caso dal fucile)")
    if players[turns[0]][2][3] == 1:
        animation2(f"- {players[turns[0]][2][3]} coltellino(Il fucile fa il doppio del danno al prossimo utilizzo)")
    elif players[turns[0]][2][3] > 1:
        animation2(f"- {players[turns[0]][2][3]} coltellini(Il fucile fa il doppio del danno al prossimo utilizzo)")
    if players[turns[0]][2][4] == 1:
        animation2(f"- {players[turns[0]][2][4]} vetrino(Mostra il prossimo proiettile)")
    elif players[turns[0]][2][4] > 1:
        animation2(f"- {players[turns[0]][2][4]} vetrini(Mostra il prossimo proiettile)")
    if players[turns[0]][2][5] == 1:
        animation2(f"- {players[turns[0]][2][5]} polarizzatore(Cambia il proiettile da pieno a vuoto e viceversa)")
    elif players[turns[0]][2][5] > 1:
        animation2(f"- {players[turns[0]][2][5]} polarizzatori(Cambia il proiettile da pieno a vuoto e viceversa)")
    if players[turns[0]][2][6] == 1:
        animation2(f"- {players[turns[0]][2][6]} telefono(Dice se un proiettile a caso rimanente e' pieno o vuoto)")
    elif players[turns[0]][2][6] > 1:
        animation2(f"- {players[turns[0]][2][6]} telefoni(Dice se un proiettile a caso rimanente e' pieno o vuoto)")
    if players[turns[0]][1] == 1:
        animation2(f"- {players[turns[0]][1]} vita")
    elif players[turns[0]][1] > 1:
        animation2(f"- {players[turns[0]][1]} vite")
    while 1:
        animation2("Scrivi Cosa Vuoi Usare:")
        if players[turns[0]][2][0] > 0: animation1("Sigarette o ")
        if players[turns[0]][2][1] > 0: animation1("Manette o ")
        if players[turns[0]][2][2] > 0: animation1("Birra o ")
        if players[turns[0]][2][3] > 0: animation1("Coltellino o ")
        if players[turns[0]][2][4] > 0: animation1("Vetrino o ")
        if players[turns[0]][2][5] > 0: animation1("Polarizzatore o ")
        if players[turns[0]][2][6] > 0: animation1("Telefono o ")
        input2 = fixtext(input('Fucile: '))
        if input2 == "sigarette":
            players = usasigarette(players, turns)
        elif input2 == "manette":
            players, iprojectile = usamanette(players, turns, iprojectile)
        elif input2 == "birra":
            players, iprojectile, projectiles = usabirra(players, turns, iprojectile, projectiles)
            if controllo(projectiles, iprojectile) == 1: break
        elif input2 == "coltellino":
            players, iprojectile = usacoltellino(players, turns, iprojectile)
        elif input2 == "vetrino":
            players = usavetrino(players, turns, iprojectile, projectiles)
        elif input2 == "polarizzatore":
            players, projectiles = usapolarizzatore(players, turns, iprojectile, projectiles)
        elif input2 == "telefono":
            players = usatelefono(players, turns, projectiles, iprojectile)
        elif input2 == "fucile":
            while True:
                input3 = input(f'Spari su te stesso(Io) o su {players[turns[1]][0]}(Nemico)? ')
                if input3.lower().strip() == 'io' or input3.lower().strip() == 'nemico' or input3.lower().strip() == \
                        players[turns[1]][0].lower().strip():
                    break
                else:
                    animation2(f'Input non valido!')
            if input3.lower().strip() == 'io':
                if projectiles[iprojectile[4]] == 1:
                    players, iprojectile = usafucileiopieno(players, turns, iprojectile)
                    break
                else:
                    iprojectile = usafucileiovuoto(iprojectile)
                    if controllo(projectiles, iprojectile) == 1: break
            else:
                if projectiles[iprojectile[4]] == 1:
                    players, iprojectile = usafucilenemicopieno(players, turns, iprojectile)
                    break
                else:
                    iprojectile= usafucilenemicovuoto(iprojectile)
                    break
        else:
            animation2('Input non valido!')
    return players, iprojectile, projectiles