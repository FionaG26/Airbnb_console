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
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Exit the command interpreter"""
        return True

    def do_EOF(self, arg):
        """Exit the command interpreter"""
        return True

    def emptyline(self):
        """Do nothing on empty input."""
        pass

    def do_create(self, arg):
        """Create a new instance of the specified class."""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Show the string representation of an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            obj_id = args[1]
            key = "{}.{}".format(cls_name, obj_id)
            storage = FileStorage()
            storage.reload()
            all_objs = storage.all()
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            obj_id = args[1]
            key = "{}.{}".format(cls_name, obj_id)
            storage = FileStorage()
            storage.reload()
            all_objs = storage.all()
            if key in all_objs:
                del all_objs[key]
                storage.save()
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Print all string representations of all instances."""
        args = arg.split()
        storage = FileStorage()
        storage.reload()
        all_objs = storage.all()
        if not args:
            print([str(all_objs[key]) for key in all_objs])
        else:
            try:
                cls_name = args[0]
                print([str(all_objs[key])
                       for key in all_objs if key.startswith(cls_name)])
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance attribute by id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            obj_id = args[1]
            key = "{}.{}".format(cls_name, obj_id)
            storage = FileStorage()
            storage.reload()
            all_objs = storage.all()
            if key not in all_objs:
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            attr_name = args[2]
            attr_value = args[3]
            setattr(all_objs[key], attr_name, attr_value)
            all_objs[key].save()
        except NameError:
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
