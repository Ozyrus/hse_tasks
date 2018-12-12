from bs4 import BeautifulSoup
import requests

page = requests.get("http://classic.newsru.com/main/27nov2018/")
soup = BeautifulSoup(page.content, 'html.parser')
hreflist = soup.find_all(class_ = "explaincolumn", href = True)
all_texts=[]
for a in hreflist:
  page1 = requests.get('http://classic.newsru.com'+a['href'])
  innersoup = BeautifulSoup(page1.content, 'html.parser')
  deletefunct = innersoup.find_all('script')
  for i in deletefunct:
    i.decompose()
  plist = innersoup.find('p')
  fulltext = plist.get_text()
  all_texts.append(fulltext)
  print(fulltext)
with open("texts.txt", 'w') as writefile:
  print('success')
  for i in all_texts:
    writefile.write(i)