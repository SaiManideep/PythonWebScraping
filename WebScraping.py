'''
Created on Feb 1, 2016

@author: Sai Manideep
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from BeautifulSoup import BeautifulSoup
import csv

wd = webdriver.PhantomJS() #Emulating browser without opening it.
wd.get("https://www.fpi.nsdl.co.in/web/Reports/Archive.aspx") 
date = raw_input("Enter date in given format: (Format : dd-mm-yyyy. Eg: 10-Jan-2016,05-Jul-2015)\n:")
script1 = 'document.getElementById("txtDate").value ="'+ date+'"'  #Strings for script to be executed
script2 = 'document.getElementById("hdnDate").value ="' + date+'"'
wd.execute_script(script1)#Setting date through JavaScript
wd.execute_script(script2) #Setting date through JavaScript
print("Date set\n")
wd.execute_script('document.getElementById("btnSubmit1").click();return false') #Hitting the submit button
wait = WebDriverWait(wd, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "tbls01"))) #Waiting till the tables appear
print("Waiting for tables\n")
soup = BeautifulSoup(wd.page_source) #Retrieving the page source
table = soup.findAll('table')[1] #Finding first table 
records = [] 
#Appending the headers to the records
records.append(['Date', 'Debt/Equity', 'Inv Route', 'Purchases', 'Sales', 'Net', 'Net in USD', 'Conversion rate'])
print("Fetching table 1\n")
#Finding the elements of first table and appending them to the records.
for tr in table.findAll('tr')[2:]:
    tds = tr.findAll('td') 
    if len(tds) == 8:
        if (str(tds[0].text.encode('utf-8')).startswith('Total')): #Ignoring "totals" of month and year
            break
        records.append([elem.text.encode('utf-8') for elem in tds])
    elif len(tds) == 5:
        records.append(['','']+[elem.text.encode('utf-8') for elem in tds])
    elif len(tds) == 6:
        records.append(['']+[elem.text.encode('utf-8') for elem in tds])
        
#Creating blank lines between first table and second table
records.append(['','','','','','','','','',''])
records.append(['','','','','','','','','',''])
records.append(['','','','','','','','','',''])
records.append(['','','','','','','','','',''])
print("Fetching table 2\n")
#Appending headers of second table
records.append(['Date', 'Derivative Product', 'Buy Contracts', 'Buy Amount', 'Sell Contracts', 'Sell amount', 'OI contracts', 'OI Amount'])
#Finding the elements of second table and appending them to the records.
table2 = soup.findAll('table')[2]
for tr in table2.findAll('tr')[2:]:
    tds = tr.findAll('td')
    if len(tds) == 8:
        if (str(tds[0].text.encode('utf-8')).startswith('Total')): #Ignoring "totals" of month and year 
            break
        records.append([elem.text.encode('utf-8') for elem in tds])
    elif len(tds) == 7:
        records.append(['']+[elem.text.encode('utf-8') for elem in tds])

print("Writing into CSV\n")
#Writing the records to a new CSV file.
with open('tables.csv','wb') as f:
    writer = csv.writer(f)
    writer.writerows(records)

print("Created tables.CSV successfully")
