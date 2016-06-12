# PythonWebScraping
Written only to scrape data from a particular website

This program fetches data from the website "https://www.fpi.nsdl.co.in/web/Reports/Archive.aspx" and copies into a CSV(Comma Separated Values) file.

It takes one date from the user, and fetches the data from 1st of that month till the date provided.
Eg : if user enters 10-Feb-2015,
Data fetched will be from 01-Feb-2015 to 10-Feb-2015. For getting full month data please enter the last date of the month.

This program was written in Python 2.7. Executing using Python3 would give some syntax errors(such as "raw_input not found". Python3 replaced raw_input with input). Please execute with Python 2.7.

Before running the program, 2 external modules (BeautifulSoup, Selenium) have to be installed.

From commandline, run "pip install BeautifulSoup" and "pip install Selenium"

While executing the program, Please enter the date in the specified format : Eg: 10-Jan-2015, 01-Dec-2015, 25-May-2014 etc., Date validation has not been provided due to time constraints, so please enter date in correct format.

An example output file "Tables.csv" has been attached.


---------------------------------------------------Thanks, Sai Manideep------------------------------------------------------------------------------
