#!/usr/bin/python3
""" console programe as entry point of command interpreter"""

import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """ class of command interpreter"""
    
    if sys.stdin.isatty():
        prompt = '(hbnb)'
    else:
        prompt = ''

    def do_quit(self, comnd):
        """cmd to exit the programm"""
        exit()

    def do_EOF(self, arg):
        """ cmd handle 'ctrl + z' or 'ctrl + d'"""
        print("")
        return True

    def emptyline(self):
        """handle  case of empty line or ENTRER"""
        pass

    dataclass = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                }

    def do_create (self, argm):
        """cmd create new intance and save it to json file"""
        if not argm:
            print("** class name missing **")
            return
        elif argm not in HBNBCommand.dataclass.keys():
            print("** class doesn't exist **")
            return
        else:
            new = HBNBCommand.dataclass[arg]()
            models.storage.save()
            print(new.id)

    def do_show (self, argm):
        """ cmd print str represnetation of instace"""
        if not argm:
            print("** class name missing **")
            return
        else:
            argms = argm.split(" ")
            if argms[0] not in HBNBCommand.dataclass.keys():
                print("** class doesn't exist **")
                return
            elif len(argms) == 1:
                print("** instance id is missing **")
                return
            else:
                k = f"{argms[0]}.{argms[1]}"
                try:
                    print(storage._FileStorage__objects[k])
                except KeyError:
                    print("** no instance found **")
    
    def do_destroy(self, argm):
        """cmd that delete  instance based on id"""
        if not argm:
            print("** class name missing **")
            return

        else:
            argms = argm.split(" ")
            if argms[0] not in HBNBCommand.dataclass.keys():
                print("** class doesn't exist **")
                return

            elif len(argms) == 1:
                print("** instance id is missing **")
                return

            else:
                k = f"{argms[0]}.{argms[1]}"
                try:
                    del(storage.all()[k])
                    strorage.save()
                except KeyError:
                    print("** no instance found **")

    def do_all(self, argm):
        """cmd that print str repr of all instance"""
        plist = []
        objects = storage._FileStorage__objects

        if argm:
            clname = argm.split()[0]
            if clname not in HBNBCommand.dataclass:
                print("** class doesn't exist **")
                return
            for key, value in objects.items():
                if key.split('.')[0] == argm:
                    plist.append(str(value))
        else:
            for key, value in objects.items():
                plist.append(str(value))

        print(plist)
    def do_update(self, args):
        """ Updates  certain object with new info """
        c_name = c_id = att_name = att_val = kwargs = ''

        # isolate cls from id/args, ex: (<cls>, delim, <id/args>)
        args = args.partition(" ")
        if args[0]:
            c_name = args[0]
        else:  # class name not present
            print("** class name missing **")
            return
        if c_name not in HBNBCommand.dataclass:  # class name invalid
            print("** class doesn't exist **")
            return

        # isolate id from args
        args = args[2].partition(" ")
        if args[0]:
            c_id = args[0]
        else:  # id not present
            print("** instance id missing **")
            return

        # generate key from class and id
        key = c_name + "." + c_id

        # determine if key is present
        if key not in storage.all():
            print("** no instance found **")
            return

        # first determine if kwargs or args
        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
            kwargs = eval(args[2])
            args = []  # reformat kwargs into list, ex: [<name>, <value>, ...]
            for k, v in kwargs.items():
                args.append(k)
                args.append(v)
        else:  # isolate args
            args = args[2]
            if args and args[0] == '\"':  # check for quoted arg
                second_quote = args.find('\"', 1)
                att_name = args[1:second_quote]
                args = args[second_quote + 1:]

            args = args.partition(' ')

            # if att_name was not quoted arg
            if not att_name and args[0] != ' ':
                att_name = args[0]
            # check for quoted val arg
            if args[2] and args[2][0] == '\"':
                att_val = args[2][1:args[2].find('\"', 1)]

            # if att_val was not quoted arg
            if not att_val and args[2]:
                att_val = args[2].partition(' ')[0]

            args = [att_name, att_val]

        # retrieve dictionary of current objects
        new_dict = storage.all()[key]

        # iterate through attr names and values
        for i, att_name in enumerate(args):
            # block only runs on even iterations
            if (i % 2 == 0):
                att_val = args[i + 1]  # following item is value
                if not att_name:  # check for att_name
                    print("** attribute name missing **")
                    return
                if not att_val:  # check for att_value
                    print("** value missing **")
                    return
                # type cast as necessary
                if att_name in HBNBCommand.types:
                    att_val = HBNBCommand.types[att_name](att_val)

                # update dictionary with name, value pair
                new_dict.__dict__.update({att_name: att_val})
                new_dict.save()

    def do_count(self, args):
        """Count current number of class instances"""
        count = 0
        for k, v in storage._FileStorage__objects.items():
            if args == k.split('.')[0]:
                count += 1
        print(count)

    def help_count(self):
        """ """
        print("Usage: count <class_name>")
if __name__ == '__main__':
    HBNBCommand().cmdloop()

    
