import sqlite3

db_name=r'cgi-bin/coachdata.sqlite'

def get_names_from_store():
    connection=sqlite3.connect(db_name)
    cursor=connection.cursor()
    
    results=cursor.execute('select name from athletes')
    response=[i[0] for i in results.fetchall()]
    connection.close()
    return response
    
def get_namesID_from_store():
    connection=sqlite3.connect(db_name)
    cursor=connection.cursor()
    cursor.execute('select name,id from athletes')
    results=cursor.fetchall()
    #print(type(results),type(results[0]))
    connection.close()
    return results
def get_athlete_from_id(athlete_id):
    connection=sqlite3.connect(db_name)
    cursor=connection.cursor()
    results=cursor.execute('select name,dob from athletes where id=?',(athlete_id,))
    name,dob=results.fetchone()
    
    results=cursor.execute('select value from timing_data where athlete_id=?',(athlete_id,))
    timing=[i[0] for i in results.fetchall()]

    connection.close()
    return {'Name':name,'DOB':dob,'data':timing,'top3':timing[:3]}

#print(get_athlete_from_id(1))
#print(get_namesID_from_store())

import time

now=time.localtime()
connection=sqlite3.connect(db_name)
cursor=connection.cursor()
#cursor.execute('CREATE TABLE test2 (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, time DATE)')
#connection.commit()

cursor.execute('insert into test (time) values(?)',(time.asctime(now),))
connection.commit()
connection.close()
    