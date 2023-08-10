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
        """hadle the case of empty line or ENTRER"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

    
