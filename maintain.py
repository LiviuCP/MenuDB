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

def right_menu_choice(menu_choice):
    if not menu_choice.isdigit():
        print_status("'" + menu_choice + "' is not a valid entry number!")
        return False
    menu_choice = int(menu_choice)
    if menu_choice < 1 or menu_choice > len(entries):
        print_status("'" + str(menu_choice) + "' is not a valid entry number!")
        return False
    return True
    
def delete_entry(entry_nr):
    if not right_menu_choice(entry_nr):
        return
    entry_nr = int(entry_nr)

    del entries[entry_nr-1]
    print_status( "Deleted entry #" + str(entry_nr))

def edit_entry(entry_nr):
    is_modified = False

    if not right_menu_choice(entry_nr):
        return False
    entry_nr = int(entry_nr)

    entry = entries[entry_nr-1]
    print("Enter the new data for each field. Press <enter> to leave unchanged.")

    print(entry[name_pos])
    new_name = input("Enter new name of the band or press return to leave unchanged (! to quit): ")
    if new_name == "":
        new_name = entry[name_pos]
    elif new_name == "!":
        return False
    else:
        is_modified = True

    print(entry[country_pos])    
    new_country = input("Enter new country or press return to leave unchanged (! to quit): ")
    if new_country == "":
        new_country = entry[country_pos]
    elif new_country == "!":
        return False
    elif not is_modified:
        is_modified = True

    print(entry[genre_pos])
    new_genre = input("Enter new genre or press return to leave unchanged (! to quit): ")
    if new_genre == "":
        new_genre = entry[genre_pos]
    elif new_genre == "!":
        return False
    elif not is_modified:
        is_modified = True

    entry = [new_name, new_country, new_genre]
    entries[entry_nr-1] = entry

    return is_modified

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
        print_status("Invalid option")
        return None

def print_status(status):
    print(status)
    print()

def main_loop():
    
    load_csv()
    
    while True:
        choice = menu_choice()
        if choice == None:
            continue
        if choice == 'q':
            print( "Exiting...")
            break
        elif choice == 'n':
            os.system("clear")
            create_entry()
            print_status("Entry created")
        elif choice == 'd':
            os.system("clear")
            entry_nr = input("Which entry do you want to delete? ")
            delete_entry(entry_nr)
        elif choice == 's':
            os.system("clear")
            show_entries()
        elif choice == 'e':
            os.system("clear")
            entry_nr = input("Which entry do you want to edit? (press ENTER to quit editing) ")
            os.system("clear")
            if str(entry_nr)=="":
                print_status("No entry modified. Returning to main menu...")
            else:
                print("You chose to edit entry: #" + entry_nr)
                os.system("clear")
                entry_modified = edit_entry(entry_nr)
                if entry_modified:
                    print_status("Entry #" + str(entry_nr) + " modified")
                else:
                    print_status("No entry modified")
        else:
            os.system("clear")
            print_status("Invalid choice.")
            
    save_database()
    

# The following makes this program start running at main_loop() 
# when executed as a stand-alone program.    
if __name__ == '__main__':
    main_loop()
