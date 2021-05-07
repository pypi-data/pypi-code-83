import sys, random
from time import sleep
from pydventure.parser import Parser, TRASH_WORDS
from pydventure.entities import game_entities_table
from pydventure.player import player
from pydventure.utils import write


class GameEngine(Parser):
    def __init__(self, introduction_text="Introduction"):
        self.end = False
        self.introduction_text = introduction_text
        self.writing_speed = 0.1
        super().__init__()

    def set_start_room(self, room):
        self.start_room = room
        self.current_room = self.start_room
        player.current_room = self.start_room

    def game_loop(self):
        
        write(self.introduction_text)

        while not self.end:
            command = input(">> ")
            if command == 'exit':
                self.end = True
            else:
                self.parser(command)

