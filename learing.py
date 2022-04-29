import sqlite3 as sql

connection = sql.connect('database3.db')
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Games (entry_id INTERGER primary key not null, Name TEXT, Type Text, Cost INTERGER, Mine TEXT)")

choice = None
while choice != "5":
    print("1) Looking for a Game?")
    print("2) Would you Like to add a Game?")
    print("3) Edit")
    print("4) Delete Employee")
    print("5) Delete Most Resent Game")
    choice = input("> ")
    print()

    if choice == "1":
        cursor.execute("select * from Games")
        print("{:>8}  {:>20}  {:>8}  {:>8}   {:>13}".format("Entry", "Name", "Type", "Cost",   "Do I Have?"))
        for record in cursor.fetchall():
           print("{:>8}  {:>20}   {:>8}  {:>8}  {:>8}".format(record[0],  record[1], record[2],   record[3],   record[4]))
           print(" ")
          




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

    elif choice == "3":
        entry = input('entry: ')
        values = [entry, ]
        cursor.execute("Delete from Games where entry_id = ?", values)
