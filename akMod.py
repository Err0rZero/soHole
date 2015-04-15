#!/usr/bin/env 
# -*- coding:utf-8 -*-

import pycurl
import log
import time

from StringIO import StringIO
from echo import echo
from DataAnalysis import dasis
from TestParameter import SearchAndReplace

class cAttack():
        def __init__(self):
                self.headers = None
                self.handle_connection = None
                self.Mod = None
                self.TestWeb = None
                self.sio = StringIO()
                self.curl = pycurl.Curl()
        	
        def closeSio(self):
                self.sio.close()
    
        def closeCurl(self):
                self.curl.close()
    
        @property
        def header(self):
                return self.hearders
	
        @header.setter
        def header(self,value):
                self.headers = value
    	
        @property
        def connection(self):
                self.handle_connection
	
        @connection.setter
        def connection(self,value):
                self.handle_connection = value.split("\n")[-1]
		
        @property
        def ackMod(self):
                return self.Mod
	
        @ackMod.setter
        def ackMod(self,value):
                self.Mod = value
	
        @property
        def testWeb(self):
                return self.TestWeb
	
        @testWeb.setter
        def testWeb(self,vulue):
                self.TestWeb = value
	
        def setCurlSetOpt(self,v,ak,rouData = {}):
                self.curl.setopt(pycurl.USERAGENT, self.header["user-agent"])
                self.curl.setopt(pycurl.COOKIEFILE, self.header["cookie"])
                self.curl.setopt(pycurl.REFERER,self.header["path"])
                self.curl.setopt(pycurl.WRITEFUNCTION, self.sio.write)
                if v == "post" and self.ackMod != "csrf":
                        self.curl.setopt(pycurl.URL, self.header["path"]) 	
                        self.curl.setopt(pycurl.POSTFIELDS, ak[1:])
                if v == "get" and self.ackMod != "csrf":
                        self.curl.setopt(pycurl.URL, ak)
                if self.ackMod == "csrf":
                        self.curl.setopt(pycurl.URL,self.header["path"])
                        self.curl.setopt(pycurl.REFERER,ak)
                        if v == "post":
                                self.curl.setopt(pycurl.POSTFIELDS,rouData["fields"])
                self.curl.setopt(pycurl.VERBOSE, True)
                self.curl.setopt(pycurl.FOLLOWLOCATION, 1)
                self.curl.setopt(pycurl.MAXREDIRS, 5)
                self.curl.setopt(pycurl.CONNECTTIMEOUT, 60)
                self.curl.setopt(pycurl.TIMEOUT, 300)
		
        def HttpPost(self):
                retak = []
                ak_List = []
                rouData = {}
                postData = self.connection
                rouData["fields"] = postData
                if len(postData) < 1:
                        return False
                if self.header["path"].find(self.testWeb) != -1:
                        if self.ackMod == "csrf":
                                ak_List = SearchAndReplace("","csrf")
                        else:
                                ak_List = SearchAndReplace("?" + postData)
                else:
                        return False
    			
                if len(ak_List) == 0:
                        return False
    	
                echoAk = ""
                for ak in ak_List:
                        if self.ackMod == "csrf":
                                echoAk = ak
                        else:
                                echoAk = ak[1:]
                        print echo.fail("#Attack Post    -------->     ") + echo.high(echoAk)
                        try:
                                self.setCurlSetOpt("post",ak,rouData)
                                self.curl.perform()
                                if self.curl.getinfo(self.curl.HTTP_CODE) == 200:
                                        html = self.sio.getvalue()
                                        if self.ackMod == "csrf":
                                                retak.append(self.header["path"] + ":" + echoAk)	
                                                continue;	
                                        ds = dasis(html)
                                        if ds.start() == 1:
                                                retak.append(headers["path"] + ":" + echoAk)
                                                del ds
                                        else:
                                                pass
                        except KeyboardInterrupt:
                                exit()
                        except pycurl.error , e:
                                if e[0] == 56:
                                        print e[1]
                                        #raw_input("Press Enter to continue: ")
                                        break;
                        except:
                                continue;
                        finally :
                                pass
    	#return retak
                self.retInfo("post",retak)
                return True

        def HttpGet(self):
                retak = []
                ak_List = []
                
                if self.header["path"].find(self.testWeb) != -1:
                        if self.ackMod == "csrf":
                                ak_List = SearchAndReplace("","csrf")
                        else:
                                ak_List = SearchAndReplace(self.header["path"])
                else:
                        return False
    	
                if len(ak_List) == 0:
                        return False
    	
                for ak in ak_List:
                        print echo.fail("#Attack Get    -------->     ") + echo.high(ak)
                        try:
                                self.setCurlSetOpt("get",ak)
                                self.curl.perform()
                                if self.curl.getinfo(self.curl.HTTP_CODE) == 200:
                                        html = self.sio.getvalue()
                                        if self.ackMod == "csrf":
                                                retak.append(self.header["path"] + ":" + ak)
                                                ds = dasis(html)
                                                continue;
                                        if ds.start() == 1:
                                                retak.append(ak)
                                                del ds
                                else:
                                        pass
                        except KeyboardInterrupt:
                                exit()
                        except pycurl.error , e:
                                if e[0] == 56:
                                        print e[1]
                                        #raw_input("Press Enter to continue: ")
                                        break;
                        except:
                                continue;
                        finally :
                                pass
    	#return retak
                self.retInfo("get",retak)
                return True

        def retInfo(self,v,retak):
        	seavfile = time.strftime("%d%m%Y")
                if len(retak) != 0:
                        print echo.fail(v + " Vulnerability connection :  " + str(len(retak)) + "\r\n")
                        for ra in retak:
                                log.writeLog(str(seavfile),self.ackMod + "  " + self.testWeb + v + "  " + ra)
                                print echo.high(ra) 
                                print "log save ok. path : " + log.getLogFile() + "/" + self.testWeb + ".log\r\n"
                raw_input("Log Save Ok .. Press Enter to continue: ")
    			
if __name__ == "__main__":
        pass
