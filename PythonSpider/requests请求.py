import requests
url = 'https://www.sogou.com/web?query=%E5%91%A8%E6%9D%B0%E4%BC%A6'

head = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70"
}

req = requests.get(url, headers=head)

print(req)
print(req.text)
