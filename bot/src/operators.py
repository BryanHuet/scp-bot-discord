import re
import requests
from bs4 import BeautifulSoup


def search_query(message):
    regex_engine = re.compile(r"(scp|SCP)-(\d+)")
    result = regex_engine.search(message)
    if result:
        position = result.span()

        query = message[position[0]:position[1]]
        query = query.split('-')[1]

        while len(query) < 3:
            query = '0'+query

        return query
    return '-1'


def get_scp_liste(url):
    request = requests.get(url)
    request.status_code

    soup = BeautifulSoup(request.content, features="lxml")
    main_div = soup.find('div', {'id': 'page-content'})
    scp_liste = main_div.find_all('a')

    return scp_liste


def get_scp_info(scp_query, scp_liste):
    scp = {'name': '', 'img': '', 'url': ''}
    for element in scp_liste:
        el = str(element)
        if scp_query in el and 'scp-'+scp_query in el:
            scp['name'] = element.parent.get_text()
            if 'href' in element.attrs:
                scp['url'] = element['href']

    return scp


def get_scp_img(scp_object, base_url):
    request_img = requests.get(base_url+scp_object['url'])
    
    soup_scp = BeautifulSoup(request_img.content, features="lxml")
    scp_img = soup_scp.find_all("div", {"class": "scp-image-block"})

    if len(scp_img) >= 1:
        scp_object['img'] = scp_img[0].img['src']

    return scp_object


def search_scp(query, database, page_list):
    base_url = database
    query_int = int(query)
    my_scp = {'name': 'NO SCP FOUND', 'img': ''}
    series = ''

    if (query_int < 0) | (query_int > 9000):
        return my_scp

    if 999 < query_int < 2000:
        series = '-2'
    elif 1999 < query_int < 3000:
        series = '-3'
    elif 2999 < query_int < 4000:
        series = '-4'
    elif 3999 < query_int < 5000:
        series = '-5'
    elif 4999 < query_int < 6000:
        series = '-6'
    elif 5999 < query_int < 7000:
        series = '-7'
    elif 6999 < query_int < 8000:
        series = '-8'
    elif 7999 < query_int < 9000:
        series = '-9'

    scp_liste = get_scp_liste(base_url+'/'+page_list+series)
    my_scp = get_scp_info(query, scp_liste)
    my_scp = get_scp_img(my_scp, base_url)

    return my_scp
