#!/usr/bin/python
#######################
'''
We are making a program that lets the user reset the database. If a user wishes to skip a step, they may change the activate variable from true to false at the appropriate location
'''
#######################

import sys
import csv

if (sys.version_info >=(3,0)):
    py3 = True
else:
    py3 = False
if py3:
	import pymysql as MySQLdbs
    #print("Python 3.0")
else:
	import MySQLdb  as MySQLdbs
    #print("Less than Python 3.0")



#######################
'''
We want to be able to edit it for the local system.
'''
fo = open("../data/DBInfo.txt","r")
dbVals = []
for index in range(5):
    line = fo.readline().strip( '\n' )
    #print(line)
    dbVals.append(line)

fo.close()

#######################

db = MySQLdbs.connect(host=dbVals[0], port=int(dbVals[1]), user =dbVals[2], passwd=dbVals[3], db=dbVals[4])

# Open database connection

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
stmts = ['email_table', 'mailing']

#This step lets us destroy the tables to be able to recreate them
activate = True
if (activate):
    for val in stmts:
        try:

            cursor.execute("SHOW TABLES LIKE '%s'" %(val))

            result = cursor.fetchone()
            if result:
                try:
                    cursor.execute("DROP TABLE IF EXISTS %s;"%(val))
                    db.commit()
                except:
                    db.rollback()
                    print("%s does not exist."%(val))
        except:
            print("%s detection attempt failed."%(val))
            db.rollback()

'''CREATE TABLE email_table (
  addr varchar(255) NOT NULL,
  domain varchar(100) DEFAULT NULL,
  date_added date DEFAULT NULL,
  domain_percent_increase float DEFAULT '0',
  PRIMARY KEY (addr),
  UNIQUE KEY addr_UNIQUE (addr)
  '''
# Create table as per requirement
sql1 = '''CREATE TABLE email_table (
  addr varchar(255) UNIQUE NOT NULL UNIQUE,
  domain varchar(100) DEFAULT NULL,
  date_added date DEFAULT NULL,
  domain_percent_increase float DEFAULT '0',
  PRIMARY KEY (addr)
);'''

sql2 = '''CREATE TABLE mailing (
  addr varchar(255) NOT NULL
);'''

#This step lets us create or recreate the tables
activate = True
if (activate):
    try:
        cursor.execute(sql1)
        db.commit()
        print("email_table created")

    except:
        db.rollback()
        print("email_table failure")


    try:
        cursor.execute(sql2)
        db.commit()
        print("mailing created")

    except:
        db.rollback()
        print("mailing failure")
    # disconnect from server


#This step lets us populate the table with some pre-existing data.


activate = True
if activate:
    f = open("../data/StartingValues.csv", "r")
    f.readline()
    print("Adding default values...")
    for row in csv.reader(f):
        toDelete = row[0], row[1], row[2], row[3]
        sqlQuery = """INSERT INTO email_table (addr, domain, date_added, domain_percent_increase)
        VALUES ('%s', '%s', '%s', %s);""" % (row[0], row[1], row[2], row[3])

        try:
            cursor.execute(sqlQuery)
            db.commit()
        except:
            db.rollback()
            print("Addition failure")

    print("Default values added.")
    f.close()


db.close()