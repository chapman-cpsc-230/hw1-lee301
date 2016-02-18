"""File: <interest_rate.py>

Copyright (c) 2016 <Krystal Lee>

License: (http://img.shields.io/badge/license-MIT-blue.svg)](http://en.wikipedia.org/wiki/MIT_License)
"""
#Exercise 1.6
#Let p be a bank's interest_rate in percent per year. An initial amount A has grown to A(1+p/100)**n after n years.
#Make a program for computing how much money 1000 euros have grown to after three years with 5 percent interest_rate.

#p=interest rate in percent per year
#n=number of years
#A=initial amount

A=1000 #euros
n=3.0 #years
p=5.0 #percent

result = A*(1+p/100)**n
print "After %d years, the value will grow to be %.2f euros with %d percent interest with %d euros." % (n, result, p, A)
