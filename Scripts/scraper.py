import requests
from bs4 import BeautifulSoup
import pandas as pd


URL = 'https://www.dgft.gov.in/CP/?opt=trade-statistics'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
page = requests.get(URL, headers)

try:
    dfs = pd.read_html(page.content)
    print(dfs)
except Exception as e:
    print(e)

try:
    soup = BeautifulSoup(page.content, "html.parser")
    table = soup.find_all('table')[4]
    print(table)
except Exception as e:
    print(e)