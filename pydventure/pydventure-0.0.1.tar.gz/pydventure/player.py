from pydventure.utils import write

class Player:
    def __init__(self):
        self.inventory = []
        self.current_room = None
    
    def remove_from_inventory(self, entity):
        if entity in self.inventory:
            self.inventory.remove(entity) # Remove the entity from inventory
            entity.add_object_to_room(self.current_room) # Add the entity to the current room
        else:
            return write(f"You don't have any {entity.name} in your inventory.")

    def add_to_inventory(self, entity):
        if entity not in self.inventory:
            entity.remove_object_from_room(entity.room)
            self.inventory.append(entity)
    
    def has_entity(self, entity):
        if entity in self.inventory:
            return True
        return False
    
    def p_inventory(self):
        if self.inventory:
            return write(f'You have {", ".join([item.name for item in self.inventory])} in your inventory.')
        else:
            return write(f'You have nothing in your inventory.')

player = Player()