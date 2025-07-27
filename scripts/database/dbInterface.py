import sqlite3
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "db.db")  # adjust if needed

def addProfile(username, password, country):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect("database/db.db")
        print(f"Connected to database: db.db")
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")

    cursor = conn.cursor()
    print("inserting name: ")
    print(username)
    cursor.execute("INSERT INTO Profiles (username, password, country) VALUES (?, ?, ?)", (username, password, country))
    conn.commit()
    print("Profile added successfully.")

    cursor.close()
    conn.close()



def get_email_fb():
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        print(f"Connected to database: db.db")
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    
    cursor = conn.cursor()
    cursor.execute("SELECT * from Profiles where fb_used = 0 Limit 1")
    row = cursor.fetchone()



    if row:
        id = row[0]
        return (row[0], row[1], row[2])

    else:
        print("No matching row found.")

    conn.close()



