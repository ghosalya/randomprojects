import urllib,re

def email_grabber(target_url, email_address, link_address):
    htmlFile = urllib.urlopen(target_url)
    html = htmlFile.read()
    regexp_email = r'[\w\.-]+@[\w\.-]+';
    pattern = re.compile(regexp_email)
    emailAddresses = re.findall(pattern, html)
    print_dict(emailAddresses)

    for v in emailAddresses:
        email_address.append(v)

    link_addr = link_grabber(target_url)
    for link in link_addr:
        try:
            lnk = link[7:].strip('"')
            if "http:" not in lnk:
                lnk = target_url+lnk
            print(lnk)
            if lnk not in link_address:
                email_grabber(lnk, email_address, link_address)
                link_address.append(lnk)
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
        print d

email = []
links = []

email_grabber("http://www.rotex.com", email, links)