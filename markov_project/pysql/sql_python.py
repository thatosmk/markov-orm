from setup import *
from sqlalchemy import create_engine
import pandas as pd
import numpy as np


def create_connection(driver, user, password,host,database):
    # create a database connection to the database(parameter)
    con =   create_engine('mysql+'+driver+'://'+user+':'+password+host+database)

    # connect to the database 
    # return a connection(connected) object
    return con.connect()


connection = create_connection(driver, username, password, host, db)

def get_table(con, query):
    # given a valid connection to the database and a query
    # return a table from the given query(parameter)
    res = con.execute(query)

    # return an iterable object
    return res

def get_dataframe(table_name, con):
    # from the given table name, return the dataframe with the data in the
    # table (look at the sqlalchemy documentation for more sql functions)
    df = pd.read_sql_table(table_name, con)

    # return a list containing data in the row contained in a list as well
    return list(df.iterrows())

#def df_to_matrix(df):
    # convert the dataframe object to a matrix
    # iterate through the rows of the dataframe
    
# set up a connection

def test_run(connection, table):
    
##    connection =  create_connection(username, password, host, db)
    query = "select * from "+ "`" + table +"`"
    
    return get_table(connection, query).fetchall()

def test():
##    host = "@analytics.technocore.co.za:3306/"
##    username = "Ryan"
##    password = "Ryan12345"
##    db = "analytics_ryan"
    table = "markov"
    return test_run(connection, table)

def push_to_sql(table_name, erp, ewoff, total, con=connection):
    query = "CREATE TABLE " + str(table_name) + " ( `Eventual repaid` float, `Eventual write off` float, `total` float);"
    query_2 = "INSERT INTO " + str(table_name) + " VALUES "+" (" + str(erp) + "," + str(ewoff) + "," + str(total) + ") ;"
    
    con.execute(query)
    con.execute(query_2)

print "Import Successful"
##print table
##print get_dataframe('markov', connection)

