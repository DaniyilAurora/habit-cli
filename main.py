import messages
from database import Database
from parser import parse

# Initialise database
db = Database()

command = input(messages.type_command)

while command != "-1" and command != "exit":
    parsed_command = parse(command)

    if parsed_command[0] == "add":
        # Validation checks
        if len(parsed_command) != 4:
            print(messages.incorrect_usage)
        else:
            print(parsed_command)

    elif parsed_command[0] == "help":
        print(messages.help)
    else:
        print(messages.unknown)

    command = input(messages.type_command)

print(messages.exit)