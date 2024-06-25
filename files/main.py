from functions import *

players: list = initgame(totplayers = askplayers(), lifes = asklifes())
iprojectile: list = [0]  #[Proiettili(0), P.Pieni(1), P.Vuoti(2), Danno(3), P.Numero(4), Lucchetto(5), P.Tot.(6)]
turns: list = [-2, -1]  #[Attaccante(0), Attaccato(1)]
projectiles: list = []
while 1:
    players = checkifdead(players, turns)
    if len(players) == 1: break
    if iprojectile[0] == 0:
        iprojectile, projectiles = regenprojectiles(players)
        players = genoggetti(players)
    iprojectile, turns = ctrlturni(players, iprojectile, turns)
    if players[turns[0]][0] == 'Bot': players, iprojectile = botgameplay(players, turns, iprojectile, projectiles)
    elif players[turns[0]][1] < 1: pass
    else: players, iprojectile, projectiles = playergameplay(players, turns, iprojectile, projectiles)
print(f'\n{Back.BLUE}{players[0][0]} ha vinto!')