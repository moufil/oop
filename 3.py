












from random import randrange

class Card:
    """ 
        Одна игральная карта 
        0 - ♠
        1 - ♣
        2 - ♥
        3 - ♦
    """
    
    RANKS = ["Т", "2", "3", "4", "5", "6", "7", "8", "9", "10", "В", "Д", "K"]
    SUITS = [u'\u2660', u'\u2663', u'\u2665', u'\u2666'] 

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        return Card.RANKS[self.rank - 1] + Card.SUITS[self.suit]

players_count = int(input('Сколько игроков играет : '))
score = [0] * players_count
for round in range(int(input("Кол-во раундов : "))):
    players = []
    for i in range(players_count):
        players.append(Card(randrange(1, 14), randrange(0, 4)))

    winner = []
    count = 0
    noone = False
    for i in range(len(players)):
        print(f"У игрока {i + 1} выпала карта {str(players[i])}")
        if count < players[i].rank:
            count = players[i].rank
            winner = [i]
            noone = False
        elif count == players[i].rank:
            winner.append(i)
            noone = True

    if len(winner) <= 1:
        print(f"В раунде {round + 1} победил игрок {winner[0] + 1}")
        score[winner[0]] += 1
    else:
        print(f"В раунде {round + 1} ничья")
    print("")

final = ''
for i in range(players_count):
    final += f'У игрока {i + 1} {score[i]} очков \n'

print(final)