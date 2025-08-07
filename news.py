import requests
from bs4 import BeautifulSoup as bs
url="https://www.bbc.com"
page=requests.get(url)
h2=[]
if page.status_code==200:
    html_code=page.text
    soup=bs(html_code,'html.parser')
    h2_tags=soup.find_all('h2')
    for i in h2_tags:
        textofh2=i.get_text(strip=True)
        h2.append(textofh2)
    with open("titlefile.txt","w") as f:
        for i in h2:
            f.write(i+"\n")
    print("Titles saved")
else:
    print("failed to load the page")
    
    

    


