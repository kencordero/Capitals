#User Interface

from os import system

def clearScreen():
	system("cls")

def displayList(countries):
	clearScreen()
	print("\nList of countries")
	for country in countries:
		print("{0}, {1}".format(country[0], country[1]))
		
def displayMenu():
	clearScreen()
	print("Main menu")
	print("1) Display List")
	print("2) Add Item")
	print("0) Quit")
	
def inputCountry(country):
	country.name = input("Enter the name of the country: ")
	country.capital = input("Enter the capital of the country: ")
	
def menuOptionError():
	print("Select a valid option from the menu!")
	
def pause():
	system("pause")