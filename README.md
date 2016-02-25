# IE
Domain Name MySQL Database

This runs in Python 2.7.
Use the command line. This is designed for Windows.

This was a project I did for Index Exchange as a test. I have modified it from its original form.

A person should set the DBInfo.txt in the data folder to their local repository. It contains the IP Address (127.0.01 by default), the port number (3300 by default), the user name (should be changed), the password (should be changed), and the name of the repository (should be changed).

They then should go to pyFiles, and run create_reset_tables.py before they begin. This will delete the table, so be careful.  It will populate the table with some starting values found in the same folder. If you want to change whether or not the table is created or dropped at the beginning they can do so here.

insert_values.py and sort_data.py can be run concurrently, and it is even recommended if you do not have a pre-existing means of generating new addresses. I recommend starting insert_values.py if there is no pre-existing database that is taking in new data, but sort_data.py will either wait until the scheduled time or until manually activated.
