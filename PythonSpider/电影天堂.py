import requests
import re
import csv
head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
    }
def RequestsUrl():
    url = "https://www.dytt89.com/"
    Requests_get = requests.get(url, headers=head)
    Requests_get.encoding = 'gb2312'
    Requests_get.close()
    return Requests_get

def CheckHTML():
    print(RequestsUrl().text)

def ExtractHref():
    rule = re.compile(r"2022必看热片.*?<ul>(?P<HotURL>.*?)</ul>", re.S)
    rule2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)
    rule3 = re.compile(r'title="(?P<title>.*?)"')

    HotMovie_2022 = rule.finditer(RequestsUrl().text)
    HotMovie_2022_href_list = []
    HotMovie_2022_Frame_list = []
    for i in HotMovie_2022:
        HotMovie_2022_Frame = i.group('HotURL').strip()
        HotMovie_2022_href = rule2.finditer(HotMovie_2022_Frame)
        HotMovie_2022_Frame_list.append(HotMovie_2022_Frame)

        for x in HotMovie_2022_href:
            HotMovie_2022_href_url = x.group('href')
            HotMovie_2022_href_list.append("https://www.dytt89.com"+HotMovie_2022_href_url)

    title = rule3.finditer(HotMovie_2022_Frame)
    HotMovie_2022_titles= []
    for t in title:
        titles = t.group('title'.strip())
        HotMovie_2022_titles.append(titles)

    return [HotMovie_2022_Frame_list, HotMovie_2022_href_list, HotMovie_2022_titles]

def Check():
    one = ExtractHref()[0]
    two = ExtractHref()[1]
    three = ExtractHref()[2]
    print(one)
    print(two)
    print(three)

def ExtractSubpageInfo():
    url = ExtractHref()[1]
    rule = re.compile(r'.*?<div class="title_all"><h1>(?P<title>.*?)</h1></div>.*?'
                      r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf">.*?<a href="(?P<bt>.*?)">', re.S)
    db = open('电影天堂2022热门必看电影.csv', 'w', newline='')
    csv.writer(db).writerow(["影片名", "bt链接"])
    for i in url:
        response = requests.get(i, headers=head)
        response.encoding = 'gb2312'

        MovieInfo = rule.finditer(response.text)
        MovieHot = csv.writer(db)
        for x in MovieInfo:
            dic = x.groupdict()
            MovieHot.writerow(dic.values())
            # print(x.groupdict())
        print("写入完成！")
    db.close()




if __name__ == '__main__':
    RequestsUrl()
    # CheckHTML()
    ExtractHref()
    ExtractSubpageInfo()