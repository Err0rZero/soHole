#-*- coding:utf-8 -*-
#!/usr/bin/python

import re
from GarbageData import data

#分解参数
def DecompositionParameters(rData):
	dataStr = None
	param_data = []
	try:
		tmp = rData.split("?")
	except:
		return param_data

	if re.search(u"(\.js)|(\.css)|(\.html)|(\.htm)|(\.shtml)",tmp[0]) == None:
		try:
			dataStr = tmp[1]
		except:
			return param_data
		if dataStr.find("&") == -1:
			if dataStr.find("=") != -1:
				param_data.append(dataStr.split("=")[1])
			else:
				param_data.append(dataStr)
		else:
			for d in dataStr.split("&"):
				param_data.append(d.split("=")[1])

	return param_data

def CsrfReferer():
	return data.csrf()

#查找参数并且替换
def SearchAndReplace(rData = "",mod = "xss"):
	retPath = []
	if mod == "csrf":
		for ak in CsrfReferer():
			retPath.append(ak)
		return retPath
	
	param_data = DecompositionParameters(rData)
	if param_data == None:
		return retPath
	for pd in param_data:
		if rData.find(pd):
			if mod == "xss":
				for ak in data.xss():
					retPath.append(rData.replace(pd,ak)) 

	return retPath


if __name__ == "__main__":
	#print SearchAndReplace("asdasd")

	s = SearchAndReplace("?__RequestVerificationToken=byql2lKHM71EHq3pSAMj57Ef_mQunNAHGbYvDd91DqlAUA7cDKF7OtW9GF2OaSGn2XnKSepLM-TaMS4OnxkxrZTKzcilk-gMNkAXGC_NrjI1&UserName=hello99&Password=123456&Code=282F&RememberMe=false")
	for ss in s:
		print ss
		print "---"
