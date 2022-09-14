from bs4 import BeautifulSoup
import requests
import os
import time
#思路
#拿到主页面源代码，提取子页面链接
#通过子页面找到图片下载地址
#下载图片

class Bizhi360Img:
    def __init__(self):
        self.Homeurl = 'http://bizhi360.com/meinv/index.html'
        self.head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27'
        }

    def Get_HomeHTML(self):
        resp = requests.get(url=self.Homeurl, headers=self.head)
        resp.encoding = 'utf-8'
        # print(resp.text)
        return resp.text

    def Get_Subpage_Link(self):
        HomeHTML= BeautifulSoup(self.Get_HomeHTML(), 'html.parser')
        HomeHTML_ALLURL = HomeHTML.find("div", class_="pic-list").findAll("a")
        # print(HomeHTML_ALLURL)
        Subpages_Link = []
        for i in HomeHTML_ALLURL:
            Subpages_href = i.get("href")
            # print(Subpages_href)
            Subpages_Link.append("http://bizhi360.com" + Subpages_href)
        return Subpages_Link


    def Get_SubpageHTML(self):
        SubpageHTML = []
        for x in self.Get_Subpage_Link()[1:]:
            resp = requests.get(url=x, headers=self.head)
            resp.encoding = 'utf-8'
            SubpageHTML.append(BeautifulSoup(resp.text, 'html.parser'))
        # print(SubpageHTML)
        return SubpageHTML

    def Get_DownloadLink(self):
        SubpageHTML = self.Get_SubpageHTML()
        DownLoadLinks = []
        ImgName = []
        for n in SubpageHTML:
            DownLoadLinks.append(n.find("figure").find("img").get('src'))
            ImgName.append(n.find("figure").find("img").get('alt'))
        # print(ImgName)
        # print(DownLoadLinks)
        return DownLoadLinks

    def Get_IMG(self):
        imglink = self.Get_DownloadLink()
        for g in imglink:
            n = 1
            #下载图片
            img_resp = requests.get(g)
            #写入
            img_name = g.split("/")[-1]
            f = open(f'img_name', 'wb')
            f.write(img_resp.content)
            n +=1
            print(f"成功下载{n}张图片")
if __name__ == '__main__':
    # Bizhi360Img().Get_HomeHTML()
    # Bizhi360Img().Get_Subpage_Link()
    # Bizhi360Img().Get_SubpageHTML()
    # Bizhi360Img().Get_DownloadLink()
    Bizhi360Img().Get_IMG()