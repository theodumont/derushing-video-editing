# encoding: utf-8
"""
CLI for the video_logging.py module.
"""

import os
import sys
import json
import src.video_logging as log


class CLI(object):
    """CLI for the video_logging module."""

    def __init__(self, data):
        """
        Class constructor.
        """
        # data files
        self.EXTENSIONS = data["EXTENSIONS"]
        self.HELP = data["HELP"]
        self.HEADER = data["HEADER"]
        # list of all parameters accepted to trigger the different modes.
        self.change_list = ["cd", "c", "go"]
        self.folder_list = ["folder", "f", "folders"]
        self.trash_list = ["trash", "t", "short"]
        self.date_list = ["date", "d", "when"]
        self.help_list = ["help", "h", "?", "what", "how"]
        self.exit_list = ["exit", "e", "leave", "l", "quit", "q"]
        # folder to clean
        self.folder = os.getcwd()

    def read_command(self, command):
        """
        Read from the users command.
        """
        # cursor is used to keep track of how many argument we read from the users command.
        cursor = 0
        split_command = str.split(command)
        if len(split_command) == 0:
            # Empty line, we can just ignore it
            return
        # else ...
        instruction = split_command[0]
        cursor += 1

        if instruction.lower() in self.change_list:
            self.process_change_dir(split_command, cursor)

        elif instruction.lower() in self.folder_list:
            self.process_folder()

        elif instruction.lower() in self.trash_list:
            self.process_trash(split_command, cursor)

        elif instruction.lower() in self.date_list:
            self.process_date()

        elif instruction.lower() in self.help_list:
            self.process_help(split_command, cursor, self.EXTENSIONS, self.HELP)

        elif instruction.lower() in self.exit_list:
            self.exit()
        else:
            print(f"The input command {command} could not be parsed, because the tool did not understand the term '{instruction}'. If you wish to you can use :\n'>> help'\nThat instruction will bring a list of the available instruction and their use cases.")

    def exit(self):
        """
        Used to leave the tool.
        """
        print("Leaving the tool...\n")
        sys.exit(0)

    def process_change_dir(self, split_command, cursor):
        """
        When the 'cd' command is read.
        """
        if len(split_command) == cursor:
            # i.e. we have no more arguments available
            print(f"Where do you want to go?")
            print(f"The syntax to change directory is:\n'>> cd <directory>'")
        else:
            directory = " ".join(split_command[cursor:])
            cursor += 1
            try:
                os.chdir(directory)
                self.folder = os.getcwd()
                # display(self)
            except FileNotFoundError as e:
                print(f"Cannot find the {directory} directory. The correct syntax to change the directory is :\n'>> cd <directory>'")

    def process_folder(self):
        """
        When the 'folder' command is read.
        """
        log.folder_sort(self.EXTENSIONS)

    def process_trash(self, split_command, cursor):
        """
        When the 'trash' command is read.
        """
        if len(split_command) == cursor:
            # i.e. we have no more arguments available
            print(f"What time limit do you want to impose?")
            print(f"The syntax to choose the time limit is:\n'>> trash <time limit>'\nTime limit has to be a positive int value.")
        else:
            time_limit = split_command[cursor]
            cursor += 1
            try:
                int_time_limit = int(time_limit)
                if int_time_limit <= 0:
                    print(f"You asked the tool to take {time_limit} as a time limit, but negative (zero included) values are not valid in that context. Please input a positive integer.")
                else:
                    log.trash_videos(int_time_limit, self.EXTENSIONS)
            except ValueError as e:
                print(f"Could not parse {time_limit} as a positive int. The correct syntax to choose the time limit is :\n'>> trash <time_limit>'")

    def process_date(self):
        """
        When the 'date' command is read.
        """
        log.sort_by_date()

    def process_help(self, split_command, cursor, EXTENSIONS, HELP):
        """
        When the 'help' command is read.
        """
        if len(split_command) == cursor:
            # i.e. no more arguments to read, just printing command list.
            print("".join(HELP["help"]))
        else:
            topic = split_command[cursor]
            cursor += 1
            if topic in self.exit_list:
                print(HELP["exit"])
            elif topic in self.change_list:
                print(HELP["change"])
            elif topic in self.folder_list:
                print(HELP["folder"])
                for directory in EXTENSIONS:
                    print(f"{directory}:".ljust(11, ' ') + str(EXTENSIONS[directory]))
                print(HELP["folder-creation"])
            elif topic in self.trash_list:
                print(HELP["trash"])
            elif topic in self.date_list:
                print(HELP["date"])
            elif topic in self.help_list:
                print(HELP["help-twice"])
            else:
                print(HELP["other"])



if __name__ == '__main__':
    os.system('cls')
    with open('src/data.json', 'r') as file:
        data = json.load(file)
    cli = CLI(data)

    print("\n".join(cli.HEADER))

    while True:
        try:
            print()
            print(cli.folder)
            command = input(">> ")
            cli.read_command(command)
        except (EOFError, KeyboardInterrupt):
            print("exit")  # In order to avoid ugly output
            cli.exit()
            break
