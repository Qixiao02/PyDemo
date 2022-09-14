import requests
import re
import csv
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
}
#re解析
rule = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<movie>.*?)</span>.*?'
                  r'<br>(?P<year>.*?)&nbsp.*?'
                  r'/&nbsp;(?P<country>.*?)&nbsp;'
                  r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                  r'<span>(?P<people>.*?)人评价</span>', re.S)
db = open('doubanTop250.csv', 'w', encoding='utf-8', newline='')
csv.writer(db).writerow(["影片名", "上映年份", "国家", "评分", "评分人数"])
for i in range(0, 275, 25):
    url = f"https://movie.douban.com/top250?start={i}&filter="
    doubanTop250 = requests.get(url, headers=head)
    print(doubanTop250.text)
    doubanTop250.close()
    doubanTop250_rule = rule.finditer(doubanTop250.text)

    doubanTop250_csv = csv.writer(db)
    for it in doubanTop250_rule:
        dic = it.groupdict()
        dic['year'] = dic['year'].strip()
        doubanTop250_csv.writerow(dic.values())
        # print(dic)
        print("写入完成！")
db.close()
doubanTop250.close()
