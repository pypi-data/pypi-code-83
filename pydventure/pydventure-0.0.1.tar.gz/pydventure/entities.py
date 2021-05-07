from pydventure.utils import write
from pydventure.player import player

#######################
# 1 ENTITIES TABLE
#######################

class GameEntitiesTable:
    """
        Store all entities from the game
        :param rooms: dict\n
        :param objects: dict\n
        function get_room(room_name): return room entity based on its name.\n
        function get_object(object_name): return object entity based on its name.\n
        function get_entity(entity_name): return entity based on its name.\n
        function add_room(room_entity, synonyms): add a room entity to the entities table.
        function add_object(object_entity, synonyms): add an object entity to the entities table.
        function add_entity(entity, synonyms): add an entity to the entities table.
    """
    def __init__(self, rooms={}, objects={}):
        self.rooms = rooms
        self.objects = objects
    
    def get_room(self, room_name):
        for synonyms in self.rooms:
            if room_name in synonyms:
                return self.rooms[synonyms]
        return None

    def get_object(self, object_name):
        for synonyms in self.objects:
            if object_name in synonyms:
                return self.objects[synonyms]

    def get_entity(self, entity_name):
        # Check if it is a room
        if self.get_room(entity_name):
            return self.get_room(entity_name)
        elif self.get_object(entity_name):
            return self.get_object(entity_name)
        else:
            return None

    def add_room(self, room_entity, synonyms):
        if not self.get_room(room_entity.name):
            self.rooms[tuple(synonyms)] = room_entity
    
    def add_object(self, object_entity, synonyms):
        if not self.get_room(object_entity.name):
            self.objects[tuple(synonyms)] = object_entity

    def add_entity(self, entity, synonyms):
        if entity.entity_type == "room":
            self.add_room(entity, entity.synonyms)
        else:
            self.add_object(entity, entity.synonyms)

game_entities_table = GameEntitiesTable()

#-#-#-#-#-#-#-#-#

#######################
# 2 ENTITIES BUILDER
#######################

class EntityBuilder:

    def __init__(self, name, description, entity_type, synonyms=[], routine=""):
        self.entity_type = entity_type
        self.name = name
        self.description = description
        self.synonyms = [synonym.lower() for synonym in synonyms]
        self.routine = routine
        

        game_entities_table.add_entity(self, self.synonyms)
    




    def examine(self):
        return write(self.description)


class RoomEntity(EntityBuilder):
    """
    Create a Room object.

    :param id: str (give the upcase name is a good convention, if the name is unique accross your game)\n
    :param name: str\n
    :param description: str\n
    :param exits: array of rooms id (order matters [N,E,S,W])\n
    :param objects: array of objects id available in the room\n
    :param synonyms: array of string\n
    """
    def __init__(self, name, description="", exits=[], synonyms=[], flags=["f_on"], state={}, routine=""):
        super().__init__(name.lower(), description, "room", synonyms, routine=routine)
        self.exits = exits
        self.objects = []
        


    def show_description(self):
        write(self.description)
        if self.objects:
            write("In this room there are :")
            objects = "\n".join([entity.name for entity in self.objects])
            write(objects)
                
    def has_entity(self, entity):
        if entity in self.objects:
            return True
        return False

    def look(self):
        write(f'You are looking at the {self.name}')
        return self.show_description()
    
    def examine(self):
        write(f'You are examining the {self.name}')
        return self.show_description()

class ObjectEntity(EntityBuilder):
    """
        Create an Object entity.

        :param name: str\n
        :param description: str\n
        :param room: RoomEntity type object - Room where the Object will be\n
        :param synonyms: array of synonyms for the name of the object\n
        :param flags: array\n
        :param state: dict\n
    """
    def __init__(self, name, description, room, synonyms=[], flags=["f_take"], state={}, routine=""):
        super().__init__(name.lower(), description, "object", synonyms, routine=routine)
        self.room = room
        self.flags = flags
        self.state = state

        self.add_object_to_room(room)
    

    def add_object_to_room(self, room):
        room.objects.append(self)

    def remove_object_from_room(self, room):
        room.objects.remove(self)
        
    def set_state(self, name_of_state, new_state):
        print(self.state, name_of_state)
        if name_of_state in self.state:
            self.state[name_of_state] = new_state
        else:
            raise KeyError

    def has_flag(self, flag):
        return flag in self.flags

    def take(self):
        """
            Take an object and add to the inventory of the player if the object exists

            :param item: array
        """
        if self.has_flag("f_take"):
            if player.current_room.has_entity(self):
                player.add_to_inventory(self)
                return write(f"You took the {self.name} and put it in your inventory.")
            elif player.has_entity(self):
                return write("You already have it.")
        else:
            return write("You can't take this object")

    def drop(self):
        player.remove_from_inventory(self)
        return write(f"You dropped {self.name}.")
    
    def examine(self):
        if self.state["on"]:
            return write("Lamp is on")
        else:
            return write("Lamp is off")

#-#-#-#-#-#-#-#-#


