import json


class Player:
    VERSION = "1.0"


    def betRequest(self, game_state):
        game_data = game_state

        print(game_data)

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

        actives_couter = 0
        for player in game_data["players"]:
            if player["status"] == "active":
                actives_couter += 1

        if actives_couter > 2:
            return 0
        else:
            return to_raise

    def showdown(self, game_state):
        pass
