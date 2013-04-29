import sqlite3

#connect to database
DB_PATH = 'World.db3'
con = sqlite3.connect(DB_PATH)
con.row_factory = sqlite3.Row
cur = con.cursor()

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
	while True:
		question()