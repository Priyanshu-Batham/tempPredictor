import sqlite3

# --------------------------------------------------------------->>>>>>>>>>>
def createTable():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    create_table_query = '''
    CREATE TABLE IF NOT EXISTS userInfo (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        mobileno TEXT,
        email TEXT
    );
    '''
    cursor.execute(create_table_query)
    conn.commit()
    conn.close()
# --------------------------------------------------------------->>>>>>>>>>>

def createAccount(username, password, mobile, email):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    insert_query = '''
    INSERT INTO userInfo (username, password, mobileno, email)
    VALUES (?, ?, ?, ?)
    '''
    try:
        cursor.execute(insert_query, (username, password, mobile, email))
        conn.commit()
    except sqlite3.Error as e:
        print("Error:",e)

    conn.close()
# --------------------------------------------------------------->>>>>>>>>>>

def showUserData():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    fetch_query = '''
    SELECT * FROM userInfo;
    '''
    try:
        cursor.execute(fetch_query)
        data = cursor.fetchall()
        print(data)
    except:
        print("Couldn't Fetch Results")
        
    conn.commit()
    conn.close()
# --------------------------------------------------------------->>>>>>>>>>>

def isUserPresent(username, password):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    login_query = '''
    SELECT * FROM userInfo 
    WHERE username = ? AND password = ?
    '''
    cursor.execute(login_query,(username, password))
    data = cursor.fetchall()

    conn.commit()
    conn.close()

    return True if data else False
# --------------------------------------------------------------->>>>>>>>>>>

def isCredentialsCorrect(username, mobile, email):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    credential_query = '''
    SELECT * FROM userInfo 
    WHERE username = ? AND mobileno = ? AND email = ?
    '''
    cursor.execute(credential_query,(username, mobile, email))
    data = cursor.fetchall()

    conn.commit()
    conn.close()

    return True if data else False
# --------------------------------------------------------------->>>>>>>>>>>

def changePassword(username, password):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    change_query = '''
    UPDATE userInfo 
    SET password = ? 
    WHERE username = ?
    '''
    try:
        cursor.execute(change_query,(password, username))
        print(cursor.rowcount)
        print("password changed successfully")
    except:
        print("Couldn't Change Password")
    conn.commit()
    conn.close()
# --------------------------------------------------------------->>>>>>>>>>>

def clearUserInfo():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM userInfo;")
    
    conn.commit()
    conn.close()

# -------------------------------------------------------------------------------------->>>>>>>>
# -----------------------------------DATASET--QUERIES----------------------------------->>>>>>>>
# -------------------------------------------------------------------------------------->>>>>>>>

def createDataset():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    create_table_query = '''
    CREATE TABLE IF NOT EXISTS dataset (
        id INTEGER PRIMARY KEY,
        temp INTEGER NOT NULL
    );
    '''
    cursor.execute(create_table_query)
    conn.commit()
    conn.close()
# --------------------------------------------------------------->>>>>>>>>>>

def getData():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    query = '''
    SELECT * FROM dataset;
    '''
    cursor.execute(query)
    data = cursor.fetchall()

    conn.close()
    return data
# --------------------------------------------------------------->>>>>>>>>>>


def addData(temp):
    if temp == '':
        print("Enter some Data")
        return "Enter some Data"
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    query = '''
    INSERT INTO dataset (temp)
    VALUES (?)
    '''
    if all(char.isdigit() for char in temp):
        try:
            cursor.execute(query,(temp,))
            conn.commit()
            conn.close()
            print("Temperature Recorded")
            return "Temperature Recorded"
        except KeyError as e:
            print(e)
    else:
        conn.commit()
        conn.close()
        print("Give Numeric Values")
        return "Give Numeric Values"
# --------------------------------------------------------------->>>>>>>>>>>

def deleteData(day):

    if(day == ""):
        return "Enter the Day Number"

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    query = '''
    DELETE FROM dataset 
    WHERE id = (?)
    '''
    if all(char.isdigit() for char in day):
        try:
            cursor.execute(query,(day,))
            conn.commit()
            conn.close()
        except:
            print("Error occured")
        else:
            return "Temperature Deleted"
    else:
        conn.commit()
        conn.close()
        print("Enter Numeric Values")
        return "Enter Numeric Values"

    
# --------------------------------------------------------------->>>>>>>>>>>

def updateData(day, temp):

    if(day == "" or temp == ""):
        return "Enter Data in both fields"

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    query = '''
    UPDATE dataset 
    SET temp = (?)
    WHERE id = (?)
    '''
    if all(char.isdigit() for char in day) and all(char.isdigit() for char in temp):
        try:
            cursor.execute(query,(temp, day))
        except:
            conn.commit()
            conn.close()
            print("Error occured")
            return "Error Occured"
        else:
            return "Temperature Updated"
    else: 
        print("Enter Numeric Values")
        return "Enter Numeric Values"

    
# --------------------------------------------------------------->>>>>>>>>>>

def clearDataset():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM dataset;")
    
    conn.commit()
    conn.close()
