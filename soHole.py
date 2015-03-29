#!/usr/bin/env 
#-*- coding:utf-8-*-

import socket
import threading 
import select
import sys

from akMod import cAttack
from echo import echo
from AnalyticalHander import httpheader
from thread import allocate_lock

reload(sys)
sys.setdefaultencoding("utf-8")

LISTENIP = "127.0.0.1"#socket.gethostbyname(socket.gethostname())
LISTENPORT = 9899
BUFLEN = 65535
mylock = allocate_lock()

class ProxyClass():
	def __init__(self,conn,addr,TestWEb,mod = "csrf"):
		self.attack = cAttack()
		self.attack.testWeb = TestWEb
		self.attack.ackMod = mod
		#print self.attack.testWeb
		self.source = conn
		self.headers = {}
		self.handle_connection = ""
		self.des = None
		self.start()
		
	def getHeader(self):
		data = self.source.recv(BUFLEN)
		self.headers,self.handle_connection = httpheader(data)
		self.attack.header = self.headers
		self.attack.connection = self.handle_connection
		
		
	def go_LINE(self):
		req_headers = self.handle_connection
		self.des = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		hp = self.headers["host"].split(":")
		if len(hp) == 1:
			hp.append(80)
		try:
			self.des.connect((hp[0],int(hp[1])))
		except socket.error,arg:
			self.source.sendall("/1.1" + str(arg[0]) + "Fail\r\n\r\n")
			self.source.close()
			self.des.close()
		else:
			data = ""
			buf =  ""
			#self.ak_HttpGet()
			#line ok
			if req_headers.find("Connection") >= 0:
				pass
				req_headers = self.handle_connection.replace("keep-alive","close")
			else:
				req_headers += self.handle_connection + "Connection:close\r\n"
			req_headers += "\r\n"
			try:
				self.des.sendall(req_headers)
			except:
				self.source.sendall(data)
				self.source.close()
				return
			(rList,wList,eList) = select.select([self.des], [], [],3) 
			if eList:
				self.source.sendall(data)
				self.source.close()
				return
			for sock in rList: 
				while True:
					try:
						buf = sock.recv(BUFLEN)
						data += buf
					except:
						buf = None
					finally:
						if not buf:
							sock.close()
							break;
		self.source.sendall(data)
		self.source.close()

	def start(self):
		self.getHeader()
		if self.headers is None:
			return
		if self.headers["method"] == "GET":
			#
			self.attack.HttpGet()
			self.go_LINE()
			
		elif self.headers["method"] == "POST":
			#
			self.attack.HttpPost()
			self.go_LINE()

		elif self.headers["method"] == "CONNECT":
			pass

class ServerClass():#threading.Thread):
	def __init__(self,host,port,TestWeb,TestMod,header = ProxyClass):
		#threading.Thread.__init__(self)
		self.host = host
		self.port = port
		self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		self.server.bind((host,port))
		self.server.listen(500)
		self.header = header
		self.TestWeb = TestWeb
		self.TestMod = TestMod
	def run(self):
		while True:
			#mylock.acquire()
			try:
				conn,addr = self.server.accept()
				self.header(conn,addr,self.TestWeb,self.TestMod)
			except KeyboardInterrupt:
				exit();
			#mylock.release()


def main():
	if len(sys.argv) != 3:
		print "usage : " + sys.argv[0] + " 127.0.0.1:80 csrf"
		exit()
	print echo.no("Proxy ip : ") + echo.high(str(LISTENIP)) + echo.no(" <-> Proxy port : " )+ echo.high(str(LISTENPORT))
	TestWeb = sys.argv[1].split(":")[0]
	TestMod = sys.argv[2]
	print echo.no("TestWEb : " ) + echo.high(TestWeb)
	print echo.no("TestMod : ") + echo.high(TestMod)
	s = ServerClass(LISTENIP,LISTENPORT,TestWeb,TestMod)
	s.run()
	

if __name__ == '__main__':
	main()
