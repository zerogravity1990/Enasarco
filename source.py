#!/usr/bin/python

import main
import sys

def starting():
    util = main.Utility()
    mandate_list = ["monomandatario", "plurimandatario"]
    print "Welcome, initializing data"
    print "Insert your name and type of mandate."
    print "What's your name?"
    agent_name = raw_input(">>>")
    print "Type of mandate?"
    mandate = raw_input(">>>")
    if util.check_answer(mandate, mandate_list) is not True:
        print "Only \'monomandatario\' and \'plurimandatario\' are accetable"
        starting()
    else:
        print "%s and %s, it's all correct?" % (agent_name, mandate)
        current_answer = raw_input("y/n >>>")
        if util.check_answer(current_answer, util.yes_list):
            agent = main.Agent(agent_name, mandate)
            print agent.name, agent.mandate, "all ok"
            db = main.Database()
            db.check_existing_db()
            db.insert_data(agent.name, agent.mandate)
        else:
            print "type your name again"
            starting()

starting()
print "\n \n \n"
db2 = main.Database()
db2.get_agent_data()
