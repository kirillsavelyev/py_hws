# -*- coding: utf-8 -*-

__author__ = 'kirillsavelyev'

from bs4 import BeautifulSoup as bs
import xlsxwriter
import requests
from urllib.parse import urlparse, parse_qs


def main():
    """ The main function. Reads the list of requests
    and makes queries on google.com
    After the completion of all requests and the preparation of the results,
    the export function starts """

    # reading file with queries
    queries = []
    with open('queries', 'r') as file:
        for i in file:
            queries.append(i.strip())

    url = 'http://google.com'
    search = '/search?q='
    total_result = []

    # make request on google.com for each question
    for q in queries:
        r = requests.get(url + search + q)

        # Preparing html with BeautifulSoup
        # and searching for headings with the required CSS class
        if r.status_code == 200:
            h3_results = bs(r.text, 'lxml').find_all('h3', class_='r')
        else:
            print('Something is wrong, the server may have blocked your IP.',
                  'status code: {}'.format(r.status_code))
            raise SystemExit

        # parsing of the URL for each element of the search result
        full_url_results = []
        for h3 in h3_results:
            raw_url = urlparse(h3.find('a').get('href'))
            if raw_url.path == '/url':
                full_url_results.append(parse_qs(raw_url.query)['q'][0])

        # filling of the list of final results
        total_result.append([q, full_url_results])

    # starting the export to excel function
    xlsx_write(total_result)


def xlsx_write(t_result):
    """ The export function. Creates the excel file and worksheet
    Then writes the results of queries in the file """

    # creating an excel file
    with xlsxwriter.Workbook('search_results.xlsx') as workbook:
        worksheet = workbook.add_worksheet()
        row = 0
        col = 0

        # creating column names
        worksheet.write(row, 0, 'Поисковый запрос')
        worksheet.write(row, 1, 'Результаты на первой странице выдачи')
        worksheet.set_column(0, 0, 30)
        row += 1

        # writing results in to a file
        for query, results in t_result:
            for result in results:
                worksheet.write(row, col, query)
                worksheet.write(row, col + 1, result)
                row += 1


if __name__ == '__main__':
    main()
