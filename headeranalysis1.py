#! python 3

#######################################################################################################
#######################################################################################################
#####       Mail header analyzer v.1 : Written by Daniel Henderson                                  ###
#####       Script to analyze headers text file                                                     ###
#####       Takes header txt and with Regex copies most wanted info                                 ###
#####       Still needs to import headers.txt file                                                  ###
#####       Still can find a way to concatenate print results to one line to make code even shorter ###
#######################################################################################################
#######################################################################################################


import re

headers = ''' xxxx  '''

returnPath = re.compile(r'''(Return-Path: .*)''', re.I | re.VERBOSE) #Matches Return Path specifically
msgSender = re.compile(r'''(Sender: .*)''', re.I | re.VERBOSE) #Matches Msg Sender specifically
receivedFrom = re.compile(r'''(From: .*)''', re.I | re.VERBOSE) #Matches Return Path specifically
msgSubject = re.compile(r'''(Subject: .*)''', re.I | re.VERBOSE) #Matches Msg Subject specifically
xoriginatingIp = re.compile(r'''(x [-orginiating]+? ip: .*)''', re.I | re.VERBOSE) #Matches x-originating-ip specifically

print(returnPath.findall(headers))
print(msgSender.findall(headers))
print(receivedFrom.findall(headers))
print(msgSubject.findall(headers))
print(xoriginatingIp.findall(headers))
