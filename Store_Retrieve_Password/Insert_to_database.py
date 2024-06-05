#import the required 
import mysql.connector
from cryptography.fernet import Fernet

#replace it with your credentials
mydb = mysql.connector.connect(
  host="<your hostname>",
  user="<your_username>",
  password="<your_password>",
  database="<your_database>"
)

#replace the text with the password that needs to be encrypted.
to_encrypt="<password>"

#use this the first time and make sure to store the key and remove this code and use the keys for further encrypting.
key=Fernet.generate_key()
print(key)

#create the instance with the key that is created
fernet_instance = Fernet(key)

# use .encode() to change the string to byte stream.
encrypted_text = fernet_instance.encrypt(to_encrypt.encode())
print(encrypted_text)

#Insert the values into DB 
db_execute=mydb.cursor()
query = "INSERT INTO <table> (<column1>, <column2>) VALUES (%s, %s)"
db_execute.execute(query, ("<your_username>", encrypted_text))
mydb.commit()