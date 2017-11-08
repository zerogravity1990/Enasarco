#!/usr/bin/env python

import ConfigParser

class Agent(object):
    def __init__(self, name, mandate):
        self.name = name
        self.mandate = mandate

class Invoice(object):
    def __init__(self, date, number, net_value):
        self.date = date
        self.number = number
        self.net_value = net_value

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
