# -maintain.py *- coding: utf-8 -*-
"""
This program maintains a menu driven database containing various rock bands
"""
import os
import csv


entries = []
name_pos = 0
country_pos = 1
genre_pos = 2
table_header = [ 'Name', 'Country', 'Genre' ]

def right_menu_choice(which):
    if not which.isdigit():
        print ("'" + which + "' is not a valid entry number!")
        print()
        return False
    which = int(which)
    if which < 1 or which > len(entries):
        print ("'" + str(which) + "' is not a valid entry number!")
        print()
        return False
    return True
    
def delete_entry(which):
    if not right_menu_choice(which):
        return
    which = int(which)

    del entries[which-1]
    print( "Deleted entry #", which)
    print()

def edit_entry(which):
    if not right_menu_choice(which):
        return
    which = int(which)
        
    entry = entries[which-1]
    print("Enter the data for a new entry. Press <enter> to leave unchanged.")
    
    print(entry[name_pos])
    new_name = input("Enter new name of the band or press return to leave unchanged: ")
    if new_name == "":
        newname = entry[name_pos]
        
    print(entry[country_pos])    
    new_country = input("Enter new country or press return to leave unchanged: ")
    if new_country == "":
        new_country = entry[country_pos]

    new_genre = input("Enter new genre or press return to leave unchanged: ")
    if new_genre == "":
        new_genre = entry[genre_pos]

    entry = [new_name, new_country, new_genre]
    entries[which-1] = entry

  
def save_database():

    f = open("database.csv", 'w', newline='')
    for item in entries:
        csv.writer(f).writerow(item)
    f.close()
  
def load_csv():
    if os.access("database.csv",os.F_OK):
        f = open("database.csv")
        for row in csv.reader(f):
            entries.append(row)
        f.close()

def show_entries():
    os.system("clear")
    show_entry(table_header, "")
    index = 1
    for entry in entries:
        show_entry(entry, index)
        index = index + 1
    print()

def show_entry(entry, index):
    outputstr = "{0:>3}  {1:<20}  {2:<20}  {3:<20}"
    print(outputstr.format(index, entry[name_pos], entry[country_pos], entry[genre_pos]))

def create_entry():
    print("Enter the data for a new entry:")
    new_name = input("Enter name: ")
    new_country = input("Enter country: ")
    new_genre = input("Enter genre: ")
    entry = [new_name,new_country,new_genre]
    entries.append(entry)
    
def menu_choice():
    """ List all possible options """
    print("Choose one of the following options?")
    print("s: show  "   , end='')
    print("n: new  "    , end='')
    print("d: delete  " , end='')
    print("e: edit  "   , end='')
    print("q: quit  ")
    chosen_option = input("Chosen option: ")    
    if chosen_option.lower() in ['n','d', 's','e', 'q']:
        return chosen_option.lower()
    else:
        os.system("clear")
        print(chosen_option +"?")
        print("Invalid option")
        print()
        return None


def main_loop():
    
    load_csv()
    
    while True:
        choice = menu_choice()
        if choice == None:
            continue
        if choice == 'q':
            print( "Exiting...")
            break     # jump out of while loop
        elif choice == 'n':
            create_entry()
            os.system("clear")
            print("Entry created")
            print()
        elif choice == 'd':
            which = input("Which item do you want to delete? ")
            print("which is ", which)
            os.system("clear")
            delete_entry(which)
        elif choice == 's':
            show_entries()
        elif choice == 'e':
            which = input("Which item do you want to edit? ")
            print("which is ", which)
            edit_entry(which)
            os.system("clear")
            print("Entry modified")
            print()
        else:
            os.system("clear")
            print("Invalid choice.")
            print()
            
    save_database()
    

# The following makes this program start running at main_loop() 
# when executed as a stand-alone program.    
if __name__ == '__main__':
    main_loop()
