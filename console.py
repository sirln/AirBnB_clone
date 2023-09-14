#!/usr/bin/python3
'''
HBNB Console Module
'''
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    '''
       HBNBCommand class
    '''
    prompt = '(hbnb) '
    ALLOWED_CLASSES = [
                        "Amenity",
                        "BaseModel",
                        "City",
                        "",
                        "Review",
                        "State",
                        "User"
                    ]

    def do_quit(self, args):
        '''Quit command to exit the program
        '''
        return True

    def do_EOF(self, args):
        '''Handle EOF and print a new line before exiting
        '''
        print()
        return True

    def emptyline(self):
        '''
        Handle empty line
        '''
        pass

    def do_create(self, args):
        '''Create a new instance of BaseModel class. \
save the instance to a JSON file and prints its id
        '''
        commands = args.split()
        if not commands:
            print('** class name missing **')
            return
        if commands[0] not in HBNBCommand.ALLOWED_CLASSES:
            print("** class doesn't exist **")
            return
        try:
            # class_name = eval(commands[0])
            # class_inst = class_name()
            class_inst = eval(commands[0])()
            print(f'{class_inst.id}')
            storage.save()
        except Exception:
            print("** class doesn't exist **")

    def do_show(self, args):
        '''Prints the string representation \
of an instance based on the class name and id
        '''
        commands = args.split()
        if not commands:
            print('** class name missing **')
            return
        if len(commands) < 2:
            print('** instance id missing **')
            return
        if commands[0] not in HBNBCommand.ALLOWED_CLASSES:
            print("** class doesn't exist **")
            return
        try:
            if eval(commands[0]):
                pass
        except Exception:
            print("** class doesn't exist **")
            return

        class_instances = storage.all()
#        for key in class_instances.keys():
#            x = key.split('.')
#            inst_id = x[1]
#            if commands[1] == inst_id:
#                print(class_instances[key])
        key = f'{commands[0]}.{commands[1]}'
        if key in class_instances:
            print(class_instances[key])
        else:
            print('** no instance found **')

    def do_destroy(self, args):
        '''Delete an instance based on the class name an id \
save the changes into the JSON file)
        '''
        commands = args.split()
        if len(commands) == 0:
            print('** class name missing **')
            return
        if len(commands) < 2:
            print('** instance id missing **')
            return
        if commands[0] not in HBNBCommand.ALLOWED_CLASSES:
            print("** class doesn't exist **")
            return
        try:
            if eval(commands[0]):
                pass
        except Exception:
            print("** class doesn't exist **")
            return

        class_instances = storage.all()
#        for key in class_instances.keys():
#            x = key.split('.')
#            inst_id = x[1]
#            if commands[1] == inst_id:
#                del class_instances[key]
#                storage.save()
#            else:
#                print('** no instance found **')
        key = f'{commands[0]}.{commands[1]}'
        if key in class_instances:
            del class_instances[key]
            storage.save()
        else:
            print('** no instance found **')

    def do_all(self, args):
        '''Print all string representation of all \
instances based or not on the class name
        '''
        commands = args.split()
        if len(commands) == 0:
            instances = storage.all().values()
            for instance in instances:
                print(instance)
            return
        if commands[0] not in HBNBCommand.ALLOWED_CLASSES:
            print("** class doesn't exist **")
            return
        try:
            if eval(commands[0]):
                pass
        except Exception:
            print("** class doesn't exist **")

        # instances = storage.all().values()
        # list_instances = [str(instance) for instance in instances]
        # print(list_instances)
        for key, instance in storage.all().items():
            if commands[0] in key:
                print(instance)

    def do_update(self, args):
        ''' Updates an instance based on the class name and id by adding \
or updating attribute save the changes into the JSON file
        '''
        commands = args.split()
        if len(commands) == 0:
            print('** class name missing **')
            return
        if len(commands) == 1:
            print('** instance id missing **')
            return
        if len(commands) == 2:
            print('** attribute name missing **')
            return
        if len(commands) == 3:
            print('** value missing **')
            return
        if commands[0] not in HBNBCommand.ALLOWED_CLASSES:
            print("** class doesn't exist **")
            return
        try:
            if eval(commands[0]):
                pass
        except Exception:
            print("** class doesn't exist **")
            return

        class_instances = storage.all()
        key = f'{commands[0]}.{commands[1]}'
        attr_list = ['id', 'created_at', 'updated_at']
        allowed_data_types = ['str', 'int', 'float']
        attr_name = commands[2]
        attr_value = commands[3]
        if key in class_instances:
            instance = class_instances[key]
            ''''
            if hasattr(instance, attr_name) and attr_name not in attr_list:
                attr_type = type(getattr(instance, attr_name))
                casted_value = attr_type(attr_value)
                setattr(instance, attr_name, casted_value)
                storage.save()
            else:
                if type(attr_name).__name__ in allowed_data_types:
                    if (type(attr_name).__name__) == 'str':
                        attr_value = attr_value.strip('"').strip("'")
                    setattr(instance, attr_name, attr_value)
                    storage.save()
            '''
            if hasattr(instance, attr_name):
                attr_type = type(getattr(instance, attr_name))
                try:
                    casted_value = attr_type(attr_value)
                    setattr(instance, attr_name, casted_value)
                except ValueError:
                    print("** value type does not match attribute type **")
                storage.save()
        else:
            print('** no instance found **')


if __name__ == "__main__":
    HBNBCommand().cmdloop()
