# We are connecting our coin database python file to Datagrip DBMS.
# Every SQL statement is executed one at a time. So, to execute an SQL statement, the other SQL statements have to be commented out.

import sqlite3

conn = sqlite3.connect("user_account.sqlite") #generates sqlite database file.

cursor = conn.cursor() # used to execute the SQL statements.

#create table in the datagrip dbms:
sql_query = """CREATE TABLE account(  
  id integer PRIMARY KEY,
  balance integer NOT NULL
)"""

def getTokenFromFaucet(): # Get the current state of accounts and balance.
    self.id =id
    self.balance = balance
sql = """INSERT INTO account(id, balance)
              #VALUES('4', '$14'),
                  #  ('5', '$17'),
                  #  ('6', '$20')
        """

def getTokenFromFaucet(): # Get test coins from faucet.Update state of coin database and balance of the account.
    self.id = id
    self.balance = balance

sql1 = "SELECT * FROM account;"
sql2 =  "UPDATE account SET balance = '$80' WHERE id = 5;"

#cursor.execute(sql_query) # execute the query above by calling the execute method of the cursor object
#cursor.execute(sql)
#cursor.execute(sql1)
cursor.execute(sql2)
conn.commit()