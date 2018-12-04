#import requests
#from bs4 import BeautifulSoup
#from csv import writer
#
#response = requests.get('https://finviz.com/screener.ashx?f=sec_technology&v=121')
#
#soup = BeautifulSoup(response.text,'html.parser')
#
#posts = soup.find_all(class_='td')
#
#with open('posts.csv','w') as csv_file:
#    csv_writer = writer(csv_file)
#    headers = ['Data']
#
#
#    for post in posts:
#        data = soup.find(class_='screener-link').get_text()


#Currently in development

