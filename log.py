#!/usr/bin/env 
# -*- coding:utf-8 -*-

import os
import logging

def getLogFile():
	logfile = os.path.split(os.path.realpath(__file__))[0]
	return logfile

def writeLog(filename,data):
	logger = logging.getLogger()
	handler=logging.FileHandler(getLogFile()  + "/" + filename + ".log")
	logger.addHandler(handler)
	logger.setLevel(logging.NOTSET)
	logger.info(data)

if __name__ == '__main__':
	print getLogFile()