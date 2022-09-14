import requests
url = "https://movie.douban.com/j/chart/top_list"
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70"
}
param = {
    'type': "24",
    'interval_id': '100:90',
    'action': "",
    'start': 0,
    'limit': 1
}
douban_comedy = requests.get(url=url, headers=head, params=param)
print(douban_comedy.request.url)
# print(douban_comedy.json())
douban_comedy.close()