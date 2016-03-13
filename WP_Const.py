#This Page is intended to provide constant String access for the Library file, and also provides constant string generstion in a dynamic manner#

data = {"log":"","pwd":"","wp-submit":"Log In","testcookie":"1","User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36"}
cookie = {"wordpress_test_cookie":"WP+Cookie+check"}


wpLogSuffix = "/wp-login.php"
wpInfoSuffix = "/readme.html"


ConnErrCkLogPg = "Connection Error on Checking Login Page"
ConnErrBrute = "ConnectionError on Login Page Bruteforcing"
ConnErrEnum = "AuthorEnum Connection Error"



authorRE = "\/author\/(.*?)\/"



sign_BruteStarts = "\t\t->Brute Force Starts:"
sign_HIT = "\t"*4+"->>>-->>>>>>HIT!<<<<<<--<<<-"
sign_MISS = "\t"*4+"->>[MISS]"
sign_NoFurtherAttack = "0 User/403 Detected, Attack Stopped!"
sign_zeroUser = "No User could be Enumerated!"



def BombStartReport(num):
	return "\n"+"*"*80+"\n\t\t\t\t<## "+str(num)+" ##>"

def AccountReport(result):
    return "\t"*4+"Username: "+result["log"]+"; Password:"+result["pwd"]

def userEnumReport(numUser):
    return "-> User Enumeration Finished:\n\t\t\tFound "+str(numUser)+" Users"
    
def userFoundReport(user):
    return "-> Found User: "+user
    
def startTestingReport(url):
    return "\t\t\t>>>Tesing URL:<<<\n\t\t"+url  
    