import sqlite3 as sql

connection = sql.connect('database3.db')
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Games (entry_id INTEGER primary key autoincrement, Name TEXT, Type Text, Cost INTEGER, Mine TEXT)")

choice = None
while choice != "5":
    print("1) Looking for a Game?")
    print("2) Would you Like to add a Game?")
    print("3) Update excitng")
    print("4) Delete")
    print("5) Delete Most Resent Game")
    choice = input("> ")
    print()

    if choice == "1":
        print('How do we want to search today do you want to see all of the games, by a certin name, by cost, ones I own. (all, name, cost, own')
        search = input("")
        if search == 'all':
            cursor.execute("select * from Games")
            print("{:>8}  {:>20}  {:>8}  {:>8}   {:>13}".format("Entry", "Name", "Type", "Cost",   "Do I Have?"))
            for record in cursor.fetchall():
               print("{:>8}  {:>20}   {:>8}  {:>8}  {:>8}".format(record[0],  record[1], record[2],   record[3],   record[4]))
               print(" ")
        elif search == 'name':
            name = input('What game are you thinking of: ')
            name = (name, )
            cursor.execute("select Name, Cost, Mine, count(*) from Games where Name like ? ", name)
            print("{:>8} {:>8} {:>8} {:>8}".format("Name", "Cost", "Do I Have", "Recomeded"))
            for record in cursor.fetchall():
                print("{:>8}  {:>8}   {:>8} {:>8} ".format(record[0],  record[1], record[2], record[3]))
        elif search == "own":
            cursor.execute("Select Name, Type, Mine from Games where Mine like 'Yes' group by Name")
            print("{:>8} {:>8} {:>8}".format("Name", "Type", "I own it"))
            for record in cursor.fetchall():
                print("{:>8} {:>8} {:>8}".format(record[0], record[1], record[2]))
        elif search == "cost":
            cost = input("How much are do we have to spend on a Game: $")
            cost = (cost,)
            cursor.execute("select Name, Type, Mine, Cost from Games where Cost > ? group by Name", cost)
            print("{:>8} {:>8} {:>8} {:>8}".format("Name", "Type", "Already Owned", "Cost"))
            for record in cursor.fetchall():
                print("{:>8} {:>8} {:>8}".format(record[0], record[1], record[2], record[3]))

    elif choice == "2":
        # This is going to add a game to the folder
        cursor.execute("select count(*) from Games")
        "{:>8}".format("Entry")
        for record in cursor.fetchall():
            entry = ("{:>8}".format(record[0]))
        entry = int(entry) + 1
        Name = input("Name: ")
        Type = input("Type (Board or Card): ")
        Cost = input("Cost: $")
        Mine = input("Does Tyson own it?(Yes or No):  ")
        values = (entry, Name, Type, Cost, Mine)


        cursor.execute("INSERT INTO Games values(?, ?, ?, ?, ?)", values)
        connection.commit()

# Going to edit the game
    elif choice == "3":
        id = input("What is the Id of the Game that we got? ")
        id = (id,)
        cursor.execute("Update Games Set Mine = 'Yes' Where entry_id = ?", id)
        connection.commit()

# Here we are going to delete the game by it Entry ID
    elif choice == "4":
        entry = input('entry: ')
        values = [entry, ]
        cursor.execute("Delete from Games where entry_id = ?", values)
        connection.commit()
