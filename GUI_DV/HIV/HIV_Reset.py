import csv
import sqlite3
#This file uses data from http://data.worldbank.org/topic/health
#This program is meant to clear the database before running.
f = open("../../AllData/8_Topic_en_csv_v2.csv", encoding="utf8")
sqlLocation = '../../AllData/SQL_HIV_Rate.sqlite'
START_YEARS = 1960
LATEST_YEARS = 2015
RANGE_YEARS = LATEST_YEARS-START_YEARS
#---#
SUFFIX_VAL = ""

def yearRangesCalc(startYear, totalYears, sqlType=''):
    #creates the range of years. This can either be used to help create the table or
    #set aside numbers for it.
    yRanges = ''
    #This program is using data from
    if startYear < START_YEARS or startYear + totalYears > LATEST_YEARS:
        #If the year is either higher or lower than our data.
        #needs manual update
        print("Outside %s data range")%LATEST_YEARS
        return yRanges
    for x in range(startYear, startYear + totalYears):
        yRanges += ', Y%s %s' %(x, sqlType)
        #creats a string that reads ",Y1960, Y1961, Y1962..., Y2014 "
    return yRanges

def startValues(tableCreate, suffix, yearStringRange):
    #Creates the tables to be used
    returnText = """CREATE TABLE %s%s
    (
    Country TEXT%s);""" % (tableCreate, suffix, yearStringRange)

    return returnText

def returnSQLQuery(rowVal, hivVal, sqlCalls, suffix):
    #creates the calls to be used
    listSQL = []
    #grabs the country name and a range of years
    entry = '\"%s\"' %(row[0])
    listSQL.append(entry)

    #Adds the information from the end of the csv file.
    listSQL.extend(row[-(LATEST_YEARS-START_YEARS+1):-(LATEST_YEARS-START_YEARS-RANGE_YEARS+1)])
    for idx, value in enumerate(listSQL):
        if idx == 0:
            #You want to skip the first value, supposedly 'Country'
            continue
        if value == '':
            #Sets any null values to 0.
            listSQL[idx] = "0"
    joinSql = ','.join(listSQL)
    returnSQLQuery = """INSERT INTO %s%s (%s%s)
                        VALUES (%s)""" % (hivVal, suffix, "Country", sqlCalls, joinSql)
    return returnSQLQuery
    
#these values are created so you don't have to always manually write all the values for the
#sql creations or calls.
sqlCreate = yearRangesCalc(START_YEARS, RANGE_YEARS, 'FLOAT')
sqlCall = yearRangesCalc(START_YEARS, RANGE_YEARS)

commands = ["drop table if exists \"Women's share of population ages 15+ living with HIV (%)\";",
            "drop table if exists \"Prevalence of HIV, total (% of population ages 15-49)\";",
            "drop table if exists \"Prevalence of HIV, female (% ages 15-24)\";",
            "drop table if exists \"Prevalence of HIV, male (% ages 15-24)\";",
            "drop table if exists \"Antiretroviral therapy coverage (% of people living with HIV)\";",

    startValues("\"Women's share of population ages 15+ living with HIV (%)\"", SUFFIX_VAL, sqlCreate),
    startValues("\"Prevalence of HIV, total (% of population ages 15-49)\"", SUFFIX_VAL, sqlCreate),
    startValues("\"Prevalence of HIV, female (% ages 15-24)\"", SUFFIX_VAL, sqlCreate),
    startValues("\"Prevalence of HIV, male (% ages 15-24)\"", SUFFIX_VAL, sqlCreate),
    startValues("\"Antiretroviral therapy coverage (% of people living with HIV)\"", SUFFIX_VAL, sqlCreate)]


           
            
conn = sqlite3.connect(sqlLocation)
cursor = conn.cursor()

print("Opened database successfully");

try:
#resets the database.
    for sqlQuery in commands:
        cursor.execute(sqlQuery)
        conn.commit()
    print("Database restarted!")
except:
    conn.rollback()
    print("Database restart failed")

listSQL = []
#Gets us to the line after 'Country Name'
while True:
    #
    line = f.readline().split(',')
    if not line:
        pass
    if line[0] == "\"Country Name\"":
        break
        
print("-"*10)

stop = 0 #In case I want to only do a limited number of iterations for debugging purposes.
print("Beginning insertions.")
for row in csv.reader(f):
    sqlQuery = ""
    if row[2] == "Women's share of population ages 15+ living with HIV (%)":
        sqlQuery = returnSQLQuery(row, "\"Women's share of population ages 15+ living with HIV (%)\"", sqlCall, SUFFIX_VAL)
    elif row[2] == "Prevalence of HIV, total (% of population ages 15-49)":
        sqlQuery = returnSQLQuery(row, "\"Prevalence of HIV, total (% of population ages 15-49)\"", sqlCall, SUFFIX_VAL)
    elif row[2] == "Prevalence of HIV, female (% ages 15-24)":
        sqlQuery = returnSQLQuery(row, "\"Prevalence of HIV, female (% ages 15-24)\"", sqlCall, SUFFIX_VAL)
    elif row[2] == "Prevalence of HIV, male (% ages 15-24)":
        sqlQuery = returnSQLQuery(row, "\"Prevalence of HIV, male (% ages 15-24)\"", sqlCall, SUFFIX_VAL)
    elif row[2] == "Antiretroviral therapy coverage (% of people living with HIV)":
        sqlQuery = returnSQLQuery(row, "\"Antiretroviral therapy coverage (% of people living with HIV)\"", sqlCall, SUFFIX_VAL)


    if not sqlQuery == "":
        try:
            #inserts the value into the database.
            cursor.execute(sqlQuery)
            conn.commit()
        except:
            conn.rollback()
            print("Query insertion failure!")
            print(sqlQuery)

    #Done for testing purposes
    '''if stop > 100:
        break
    stop += 1'''


# disconnect from server
conn.close()
print("Completed!")