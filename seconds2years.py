"""File: <seconds2years.py>

Copyright (c) 2016 <Krystal Lee>

License: (http://img.shields.io/badge/license-MIT-blue.svg)](http://en.wikipedia.org/wiki/MIT_License)
"""
#Exercise 1.3
#can a newborn baby in Norway expect to live for one billion (10^9) seconds?
#write a Python program for doing arithmetics to answer the question.

seconds = 1000000000
minutes = seconds/60
hours = minutes/60
days = hours/24
years = days/365
print years

print "The child will live to be %d." % years
