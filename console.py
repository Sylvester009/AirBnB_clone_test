#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        print()
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
            return

        try:
            new_inst = eval(arg)()
            new_inst.save()
            print(new_inst.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return

        try:
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
                return
            elif len(args) == 1:
                print("** instance id missing **")
                return

            instances = storage.all()
            inst_key = args[0] + "." + args[1]
            if inst_key not in instances:
                print("** no instance found **")
                return

            print(instances[inst_key])
        except Exception as e:
            print("**", e.__class__.__name__, str(e), "**")

    def do_all(self, arg):
        args = arg.split()
        try:
            if args and args[0] not in storage.classes():
                print("** class doesn't exist **")
                return

            instances = storage.all()
            if not args:
                print([str(obj) for obj in instances.values()])
            else:
                print([str(obj) for obj in instances.values() if obj.__class__.__name__ == args[0]])
        except Exception as e:
            print("**", e.__class__.__name__, str(e), "**")

    def do_update(self, arg):
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return

        try:
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
                return
            elif len(args) == 1:
                print("** instance id missing **")
                return
            elif len(args) == 2:
                print("** attribute name missing **")
                return
            elif len(args) == 3:
                print("** value missing **")
                return

            instances = storage.all()
            inst_key = args[0] + "." + args[1]
            if inst_key not in instances:
                print("** no instance found **")
                return

            instance = instances[inst_key]
            setattr(instance, args[2], args[3])
            storage.save()
        except Exception as e:
            print("**", e.__class__.__name__, str(e), "**")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
