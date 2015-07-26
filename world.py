import sqlite3

#connect to database
DB_PATH = 'res/World.db3'
def get_db_cursor():
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    return con.cursor()

def question():
	cur.execute('SELECT * FROM countries ORDER BY RANDOM() LIMIT 1;')
	country = cur.fetchone()		
	answer = input(country['name'] + ': ')	
	if (answer == country['capital']):
		print('Correct!')		
		#TODO Add stats
	else:
		print('Wrong! The correct answer was ' + country['capital'])
		#TODO Add stats
	
if (__name__ == '__main__'):
    cur = get_db_cursor()
    while True:
	    question()