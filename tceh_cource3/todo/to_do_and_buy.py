# -*- coding: utf-8 -*-

from __future__ import print_function

import inspect
import sys

from commands import (
    BaseCommand,

    UserExitException,
)
from models import (
    Storage,
)
from utils import get_input_function

__author__ = 'sobolevn'


def get_routes():
    # Dynamic load
    # def class_filter(klass):
    #     return inspect.isclass(klass) \
    #            and klass.__module__ == BaseCommand.__module__ \
    #            and issubclass(klass, BaseCommand) \
    #            and klass is not BaseCommand

    # routes = inspect.getmembers(
    #     sys.modules[BaseCommand.__module__],
    #     class_filter
    # )
    # return dict((route.label(), route) for _, route in routes)

    from commands import ListCommand, NewCommand, ExitCommand
    return {
        ListCommand.label(): ListCommand,
        NewCommand.label(): NewCommand,
        ExitCommand.label(): ExitCommand,
        # DoneCommand.label(): DoneCommand,
    }


def perform_command(command):
    command = command.lower()
    routes = get_routes()

    try:
        command_class = routes[command]
        command_inst = command_class(command)

        storage = Storage()
        command_inst.perform(storage.items)
    except KeyError:
        print('Bad command, try again.')
    except UserExitException as ex:
        print(ex)
        raise


def parse_user_input():
    input_function = get_input_function()

    message = 'Input your command: (%s): ' % '|'.join(
            get_routes().keys())
    return input_function(message)


def main():
    while True:
        try:
            command = parse_user_input()
            perform_command(command)
        except UserExitException:
            break
        except KeyboardInterrupt:
            print('Shutting down, bye!')
            break


if __name__ == '__main__':
    main()
