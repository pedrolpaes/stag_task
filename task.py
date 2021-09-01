import methods

log = open('qgames.log', 'r')
gameCounter = 1
games = {}
deathReport = {}

for i in log:
    if "InitGame:" in i:
        total_kills=0
        playerList = []
        kills = {}
        gameName = "game_"+str(gameCounter)
        gameCounter+=1
        games[gameName] = {
            'total_kills': total_kills, 
            'players': playerList, 
            'kills': kills
        }
        killed_by_means = {}
        deathReport[gameName] = {'killed_by_means': killed_by_means}  

    if "ClientUserinfoChanged:" in i:
        playerName = methods.getPlayerName(i)
        if playerName not in games[gameName]['players']: #Se o jogador ainda não existe no dicionário''players', 'players' e 'kills' inicializam devidamente
            games[gameName]['players'].append(playerName)
            games[gameName]['kills'][playerName] = 0

    if "Kill" in i:
        games[gameName]['total_kills'] = total_kills=total_kills+1 #incrementa no contador total de mortes

        causeOfDeath = methods.getCauseOfDeath(i)
        if causeOfDeath in deathReport[gameName]['killed_by_means'].keys(): #Se a causa da morte já existe na lista de mortes da partida atual, incrementa em 1
            deathReport[gameName]['killed_by_means'][causeOfDeath]+=1
        else:                                                               # se não, inicializa essa nova causa com 1
            deathReport[gameName]['killed_by_means'][causeOfDeath]=1
        
        if "<world>" in i:
            killedName = methods.getKilledName(i)
            games[gameName]['kills'][killedName] = games[gameName]['kills'][killedName]-1 
        else:
            killerName = methods.getKillerName(i)
            killedName = methods.getKilledName(i)
            if killerName != killedName: #Um player não ganha kill por matar a si mesmo
                games[gameName]['kills'][killerName] = games[gameName]['kills'][killerName]+1

methods.showGameInfo(games)
print("")
methods.showLeaderboard(games)
print("")
methods.showDeathInfo(deathReport)