winners = {
    "Rock": ("Scissors", "Lizard"),
    "Scissors": ("Paper", "Lizard"),
    "Paper": ("Rock", "Spock"),
    "Lizard": ("Spock", "Paper"),
    "Spock": ("Scissors", "Rock"),
}

method = {
    "Rock": ("crushes Scissors", "crushes Lizard"),
    "Scissors": ("cuts Paper", "decapitates Lizard"),
    "Paper": ("covers Rock", "disproves Spock"),
    "Lizard": ("poisons Spock", "eats Paper"),
    "Spock": ("smashes Scissors", "vaporizes Rock"),
}


class Game:
    def __init__(self, game_id):
        self.p1_went = False
        self.p2_went = False
        self.ready = False
        self.id = game_id
        self.moves = ["", ""]
        self.wins = [0, 0]
        self.ties = 0
    # end

    def get_player_move(self, p):
        """
        :param p: [0, 1]
        :return: Move
        """
        return self.moves[p]
    # end

    def play(self, player, move):
        print(self.moves)
        self.moves[player] = move
        if player == 0:
            self.p1_went = True
        else:
            self.p2_went = True
        # end
    # end

    def connected(self):
        return self.ready
    # end

    def both_went(self):
        return self.p1_went and self.p2_went
    # end

    def winner(self):
        p1 = self.moves[0]
        p2 = self.moves[1]

        if p2 in winners[p1]:
            return 0, p1 + " " + method[p2][winners[p1].index(p2)]
        elif p1 in winners[p2]:
            return 1, p2 + " " + method[p1][winners[p2].index(p1)]
        else:
            return -1, -1
    # end

    def reset_went(self):
        self.p2_went = False
        self.p1_went = False
    # end
# end
