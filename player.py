import json


class Player:
    VERSION = "1.0"

    def get_ranks(self, cards_to_choose_from):
        ranks = []
        for card in range(len(cards_to_choose_from)):
            for cardkey in cards_to_choose_from[card].keys():
                if cardkey == "rank":
                    ranks.append(cards_to_choose_from[card][cardkey])
        return ranks

    def get_suits(self, cards_to_choose_from):
        suits = []
        for card in range(len(cards_to_choose_from)):
            for cardkey in cards_to_choose_from[card].keys():
                if cardkey == "suit":
                    suits.append(cards_to_choose_from[card][cardkey])
        return suits

    def is_flush(self, cards_to_choose_from):
        suits = self.get_suits(cards_to_choose_from)
        for suit in suits:
            if suits.count(suit) > 4:
                return True

    def is_poker(self, cards_to_choose_from):
        ranks = self.get_ranks(cards_to_choose_from)
        for rank in ranks:
            if ranks.count(rank) > 3:
                return True

    def is_drill(self, cards_to_choose_from):
        ranks = self.get_ranks(cards_to_choose_from)
        for rank in ranks:
            if ranks.count(rank) > 2:
                return True


    def is_high_pair(self, cards_to_choose_from):
        ranks = self.get_ranks(cards_to_choose_from)
        HIGHPAIRS = ["10", "J", "Q", "K", "A"]

        for rank in ranks:
            if ranks.count(rank) > 1:
                if rank in HIGHPAIRS:
                    return True

    def get_number_of_pairs(self, cards_to_choose_from):
        num_of_pairs = 0
        ranks = self.get_ranks(cards_to_choose_from)

        for rank in ranks:
            if ranks.count(rank) > 1:
                ranks.remove(rank)
                ranks.remove(rank)
                num_of_pairs += 1

        for rank in ranks:
            if ranks.count(rank) > 1:
                num_of_pairs += 1

        return num_of_pairs

    def betRequest(self, game_state):
        game_data = game_state

        game_round = game_data["round"]
        in_action = game_data["in_action"]  # our player's index
        current_buy_in = game_data["current_buy_in"]
        minimum_raise = game_data["minimum_raise"]
        me = game_data["players"][in_action]
        bet_already_made_me = me["bet"]  # players[in_action][bet]
        my_cards = me["hole_cards"]
        community_cards = game_data["community_cards"]

        cards_to_choose_from = my_cards + community_cards

        to_call = current_buy_in - bet_already_made_me
        to_raise = to_call + minimum_raise

        actives_counter = 0

        for player in game_data["players"]:
            if player["status"] != "out":
                actives_counter += 1

        if game_round == 0:
            if self.get_number_of_pairs(cards_to_choose_from) == 1 or current_buy_in < 20:
                if current_buy_in <= 50:
                    return to_call
                elif self.is_high_pair(cards_to_choose_from) and current_buy_in <= 100:
                    return to_call

        if self.is_poker(cards_to_choose_from):
            to_raise += 400
            return to_raise

        if self.is_flush(cards_to_choose_from):
            to_raise += 300
            return to_raise

        if self.is_drill(cards_to_choose_from):
            to_raise += 200
            return to_raise

        if self.is_high_pair(cards_to_choose_from) and game_round < 2:
            to_raise += 50

        if self.get_number_of_pairs(cards_to_choose_from) == 2:
            to_raise += 100
            return to_raise
        elif self.get_number_of_pairs(cards_to_choose_from) == 1:
            return to_raise

        if actives_counter > 2:
            return 0
        else:

            if game_round == 0:
                if self.get_number_of_pairs(cards_to_choose_from) == 1 or current_buy_in < 20:
                    if current_buy_in <= 50:
                        return to_call
                    elif self.is_high_pair(cards_to_choose_from) and current_buy_in <= 50:
                        return to_call

            if self.is_poker(cards_to_choose_from):
                to_raise += 300
                return to_raise

            if self.is_flush(cards_to_choose_from):
                to_raise += 150
                return to_raise

            if self.is_drill(cards_to_choose_from):
                to_raise += 50
                return to_raise

            if self.is_high_pair(cards_to_choose_from) and game_round < 2:
                to_raise += 20

            if self.get_number_of_pairs(cards_to_choose_from) == 2:
                to_raise += 30
                return to_raise
            elif self.get_number_of_pairs(cards_to_choose_from) == 1:
                return to_raise

            return to_call



    def showdown(self, game_state):
        pass




