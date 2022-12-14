"""
File: webcrawler.py
Name: Antina Yeh
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #

        tags = soup.find_all('table', {'class': 't-stripe'})

        num = []
        for tag in tags:
            tag = tag.tbody.text
            num = tag.split()

        male_sum = 0
        female_sum = 0
        for i in range(len(num)):
            index = i + 1  # set index
            # check if more than 200 sets of data
            if index > 1000:
                break
            # check if num[i] is a male data or  female data
            if index % 5 == 3 or index % 5 == 0:
                n = float(num[i].replace(',', ''))  # remove comma
                if index % 5 == 3:
                    male_sum += n
                else:
                    female_sum += n

        print('Male Number:', int(male_sum))
        print('Female Number:', int(female_sum))





if __name__ == '__main__':
    main()
