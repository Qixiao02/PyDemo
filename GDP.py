import requests
from lxml import etree
import csv

url = "https://gdp.gotohui.com/data-3412"

head = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70 '
}

resp = requests.get(url=url, headers=head)
# print(resp.text)


etree = etree.HTML(resp.text)
data = etree.xpath('/html/body/div[4]/div/div[1]/div[3]/table/tr/td')
# for i in data:
#     print(i.text)

db = open("中国历年GDP总和.csv", 'w', newline='')
write_data = csv.writer(db)
write_data.writerow(['时间', 'GDP(美元)', '占世界比例(%)', '人均GDP(美元)'])
for i in data:
    write_data.writerows(i.text)
db.close()
