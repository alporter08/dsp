# -*- coding: utf-8 -*-

import re

def degrees(file):
    fin = open(file)
    next(fin) #skip first line (header)

    degrees = []

    for line in fin:
        l = line.split(',')
        l = [x.strip() for x in l]
        degrees.append(l[1])

    degrees_clean = []

    for item in degrees:
        x = re.sub('\.','',item) #remove periods from degrees
        degrees_clean = degrees_clean + x.split()

#create dictionary with frequencies
    d = {}

    for item in degrees_clean:
        if item not in d:
            d[item] = 1
        else:
            d[item] += 1


    return len(d), d


def titles(file):
    fin = open(file)
    next(fin) #skip first line (header)

    titles = []

    for line in fin:
        l = line.split(',')
        l = [x.strip() for x in l]
        title = l[2]
        x = re.sub(' .. Biostatistics','',title) #remove ' of Biostatistics' from degrees
        titles.append(x)

#create dictionary with frequencies
    d = {}

    for item in titles:
        if item not in d:
            d[item] = 1
        else:
            d[item] += 1


    return len(d), d

def emails(file):
    fin = open(file)
    next(fin) #skip first line (header)

    emails = []

    for line in fin:
        l = line.split(',')
        l = [x.strip() for x in l]
        emails.append(l[3])

    domains = []

#extract domain name
    for item in emails:
        item = item.split('@')
        domains.append(item[1])

    #create dictionary with frequencies
    d = {}

    for item in domains:
        if item not in d:
            d[item] = 1
        else:
            d[item] += 1

    return len(d), d  
