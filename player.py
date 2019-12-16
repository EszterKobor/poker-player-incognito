import json


class Player:
    VERSION = "1.0"


    def betRequest(self, game_state):
        game_data = json.loads(game_state)

        in_action = game_state["in_action"]  # our player's index
        current_buy_in = game_state["current_buy_in"]
        minimum_raise = game_state["minimum_raise"]
        bet_already_made_me = game_data["players"][in_action]["bet"]  # players[in_action][bet]

        to_call = current_buy_in - bet_already_made_me
        to_raise = to_call + minimum_raise

        return to_raise


    def showdown(self, game_state):
        pass

