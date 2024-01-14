#!/usr/bin/python3
"""This module defines the HBNBCommand class, a command interpreter for the AirBnB project."""

import cmd
from models import storage
from models.base_model import BaseModel

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

    def do_show(self, mint):
        """
        Prints the string representation of an instance based on the class name and id.
        Usage: show <class name> <id>
        """
        args = mint.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if class_name not in ["BaseModel"]:
                raise NameError
            obj_id = args[1]
            key = class_name + "." + obj_id
            obj = storage.all().get(key)
            if obj:
                print(obj)
            else:
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, mint):
        """
        Deletes an instance based on the class name and id.
        Usage: destroy <class name> <id>
        """
        args = mint.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if class_name not in ["BaseModel"]:
                raise NameError
            obj_id = args[1]
            key = class_name + "." + obj_id
            obj = storage.all().get(key)
            if obj:
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, mint):
        """
        Updates an instance based on the class name and id by adding or updating attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = mint.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if class_name not in ["BaseModel"]:
                raise NameError
            obj_id = args[1]
            key = class_name + "." + obj_id
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
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, mint):
        """
        Prints all string representation of all instances based or not on the class name.
        Usage: all [<class name>]
        """
        args = mint.split()
        objects = storage.all()
        if not args:
            print([str(obj) for obj in objects.values()])
        else:
            try:
                class_name = args[0]
                if class_name not in ["BaseModel"]:
                    raise NameError
                filt_obj = [str(obj) for obj in objects.values() if obj.__class__.__name__ == class_name]
                print(filt_obj)
            except NameError:
                print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
