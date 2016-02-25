import sys
if sys.version_info >(3,):
	import pymysql as MySQLdb
else:
	import MySQLdb

import MySQLdb
import time, random

####################
'''
We are randomly generating new names and emails to showcase that our main program can accept new data while it's activated.
'''
####################
domain = ['gmail', 'yahoo', 'hotmail', 'sympatico', 'aol', 'comcast', 'msn', 'hushmail',  'fakemail', 'pseudomail', 'liarmail', 'bogusmail', 'mockmail', 'phonymail', 'fakecompany', 'pseudocompany', 'liarcompany','boguscompany', 'mockcompany', 'phonycompany', 'fakedomain', 'pseudodomain', 'liardomain', 'bogusdomain', 'mockdomain', 'phonydomain', 'fakebusiness', 'pseudobusiness', 'liarbusiness', 'bogusbusiness', 'mockbusiness', 'phonybusiness',]
tld = ['com', 'ca', 'net', 'edu', 'uk', 'co', 'int', 'gov', 'mil', 'ai', 'ao', 'es', 'eu', 'in', 'ke', 'mk', 'biz', 'aero', 'mobi']

first_names = ['Lewis', 
'Zona', 
'Shirlene', 
'Georgiana', 
'Cassie', 
'Clarinda', 
'Sarai', 
'Wanda', 
'Jeanice', 
'Telma', 
'Dannie', 
'Min', 
'Wiley', 
'Giuseppe', 
'Becki', 
'Jonah', 
'Jody', 
'Piedad', 
'Sharyn', 
'Hobert', 
'Hyacinth', 
'Angelique', 
'Jamee', 
'Carmela', 
'Garrett', 
'Bryon', 
'Jerrie', 
'Jannet', 
'Allen', 
'Erica', 
'Terresa', 
'Peggie', 
'Dorathy', 
'Loree', 
'Naoma', 
'Wava', 
'Karine', 
'Ed', 
'Richelle', 
'Tiffani', 
'Chante', 
'Elisa', 
'Curtis', 
'Hyon', 
'Zachary', 
'Trent', 
'Dewitt', 
'August', 
'Francie', 
'Theo']
			
last_names = ['Osborne', 
'Stone', 
'Barron', 
'Walsh', 
'French', 
'Potter', 
'Odom', 
'Callahan', 
'Murillo', 
'Bass', 
'Sandoval', 
'Pugh', 
'Clarke', 
'Dominguez', 
'Cochran', 
'Trevino', 
'Acevedo', 
'Cervantes', 
'Hicks', 
'Howard', 
'Cantu', 
'Hodges', 
'Pham', 
'Shields', 
'Hess', 
'Hunter', 
'Ryan', 
'Velez', 
'Valenzuela', 
'Goodman', 
'Fowler', 
'Mercado', 
'Frederick', 
'Tate', 
'Houston', 
'Moon', 
'Richmond', 
'Pierce', 
'Gomez', 
'Roach', 
'Ramirez', 
'Haas', 
'Flynn', 
'Lara', 
'Sanchez', 
'Case', 
'Huber', 
'Watson', 
'Friedman', 
'Bautista', 
'Arellano', 
'Manning', 
'Harris', 
'Silva', 
'Sharp', 
'Mata', 
'Dyer', 
'Dillon', 
'Hebert', 
'Davies', 
'Watkins', 
'Cooke', 
'Cain', 
'Tucker', 
'Myers', 
'Hubbard', 
'Kaufman', 
'Becker', 
'Gallegos', 
'Garrison', 
'Macias', 
'Davidson', 
'Sosa', 
'Long', 
'Kent', 
'Baker', 
'Solis', 
'Yu', 
'Hoover', 
'Owen', 
'Short', 
'Briggs', 
'Mooney', 
'Riley', 
'Hatfield', 
'Valentine', 
'Taylor', 
'Gates', 
'Rivas', 
'Rivera', 
'English', 
'Kirk', 
'Mcdowell', 
'Butler', 
'Morrison', 
'Olson', 
'Gray', 
'Aguirre', 
'Garrett', 
'Melendez']

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
db = MySQLdb.connect(host=dbVals[0], port=int(dbVals[1]), user =dbVals[2], passwd=dbVals[3], db=dbVals[4])
#######################

cursor = db.cursor()

'''
We are making an insertion program. Every time period, we insert another number queries of a
randomly generated email address consisting of first_name.last_name@domain.tld That way,
we can simulate the insertion of new dates on a much faster scale.

That way, the other program can test to see if it's doing the calculations right to determine when dates are inserted
'''
x = 0
big_chance = 40
medium_chance = 75


while True:
	#A random number generator. we want to generate domain names, but we want to favour some more than others
	random_chance = random.randint(0, 100)
	if random_chance < big_chance:
		domain_chance = 2
	elif random_chance < medium_chance:
		domain_chance = 5
	else:
		domain_chance = len(domain)-1
		
	
	random_chance = random.randint(0, 100)
	if random_chance < big_chance:
		tld_chance = 2
	elif random_chance < medium_chance:
		tld_chance = 5
	else:
		tld_chance = len(tld)-1
		
#creates email first_name.last_name@domain.top_level_domain
	sqlvalue =  '%s.%s@%s.%s' % (first_names[random.randint(0, len(first_names)-1)],
			last_names[random.randint(0, len(last_names)-1)], 
			domain[random.randint(0, domain_chance)], 
			tld[random.randint(0, tld_chance)])
	
	
	print(sqlvalue)
	try:
		sqlquery = """INSERT IGNORE INTO MAILING (addr)
			VALUES ('%s')""" % sqlvalue
		cursor.execute(sqlquery)
		db.commit()
	
	except:
		db.rollback()
	
	x+=1
	#after sticking a certain number of entries into the table, we take breaks and then start adding smaller numbers of entries
	if x % 50 == 0 and x > 2000:
		time.sleep(15)