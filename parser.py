def parse(command: str):
    if command.count("'") != 2 and command.count('"') != 2: # If command (specifically argument 1) doesn't have two speech marks, return an error
        return ["add", "error"]
    
    # This loop separates strings by space, 
    # but if it encounters a speech mark, 
    # it will make further characters as one string, ignoring space
    in_speechmarks = False
    parsed_command = []
    last_string = ""
    for i in range(len(command)):
        if not in_speechmarks:
            if command[i] == " ":
                parsed_command.append(last_string)
                last_string = ""
            elif command[i] == "'" or command[i] == '"':
                in_speechmarks = True
            else:
                last_string += command[i]
        else:
            if command[i] == "'" or command[i] == '"':
                in_speechmarks = False
            else:
                last_string += command[i]
    
    if last_string:
        parsed_command.append(last_string) # Add last argument

    return parsed_command