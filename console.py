#!/usr/bin/python3
"""This module defines the HBNBCommand class, a command interpreter for the AirBnB project."""

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exit the command interpreter."""
        return True

    def do_EOF(self, arg):
        """Exit the command interpreter (Ctrl-D)."""
        print()
        return True

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
