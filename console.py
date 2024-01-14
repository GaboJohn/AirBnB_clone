#!/usr/bin/python3
"""This module defines the HBNBCommand class, a command interpreter for the AirBnB project."""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, mint):
        """Exit the command interpreter."""
        return True

    def do_EOF(self, mint):
        """Exit the command interpreter (Ctrl-D)."""
        print()
        return True

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

    def do_create(self, mint):
        """
        Creates a new instance of BaseModel, saves it, and prints the id
        """
        if not mint:
            print("** class name missing **")
            return
        try:
            inst = eval(mint)()
            inst.save()
            print(inst.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, args):
        """
        Prints the string representation of an instance based on the class name and id.
        Usage: show <class name> <id>
        """
        if not args:
            print("** class name missing **")
            return

        arg_list = args.spilt()
        class_name = arg_list[0]
        try:
            eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return

        if len(arg_list) < 2:
            print("** instance id missing **")
            return

            obj_id = arg_list[1]
            key = "{}.{}".format(class_name, obj_id)
            obj = storage.all().get(key)
            if obj:
                print(obj)
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id.
        Usage: destroy <class name> <id>
        """
        if not args:
            print("** class name missing **")
            return

        arg_list = args.split()
        class_name = args_list[0]
        try:
            eval(class_name)
        except NameError:
             print("** class doesn't exist **")
             return
        
        if len(arg_list) < 2:
             print("** instance id missing **")
             return

        obj_id = arg_list[1]
        key = "{}.{}".format(class_name, obj_id)
        obj = storage.all().get(key)
        if obj:
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding or updating attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        if not args:
            print("** class name missing **")
            return

        args_list = args.split()
        class_name = args_list[0]
        try:
            eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return

        if len(arg_list) < 2:
            print("** instance id missing **")
            return

            obj_id = args[1]
            key = "{}.{}".format(class_name, obj_id)
            obj = storage.all().get(key)
            if obj:
                if len(args) < 3:
                    print("** attribute name missing **")
                    return

                attr_name = args[2]
                if len(args) < 4:
                    print("** value missing **")
                    return
                attr_value = args[3].strip('"')
                if hasattr(obj, attr_name):
                    attr_type = type(getattr(obj, attr_name))
                    setattr(obj, attr_name, attr_type(attr_value))
                    storage.save()
                else:
                    print("** attribute doesn't exist **")
            else:
                print("** no instance found **")

    def do_all(self, args):
        """
        Prints all string representation of all instances based or not on the class name.
        Usage: all [<class name>]
        """

        args_list = args.split()
        objects = storage.all()
        
        if not arg_list:
            print([str(obj) for obj in objects.values()])
        else:
            try:
                class_name = arg_list[0]
                eval(class_name)
                filt_obj = [str(obj) for obj in objects.values() if obj.__class__.__name__ == class_name]
                print(filt_obj)
            except NameError:
                print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
