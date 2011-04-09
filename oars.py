import urllib , urllib2,cookielib,string,getpass,re
import BeautifulSoup,itertools
username=raw_input("Username : ")
passwd=getpass.getpass()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
urllib2.install_opener(opener)
params=urllib.urlencode(dict(LoginId=username,Password=passwd))
try :
    oars = opener.open("http://172.26.142.65:6060/login.asp",params)
except :
    print ("Wrong Username or password ")
    exit(1)
oars.close()

oars=opener.open("http://172.26.142.65:6060/Student/Afteradd_dropStatus.asp")

soup=BeautifulSoup.BeautifulSoup(oars.read())
for tag in soup.recursiveChildGenerator():
    if isinstance(tag,BeautifulSoup.Tag) and tag.name in ('td'):
        if tag.attrs==[]:
            print tag.string ,
            print '\n'

#pretty=soup.prettify()
tags=soup.findAll(align = None)
#print(tags)

oars.close()
choice=raw_input("Want to view previous Courses  (y/n)")
if choice.lower()=='y':
    oars=opener.open("http://172.26.142.65:6060/Student/Transcript.asp")
    soup=BeautifulSoup.BeautifulSoup(oars.read())
    #print(soup.prettify())
    #print(soup.prettify())
    regex = re.compile("^[\s]+([A-Z]+[A-Z0-9\s\-]*)[\n]",re.MULTILINE)
    a=regex.findall(soup.prettify())
    #print(a)
    #a.pop(0)
    b = ['\t\t\t'.join((x, y) if y else (x,)) for x, y in itertools.izip_longest(a[0::3], a[1::3])]
    a = ['\t'.join((x, y) if y else (x,)) for x, y in itertools.izip_longest(b[0::1], a[2::3])]
    #print(a)
    for i in a:
        print(i) 
    #print(a)
    #for tag in soup.recursiveChildGenerator():
    #    if isinstance(tag,BeautifulSoup.Tag) and tag.name in ('td'):
    #        if tag.attrs in [[],['align']]:
    #            print(tag.string)
    oars.close()

#soup=bs()
#print (soup)
