#!/usr/bin/python3
"""
Module for console
"""
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand console class
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def do_EOF(self, arg):
        """
        EOF (Ctrl+D) signal to exit the program.
        """
        print()
        return True

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def help_quit(self):
        """
        Quit command to exit the program
        """
        print("Quit command to exit the program")

    def help_EOF(self):
        """
        EOF command to exit the program
        """
        print("EOF (Ctrl+D) signal to exit the program.")

    def do_help(self, arg):
        """
        Get help for commands
        """
        cmd.Cmd.do_help(self, arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
