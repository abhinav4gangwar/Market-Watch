import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

#conneting to mongodb atlas
client = MongoClient('mongodb+srv://bpsfocusenergy:bpsfocusenergy32@cluster0.3muhn.mongodb.net/bps?retryWrites=true&w=majority')
db = client.bps
collection = db.news_update

#fetching moneycontrol url
url = r'https://www.moneycontrol.com/'
r = requests.get(url)


soup = BeautifulSoup(r.content, 'html5lib')

#convert from single to multiple keywords
keywords = 'ICICI'

link_array =[]

a_tag_array = soup.find_all('a')
# print ("technical" in str(a_tag_array[100].get_text()).lower())
for i in a_tag_array:
    # print (i.get_text())
    if keywords in str(i.get_text()).lower():
        link_array.append(i['href'])

[print (i) for i in link_array]

#removing non news array items
filtered_link_array = []
for i in link_array:
    if i.count('stockpricequote')==0:
        filtered_link_array.append(i)



#removing duplicates
link_array = [*set(filtered_link_array)]



for i in link_array:
    reqs = requests.get(i)
    soup = BeautifulSoup(reqs.text, 'html.parser')

    data = {

    'title':soup.h1.get_text(),
    'img': soup.find('div', 'article_image').img['data-src'],
    'date': soup.find('div', 'article_schedule').span.get_text(),
    'desc': soup.h2.get_text()

    }
    print (data)
    collection.insert_one(data)


