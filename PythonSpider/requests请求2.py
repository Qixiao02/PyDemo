import requests
URL = 'https://fanyi.baidu.com/sug'
key = input("要翻译的词:")
words ={
    "kw": key
}
fanyi = requests.post(URL, data=words)
print(fanyi.json())