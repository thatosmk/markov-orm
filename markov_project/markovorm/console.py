#!/usr/bin/python
import logging
from python_markov import PyMarkov
from sql_python import SQLPy
import time
from setup import *

logging.basicConfig(
        filename="test.log",
        level=logging.DEBUG,
        format="%(asctime)s:%(funcName)s:%(message)s"
        )

def connect():
    """ call SQLPy with credentials to connect """
    
    con = SQLPy(user, password, server, database, driver)

    return con

def startup():
    """ print the startup string """
    import os

    logging.debug("Stared the console")
    print "Welcome to PyMarkov\n"

    # check if a file exists
    if os.path.isfile("setup.py") :
        # prompt for credentials
        logging.debug("Connected to the database\n")
        print "Connected to the database\n"
        return connect()
    else:
        # go ahead connect to the database
        logging.debug("Getting credentials from user for setup.py")
        return get_cred()

def get_cred():
    """ gather credentials """
    import getpass 

    user = raw_input("username: ")
    password= getpass.getpass("password: ")
    database= raw_input("database_name: ")
    server= raw_input("host: ")
    driver= raw_input("linux/win - type(linux or win): ")
    # save credentials?
    save = raw_input("Store credentials?(Y/n): ")
    
    if (driver.lower() == "linux"):
        driver = "mysqldb"
    else: 
        driver = "pymysql"


    # prompt to ask to save credentials
    if (save.lower() == 'y'):
        # write to text file
        with open("setup.py", 'w') as f:
            f.write("user="+"\""+user+"\""+"\n")
            f.write("password="+"\""+password+"\""+"\n")
            f.write("server="+"\""+server+"\""+"\n")
            f.write("database="+"\""+database+"\""+"\n")
            f.write("driver="+"\""+driver+"\""+"\n")
            f.close()
    print "Credentials saved."
    # establish a connection
    con = SQLPy(user, password, server, database, driver)
    
    return con

def common_cmds():
    """ print common commands for user to get started """
    print "Type 'show transition matrix' to get the transition matrix"
    print "     'quit' to exit" 
    print "     'show data' to get the matrix before transition matrix" 
    print "     'show absorbing' to get the absorbing matrix" 
    print "     'show non-absorbing' to get the absorbing matrix" 

if __name__ == "__main__":

    db = startup()
    # grab the table data
    print "Enter your query: "
    query = raw_input()
    
    
    data = db.get_table(query)
   
    # re enter a valid query
    while(data == None):
        query =  raw_input("Enter your query: ")
        data  = db.get_table(query)

    # call PyMarkov
    markov = PyMarkov(data) 

    print "You can now start making you computations."

    print "Type these commmon commands"
    # print common cmds
    common_cmds()

    # hard code the data_matrix
    matrix = markov.get_matrix_array()

    # begin the console prompt
    cmd = raw_input("pymarkov>")

    while(cmd.lower() != "quit"):
        if cmd == "show transition matrix": 
            # measure time for the function
            logging.debug("Printed Transition matrix \n"+str(markov.get_trans_matrix()))
            print markov.get_trans_matrix()
        elif cmd == "show data": 
            print matrix
        elif cmd == "show absorbing": 
            logging.debug("Printed Absorbing matrix \n"+str(markov.get_abs_matrix(matrix)))
            print markov.get_abs_matrix(matrix)
        elif cmd == "show non-absorbing": 
            logging.debug("Printed non-absorbing matrix \n"+str(markov.get_transient_matrix(matrix)))
            print markov.get_transient_matrix(matrix)
        elif cmd == "show abs states": 
            print markov.abs_states()
        elif cmd == "show non abs states": 
            print markov.trans_states()
        elif cmd == "help": 
            logging.debug("Looked up help commands")
            common_cmds()
        elif cmd == "show forecast": 
            print markov.forecast(2)
        else:
            print "Sorry unknown command"
            logging.debug("Unknown command: %s" % cmd)
            common_cmds()

        cmd = raw_input("pymarkov>")
    # log the action of quitting
    logging.debug("Quit from program") 
