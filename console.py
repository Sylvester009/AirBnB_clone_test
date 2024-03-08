#!/usr/bin/python3
import cmd
import re
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        print()
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file)"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.all():
            print("** class doesn't exist **")
            return

        new_instance = storage.all()[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.all():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all()[args[0]]:
            print("** no instance found **")
            return

        print(storage.all()[args[0]][key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.all():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all()[args[0]]:
            print("** no instance found **")
            return

        del storage.all()[args[0]][key]
        storage.save()

    def do_all(self, line):
        """Prints all instances of a class."""
        args = line.split()
        if args and args[0] not in storage.all():
            print("** class doesn't exist **")
            return

        instances = storage.all().get(args[0], {}).values() if args else storage.all()
        print([str(obj) for obj in instances])

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        match = re.match(r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s(".*"|[^"]\S*)?)?)?)?', line)
        if not match:
            print("** invalid command format **")
            return

        classname, uid, attribute, value = match.groups()

        if classname not in storage.all():
            print("** class doesn't exist **")
            return
        if not uid:
            print("** instance id missing **")
            return

        key = "{}.{}".format(classname, uid)
        if key not in storage.all()[classname]:
            print("** no instance found **")
            return
        if not attribute:
            print("** attribute name missing **")
            return
        if not value:
            print("** value missing **")
            return

        obj = storage.all()[classname][key]
        setattr(obj, attribute, value)
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
