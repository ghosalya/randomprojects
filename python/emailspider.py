import urllib,re

def email_grab(target_url):
    htmlFile = urllib.urlopen(target_url)
    html = htmlFile.read()
    regexp_email = r'[\w\.-]+@[\w\.-]+';
    pattern = re.compile(regexp_email)
    emailAddresses = re.findall(pattern, html)
    return emailAddresses

def email_grabber(target_url, email_address, link_address):
    print "grabbing from main"+target_url
    emailAddresses = email_grab(target_url)
    print_dict(emailAddresses)

    for v in emailAddresses:
        email_address.append(v)

    link_addr = link_grabber(target_url)
    for link in link_addr:
        try:
            lnk = link[7:].strip('"')

            if "http" not in lnk:
                lnk = target_url+lnk
                
            emails = email_grab(lnk)
            for v in emails:
                email_address.append(v)
                
        except KeyboardInterrupt:
            quit()
        except:
            pass
        

    #print all matches
    #return emailAddresses

def link_grabber(target_url):
    htmlFile = urllib.urlopen(target_url)
    html = htmlFile.read()
    regexp_link = r'a href=\"\S+\"';
    pattern = re.compile(regexp_link)
    linkAddresses = re.findall(pattern, html)

    #print all matches
    return linkAddresses

def print_dict(dictt):
    for d in dictt:
        print(d)


email = []
links = []

email_grabber("http://www.ezbuy.com", email, links)
print_dict(email)