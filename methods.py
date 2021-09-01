import json
    
def showDeathInfo(deathDict):
    print('Death Report: ')
    print(json.dumps(deathDict, indent=4)) #Printa todos os meios de mortes que aconteceram em cada partida


def showGameInfo(gameDict):
    print("Grouped information per match: ")
    print(json.dumps(gameDict, indent=4)) #Printa a informação de cada partida usando json.dumps


def showLeaderboard(gameDict):
    playerScores = {}
    for k in gameDict: #Esse 'for' serve apenas para agrupar o total de kills por jogador no dicionário 'playerScores'
        for j in gameDict[k]:
            if j=='kills':
                for a in gameDict[k][j]:
                    if a not in playerScores:
                        playerScores[a] = gameDict[k][j][a]
                    else:
                        playerScores[a] = playerScores[a]+gameDict[k][j][a]

    playerRanking = {k: v for k, v in sorted(playerScores.items(), key=lambda v: v[1], reverse=True)} #Ordena meu dicionário playerScores em ordem decrescente

    print("Player Ranking: ")
    rankingNumber = 1
    for k, v in playerRanking.items():
        if v>0:
            print(f'{rankingNumber}º',k,'--',v,'pts')
            rankingNumber+=1


def getKillerName(i):
    killerName = i.split(':')
    killerName = killerName[3].split('killed')
    killerName = killerName[0].strip()
    return killerName


def getKilledName(i):
    killedName = i.split(':')
    killedName = killedName[3].split('killed')
    killedName = killedName[1].split('by')
    killedName = killedName[0].strip()
    return killedName


def getCauseOfDeath(i):
    causeOfDeath = i.split('by')
    causeOfDeath = causeOfDeath[1].strip()
    return causeOfDeath


def getPlayerName(i):
    playerName = i.split('n\\')
    playerName = playerName[1].split('\\t')
    playerName = playerName[0].strip()
    return playerName