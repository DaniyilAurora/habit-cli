import sqlite3

class Database():
    def __init__(self):
        self.connection = sqlite3.connect("habits.db")
        self.cursor = self.connection.cursor()