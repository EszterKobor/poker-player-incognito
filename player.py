import json


class Player:
    VERSION = "1.0"


    def betRequest(self, game_state):
        game_data = json.loads(game_state)

        in_action = game_data["in_action"]  # our player's index
        current_buy_in = game_data["current_buy_in"]
        minimum_raise = game_data["minimum_raise"]
        me = game_data["players"][in_action]
        bet_already_made_me = me["bet"]  # players[in_action][bet]
        my_cards = me["hole_cards"]
        community_cars = game_data["community_cards"]
        # card_a_can_choose_from =

        to_call = current_buy_in - bet_already_made_me
        to_raise = to_call + minimum_raise



        return 1000


    def showdown(self, game_state):
        pass

