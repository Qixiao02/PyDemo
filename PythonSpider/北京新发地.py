import requests
import json
import csv
url = "http://www.xinfadi.com.cn/priceDetail.html"
class DailyPrice:
    def __init__(self):
        self.url = "http://www.xinfadi.com.cn/getPriceData.html"
        self.head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27'
        }
        self.data = {
            "limit": 362272,
            "current": "",
            "pubDateStartTime": "",
            "pubDateEndTime": "",
            "prodPcatid": "",
            "prodCatid": "",
            "prodName": ""
        }
    def WriteData(self):
        res = requests.post(url=self.url, data=self.data, headers=self.head)
        DailyPrice_Data = json.loads(res.text)
        db = open('北京新发地每日菜价.csv', 'w', encoding='utf-8', newline='')
        Write_Data = csv.writer(db)
        Write_Data.writerow(["一级分类", "品名", "最低价", "平均价格", "最高价", '发布日期'])
        for i in DailyPrice_Data["list"]:
            # Write_Data.writerow(i)
            Write_Data.writerow([i["prodCat"], i["prodName"], i["lowPrice"], i["avgPrice"], i["highPrice"], i["pubDate"]])
        db.close()
        print("爬取完成！")
if __name__ == '__main__':
    DailyPrice().WriteData()