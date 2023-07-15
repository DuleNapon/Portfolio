import mysql.connector
import os

# MySQL connection configuration
config = {
    "database": "portfolio",
    "username": os.environ["username"],
    "host": os.environ["host"],
    "password": os.environ["password"]
}

# Directory to save PDF files
pdf_directory = 'static/Certificates'

# Establish a connection to MySQL
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

# Retrieve data from the Certificates table
select_query = "SELECT Cert_Name, Cert_File FROM Certificates"
cursor.execute(select_query)
data = cursor.fetchall()

# Close the cursor and database connection
cursor.close()
cnx.close()

# Prepare the certificates list of dictionaries
certificates = []
for row in data:
    cert_name = row[0]
    cert_file = row[1]

    # Generate a unique file name based on the certificate name
    file_name = f"{cert_name}.pdf"
    file_path = os.path.join(pdf_directory, file_name)

    # Save the PDF file to the server's file system
    with open(file_path, 'wb') as file:
        file.write(cert_file)

    certificate = {
        "name": cert_name,
        "file_path": file_path
    }

    certificates.append(certificate)

print(certificates)