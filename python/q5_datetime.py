# Hint:  use Google to find python function

####a)
import datetime

date_start = '01-02-2013'
date_stop = '07-28-2015'

a = datetime.datetime.strptime(date_start, "%m-%d-%Y")
b = datetime.datetime.strptime(date_stop, "%m-%d-%Y")
c = b - a
print str(c)


####b)
date_start = '12312013'
date_stop = '05282015'

a = datetime.datetime.strptime(date_start, "%m%d%Y")
b = datetime.datetime.strptime(date_stop, "%m%d%Y")
c = b - a
print str(c)

####c)
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'

a = datetime.datetime.strptime(date_start, "%d-%b-%Y")
b = datetime.datetime.strptime(date_stop, "%d-%b-%Y")
c = b - a
print str(c)
