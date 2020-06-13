# importing libraries 
import requests 
from bs4 import BeautifulSoup 
import os 
import numpy as np 
import matplotlib.pyplot as plt 

extract_contents = lambda row: [x.text.replace('\n', '') for x in row] 
URL = 'https://www.mohfw.gov.in/'
	
SHORT_HEADERS = ['SNo', 'State','Indian-Confirmed(Including Foreign Confirmed)','Cured','Death'] 
	
response = requests.get(URL).content 
soup = BeautifulSoup(response, 'html.parser') 
header = extract_contents(soup.tr.find_all('th')) 

extract_contents = lambda row: [x.text.replace('\n', '') for x in row] 
URL = 'https://www.mohfw.gov.in/'

SHORT_HEADERS = ['SNo', 'State','Indian-Confirmed', 
                'Foreign-Confirmed','Cured','Death'] 

response = requests.get(URL).content 
soup = BeautifulSoup(response, 'html.parser') 
header = extract_contents(soup.tr.find_all('th')) 

stats = [] 
all_rows = soup.find_all('tr') 

for row in all_rows: 
    stat = extract_contents(row.find_all('td')) 
    if stat: 
        if len(stat) == 5: 
            # last row 
            stat = ['', *stat] 
            stats.append(stat) 
        elif len(stat) == 6: 
            stats.append(stat) 

stats[-1][1] = "Total Cases"

stats.remove(stats[-1]) 

objects = [] 
for row in stats : 
    objects.append(row[1]) 

y_pos = np.arange(len(objects)) 
performance = [] 
for row in stats :
    i=int(row[2]) 
    if row[3]=='':
        j=0
    else:
        j=(int(row[3]))
    performance.append(i+j) 

plt.barh(y_pos, performance, align='center', alpha=0.5, 
                color=(0.2, 0.4, 0.6, 0.6), 
                edgecolor=(106/256.0, 27/256.0, 154/256.0)) 

plt.yticks(y_pos, objects) 
plt.xlim(1,800000) 
plt.xlabel('Number of Cases') 
plt.title('Corona Virus Cases') 
plt.show() 