#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """EOF command to exit the program"""
        print("")
        return True 

    prompt = "(hbnb) "

    def emptyline(self):
        """Dosen't execute anything upon an empty line prompt"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
