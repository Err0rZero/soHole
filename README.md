# soHole

一个WEB代理 FUZZER程序。
现已实现 XSS FUZZ and CSRF FUZZ。

请自行下载安装 pycurl 和 bs4包

基于代理方式的FUZZ工具
run : python soHole.py http://xxx.com/

设置你的browser为代理模式
你提交的任何GET和POST数据都将进行FUZZ测试。
