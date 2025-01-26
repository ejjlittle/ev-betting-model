import requests
from bs4 import BeautifulSoup
import NBA_Constants

#get response from NBA get request
response = requests.get(NBA_Constants.URL, 
                         headers=NBA_Constants.HEADERS,
                         cookies=NBA_Constants.COOKIES,
                           params=NBA_Constants.PARAMS)

#check requests connection
if response.status_code != 200:
    exit("Error fetching website data")

print(response.text)