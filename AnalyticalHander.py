#-*- coding:utf-8 -*-
#!/usr/bin/python

from BaseHTTPServer import BaseHTTPRequestHandler
from StringIO import StringIO

class HTTPRequest(BaseHTTPRequestHandler):
	def __init__(self, request_text):
		self.rfile = StringIO(request_text)
		self.raw_requestline = self.rfile.readline()
		self.error_code = self.error_message = None
		self.parse_request()

	def send_error(self, code, message):
		self.error_code = code
		self.error_message = message

	def quit(self):
		self.rfile.close()

def httpheader(header_str):
	request = HTTPRequest(header_str)
	ret_Header = header_str
	ret_Quest = {}
	try:
		ret_Quest["method"] = request.command
		ret_Quest["path"] =request.path
	except:
		print "httpheader Error ..."
		exit()
		
	try:
		ret_Quest["version"] = request.request_version
	except:
		ret_Quset["version"] = 1.1
	#ret_Quest["header"] = lineheader
	for a in request.headers.keys() :
		ret_Quest[a] = request.headers[a]
	return (ret_Quest,ret_Header)

