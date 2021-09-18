from sqlite3 import connect, Row

#creates the tables users and topics
def createDB():
    # Setup the database
    DB_FILE = "app.db"
    db = connect(DB_FILE)
    db.row_factory = Row
    c = db.cursor()
    q = "CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT, destination TEXT, modeOfTransport TEXT)"
    c.execute(q)
    db.commit()
    db.close()


#Adds a user to the users table given user's input
def addUser(username,password):
    DB_FILE = "app.db"
    db = connect(DB_FILE)
    c = db.cursor()
    c.execute("INSERT INTO users VALUES (?,?,?,?)", (str(username), str(password), str(""), str("")))
    db.commit()
    db.close()

#checks if username is taken
def checkUsername(username):
    DB_FILE = "app.db"
    db = connect(DB_FILE)
    c = db.cursor()
    cur = c.execute("SELECT username FROM users")
    usernames = cur.fetchall()
    db.commit()
    db.close()
    for row in usernames:
        if username in row:
            return True
    return False

#checks if the login creditionals are valid
def checkUser(username, password):
    DB_FILE = "app.db"
    db = connect(DB_FILE)
    c = db.cursor()

    if checkUsername(username):
        cur = c.execute("SELECT password FROM users WHERE username = ?", (str(username),))
        userPassword = cur.fetchall()
        db.commit()
        db.close()
        for row in userPassword:
            if password in row:
                return True
            else:
                return False
    else:
         return False


#write user data to database
def userDataToDB(user, locations, modes):
    str_locations = ""
    str_modes = ""

    for location in locations:
        str_locations += location + ","
    str_locations = str_locations[:-1]

    for mode in modes:
        str_modes += mode + ","
    str_modes = str_modes[:-1]

    DB_FILE = "app.db"
    db = connect(DB_FILE)
    c = db.cursor()

    c.execute("UPDATE users SET destination=?, modeOfTransport=? WHERE username=?", (str(str_locations),str(str_modes),str(user)))

    db.commit()
    db.close()


#print database
def printDB():
    DB_FILE = "app.db"
    db = connect(DB_FILE)
    c = db.cursor()
    cur = c.execute("SELECT * FROM users")
    rows = cur.fetchall()
    db.commit()
    db.close()
    for row in rows:
        print(row)
