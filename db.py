import sqlite3 as db
from datetime import datetime

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
        cursor.execute("INSERT INTO games (player_name, date, turns_played) VALUES (:name, :date, :turns)", {'name': name.lower(), 'date': date, 'turns': turns_played})
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
    
        cursor.execute("SELECT COUNT(*) FROM games WHERE player_name == :name", {'name': player_name.lower()})
        stats['games_played'] = cursor.fetchone()[0]
        cursor.execute("SELECT date, turns_played FROM games WHERE player_name == :name ORDER BY date", {'name': player_name.lower()})
        # stats['turns_per_game'] = cursor.fetchall()
        results = []
        for row in cursor:
            results.append({
                'date': datetime.utcfromtimestamp(row[0]).strftime('%Y-%m-%d %H:%M:%S'),
                'turns_played': row[1]
                })
        stats['turns_per_game'] = results
        conn.commit()
        conn.close()
        return stats
