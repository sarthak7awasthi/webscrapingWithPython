from bs4 import BeautifulSoup
import requests
import csv

soup = BeautifulSoup(requests.get("http://localhost:3000/").text, 'lxml')

csv_file = open('data.csv', 'w', newline='')
writer = csv.writer(csv_file)

writer.writerow(['title', 'summary', 'links'])

for article in soup.find_all('div', class_='post'):
    title = article.h3.a.text
    summary = article.p.text
    link = "http://localhost:3000{}".format(article.h3.a['href'])
    row = [title, summary, link]
    writer.writerow(row)

csv_file.close()