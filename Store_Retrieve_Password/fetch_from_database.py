#import the required modules
import mysql.connector
from cryptography.fernet import Fernet

#replace it with your credentials
mydb = mysql.connector.connect(
  host="<your hostname>",
  user="<your_username>",
  password="<your_password>",
  database="<your_database>"
)

key = b'<your_encryption_key>'  # Replace with your actual stored key

#create the instance with the key that is created
fernet_instance = Fernet(key)


#fetch all the required data from the database
db_execute=mydb.cursor()
db_execute.execute("select * from <your_table>")
db_results=db_execute.fetchall()

#use this to display all the username and passwords from the retrieved records
#Note: x[0] and x[1] is used as there are two columns in the local database. Change it accordingly for your database.
for x in db_results:
    print(f"user - {x[0]} password - {fernet_instance.decrypt(x[1].encode()).decode()}")

#use this to display the required password.
for x in db_results:
        if x[0]=='<required user name>':
            print(f"user - {x[0]} password - {x[1]})