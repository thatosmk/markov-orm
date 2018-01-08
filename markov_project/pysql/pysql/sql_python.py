from sqlalchemy import create_engine
#import pandas as pd
#import numpy as np


def create_connection(driver, user, password,host,database):
    # create a database connection to the database(parameter)
    con =   create_engine('mysql+'+driver+'://'+user+':'+password+host+database)

    # connect to the database 
    # return a connection(connected) object
    return con.connect()

def init_con():

    host = "@analytics.technocore.co.za:3306/"
    username = "Ryan"
    password = "Ryan12345"
    db = "analytics_ryan"

    driver = "mysqldb"

    print "\nOpenening Connection to..."
    print host+db

    
    return create_connection(driver, username, password, host, db)


connection = init_con()
print "Connected\n"

def get_col_names(table_name,con=connection):
    query = "select * from " + table_name
    result = con.execute(query)
    return result.keys()
    

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

def parse_values(values):
    headings = []
    vals = []
    for i in sorted(values.iterkeys()):
        headings.append(i)
        vals.append(values[i])
    return [headings,vals]

def parse_values_2(values, headings):
    
    to_pad = len(values[0])
    pad_with = len(headings[0])
    pad = pad_with-to_pad

    values_strip = []
    for i in values:
        values_strip.append(i[0])
   

    for i in xrange(0,pad):
        values_strip[0].append(0)
##    for i in values_strip:
##        print i
    return [headings,values_strip]

def does_table_exist(table_name):
    query = "SHOW TABLES LIKE "+ "'" +str(table_name)+ "'" + " ;"
##    print query
    result = connection.execute(query).fetchall()
    result_str = []
    
    if not result:
        return False

    for i in result[0]:
        result_str.append(str(i))
        
    if table_name in result_str:
        
        print "Table "+table_name +" exists"
        return True
    else:
        return False   

def create_table_query(feed, table_name):

    newfile = 0

    #if table exists, change table_name: could add overwrite
    while does_table_exist(table_name):
        for i in xrange(0,len(table_name)):
            if table_name[len(table_name)-i - 1].isdigit():
                continue
            else:
                table_name=table_name[:len(table_name)-i]
                break
        table_name += str(newfile)
        newfile+=1
    
    print "Results written to "+table_name
    
    headings, values = parse_values(feed)
##    headings, values = parse_values_2(feed,["CD0","CD1","CD2","CD3","Repaid","WriteOff"])
    
    # create table with headings
    create_table = "CREATE TABLE " + table_name + " ("
    for i in headings:
        create_table += "`"
        create_table += str(i)
        create_table += "` float,"
    create_table += " total float"
    create_table+=");"

    fill_table = "INSERT INTO " + table_name + " VALUES ("
    for i in values:
##        print i
        fill_table += str(sum(i))
        fill_table += ","
    total = 0
    for i in values:
        total+= sum(i)
    total = str(total)
    fill_table += total
    fill_table+=");"

    return (create_table, fill_table)

def create_table_query_2(feed, col_names, table_name):

    newfile = 0

    #if table exists, change table_name: could add overwrite
    while does_table_exist(table_name):
        for i in xrange(0,len(table_name)):
            if table_name[len(table_name)-i - 1].isdigit():
                continue
            else:
                table_name=table_name[:len(table_name)-i]
                break
        table_name += str(newfile)
        newfile+=1
        
    
##    headings, values = parse_values(feed)
    
    headings, values = parse_values_2(feed,col_names)
    headings.append("Total")
    
    # create table with headings
    create_table = "CREATE TABLE " + table_name + " (Month int NOT NULL AUTO_INCREMENT ,"
    fill_table = "INSERT INTO " + table_name + " ( "
    for i in headings:
        fill_table += "`"
        fill_table += str(i)
        fill_table += "`,"
        
        create_table += "`"
        create_table += str(i)
        create_table += "` float,"
##    create_table = create_table[:-1]
    fill_table = fill_table[:-1]
    fill_table += ") "
    create_table+="PRIMARY KEY (Month));"
    
    fill_table += "VALUES "
    
##    print values
    values = values[1:]
    for i in values:
        fill_table += "("
        for j in i:
        
            fill_table += str(j)
            fill_table += ","
            
        fill_table+=str(sum(i))
        
##        fill_table = fill_table[:-1]
        fill_table += "),"
    fill_table = fill_table[:-1]
##    print fill_table

    return (create_table, fill_table)

def push_to_sql(query, con=connection):
    
    con.execute(query[0])
    con.execute(query[1])

##print "Import Successful"
##print table
##print get_dataframe('markov', connection)

