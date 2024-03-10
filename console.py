#!/usr/bin/python3
import cmd
import re
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF (Ctrl+D) signal to exit the program.
        """
        print()
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """
        Create a new instance of BaseModel and save it to the JSON file.
        Usage: create <class_name>
        """
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
        """
        Show the string representation of an instance.
        Usage: show <class_name> <id>
        """
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        Delete an instance based on the class name and id.
        Usage: destroy <class_name> <id>
        """
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
        """
        Print the string representation of all instances or a specific class.
        Usage: all [<class_name>]
        """
        objects = storage.all()
        if not line:
            print([str(obj) for obj in objects.values()])
        elif line in self.valid_classes:
            print([str(obj) for key, obj in objects.items() if key.split('.')[0] == line])
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
        Update an instance by adding or updating an attribute.
        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        classname, uid = args[:2]
        key = "{}.{}".format(classname, uid)
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        obj = storage.all()[key]
        attribute = args[2]
        value = args[3]
        if hasattr(obj, attribute):
            try:
                value = eval(value)
            except (NameError, SyntaxError):
                pass
            setattr(obj, attribute, value)
            obj.save()
        else:
            print("** no attribute found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
