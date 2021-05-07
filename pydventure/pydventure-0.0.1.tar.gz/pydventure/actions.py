from types import FunctionType
from pydventure.utils import write

class ActionCommands:
    def __init__(self):
        self.actions_table = {}
        self.standalone_action = ['look', 'examine']

    def add_action(self, command, synonyms):
        self.actions_table[tuple(synonyms)] = command

    def get_action(self, command):
        for action_synonyms in self.actions_table:
            if command in action_synonyms:
                return self.actions_table[action_synonyms]
        return None

game_actions_table = ActionCommands()


game_actions_table.add_action("p_move", ['move', 'go', 'walk'])
game_actions_table.add_action("look", ['look', 'l'])
game_actions_table.add_action("p_inventory", ['inventory', 'i', 'backpack'])
game_actions_table.add_action("o_throw", ['throw','launch', 'toss', 'lift'])
game_actions_table.add_action("take", ['take', 'grab', 'catch'])
game_actions_table.add_action("drop", ['drop',])
game_actions_table.add_action("examine", ['examine','check','lookat'])





