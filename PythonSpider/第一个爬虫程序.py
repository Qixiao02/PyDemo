from urllib.request import urlopen
url = 'http://www.baidu.com'
s = urlopen(url)
# print(s.read().decode('utf-8'))
with open('baidu.html', 'w', encoding='utf-8') as f:
    f.write(s.read().decode('utf-8'))
    f.close()
    print("写入完成！")

# print(type(s))