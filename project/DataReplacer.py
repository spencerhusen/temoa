import sys
import sqlite3
from sqlite3 import Error

# Establishes sqlite3 connection with sqlite file used to run CapEx
def establish_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        # Returns established connection to main method
        return conn
    except Error as e:
        print(e + "\n")
    return None

# Replaces data in DEQ_HourlyTemplate.dat with data from CapEx output
def replace_data(connection, outputFile):
    cur = connection.cursor()
    # Prepares destination file for writing (DEQ_HourlyTemplate.dat)
    dest = open(outputFile, "a")

    # SQLite3 command(s) responsible for selecting needed data and writing it to DEQ_HourlyTemplate.dat
    """
    #TODO
    command = "SELECT * FROM ...
    dataColumn = cur.execute(command)
    dest.write(dataColumn)
    """

    # Commits the changes and closes the connection to the database (input file)
    conection.commit()
    connection.close()

# Executes main functionality of program
def main():
    # Stores command line argument (name of CapEx output) as variable
    inputFile = sys.argv[1]
    outputFile = "DEQ_HourlyTemplate.dat"
    # Establishes connection with database (CapEx output)
    conn = establish_connection(inputFile)
    # Runs replace_data function
    replace_data(conn, inputFile, outputFile)

if __name__ == "__main__":
    main()
