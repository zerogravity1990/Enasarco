#!/usr/bin/python
import sqlite3
import ConfigParser
import os

class Agent(object):
    def __init__(self, name, mandate):
        self.name = name
        self.mandate = mandate


class Invoice(object):
    def __init__(self, date, number, net_value, enasarco_rate):
        self.date = date
        self.number = number
        self.net_value = net_value
        self.enasarco_rate = enasarco_rate
        self.iva = net_value * 0.22
        self.total_of_invoice = self.net_value + self.iva
        self.ritenuta_acconto = net_value * 0.23 * 0.5
        self.enasarco = self.net_value * self.enasarco_rate


class Parameters(object):
    def __init__(self):
        self.config_file_path = 'config.ini'

    def loader(self, config_file_path):
        self.config_file_path = config_file_path
        Config = ConfigParser.ConfigParser()
        Config.read(config_file_path)
        self.rate = Config.get('Parameters', 'rate')


class Algorithms(object):
    def calc_enasarco(self, net_value, rate):
        enasarco_quote = float(net_value)*float(rate)/100
        self.result = round(enasarco_quote, 2)


class Database(object):
    def __init__(self):
        # pass
        self.db_filename = 'main.db'
    def check_existing_db(self):
        self.db_filename = 'main.db'
        self.db_is_new = not os.path.exists(self.db_filename) # checking existence of filename db
        self.conn = sqlite3.connect(self.db_filename) # connecting to a not existing db will create it
        if self.db_is_new is True:
            print "creating db"
            self.create_tables()
        else:
            print "db already exists"
            # TODO inserting some init data
        self.conn.close()

    def create_tables(self):
        '''Create database table'''
        #TODO generalize the use of the method
        self.conn.execute('''CREATE TABLE AGENTS
                        (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        NAME TEXT NOT NULL,
                        MANDATE TEXT NOT NULL);''')
        print "table created"

    def insert_data(self, name, mandate):
        '''method for inserting data into database'''
        #TODO generalize the use of the method
        self.conn = sqlite3.connect(self.db_filename)
        with self.conn:
            self.conn.execute('''INSERT INTO AGENTS \
                            (NAME, MANDATE) \
                            VALUES (?, ?)''', (name, mandate));
        self.conn.commit() # without this call data aren't write into the db
        print "data ok"

    def get_agent_data(self):
        '''Method for getting agent parameters from db'''
        self.conn = sqlite3.connect(self.db_filename)
        with self.conn:
            self.cur = self.conn.cursor()
            self.cur.execute('''SELECT * FROM AGENTS''');
            self.rows = self.cur.fetchall()
            for self.row in self.rows:
                print self.row


class Utility(object):
    def __init__(self):
        self.yes_list = ["yes", "y", "yeah", "yep"]
        self.no_list = ["no", "n", "none", "nope"]

    def check_answer(self, user_input, check_list):
        self.user_input = user_input.lower()
        self.check_list = check_list
        print self.user_input, self.check_list
        for elements in self.check_list:
            if elements in self.user_input.split():
                return True
