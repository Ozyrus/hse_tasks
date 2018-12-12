from bs4 import BeautifulSoup
import requests


page = requests.get('http://classic.newsru.com/main/04dec2018/')

parsed = BeautifulSoup(page.content, 'html.parser')
pagelinks = parsed.find_all("a", class_="explaincolumn")
pagelinks_clear = [i['href'] for i in pagelinks]
for i in pagelinks_clear:
  page_i = requests.get('http://classic.newsru.com'+i)
  parsed_i = BeautifulSoup(page_i.content, 'html.parser')
  all_functions = parsed_i.find_all('script')
  for a in all_functions:
    a.decompose()
  page_text = parsed_i.find("p")
  page_text_clear = page_text.get_text()
  with open(i.replace('/','.')+'.txt','w', encoding = "UTF-8") as openfile:
    openfile.write(page_text_clear)