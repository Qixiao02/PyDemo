import time
import requests
import csv
import json

head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 '
                  'Safari/537.36 Edg/105.0.1343.27 '
}
params = {
    'keyword': "",
    'pageIndex': 1,
    'pageSize': 20,
    'searchType': 0,
    'locationId': 290,
    'genreTypes': "",
    'area': "中国",
    'year': ""
}
num = []
url = "http://front-gateway.mtime.com/mtime-search/search/unionSearch2"
resp = requests.post(url=url, headers=head, params=params)
dict = json.loads(resp.text)
new_dict = []


def getstamp():
    return round(time.time() * 1000)


for i in dict["data"]["movies"]:
    # print(i['movieId'])
    new_dict.append(i['movieId'])
# print(new_dict)


f = open("时光网.csv", "w", encoding="utf-8", newline="")
# #创建写入器
write_data = csv.writer(f)
write_data.writerow(['电影名', '英文名', "评分人数"])
for i in new_dict:
    url = "http://front-gateway.mtime.com/library/movie/detail.api?tt={}&movieId={}".format(getstamp(), i)
    resp2 = requests.get(url)
    dict1 = json.loads(resp2.text)
    # print(dict1)

    data = dict1['data']['basic']
    name = data['name']
    nameEn = data['nameEn']
    ratingCount = data['ratingCount']

    # print(name)
    # print(nameEn)
    # print(ratingCount)
    write_data.writerows([[data['name'], data["nameEn"], data["ratingCount"]]])
f.close()
