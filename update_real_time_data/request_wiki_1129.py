from csv import DictWriter

import requests
from datetime import date
from lxml import etree
import csv

file_name = date.today().strftime("%b%d%Y") + '.csv'

url = "https://vi.m.wikipedia.org/wiki/B%E1%BA%A3n_m%E1%BA%ABu:D%E1%BB%AF_li%E1%BB%87u_%C4%91%E1%BA%A1i_d%E1%BB%8Bch_COVID-19_t%E1%BA%A1i_Vi%E1%BB%87t_Nam"

html_content = requests.get(url).text

html = etree.HTML(html_content)
tables = html.findall('body/div/div/main/div/div/div/div/div/table/tbody')
print(len(tables))
for i in tables:
    print(i)
    rows = iter(i)

    headers = ['Tinh thanh', 'Ca nhiem', 'Tu vong', 'Ca mac moi', 'Tong luot tiem chung', 'Mui 1', 'Ti le mui 1',
               'Mui 2', 'Ti le mui 2', 'So lieu phan phoi', 'Dan so', 'So lieu tren 100 nguoi']
    with open(file_name, 'a') as output_file:
        writer = csv.writer(output_file)
        writer: DictWriter = csv.DictWriter(output_file, fieldnames=headers, lineterminator='\n')
        writer.writeheader()

        for row in rows:
            values = [col.text for col in row]
            try:
                values[0] = row.find('td/a').text
            except:
                print('Expected Exceptions')
            try:
                values[0] = values[0].encode('utf-8')
                for i in range(1, len(values)):
                    values[i] = values[i].rstrip().replace('.', '')
                writer.writerow(
                    {'Tinh thanh': values[0], 'Ca nhiem': values[1], 'Tu vong': values[2], 'Ca mac moi': values[3],
                     'Tong luot tiem chung': values[4], 'Mui 1': values[5], 'Ti le mui 1': values[6],
                     'Mui 2': values[7], 'Ti le mui 2': values[8], 'So lieu phan phoi': values[9],
                    'Dan so': values[10], 'So lieu tren 100 nguoi': values[11]})
            except:
                print(dict(zip(headers, values)))
            # print(dict(zip(headers, values)))
