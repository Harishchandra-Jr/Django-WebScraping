import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','practice_project.settings')

import django
import csv
import requests
from bs4 import BeautifulSoup
import csv
import re

django.setup()


from trading_app.models import todays



# #####################
response = requests.get("https://in.finance.yahoo.com/most-active")
soup = BeautifulSoup(response.text,"html.parser")
tbody = soup.find("tbody")
#####################



master_data =[]  # Creating empty list master_data
for tr in tbody.find_all('tr'):         # Searching all the table rows from table body
    
    tds = tr.find_all('td')              #Selecting tabal data from  table rows 
    #Adding all the data in to master_data list in dic format
    
    Comany_symbol= tds[0].text
    company_name = tds[1].text
    price_data = tds[2].text
    change = tds[3].text
    change_in_percentage = tds[4].text
    volume =tds[5].text
    Avgvol_In3Month=tds[6].text
    Market_cap=tds[7].text,
    PE_ratio= tds[8].text

    data = todays.objects.get_or_create(Comany_symbol = Comany_symbol,company_name=company_name,price_data=price_data,change=change,change_in_percentage=change_in_percentage,volume=volume,Avgvol_In3Month=Avgvol_In3Month,Market_cap=Market_cap,PE_ratio=PE_ratio )
        




# with open('names.csv', 'r', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         next_row = row
#         data = todays.objects.get_or_create(next_row)
#         print('done')
    

print('Completed')



