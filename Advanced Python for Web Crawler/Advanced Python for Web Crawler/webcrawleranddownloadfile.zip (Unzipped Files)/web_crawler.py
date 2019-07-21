import requests
from bs4 import BeautifulSoup

def crawler_web(max_pages):
    page=1
    while page <=max_pages:
        url='https://daffodilvarsity.edu.bd/department/SWE'
        source_code=requests.get(url)
        plain_text=source_code.text
        soup=BeautifulSoup(plain_text,features="html.parser")

        for link in soup.find_all('a'):   # a for a href       ,{'class':"main-contant"}
            href=link.get('href')
            print(href)

        page+=1

crawler_web(1)