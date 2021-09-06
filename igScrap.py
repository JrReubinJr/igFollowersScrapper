import pandas as pd
import csv
from proxies import collect_proxies
import requests
from bs4 import BeautifulSoup

def pullFromPrivatePhotoViewer(profile):
    url = f'https://privatephotoviewer.com/usr/{profile}'
    try:
        r = requests.get(url, timeout=6)
        soup = BeautifulSoup(r.content, 'html.parser')
        info = soup.find(class_="followerCount")
        followers = info.text.strip()
        print(f"{profile}: {followers} followers")
    except:
        followers = "N/A"
    return followers



#getFollowers takes a list of emails and an output path
def getFollowers(emails, path):
    # importing the file to write to
    f = open(path, 'a', newline='')
    writer = csv.writer(f)
    header = ['email', 'profile', 'followers']
    writer.writerow(header)

    proxies = collect_proxies()
    result=[]
    followers = None
    for email in emails:
        if '@' in email:
            at = email.index('@')
            profile = email[0:at]
            url = f"https://www.instagram.com/{profile}/"
            for ip in proxies:
                proxy = f'https://{ip}'
                r = requests.get(url, timeout=6, proxies={"https": proxy})
                try:
                    soup = BeautifulSoup(r.content, 'html.parser')
                    info = soup.find_all(class_="g47SY")
                    followers = info[1].text.strip()
                    break
                except:
                    if r.status_code == '403':
                        print('Proxy failed, trying next')
                    else:
                        followers = 'N/A'
                        break
            if followers == None:
                followers = pullFromPrivatePhotoViewer(profile)
                proxies=collect_proxies()
        else:
            profile = "Invalid Email"
            followers = 'N/A'
        writer.writerow([email, profile, followers])
    f.close()
    return True







