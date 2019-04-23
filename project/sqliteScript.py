import sqlite3
from sqlite3 import Error
global output_file 
def establish_connection(db_file):
    try:
          #establishes connection to paramterized database
        conn = sqlite3.connect(db_file)
          #prints message to console indicating if connection was established
        print("Established Connection with \"" + db_file + "\"\n");    return conn
      #catches error and prints message if connection fails
    except Error as e:
        print(e + "\n")
    return None
  #Selects 'tech' and 'capacity' data rows from SQLite file to be appended to output file    
def select_needed_fields(conn, f):
    cur = conn.cursor()
    #t = 2030
      #defines SQLIte statement that sef = open(output_file, "a")lects data from 'tech' and 'capacity' columns 
    sql = "SELECT * FROM Output_CapacityByPeriodAndTech WHERE t_periods == 2030"
    rows = cur.execute(sql)
    for row in rows:
        f.write(str(row[3]) + " ")
        f.write(str(row[4]) + "\n")
      #stores selected data from each row of the tech and capacity columns, hopefully
      #prints to console that data has been selected and returns stored data
    print("Selected Fields\n")
    return rows
  #Appends the desired data to the output .dat file    
def append_needed_data(rows, f):
      #declares SQLite statement that defines how data should be inserted into output table.
      #cursor = conn.cursor()
      #global output_file
      #insert_stmt = ("INSERT INTO tech()"
                    #"INSERT INTO capacity()"
                    #"VALUES(%s, )")
      #for i in rows:
         #cursor.execute(insert_stmt, rows)
      
      #iterates through each row in rows and inserts all 'tech' and 'capacity' data rows
    
     #writes contents of 'rows' to output file
    #This part needs work
      for row in rows:
        print(row)
      for out_row in rows:  
          f.write(out_row.str())
      #f.write (';')
      print("Appended Data\n")       
def main():
    global output_file
      #takes first CLA as name of database (input file)
    database = input("CapEx Database Name: ")
    type(database)
      #takes second CLA as name of .dat file (output file)
    output_file = input("Operational Database Name: ")
    type(output_file)
      #calls function to establish connection with database
    conn = establish_connection(database)
      #runs functions to capture and output desired data
    f = open(output_file, "a")
    table_rows = select_needed_fields(conn, f)
    
    #append_needed_data(table_rows, f)
    print("Done\n")
       
if __name__ == "__main__":
    main()