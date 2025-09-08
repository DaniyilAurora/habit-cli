import sqlite3

# time: 8:00, 8, 16, 24:00, 24:30
# Function which validates time
# Returns in format [hours, minutes], or if not valid returns False
def validate_time(time: str) -> list[int] | bool:
    try:
        if len(time) == 1 or len(time) == 2: # Format is one or two digits (7, 23)
            if not time.isnumeric(): return False # Time is not a number
            if int(time) < 0 or int(time) > 23: return False # Time is not 0 <= time <= 23

            return [int(time)]
        elif len(time) >= 3 and len(time) <= 5: # Format is three or four digits (5:00, 23:30)
            if ":" not in time: return False # Incorrect formatting

            time_splitted = time.split(":")
            if int(time_splitted[0]) < 0 or int(time_splitted[0]) > 23: return False # Hour time is not 0 <= hours <= 23
            if int(time_splitted[1]) < 0 or int(time_splitted[1]) > 59: return False # Minutes time is not 0 <= minutes <= 60

            return [int(time_splitted[0]), int(time_splitted[1])]
        
        return False
    except ValueError: # If there is a non-numerical character
        return False


class Database():
    def __init__(self):
        self.connection = sqlite3.connect("habits.db")
        self.cursor = self.connection.cursor()

        # Creating a table
        #self.cursor.execute("CREATE TABLE habits(id integer primary key, habit varchar(255), time varchar(255), regularity varchar(255))")
        #self.connection.commit()

    def add_habit(self, habit: str, time: str, regularity: str):
        pass
