import sqlite3 as db


class DB():
    def __init__(self, filename):
        self._filename = filename
        conn = db.connect(self._filename)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS games (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                player_name TEXT, 
                date INTEGER, 
                turns_played INTEGER
            )'''
        )
        conn.commit()

        conn.close()

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, value):
        self._filename = value

    def saveGame(self, name, date, turns_played):
        conn = db.connect(self._filename)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO games (player_name, date, turns_played) VALUES (:name, :date, :turns)", {'name': name, 'date': date, 'turns': turns_played})
        conn.commit()
        conn.close()
    
    def getGame(self, game_id):
        conn = db.connect(self._filename)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM games WHERE games.id == :id", {'id': game_id})
        game = cursor.fetchone()[0]
        conn.commit()
        conn.close()
        return game

    def getStatisticsByName(self, player_name):
        stats = {}

        conn = db.connect(self._filename)
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM games WHERE player_name == :name", {'name': player_name})
        stats['games_played'] = cursor.fetchone()[0]
        cursor.execute("SELECT * FROM games WHERE player_name == :name", {'name': player_name})
        stats['turns_per_game'] = cursor.fetchall()
        
        conn.commit()
        conn.close()
        return stats

    