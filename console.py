#!/usr/bin/python3
"""Module for the entry point"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    prompt= "(hbnb)"

    def do_quit(self,arg):
        """Exit the command interpreter"""
        return True

    def do_EOF(self, arg):
        """Exit the command interpreter"""
        return True

    def emptyline(self):
        """Do nothing on empty input."""
        pass
