# -*- coding: utf-8 -*-

# The football.csv file contains the results from the English Premier League.
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

def goal_diff(file):
    fin = open(file)
    next(fin)

    dict = {}

    for line in fin:
        l = line.strip().split(',')
        team = l[0]
        goals_for = int(l[5])
        goals_against = int(l[6])
        goal_diff = abs(goals_for - goals_against)
        dict[team] = goal_diff

    t = []

    pairs = [(v, k) for (k, v) in dict.iteritems()]
    pairs.sort()

    return pairs[0][1]
