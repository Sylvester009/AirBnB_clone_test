#!/usr/bin/python3
import cmd
import re
from models import storage
from datetime import datetime
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

        try:
            new_inst = eval(args[0])()
            new_inst.save()
            print(new_inst.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id."""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        instance_id = args[1] if len(args) > 1 else None
        if not instance_id:
            print("** instance id missing **")
            return

        key = "{}.{}".format(class_name, instance_id)
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """Prints all instances of a class."""
        args = line.split()
        if not args:
            print([str(obj) for obj in storage.all().values()])
        elif args[0] in storage.all():
            class_name = args[0]
            instances = [
                str(obj) for key, obj in storage.all().items()
                if key.startswith(class_name + '.')
            ]
            print(instances)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s(".*"|[^"]\S*)?)?)?)?'
        match = re.search(rex, line)

        if not match:
            print("** invalid command format **")
            return

        classname, uid, attribute, value = match.groups()

        if classname not in storage.all():
            print("** class doesn't exist **")
            return
        elif not uid:
            print("** instance id missing **")
            return

        key = "{}.{}".format(classname, uid)
        if key not in storage.all():
            print("** no instance found **")
            return
        elif not attribute:
            print("** attribute name missing **")
            return
        elif not value:
            print("** value missing **")
            return

        obj = storage.all()[key]
        setattr(obj, attribute, value)
        obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
