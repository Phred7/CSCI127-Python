# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 3: Msuic CSV Library
# Your Name(, Your Partner's Name)
# Last Modified: ??, 2018 
# ---------------------------------------
# Provide a brief overview of the program.
# ---------------------------------------

# --------------------------------------

def menu():
    print()
    print("1. Identify longest song.")
    print("2. Identify number of songs in a given year.")
    print("3. Identify all songs by a given artist.")
    print("4. You choose something that is interesting and non-trivial.")
    print("5. Quit.")

# --------------------------------------

def main():
    choice = 0
    while (choice != 5):
        menu()
        choice = int(input("Enter your choice: "))
        if (choice == 1):
            longest_song()
        elif (choice == 2):
            year = int(input("Enter desired year: "))
            songs_by_year(year)
        elif (choice == 3):
            artist = input("Enter name of artist: ").lower()
            all_songs_by_artist(artist)
        elif (choice == 4):
            pass
        elif (choice != 5):
            print("That is not a valid option.  Please try again.")

# --------------------------------------

main()
