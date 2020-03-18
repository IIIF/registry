#!/usr/bin/env python3

import json

from os import listdir
from os.path import isfile, join, isdir
import re

ignore_list = ['[.]+.*', 'src']

def processDir(path):
    for fileName in listdir(path):
        ignore=False
        for ignoreStr in ignore_list:
            if re.match(ignoreStr, fileName):
                #print ('Matched {} with {}'.format(fileName, ignoreStr))
                ignore=True
                break
        if not ignore:
            if isdir(fileName):
                processDir(fileName)
            elif fileName[-5:] == '.json':    
                print ('Processing: {}'.format(fileName))
                # process JSON
                with open('{}/{}'.format(path, fileName)) as json_file:
                    data = json.load(json_file)
            #else:
            #    print ('Ignoring {} as its not json'.format(fileName))
            
    


processDir('.')    
