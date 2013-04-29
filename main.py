#Main

import capquiz.ui as ui 
from capquiz.world import Country
import sqlite3

#connect to databasae
DB_PATH = "res/World.db3"
con = sqlite3.connect(DB_PATH)
cur = con.cursor()

while True:
	ui.displayMenu()
	usrChoice = input()
	if (usrChoice == '0'):
		break
	if (usrChoice == '1'): #Display List
		cur.execute('SELECT name, capital FROM Countries')
		countries = cur.fetchall()
		ui.displayList(countries)
	elif (usrChoice == '2'): #Add item
		country = Country()
		ui.inputCountry(country)
		cur.execute('INSERT INTO Countries(name, capital) VALUES (?, ?)', (country.name, country.capital))
	else:
		ui.menuOptionError()
	ui.pause()
	
#User chose quit from menu
if (con.in_transaction == True):
	con.commit()
	print("Changes committed")
else:
	print("No changes to commit")

cur.close()
con.close()

#SELECT name, capital FROM Countries ORDER BY RANDOM() LIMIT 1;