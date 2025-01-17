from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
import pause
import pandas as pd


# Set empty list to store data in
data = []

# The request code


def scraper(url):

    headers = {'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    req = Request(url, headers=headers)
    context = ssl._create_unverified_context()

    uClient = urlopen(req, context=context)
    html = uClient.read()
    uClient.close()

    return BeautifulSoup(html, 'html.parser')


# Nested for loop:
# First for loop loops trough all numbers from 1970 to (not including) 2021 - We need this to generate years
# Second loop loops through the strings 04, 08, 12 - We sample 1 April, 1 August, and 1 December
for year in range(1970, 2020):
    for month in ['04', '08', '12']:

        # We build a custom url for the charts of every month of every year 1970-2020. Per iteration of the nested for loops, we get a different year-month combination
        url = 'https://www.billboard.com/charts/hot-100/' + \
            str(year) + '-' + str(month) + '-01/'
        print(url)

        soup = scraper(url)  # We get the html

        # Narrow down to the chart info
        chartdata = soup.find(
            'div', class_='u-max-width-960 lrv-u-margin-lr-auto')

        # loop through each chart item
        for i in chartdata.find_all('ul', class_='lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max'):
            rank = i.find('span', class_='c-label  a-font-primary-bold-l u-font-size-32@tablet u-letter-spacing-0080@tablet')  # Get rank
            title = i.find('h3').getText().strip()  # Get title text
            artist = i.find('span').getText().strip()  # Get artist text
            print(year, month, rank, '-', title, 'by', artist)
         

            if rank <= 20:  # Only keep if it's in the top 20

                entry = {
                    'year': year,
                    'month': month,
                    'rank': rank,
                    'artist': artist,
                    'title': title,
                }  # Define a dictionary with all the required info

                data.append(entry)  # Add dictionary to the list data

        savedata = pd.DataFrame(data)  # Convert list data to a dataframe
        # Save dataframe to file
        savedata.to_csv('billboard.csv', sep=',', index=False)

        pause.seconds(2)  # Pause for two seconds in between every request
