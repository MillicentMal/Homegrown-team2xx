import sqlite3
conn = sqlite3.connect("data.db", check_same_thread=False)
c = conn.cursor()

#Table  

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS prescriptions(dates DATE, patient_ID TEXT, prescription TEXT, diagnosis TEXT, recommendation TEXT)')

def add_data(dates,patient_ID,prescription,diagnosis,recommendation):
    c.execute('INSERT INTO prescriptions(dates,patient_ID,prescription,diagnosis,recommendation) VALUES(?,?,?,?,?)',(dates,patient_ID,prescription,diagnosis,recommendation))
    conn.commit()

def view():
    c.execute('SELECT * FROM prescriptions')
    data = c.fetchall()
    return data
