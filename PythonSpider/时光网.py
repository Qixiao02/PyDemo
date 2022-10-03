import requests
from lxml import etree
import csv
import json

head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27'
}
params = {
    'keyword': "",
    'pageIndex': 1,
    'pageSize': 20,
    'searchType': 0,
    'locationId': 290,
    'genreTypes': "",
    'area': "",
    'year': ""
}
num = []
url = "http://front-gateway.mtime.com/mtime-search/search/unionSearch2"
resp = requests.post(url=url, headers=head, params=params)
dict = json.loads(resp.text)
# print(dict)
new_dict = []
for i in dict["data"]["movies"]:
    # print(i['movieId'])
    new_dict.append(i['movieId'])
print(new_dict)

db = open("时光网.csv", "w", encoding="utf-8", newline="")
#创建写入器
write_data = csv.writer(db)




# write_data.writerow(['电影名', '英文名', "电影类型"])
# for i in dict["data"]["movies"]:
#     write_data.writerows([[i['name'], i["nameEn"], i["movieType"]]])
# db.close()
# print('写入完成!')

for i in new_dict:
    resq2 = requests.get(url=f"http://movie.mtime.com/{i}/", headers=head).text
    # print(resq2.url)
    tree = etree.HTML(resq2)
    print(resq2)
    # pepole = tree.xpath("/html/body/div[2]/div/div[3]/div[1]/div/div[2]/div[3]/div[1]/div[1]/div[3]/div/p[2]")
    # print(pepole)



