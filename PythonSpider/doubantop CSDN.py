# 拿到页面源代码  requests
import requests
# 通过re来进一步提取有效信息 re
import re
# csv处理
import csv

# 需要爬取的url
url = 'https://movie.douban.com/top250'
# 设置请求头的UA
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}
# 预编译re
obj = re.compile(
    r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>'
    r'.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
    r'<span>(?P<num>.*?)人评价</span>',
    re.S)
# 设置接收的csv文件
f = open('data.csv', mode='a+', encoding='utf-8', newline='')
# 因该页面仅有起始数不能范围获取，设置变量page表示为其实抓取的页面
for i in range(0, 250, 25):
    # 请求参数
    data = {
        # start=25&filter=
        'start': i,
        'filter': ''
    }
    # 获取数据
    resp = requests.get(url, headers=headers, params=data)
    # 转为字符串
    page_content = resp.text
    # 关闭链接，防止被拉黑
    resp.close()
    # 接收正则的结果
    ret = obj.finditer(page_content)
    # 创建写入器
    csvwritter = csv.writer(f)
    # 循环结果
    for i in ret:
        dic = i.groupdict()
        dic['year'] = dic['year'].strip()
        csvwritter.writerow(dic.values())
# 关闭文件流
f.close()

