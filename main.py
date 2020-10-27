import requests
from bs4 import BeautifulSoup

res=requests.get("https://g1.globo.com/")
res.encoding='utf-8'
soup= BeautifulSoup(res.text, 'html.parser')
posts=soup.find_all(class_="bastian-feed-item")
all_posts=[]
for post in posts:
    print(post.find('div').text)

#print('**************************')
print(posts)
#print(soup)
#print(res.status)