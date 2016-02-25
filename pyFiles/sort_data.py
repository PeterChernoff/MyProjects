import sys
if sys.version_info >(3,):
    import pymysql as MySQLdb
else:
    import MySQLdb

import msvcrt, time
#import the MySQL, time
import random # only for making examples

from datetime import date, timedelta, datetime # used to help make dates to enter

##########################################################################################
#This is an overview of the project
##########################################################################################
'''
The purpose of this project is to be able to read from a MySQL database table certain values and process them into another MySQL database table, then calculate the percent increase of the domain named used and order them by the greatest increase.
'''
##########################################################################################
##########################################################################################
#This section has code to help create examples, but is otherwise not necessary
##########################################################################################

#A sample time to make random values to enter so we don't only have date entries between a certain amount.
time_begin = date(2014, 1, 24)

# http://stackoverflow.com/questions/553303/generate-a-random-date-between-two-other-dates
# This code was a lot of help for making the test table
def random_date(start, end):
    #TO DELETE This only exists so we can create test updates. This is usually commented out.
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())))
##########################################################################################


#######################
def runExchange(db, time_format, time_adjusted, testValue=(datetime.now() + timedelta(seconds=15)).strftime('%X')):
    spacing = "\n=========================\n\n"

    while True:
        print("Next automatic SQL Call at %s. \nHit 's' to start now. \nHit 't' to check how much time before the next automatic call. \nHit 'x' to exit." % time_adjusted)
        while True:
            #This internal while loop lets us wait until a certain keypress is made, or a certain amount of time passes.

            '''
            print "For demonstration purposes, the next SQL Call happen at %s." % time_adjusted
            print "The companion file insert_value.py will be updating the mailing database while this program is running."
            '''

            debugMe = False #This is only meant for debigging purposes, and showing my thought processes
            #This lets us wait until a certain key press is made, or until scheduled (default midnight), though any time can be entered. If debug mode is on, then it also activates an amount (default 15 seconds after it's first activated starts)
            if msvcrt.kbhit():
                checkMe = chr(ord(msvcrt.getch()))
                if (checkMe == 's'.lower()):
                    #Manually starts the process
                    print("%sManual activation commencing."%spacing)
                    break
                elif (checkMe == 'x'.lower()):
                    #Exits the program
                    print("%sExiting..."%spacing)
                    return
                elif (checkMe == 't'.lower()):
                    #Gives the time until the next scheduled update
                    tdelta = (datetime.strptime(time_adjusted, time_format) - datetime.strptime(datetime.now().strftime('%X'), time_format)).total_seconds() #converts to seconds
                    if tdelta < 0:
                        tdelta += 86400 #checks if the seconds is less than 0, if so, add 1 day
                    printTime = time.strftime("%H:%M:%S", time.gmtime(tdelta))
                    print("Time until next scheduled activation is: %s."%printTime)
            elif datetime.now().strftime('%X') == time_adjusted:
                #Activates at the scheduled time
                print("%sScheduled activation commencing."%spacing)
                break
            ##### To Delete	(but only comment out)
            elif datetime.now().strftime('%X') == testValue and debugMe:
                #Activates a specified time after commencing, but only meant for deubug purposes.
                print("%sTest activation commencing."%spacing)
                break
            ##### /To Delete	(but only comment out)


        cursor = db.cursor()
        # We are getting the emails and domains from the mailing database
        sql1 = "SELECT * FROM MAILING"
        print("Retrieving queries from the 'mailing' database.")
        try:
            #Execute the SQL command
            cursor.execute(sql1)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()

            # We want to get the email address and the domain
            for row in results:
                email = row[0]
                #everything after the @ symbol is our domain
                domain = email.split("@")[-1]

                # If the domain hasn't shown up yet, add it


        except:
            print("Error: unable to fetch data sql1."	)

        # we are taking these results and placing them in the new table
        print("Sorting and inserting queries into 'email_table' database.")
        try:
            for row in results:
                #select the email to place in query
                email = row[0]

                #select the domain by chopping off everything before the '@'
                domain = email.split("@")[-1]
                #time end was used in a randomized, representing the upper limit of what could be inserted
                time_end = date.today()

                #time_used is this way in case I ever want to randomize a table, say if I cleared it
                time_used = time_end

            ##### To Delete	(but only comment out)
                #Just something to create some random date to sort
                #time_used  = random_date(time_begin, time_end)
            ##### /To Delete (but only comment out)

                # insert address, domain, and date added into email_table database, ignoring any email duplicates
                sql2a = """INSERT IGNORE INTO email_table (addr, domain, date_added)
                    VALUES ('%s', '%s', '%s')
                    ON DUPLICATE KEY UPDATE addr = '%s'""" % (email, domain, time_used, email)

                cursor.execute(sql2a)

            db.commit()

        except:
            print("Error: Unable to commit sql2.")
            db.rollback()

        #We want what has been set up in the last 30 days and the total number of entries

        sql3 = """SELECT domain, COUNT(*)
                    FROM email_table
                    WHERE DATE_SUB(CURDATE(),INTERVAL 30 DAY) <= date_added
                    GROUP BY domain
                    ORDER BY Count(*) DESC"""
        sql3a = """SELECT COUNT(*)
                    FROM email_table
                    """
        print("Selecting the values to create the percentage calculations from the 'email_table' database.")
        percent_table = {}
        try:
        #	Execute the SQL command
            #gets the total number of queries
            cursor.execute(sql3a)

            # Fetch the one row we get
            results = cursor.fetchone()
            #assigns total to a variable
            total_count = results[0]


            #Execute the SQL command
            # gets the email address ans the number of times a domain is repeated within the last 30 days
            cursor.execute(sql3)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()

            for row in results:
                domain = row[0]
                count = row[1]
                #percent increase
                percent_increment = count * 1.0 / total_count

                #updates the percent increase
                sql3b = """UPDATE email_table
                            SET domain_percent_increase = %f
                            WHERE domain = '%s' """ % (percent_increment, domain)
                try:
                    cursor.execute(sql3b)
                    db.commit()
                except:
                    db.rollback()
                    print("Error in sql3b insertion.")
                #percent_table[domain] = percent_increment
        except:
            print("Error: unable to fetch data sql3."	)

        print("\nSelecting the 50 largest domain names from the email_table database.")
        print("The results will be ordered by the largest percentage increase in the last 30 days.\n")
        sql4 = """SELECT domain, COUNT(*), domain_percent_increase
                FROM email_table
                GROUP BY domain
                ORDER BY domain_percent_increase DESC
                LIMIT 50"""

        try:
            #Execute the SQL command
            cursor.execute(sql4)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()

            for row in results:
                domain = row[0]
                count = row[1]
                percent_increase = row[2]


                domain_text = "domain=" + domain
                count_text = "count=" + str(count)
                percent_increase_text = "percent increase=%f"%(percent_increase)
                # just formatting it to look nice
                print(domain_text.ljust(30) + count_text.ljust(15) + percent_increase_text)
                #print("domain=%s count=%d, \t\tpercent increase=%f" % (domain, count, percent_increase)

        except:
            print("Error: unable to fetch data from sql4."	)

        print("\nCycle complete.")
        print("Last call completed at %s"%datetime.now().strftime("%Y-%m-%d %A, %H:%M:%S"))
        print(spacing)


#setting a time for us to activate
time_now = datetime.now()
# format for the datetime variables
time_formats = '%H:%M:%S'

# Default time assumes this program will run at midnight, however, we can change it to a different time
# or set it some time, like a minute after the program begins
time_adjusteds = datetime.strptime('00:00:00', time_formats).strftime('%X')

#time_adjusteds = (time_now + timedelta(seconds = 10)).strftime('%X')
#time_adjusteds = datetime.strptime('10:21:00', time_format).strftime('%X')
#######################
'''
We want to be able to edit it for the local system.
'''
fo = open("../data/DBInfo.txt","r")
dbVals = []
for index in range(5):
    line = fo.readline()
    dbVals.append(line.strip('\n'))

fo.close()

# Open database connection
dbs = MySQLdb.connect(host=dbVals[0], port=int(dbVals[1]), user =dbVals[2], passwd=dbVals[3], db=dbVals[4])

runExchange(dbs, time_formats, time_adjusteds)
# disconnect from server
dbs.close()


