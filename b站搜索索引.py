import requests
import os


def B_spider(keyword):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.39'
    }
    url = f'https://api.bilibili.com/x/web-interface/search/all/v2?keyword={keyword}'
    resp = requests.get(url, headers=headers)
    json_data = resp.json()
    data = json_data['data']['result'][-1]['data'][:10]
    arcurl = []
    pics = []
    titles = []
    pic_files = []
    if not os.path.exists('b站搜索缩略图'):
        os.mkdir('b站搜索缩略图')
    for d in data:
        arcurl.append(d['arcurl'])
        pics.append('https:' + d['pic'])
        titles.append(d['title'])
        content = requests.get('https:' + d['pic']).content
        pic_file = './b站搜索缩略图/' + d['pic'].split('/')[-1]
        pic_files.append(pic_file)
        with open(pic_file, 'wb') as f:
            f.write(content)
    return [(a, p, t) for a, p, t in zip(arcurl, pic_files, titles)]


if __name__ == '__main__':
    print(B_spider('大学生职业规划'))
