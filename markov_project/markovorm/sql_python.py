from sqlalchemy import create_engine
#from setup import *
import logging
""" connect sql server to python """

logging.basicConfig(
        filename="test.log",
        level=logging.DEBUG,
        format="%(asctime)s:%(funcName)s:%(message)s"
        )

class SQLPy():

    def __init__(self, user, password, server, database, driver):
        """ establish a database connection to the database(parameter) """
        connection = create_engine('mysql+'+driver+'://'+user+':'+password+'@'+server+'/'+database)

        # return a connection(connected) object
        self.con        = connection.connect()

        # write logs
        logging.debug("Created SQLPy ")

    def get_table(self, query):
        """ given a valid connection to the database and a query
            return a table from the given query(parameter) """
        try:
            res = self.con.execute(query)
            print "valid query"
            logging.debug("Valid query {}".format(query))

            # return an iterable object
            return res.fetchall()
        except:
            print "invalid query"
            logging.exception("error: ")
            return None


    def get_dataframe(self, table_name):
        """ deprecated """
        # from the given table name, return the dataframe with the data in the
        # table (look at the sqlalchemy documentation for more sql functions)
        df = pd.read_sql_table(table_name, con)

        # return a list containing data in the row contained in a list as well
        return list(df.iterrows())


    def push_to_sql(table, repaid, write_off, total, query_file):
        """ create table and push back the result to sql """

        query = "CREATE TABLE " + str(table_name) + " ( `Eventual repaid` float, `Eventual write off` float, `total` float);"
        query_2 = "INSERT INTO " + str(table_name) + " VALUES "+" (" + str(erp) + "," + str(ewoff) + "," + str(total) + ") ;"

        # create table
        self.con.execute(query)

        # insert the data into a database
        self.con.execute(query_2)

