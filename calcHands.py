from pokerkit import Card, Deck, StandardHighHand
from itertools import combinations


def getStats(inputPlayers, board):
    finalBoardSize = 5
    totalCombos = 0

    players = []
    for player in inputPlayers:
        players.append({'wins': 0, 'draws': 0, 'losses': 0, "holeCards": list(Card.parse(player))})

    currentBoardSize = len(list(Card.parse(board)))
    remainingDraws = int(finalBoardSize-currentBoardSize)

    known_cards_string = board + "".join(inputPlayers)
    known_cards = list(Card.parse(known_cards_string))
    deck = list(Deck.STANDARD)
    for card in known_cards:
        deck.remove(card)

    for combo in combinations(deck, remainingDraws):
        totalCombos += 1
        newBoard = list(Card.parse(board)) + list(combo)
        hands = []
        for player in players:
            hand = StandardHighHand.from_game(player["holeCards"], newBoard)
            player["hand"] = hand
            hands.append(hand)
        winners = []
        bestHand = max(hands)
        for player in players:
            if player["hand"] == bestHand:
                winners.append(player)
            else:
                player["losses"] += 1
        for player in winners:
            if len(winners) > 1:
                player["draws"] += 1
            else:
                player["wins"] += 1

    output = []
    for player in players:
        winRate = player['wins']/totalCombos*100
        drawRate = player['draws']/totalCombos*100
        lossRate = player['losses']/totalCombos*100
        output.append({"winRate": winRate, "drawRate": drawRate, "lossRate": lossRate})
    return(output)


inputPlayers = ["AsKs", "Th5c", "Qs6s"]
# board = 'Qh9h5s'
board = 'Qh9h'

print(getStats(inputPlayers, board))