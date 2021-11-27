import requests
from datetime import date
from lxml import etree
import csv

file_name = date.today().strftime("%b-%d-%Y") + '.csv'

url = "https://vi.wikipedia.org/wiki/%C4%90%E1%BA%A1i_d%E1%BB%8Bch_COVID-19_t%E1%BA%A1i_Vi%E1%BB%87t_Nam"

html_content = requests.get(url).text

html = etree.HTML(html_content)
tables = html.findall('body/div/div/div/div/table/tbody')
print(len(tables))
for i in tables:
    print(i)
    rows = iter(i)
    # headers = [col.text for col in next(rows)]
    # with open(file_name, 'a', encoding='utf-8') as output_file:
    #     writer = csv.writer(output_file)
    #     writer = csv.DictWriter(output_file, fieldnames=headers, lineterminator='\n')
    #     writer.writeheader()
    #     for row in rows:
    #         values = [col.text for col in row]
    #         try:
    #             values[0] = row.find('td/a').text
    #         except:
    #             print('Expected Exceptions')
    #         try:
    #             for i in range(1, len(values)):
    #                 values[i] = values[i].rstrip()
    #             print(values)
    #             # writer.writerow(
    #             #     {'Tinh thanh': values[0], 'Ca nhiem': values[1], 'Dang dieu tri': values[2], 'Hoi phuc': values[3],
    #             #      'Tu vong': values[4]})
    #             writer.writerow(
    #                 {headers[0]: values[0], headers[1]: values[1], headers[2]: values[2], headers[3]: values[3],
    #                  headers[4]: values[4]})
    #         except:
    #             print(dict(zip(headers, values)))

    headers = ['Tinh thanh', 'Ca nhiem', 'Tu vong', 'Ca mac moi']
    with open(file_name, 'a') as output_file:
        writer = csv.writer(output_file)
        writer = csv.DictWriter(output_file, fieldnames=headers, lineterminator='\n')
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
                    {'Tinh thanh': values[0], 'Ca nhiem': values[1], 'Tu vong': values[2], 'Ca mac moi': values[3]})
            except:
                print(dict(zip(headers, values)))
            # print(dict(zip(headers, values)))
