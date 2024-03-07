## Requirements:
##### ~ A GUI that interacts with at least 3 classes (Item, Book, and comic)
##### ~ Must use collections (lists, tuples, arrays, and or dictionaries)
##### ~ Must have no runtime or syntax errors and produce correct results
##### ~ Needs documentation including the proposal, class diagram, and
#####   report of results with sample output

## Plan to Fulfill Requirements:
##### ~ The GUI will have several functions in order to fulfill the requirements:
########## - Add books or comics to the "inventory"
########## - Search for items within inventory with the ability to
##########   filter out comics or books in the search
########## - Remove items from the inventory
##### ~ Will use lists within the items' attributes if it is possible to have multiple of said attribute
########## - This may require additional functionality for displaying these items to avoid errors
##### ~ dictionaries can be used to store items in the "inventory"
##### ~ We have the proposal and class diagram and thus just need reports of results (use unit testing to get these)



###----------|Main Program|----------###
from datetime import datetime
import json
import jsonpickle
import tkinter as tk
from models import book, comic
from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk

def save():
    json_string = jsonpickle.encode(inventory)
    file = open("inventory.txt", "w")
    file.write(json_string)
    file.close()

def createItem(): 
    date_format = '%Y-%m-%d'
    itemType = input("Enter the type of item you wish to enter:")
    if itemType == "Book":
        title = input("Enter the title of the book:")
        genre = input("Enter the genre of the book:")
        year = input("Enter the year of the book's release:")
        month = input("Enter the month of the book's release:")
        day = input("Enter the day of the book's release:")
        releaseDate = (datetime(int(year), int(month), int(day))).strftime("%x")
        author = input("Enter the author of the book:")
        publisher = input("Enter the publisher of the book:")
        id = 0
        for x in inventory:
            id += 1
            print("ID: ", id)
        inventory[id] = book(title, genre, releaseDate, author, publisher)
        print("You created a book")
        print(id)
        save()
    elif itemType == "Comic":
        title = input("Enter the title of the comic:")
        genre = input("Enter the genre of the comic:")
        year = input("Enter the year of the comic's release:")
        month = input("Enter the month of the comic's release:")
        day = input("Enter the day of the comic's release:")
        releaseDate = (datetime(int(year), int(month), int(day))).strftime("%x")
        author = input("Enter the author of the comic:")
        publisher = input("Enter the publisher of the comic:")
        artist = input("Enter the artist of the comic:")
        id = 0
        for x in inventory:
            id += 1
            print("ID: ", id)
        inventory[id] = comic(title, genre, releaseDate, author, publisher, artist)
        print("You created a comic")
        print(id)
        save()
    elif itemType == "quit":
        print("Stopping process...")
    else:
        print("Error: item type not recognized. Please enter either 'Book' or 'Comic'.")
        createItem()
    
