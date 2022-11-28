from dotenv import dotenv_values
from flask import Flask
from flask_cors import CORS
import ibm_db

# Get the environment variables
config = dotenv_values("backend/.env")

# Connect to db
try:
    # conn = 'dd'
    conn = ibm_db.pconnect(
        f"DATABASE={config['DB2_DATABASE']};HOSTNAME={config['DB2_HOSTNAME']};PORT={config['DB2_PORT']};SECURITY=SSL; SSLServerCertificate=backend/DigiCertGlobalRootCA.crt;UID={config['DB2_USERNAME']};PWD={config['DB2_PASSWORD']}", '', '')
    print("Connected to IBM_DB2 successfully!!")
    print(conn)
except:
    print("Failed to connect to Database!")
