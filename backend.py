import sqlite3


"""===========================================================
                        BACKEND PROGRAM
============================================================="""




"""===========================================================
         CONNECT - CREATE NEW (If not exists) FUNCTION
============================================================="""

def connect():
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        cur.execute("""
                CREATE TABLE IF NOT EXISTS account(
                id INTEGER PRIMARY KEY,
                title TEXT,
                username TEXT,
                password TEXT,
                url TEXT,
                comment TEXT);
        """)
        cur.execute("""
                CREATE TABLE IF NOT EXISTS user(
                username TEXT,
                password TEXT);
        """)
        conn.commit()
        conn.close()
        
"""===========================================================
                         INSERT FUNCTION
============================================================="""

def insert(title, username, password, url, comment):
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        cur.execute("""
                INSERT INTO account VALUES(
                NULL,?,?,?,?,?)""" ,
        (title, username, password, url, comment))
        conn.commit()
        conn.close()

def insert_user():
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        cur.execute("""
                INSERT INTO user VALUE(
                NULL, ?, ?)""",
        (username, password))
        conn.commit()
        conn.close()

"""===========================================================
                         VIEW FUNCTION
============================================================="""

def view():
        try:
                conn = sqlite3.connect("database.db")
                cur = conn.cursor()
                cur.execute("""
                        SELECT * FROM account
                """)
                ppl = cur.fetchall()
                conn.commit()
                conn    .close()
                return ppl
        except:
                OperationalError


"""===========================================================
                        DELETE FUNCTION
============================================================="""

def delete(id):
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        cur.execute("""
                DELETE FROM account WHERE id=?""",
                (id,))
        conn.commit()
        conn.close()


"""===========================================================
                          DROP FUNCTION
============================================================="""

def drop_TableAccount():
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        cur.execute("""
                DROP TABLE IF EXISTS account
        """)
        conn.commit()
        conn.close()

def drop_TableUser():
        conn = sqlite3.connect("database.db")
        cur =  conn.cursor()
        cur.execute("""
                DROP TABLE IF EXISTS user
        """)


#print(view())



connect()