def load():
    #Inventory is a dictionary containing the item(in the form of a dict) and it's ID number given
    #to it when it entered the system
    #The inventory uses JSON formated text to store the items, the code below 'loads' the inventory from the file of the same name
    inventoryFile = open("inventory.txt", "a") #creates inventory.txt if it is not already there
    inventoryFile.close()
    inventoryFile = open("inventory.txt") #reopens the file to read it
    inventoryRaw = inventoryFile.read() #inventoryRaw stores the raw string that the txt file holds
    inventoryFile.close()
    if not (len(inventoryRaw) == 0): #checks if the file is empty, like if it was just created
        print("Inventory loading...") #Status message for console while testing
        inventory = json.loads(inventoryRaw) # loads the raw inventory. At this moment the inventory is a dictionary of dictionaries, we need it to be a dictionary of items(as per our item class)
        tempInventory = {} # the loop will use this dictionary to store the actual item objects while the function iterates through the list
        for x in inventory: #This loop converts the dictionaries within Inventory into objects and places them in tempInventory
            #First we check what type of item we are looking at
            if inventory[x]['py/object'] == "__main__.book": 
                print("It's a book!") 
                tempTitle, tempGenre, tempReleaseDate, tempAuthor, tempPublisher = "", "", "", "", "" #Initialize attributes of a book
                #this loop pulls all of the values of the item out of the raw inventory and stores them in temporary variables
                for y in inventory[x]: #This loop assigns all of the values of the dictionary we are looking at to the temp attributes above
                    if inventory[x] == "py/object":
                        continue
                    elif inventory[x] == "title":
                        tempTitle = inventory[x][y]
                        continue
                    elif inventory[x] == "genre":
                        tempGenre = inventory[x][y]
                        continue
                    elif inventory[x] == "releaseDate":
                        tempReleaseDate = inventory[x][y]
                        continue
                    elif inventory[x] == "author":
                        tempAuthor = inventory[x][y]
                        continue
                    elif inventory[x] == "publisher":
                        tempPublisher = inventory[x][y]
                tempBook = book(tempTitle, tempGenre, tempReleaseDate, tempAuthor, tempPublisher)
                tempInventory[int(x)] = tempBook #assign the item to its respective spot in tempInventory
            elif inventory[x]['py/object'] == "__main__.comic":
                print("It's a comic!")
                tempTitle, tempGenre, tempReleaseDate, tempAuthor, tempPublisher, tempArtist = "", "", "", "", "", "" #Initialize attributes of a book
                #this loop pulls all of the values of the item out of the raw inventory and stores them in temporary variables
                for y in inventory[x]: #This loop assigns all of the values of the dictionary we are looking at to the temp attributes above
                    if inventory[x] == "py/object":
                        continue
                    elif inventory[x] == "title":
                        tempTitle = inventory[x][y]
                        continue
                    elif inventory[x] == "genre":
                        tempGenre = inventory[x][y]
                        continue
                    elif inventory[x] == "releaseDate":
                        tempReleaseDate = inventory[x][y]
                        continue
                    elif inventory[x] == "author":
                        tempAuthor = inventory[x][y]
                        continue
                    elif inventory[x] == "publisher":
                        tempPublisher = inventory[x][y]
                    elif inventory[x] == "artist":
                        tempArtist = inventory[x][y]
                tempComic = comic(tempTitle, tempGenre, tempReleaseDate, tempAuthor, tempPublisher, tempArtist)
                tempInventory[int(x)] = tempComic #assign the item to its respective spot in tempInventory
            #assign each value to a tempvariable for use in item init
        for x in tempInventory:
            inventory[x] = tempInventory[x]
        print("Inventory Loaded.")
        return inventory
    else:
        print("No inventory detected")
        print("Initializing inventory")
        inventory = {} #initializes the inventory
        print("Fresh Inventory initialized")
        return inventory
#id1 = book("The Hobbit", "High Fantasy", (datetime.datetime(1937, 9, 21)).strftime("%x"), "J. R. R. Tolkien", "George Allen & Unwin")

#inventory[1] = jsonpickle.encode(id1)
#inventoryFile = open("inventory.txt", "w")
#inventoryFile.write(json.dumps(inventory))
#inventoryFile.close()


### Run this as test ###
def main():
    inventory = {}
    inventory = load()
    print(inventory)
    createItem()
    choice = input("Would you like to save? (y/n) ")
    if choice == "y":
        save()
    else:
        print("No changes made")
    print(inventory)

