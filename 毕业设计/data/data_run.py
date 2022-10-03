import requests
import json
# import csv
import sqlite3
import time


class daily_price:

    def __init__(self):
        self.url = "http://www.xinfadi.com.cn/getPriceData.html"
        self.head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27 '
        }

    """获取最新页数"""

    def get_page_count(self):
        resp = requests.post(url=self.url, headers=self.head)
        counts = json.loads(resp.text)["count"]
        print(f"现在时间是:" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + f",北京新发地的菜价数据一共有{counts}条")
        return counts

    """获取页面数据"""

    def get_data_csv(self):
        data = {
            "limit": self.get_page_count(),
            "current": "",
            "pubDateStartTime": "",
            "pubDateEndTime": "",
            "prodPcatid": "",
            "prodCatid": "",
            "prodName": ""
        }
        print(f"开始获取所有页面数据....")
        res = requests.post(url=self.url, data=data, headers=self.head)
        dailyPrice_data = json.loads(res.text)
        print(f"获取完成！")

        """写入为CSV文件"""
        # db = open('北京新发地每日菜价.csv', 'w', encoding='utf-8', newline='')
        # write_data = csv.writer(db)
        # print(f"正写入数据.....")
        # write_data.writerow(["一级分类", "品名", "最低价", "平均价格", "最高价", '发布日期'])
        # for i in dailyPrice_data["list"]:
        #     write_data.writerow(
        #         [i["prodCat"], i["prodName"], i["lowPrice"], i["avgPrice"], i["highPrice"], i["pubDate"]])
        # db.close()
        # print(f"数据写入完成！")
        return dailyPrice_data

    """数据筛选"""

    def data_sort(self):
        vegetables = []
        meat = []
        fruit = []
        aquatic_products = []
        print("筛选数据中.....")
        for i in self.get_data_csv()["list"]:
            if i["prodCat"] == "蔬菜":
                vegetables.append(i)
            if i["prodCat"] == "肉禽蛋":
                meat.append(i)
            if i["prodCat"] == "水果":
                fruit.append(i)
            if i["prodCat"] == "水产":
                aquatic_products.append(i)
        print("筛选完成！")
        return vegetables, meat, fruit, aquatic_products

    def write_sqlite(self):
        conn = sqlite3.connect("data.db")
        print("数据库打开成功！")

        """创建数据表"""
        # create = conn.cursor()
        # create.execute(''' CREATE TABLE vegetables
        #             (id INT PRIMARY KEY NOT NULL,
        #             prodName TEXT NOT NULL,
        #             prodCat TEXT NOT NULL,
        #             lowPrice FLOAT NOT NULL,
        #             highPrice FLOAT NOT NULL,
        #             avgPrice FLOAT NOT NULL,
        #             place TEXT NOT NULL,
        #             unitInfo TEXT NOT NULL,
        #             pubDate TEXT NOT NULL);''')
        #
        # create.execute(''' CREATE TABLE meat
        #             (id INT PRIMARY KEY NOT NULL,
        #             prodName TEXT NOT NULL,
        #             prodCat TEXT NOT NULL,
        #             lowPrice FLOAT NOT NULL,
        #             highPrice FLOAT NOT NULL,
        #             avgPrice FLOAT NOT NULL,
        #             place TEXT NOT NULL,
        #             unitInfo TEXT NOT NULL,
        #             pubDate TEXT NOT NULL);''')
        #
        # create.execute(''' CREATE TABLE fruit
        #             (id INT PRIMARY KEY NOT NULL,
        #             prodName TEXT NOT NULL,
        #             prodCat TEXT NOT NULL,
        #             lowPrice FLOAT NOT NULL,
        #             highPrice FLOAT NOT NULL,
        #             avgPrice FLOAT NOT NULL,
        #             place TEXT NOT NULL,
        #             unitInfo TEXT NOT NULL,
        #             pubDate TEXT NOT NULL);''')
        #
        # create.execute(''' CREATE TABLE aquatic_products
        #             (id INT PRIMARY KEY NOT NULL,
        #             prodName TEXT NOT NULL,
        #             prodCat TEXT NOT NULL,
        #             lowPrice FLOAT NOT NULL,
        #             highPrice FLOAT NOT NULL,
        #             avgPrice FLOAT NOT NULL,
        #             place TEXT NOT NULL,
        #             unitInfo TEXT NOT NULL,
        #             pubDate TEXT NOT NULL);''')

        print("开始写入数据到数据库.....")

        """插入数据"""
        vegetables = self.data_sort()[0]
        meat = self.data_sort()[1]
        fruit = self.data_sort()[2]
        aquatic_products = self.data_sort()[3]
        insert = conn.cursor()
        for i in vegetables:
            insert.execute(
                """insert into vegetables values(?,?,?,?,?,?,?,?,?);""", (i["id"], i["prodName"], i["prodCat"],
                                                                          i["lowPrice"], i["highPrice"],
                                                                          i["avgPrice"], i["place"], i["unitInfo"],
                                                                          i["pubDate"]))
        for x in meat:
            insert.execute(
                """insert into meat values(?,?,?,?,?,?,?,?,?);""", (x["id"], x["prodName"], x["prodCat"],
                                                                    x["lowPrice"], x["highPrice"],
                                                                    x["avgPrice"], x["place"], x["unitInfo"],
                                                                    x["pubDate"]))
        for k in fruit:
            insert.execute(
                """insert into fruit values(?,?,?,?,?,?,?,?,?);""", (k["id"], k["prodName"], k["prodCat"],
                                                                     k["lowPrice"], k["highPrice"],
                                                                     k["avgPrice"], k["place"], k["unitInfo"],
                                                                     k["pubDate"]))
        for a in aquatic_products:
            insert.execute(
                """insert into aquatic_products values(?,?,?,?,?,?,?,?,?);""", (a["id"], a["prodName"], a["prodCat"],
                                                                                a["lowPrice"], a["highPrice"],
                                                                                a["avgPrice"], a["place"],
                                                                                a["unitInfo"],
                                                                                a["pubDate"]))
        conn.commit()
        insert.close()
        conn.close()
        print("写入完成")


if __name__ == '__main__':
    # daily_price().get_data_csv()
    # daily_price().data_sort()
    daily_price().write_sqlite()
