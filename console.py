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

    def do_quit(self, args):
        """Exit the command interpreter."""
        return True

    def do_EOF(self, args):
        """Exit the command interpreter (Ctrl-D)."""
        print()
        return True

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it, and prints the id
        """
        if not args:
            print("** class name missing **")
            return
        try:
            inst = eval(args)()
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

        arg_list = args.split()
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
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding or updating attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
               update <class name> <id> <dictionary representation>
        """
        if not args:
            print("** class name missing **")
            return

        arg_list = args.split()
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
            if len(arg_list) < 3:
                print("** attribute name missing **")
                return

            attr_name = arg_list[2]
            if len(arg_list) < 4:
                print("** value missing **")
                return

            attr_value = arg_list[3].strip('"')
            if attr_value.startswith("{") and attr_value.endswith("}"):
                try:
                    attr_dict = eval(attr_value)
                    for k, v in attr_dict.items():
                        setattr(obj, k, v)
                except (NameError, SyntaxError):
                    print("** invalid dictionary representation **")
                    return
            else:
                if hasattr(obj, attr_name):
                    attr_type = type(getattr(obj, attr_name))
                    setattr(obj, attr_name, attr_type(attr_value))
                else:
                    print("** attribute doesn't exist **")
                    return

            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """
        Prints all string representation of all instances based or not on the class name.
        Usage: all [<class name>]
               <class name>.all()
        """
        try:
            arg_list = args.split()
            objects = storage.all()

            if not arg_list:
                print([str(obj) for obj in objects.values()])
            else:
                class_name = arg_list[0]
                try:
                    obj_class = eval(class_name)
                    if len(arg_list) > 1 and arg_list[1] == '.all()':
                        obj_list = obj_class.all()
                    else:
                        raise AttributeError(f"Class '{class_name}' has no attribute 'all'")
                    print([str(obj) for obj in obj_list])
                except (NameError, AttributeError) as e:
                    print(f"** {e} **")
        except Exception as e:
            print(f"Error: {e}")

    def default(self, line):
        """Called on an input line when the command prefix is not recognized."""
        try:
            # Execute the input line as Python code
            eval_result = eval(line)
            if eval_result is not None:
                print(eval_result)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
