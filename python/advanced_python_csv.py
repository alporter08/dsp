# -*- coding: utf-8 -*-

def emails(file):
    fin = open(file)
    next(fin) #skip first line (header)

    emails = []

    for line in fin:
        l = line.split(',')
        l = [x.strip() for x in l]
        emails.append(l[3])

    fout(emails, 'emails.csv')

def fout(output, file):
    fout = open(file,'w')
    for item in output:
        fout.write(item)
        fout.write('\n')
    fout.close()
