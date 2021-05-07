
from pydventure.actions import game_actions_table
from pydventure.entities import game_entities_table
from pydventure.utils import write
from pydventure.player import player

TRASH_WORDS = ['a', 'the', 'at',]
MOVEMENT_VERBS = ('move', 'go', 'walk', 'run')
STILL_LIFE_VERBS = ('break', 'throw', 'light', 'turn')

# NEED A FUNCTION TO REMOVE SPECIAL CHARACTER ! . : 

class Parser():

    def __init__(self):
        self.trash_words = TRASH_WORDS

    def parser(self, sentence):
        hashed_sentence = sentence.lower().split(' ')
        pure_sentence = [x for x in hashed_sentence if x not in self.trash_words]
        
        action = game_actions_table.get_action(pure_sentence[0])
        if action:
            if len(pure_sentence) > 1:
                entity_name = pure_sentence[1]
                entity = game_entities_table.get_entity(entity_name)
                if entity:
                    if pure_sentence[0] in dir(entity):
                        return getattr(entity, pure_sentence[0])()
                else:
                    return write("Sorry I don't understand.")

            else:
                if action in dir(player):
                    return getattr(player, action)()
                elif action in game_actions_table.standalone_action:
                    if action in dir(player.current_room):
                        return getattr(player.current_room, action)()

        return pure_sentence