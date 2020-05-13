#!/usr/bin/env python3

import json
import math

from os import listdir
from os.path import isfile, join, isdir, exists
import os
import re

ignore_list = ['[.]+.*', 'src']

def processDir(path):
    files = []
    for fileName in listdir(path):
        ignore=False
        for ignoreStr in ignore_list:
            if re.match(ignoreStr, fileName):
                #print ('Ignoring {} with {}'.format(fileName, ignoreStr))
                ignore=True
                break
        if not ignore:
            if isdir(fileName):
                files.extend(processDir(fileName))
            elif fileName[-5:] == '.json':    
                #print ('Adding {}'.format(fileName))
                files.append('{}/{}'.format(path, fileName))
            #else:
            #    print ('Ignoring {} as its not json'.format(fileName))

    return files            
    


files = processDir('.')    
print ('Found files {}'.format(files))
pageLimit = 10
asStreams = []
for jsonFile in files:
    print ('Opening: {}'.format(jsonFile))
    with open(jsonFile) as json_file:
        data = json.load(json_file)
        for stream in data['streams']:
            asStream = { 
                    'id': stream['id'],
                    'label': stream['label']
                    }
            if 'provider' in data:
                asStream['provider'] = data['provider']
            if 'institution' in data:
                asStream['source'] = data['institution']
            asStreams.append(asStream)

# should now sort asStream in some way to ensure the newest are first. 

# Now write out streams to pages
startIndex = 0
if len(asStreams) > pageLimit:
    endIndex = pageLimit
else:
    endIndex = len(asStreams)

pageCount = 0
maxPages = math.ceil(len(asStreams) / pageLimit)
pageJson = []
baseURL = "https://registry.iiif.io"
firstRun = True
while endIndex < len(asStreams) or firstRun==True:
    print ('endIndex {} asStreams length {}'.format(endIndex, len(asStreams)))
    currentPage = {
        "@context": "http://iiif.io/api/discovery/1/context.json",
        "id": "{}/page-{}.json".format(baseURL, pageCount),
        "type": "OrderedCollectionPage",
        "partOf": {
            "id": "{}/index.json".format(baseURL),
            "type": "OrderedCollection"
        }
    }
    if pageCount != 0:
        currentPage["prev"] = {
            "id": "{}/page-{}".format(baseURL, pageCount - 1),
            "type": "OrderedCollectionPage"
        }
    print ('Page count {}, maxPages {}'.format(pageCount, maxPages))    
    if pageCount < (maxPages - 1):     
        currentPage["next"] = {
            "id": "{}/page-{}".format(baseURL, pageCount + 1),
            "type": "OrderedCollectionPage"
        }
    currentPage['orderedItems'] = []    
    for i in range(startIndex, endIndex):    
        activity = {
            'type': 'Update',
            'object': {
                'id': asStreams[i]['id'],
                'type': 'OrderedCollection',
                'nameMap': asStreams[i]['label']
            }
        }
        if 'source' in asStreams[i] or 'provider' in asStreams[i]:
            activity['actor'] = []
            if 'source' in asStreams[i]:
                actor = asStreams[i]['source']
                if 'type' not in actor:
                    actor['type'] = "Organization"

                activity['actor'].append(actor)

            if 'provider' in asStreams[i]:
                actor = asStreams[i]['provider']
                if 'type' not in actor:
                    actor['type'] = "Organization"

                activity['actor'].append(actor)

                
        currentPage['orderedItems'].append(activity)
        

    pageJson.append(currentPage)

    firstRun = False
    startIndex = endIndex
    pageCount += 1
    if len(asStreams) - endIndex > pageLimit:
        endIndex += pageLimit
    else:
        endIndex = len(asStreams)

pageCount = 1
outputDir = 'output'
if not exists(outputDir):
    os.mkdir(outputDir)

for page in pageJson:
    print ('Page: {}'.format(pageCount))
    print (json.dumps(page, indent=4))
    filename = page['id'].split('/')[-1]
    with open('output/{}'.format(filename), 'w') as outfile:
        json.dump(page, outfile, indent=4)
