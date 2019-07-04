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

def get_random_countries(n):
    cur.execute('SELECT * FROM countries ORDER BY RANDOM() LIMIT ' + n + ';')
    return cur.fetchall()
def get_all_countries():
    cur.execute('SELECT * FROM countries')
    return cur.fetchall()

def question():
    country = get_random_country()
    print('{0}/{1}'.format(correct_counter, question_counter))
    answer = raw_input('What is the capital of ' + country['name'] + '? ')
    if (answer.lower() == country['capital'].lower()):
        
        print(Fore.GREEN + 'Correct!' + Fore.RESET)
        return True
    else:
        print(Fore.RED + 'Wrong!' + Fore.RESET + ' The correct answer was ' + Fore.GREEN + country['capital'] + Fore.RESET)
        return False
	
if (__name__ == '__main__'):
    cur = get_db_cursor()
    question_counter = 0
    correct_counter = 0
    while True:
        if question():
            correct_counter += 1
        question_counter += 1