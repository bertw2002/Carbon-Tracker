from sqlite3 import connect, Row

#creates the tables users and topics
def create():
    print("HELLO")
    # Setup the database
    DB_FILE = "blogs.db"
    db = connect(DB_FILE)
    db.row_factory = Row
    c = db.cursor()
    q = "CREATE TABLE IF NOT EXISTS users(username TEXT, displayName TEXT,password TEXT)"
    b = "CREATE TABLE IF NOT EXISTS blogs(blogNumber INT, blogName TEXT, entry TEXT, creator TEXT)"
    c.execute(q)
    c.execute(b)
    db.commit()
    db.close()


#Adds a user to the users table given user's input
def addUser(username,displayName,password):
    DB_FILE = "blogs.db"
    db = connect(DB_FILE)
    c = db.cursor()
    c.execute("INSERT INTO users VALUES (?, ?, ?)", (str(username), str(displayName), str(password)))
    db.commit()
    db.close()

#checks if username is taken
def checkUsername(username):
    DB_FILE = "blogs.db"
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
    DB_FILE = "blogs.db"
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
