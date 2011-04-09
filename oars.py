import urllib , urllib2,cookielib,string,getpass,re
from subprocess import call
import BeautifulSoup,itertools
#username=raw_input("Username : ")
import cPickle
#passwd=getpass.getpass()
username = "Y9521"
passwd = "satvikch"
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
urllib2.install_opener(opener)
params=urllib.urlencode(dict(LoginId=username,Password=passwd))
try :
    oars = opener.open("http://172.26.142.65:6060/login.asp",params)
except :
    print ("Wrong Username or password ")
    exit(1)
oars.close()

#oars=opener.open("http://172.26.142.65:4040/Common/CourseListing.asp")
#print(oars.read())
#soup=BeautifulSoup.BeautifulSoup(oars.read())
#for tag in soup.recursiveChildGenerator():
#    if isinstance(tag,BeautifulSoup.Tag) and tag.name in ('a'):
#        if tag.attrs==[]:
#            print tag.string ,
#            print '\n'

#pretty=soup.prettify()
#tags=soup.findAll(align = None)
#print(tags)
#oars.close()
#choice=raw_input("Want to view previous Courses  (y/n)")
choice = 'n'
if choice.lower()=='y':
    oars=opener.open("http://172.26.142.65:4040/Common/CourseListing.asp")
    soup=BeautifulSoup.BeautifulSoup(oars.read())
    #print(soup.prettify())
    #print(soup.prettify())
    regex = re.compile("^[\s]+([A-Z]+[A-Z]*[0-9]+[A-Z0-9]*)[\n]",re.MULTILINE)
    a=regex.findall(soup.prettify())
    cPickle.dump(a, open('save.p', 'wb')) 
    #print(a)
    #a.pop(0)
    #b = ['\t\t\t'.join((x, y) if y else (x,)) for x, y in itertools.izip_longest(a[0::3], a[1::3])]
    #a = ['\t'.join((x, y) if y else (x,)) for x, y in itertools.izip_longest(b[0::1], a[2::3])]
    #print(a)
    #count = 1
    #for i in a:
    #    print(count,i)
    #    count = count+1
    #print(a)
    #for tag in soup.recursiveChildGenerator():
    #    if isinstance(tag,BeautifulSoup.Tag) and tag.name in ('td'):
    #        if tag.attrs in [[],['align']]:
    #            print(tag.string)
    oars.close()
obj = cPickle.load(open('save.p', 'rb'))
print(obj)
scrap='y'
if scrap =='y':
    for i in obj:
    	#oars=opener.open("http://172.26.142.65:4040/Utils/CourseInfoPopup2.asp?Course="+i)
    	#soup=BeautifulSoup.BeautifulSoup(oars.read())
    	#fout = open (i,"w")
    	#print(type(soup.prettify))
    	#fout.write(oars.read())
    	#fout.close
        #if call("html2text " + i +">" +i+".txt", shell=True) == 0:
        call("rm -f " + i ,shell=True)
        #else :
        #	print(i)