if __name__ == '__main__':
    #main()

    #Main GUI variable
    gui = tk.Tk()
    gui.title("Library Manager")

    #Other GUI variables
    TXT_HEIGHT = 1
    TXT_WIDTH = 37
    VET_PAD = 10
    BORDER = 5
    BUTTON_SPACE = 5
    SORTING = ""
    TYPE_LIST = ["Book", "Comic"]
    
    #Item type variable
    itemType = ""

    #Book related variables
    title       = []
    genre       = []
    year        = []
    month       = []
    day         = []
    releaseDate = []
    author      = []
    publisher   = []
    id          = []
    artist      = []

    #GUI objects
    topPane                = tk.PanedWindow(gui)
    itemTypeLabel          = tk.Label(gui, text="Item Type: ")
    itemTypeTextBox        = tk.Text(gui, height=TXT_HEIGHT, width=TXT_WIDTH, bd=BORDER)
    itemTitleLabel         = tk.Label(gui, text="Title: ")
    itemTitleTextBox       = tk.Text(gui, height=TXT_HEIGHT, width=TXT_WIDTH, bd=BORDER)
    itemGenreLabel         = tk.Label(gui, text="Genre: ")
    itemGenreTextBox       = tk.Text(gui, height=TXT_HEIGHT, width=TXT_WIDTH, bd=BORDER)
    itemYearLabel          = tk.Label(gui, text="Year: ")
    itemYearTextBox        = tk.Text(gui, height=TXT_HEIGHT, width=TXT_WIDTH, bd=BORDER)
    itemMonthLabel         = tk.Label(gui, text="Month: ")
    itemMonthTextBox       = tk.Text(gui, height=TXT_HEIGHT, width=TXT_WIDTH, bd=BORDER)
    itemDayLabel           = tk.Text(gui, text="Day: ")
    itemDayTextBox         = tk.Entry(gui, height=TXT_HEIGHT, width=TXT_WIDTH, bd=BORDER)
    itemReleaseDateLabel   = tk.Label(gui, text="Release Date: ")
    itemReleaseDateTextBox = tk.Text(gui, height=TXT_HEIGHT, width=TXT_WIDTH, bd=BORDER)
    itemAuthorLabel        = tk.Label(gui, text="Author: ")
    itemAuthorTextBox      = tk.Text(gui, height=TXT_HEIGHT, width=TXT_WIDTH, bd=BORDER)
    itemPublisherLabel     = tk.Label(gui, text="Publisher: ")
    itemPublisherTextBox   = tk.Text(gui, height=TXT_HEIGHT, width=TXT_WIDTH, bd=BORDER)
    itemIdLabel            = tk.Label(gui, text="ID: ")
    itemIdTextBox          = tk.Text(gui, height=TXT_HEIGHT, width=TXT_WIDTH, bd=BORDER)
    itemArtistLabel        = tk.Label(gui, text="ID: ")
    itemArtistTextBox      = tk.Text(gui, height=TXT_HEIGHT, width=TXT_WIDTH, bd=BORDER)

    #Add objects to appropriate pane
    topPane.add(itemTypeLabel)
    topPane.add(itemTypeTextBox)
    topPane.add(itemTitleLabel)
    topPane.add(itemTitleTextBox)
    topPane.add(itemGenreLabel)
    topPane.add(itemGenreTextBox)
    topPane.add(itemYearLabel)
    topPane.add(itemYearTextBox)
    topPane.add(itemMonthLabel)
    topPane.add(itemMonthTextBox)
    topPane.add(itemDayLabel)
    topPane.add(itemDayTextBox)
    topPane.add(itemReleaseDateLabel)
    topPane.add(itemReleaseDateTextBox)
    topPane.add(itemAuthorLabel)
    topPane.add(itemAuthorTextBox)
    topPane.add(itemPublisherLabel)
    topPane.add(itemPublisherTextBox)
    topPane.add(itemIdLabel)
    topPane.add(itemIdTextBox)
    topPane.add(itemArtistLabel)
    topPane.add(itemArtistTextBox)
    
    #Position objects using .grid method
    itemTypeLabel.grid(column = 0, row = 0, pady = VERT_PAD)
    itemTitleLabel.grid(column = 0, row = 1, pady = VERT_PAD)
    itemGenreLabel.grid(column = 0, row = 2, pady = VERT_PAD)
    itemYearLabel.grid(column = 0, row = 3, pady = VERT_PAD)
    itemMonthLabel.grid(column = 0, row = 4, pady = VERT_PAD)
    itemDayLabel.grid(column = 0, row = 5, pady = VERT_PAD)
    itemReleaseDateLabel.grid(column = 0, row = 6, pady = VERT_PAD)
    itemAuthorLabel.grid(column = 0, row = 7, pady = VERT_PAD)
    itemPublisherLabel.grid(column = 0, row = 8, pady = VERT_PAD)
    itemIdLabel.grid(column = 0, row = 9, pady = VERT_PAD)
    itemArtistLabel.grid(column = 0, row = 10, pady = VERT_PAD)
    itemTypeTextBox.grid(column = 1, row = 1, pady  = VERT_PAD)
    itemTitleTextBox.grid(column = 1, row = 2, pady = VERT_PAD)
    itemGenreTextBox.grid(column = 1, row = 3, pady = VERT_PAD)
    itemYearTextBox.grid(column = 1, row = 4, pady = VERT_PAD)
    itemMonthTextBox.grid(column = 1, row = 5, pady = VERT_PAD)
    itemDayTextBox.grid(column = 1, row = 6, pady = VERT_PAD)
    itemReleaseDateTextBox.grid(column = 1, row = 7, pady = VERT_PAD)
    itemAuthorTestBox.grid(column = 1, row = 8, pady = VERT_
