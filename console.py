#!/usr/bin/python3
""" console programe as entry point of command interpreter"""

import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage

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
        """handle the case of empty line or ENTRER"""
        pass

    dataclass = { 'BaseModel': BaseModel }

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()

    
