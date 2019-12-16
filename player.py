import json

class Player:
    VERSION = "1.0"

    def betRequest(self, game_state):
        data = json.loads(game_state)

        return 200

    def showdown(self, game_state):
        pass

