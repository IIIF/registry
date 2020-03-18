#!/usr/bin/env python3

import json

from os import listdir
from os.path import isfile, join, isdir


def processDir(path):
    for fileName in listdir(path):
        print (fileName[-5:])
        if isdir(fileName):
            processDir(fileName)
        elif fileName[-5:] == '.json':    
            # process JSON
            with open('{}/{}'.format(path, fileName)) as json_file:
                data = json.load(json_file)
        else:
            print ('Ignoring {}'.format(fileName))
            
    


processDir('.')    
