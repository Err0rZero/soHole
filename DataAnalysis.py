#! /usr/bin/python
# -*- coding:utf-8 -*-

from GarbageData import sentinelvalue
from bs4 import BeautifulSoup

class dasis():
	def __init__(self,html):
		self.soup = BeautifulSoup(html) 
	def searchA(self):
		for a in self.soup.find_all('a'):
			stra = str(a)
			if stra.find(sentinelvalue) != -1:
				return 1
		return 0

	def searchP(self):
		for p in self.soup.find_all('p'):
			stra = str(p)
			if stra.find(sentinelvalue) != -1:
				return 1
		return 0

	def searchLink(self):
		for link in self.soup.find_all('link'):
			stra = str(link)
			if stra.find(sentinelvalue) != -1:
				return 1
		return 0	

	def searchInput(self):
		for i in self.soup.find_all('input'):
			stra = str(i)
			if stra.find(sentinelvalue) != -1:
				return 1
		return 0			

	def searchSpan(self):
		for s in self.soup.find_all('span'):
			stra = str(s)
			if stra.find(sentinelvalue) != -1:
				return 1
		return 0				

	def searchImg(self):
		for i in self.soup.find_all('img'):
			stra = str(i)
			if stra.find(sentinelvalue) != -1:
				return 1
		return 0					

	def searchScript(self):
		for script in self.soup.find_all('script'):
			stra = str(script)
			if stra.find(sentinelvalue) != -1:
				return 1
		return 0						

	def start(self):
		if self.searchA() == 1:
			return 1
		if self.searchScript() == 1:
			return 1
		if self.searchImg() == 1:
			return 1
		if self.searchSpan() == 1:
			return 1
		if self.searchInput() == 1:
			return 1
		if self.searchLink() == 1:
			return 1
		if self.searchP() == 1:
			return 1
		return 0


	def __def__(self):
		del self.soup

