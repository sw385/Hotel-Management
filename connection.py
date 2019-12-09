import psycopg2
from psycopg2 import Error
import sys, os
import numpy as np
import pandas as pd
import credentials as creds
import pandas.io.sql as psql
import csv


# Set up a connection to the postgres server.
conn_string = "host="+ creds.PGHOST +" port="+ "5432" +" dbname="+ creds.PGDATABASE +" user=" + creds.PGUSER \
              +" password="+ creds.PGPASSWORD
conn=psycopg2.connect(conn_string)
print("Connected!")

# Create a cursor object
cursor = conn.cursor()

'''
Function Name: CreateTable()
Parameters:
	@table_name: a string value that contains the name of the table to be created
	@columms: a string value that is of the format "c1 data_type, c2 data_type" 
			  [anything you would put inside the parenthesis when creating a table]
Return Value: None
Purpose: Uses the create_table_query string to generate and execute a SQL statement that creates a new table in 
		 the database based on the values in the string
'''
def CreateTable(table_name, columns):
	query = '''CREATE TABLE %s (%s); ''' %(table_name,columns)
	cursor.execute(query)
	conn.commit()
	print("Table created successfully in PostgreSQL ")

'''
Function Name: LoadCSV()
Parameters:
	@file_name: a string that contains the name of the file to be loaded  
	@insert_query:a string that contains an insert query of the format 
				  "INSERT INTO table_name(c1, c2, c3) VALUES (%s,%s,%s)"
				  ********************IMPORTANT****************************
				  THE NUMBER OF  %s MUST ALWAYS MATCH THE NUMBER OF COLUMNS 
				  IN THE TABLE OF WHICH THE FILE WILL BE LOADED INTO
				  *********************************************************
Return Value: None
Purpose: Uses the paramaters values passed to load the table with values from a csv file.
'''
def LoadCSV(file_name, insert_query):
	with open (file_name, 'r') as file:
		read = csv.reader(file)
		next(read)
		for row in read:
			cursor.execute(insert_query,row)
			conn.commit()
		print("CSV File Loaded into table")

'''
Function Name: Insert()
Parameters:
	@table_name: a string that contains the name of the table to be updated 
	@columns: a string that contains the columns that are to be populated of the format 
		  'c1,c2,c3' [columns separated by commas]
	@values: a string that contains the values of the columns desired where the values 
         are separated by commas.
Return Value: None
Purpose: Uses the paramaters values passed to generate and execute a SQL statement that inserts a 
		 row based on the values of the strings passed.
'''
def Insert(table_name, columns, values):
	query = '''INSERT INTO %s (%s) values (%s);''' %(table_name,columns,values)
	cursor.execute(query)
	conn.commit()
	print("Row successfully inserted into table %s" %(table_name))

'''
Function Name: Select()
Parameters:
	@select_query: a string value contains SQL 
	@num_rows: an string value that will indicate the desired number of rows returned in the results
			   only 2 possible values : "one" && "all"
Return Value: 
	@result: an array with the desired results (if any)
Purpose: Uses the select_query string to generate a SQL statement that selects items in the database 
		 based on the values in the string and will execute the statement and return the results as 
		 an array object.
'''
def Select(select_query, num_rows):
	cursor.execute(select_query)
	if num_rows == "one":
		result = cursor.fetchone()
	elif num_rows == "all":
		result = cursor.fetchall()
	conn.commit()
	return result