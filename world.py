import sqlite3
from colorama import Fore

#connect to database
DB_PATH = 'res/World.db3'
def get_db_cursor():
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    return con.cursor()

def get_random_country():
	cur.execute('SELECT * FROM countries ORDER BY RANDOM() LIMIT 1;')
	return cur.fetchone()

def question():
	country = get_random_country()
	answer = raw_input('What is the capital of ' + country['name'] + '? ')
	if (answer.lower() == country['capital'].lower()):
		print(Fore.GREEN + 'Correct!' + Fore.RESET)
		#TODO Add stats
	else:
		print(Fore.RED + 'Wrong!' + Fore.RESET + ' The correct answer was ' + country['capital'])
		#TODO Add stats
	
if (__name__ == '__main__'):
    cur = get_db_cursor()
    while True:
	    question()