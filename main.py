#!/usr/bin/env python

import ConfigParser

class Agent(object):
    pass

class Invoice(object):
    pass

class Parameters(object):
    # def __init__(self, rate, max_import, min_import):
    #     self.rate = rate
    #     self.max_import = max_import
    #     self.min_import = min_import

    def loader(self, config_file_path):
        self.config_file_path = config_file_path
        Config = ConfigParser.ConfigParser()
        Config.read(config_file_path)
        self.rate = Config.get('Parameters', 'rate')

class Algorithms(object):
    pass

path = '/home/zero/Projects/Enasarco/config.ini'
par = Parameters()
par.loader(path)
print par.rate
