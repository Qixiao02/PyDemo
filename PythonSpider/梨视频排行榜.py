import requests
from lxml import etree
import re
class popular:
    def __init__(self):
        self.url = "https://www.pearvideo.com/popular"
        self.head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27'
        }
    def latest_Popular_Allurl(self):
        resq = requests.get(url=self.url, headers=self.head).text
        # print(resq)
        tree = etree.HTML(resq)
        # print(resq)
        lis = tree.xpath("/html/body/div[2]/div/ul/li")
        names = tree.xpath("//*[@id='popularList']/li/div/a/h2/text()")
        # print(names)
        # print(lis)
        list_URL = []
        for li in lis:
            result = li.xpath("./a/@href")[0]
            # print(result)
            url = f'https://www.pearvideo.com/' + result
            # print(url)
            list_URL.append(url)
        # print(list_URL)
        return (list_URL,names)
    def Video_URL(self):
        video_urls =[]
        for i in self.latest_Popular_Allurl()[0]:
            resq = requests.get(url=i, headers=self.head).text
            tree = etree.HTML(resq)
            result = tree.xpath("/html/body/div[2]/div[1]/div[1]/div[1]/div[2]/@data-cid")
            results = result[0]
            # print(results)
            video_url = f"https://www.pearvideo.com/videoStatus.jsp?contId=" + results
            # print(video_url)
            head = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27',
                #防盗链 溯源
                'Referer': f'https://www.pearvideo.com/video_' + results
            }
            # print(head.items())
            resp = requests.get(url=video_url, headers=head)
            dic = resp.json()
            srcurl = dic['videoInfo']['videos']["srcUrl"]
            systemTime = dic["systemTime"]
            # print(systemTime)
            video_urls.append(srcurl.replace(systemTime, f"cont-{results}"))
        return video_urls
    def DownloadVideo(self):
        VideoName = self.latest_Popular_Allurl()[1]
        # for i in VideoName:
        #     print(i)
        video_urls = self.Video_URL()
        # for i in video_urls:
        #     print(i)

        n = 0
        for x in video_urls:
            n = n+1
            resp = requests.get(x)
            f = open(f"{n}.mp4", "wb")
            f.write(resp.content)
            f.close()
            print(f"{n}下载完成！")
if __name__ == '__main__':
    # popular().Video_URL()
    popular().DownloadVideo()