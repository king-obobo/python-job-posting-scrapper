from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_html(sequence_no):
    html = urlopen(f'https://www.timesjobs.com/candidate/job-search.html?from=submit&luceneResultSize=25&txtKeywords=python&postWeek=3&searchType=personalizedSearch&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&pDate=I&sequence={sequence_no}&startPage=1')
    soup = BeautifulSoup(html, 'lxml')
    # print(soup)
    return soup.find_all('li', {'class': 'clearfix job-bx wht-shd-bx'})