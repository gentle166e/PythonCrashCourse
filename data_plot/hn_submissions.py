#!/usr/bin/env python
# coding=utf-8


'''
@Description:
@Version    :0.1
@CreateTime :2020/03/28 Saturday 15:55:33
@Author     :Le
@LastEditor :
@EditTime   :
'''


import requests

from operator import itemgetter

# 执行API调用并存储响应
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
proxies = {
    "http": "http://10.10.1.10:3128",
    "https": "http://10.10.1.10:1080",
}
r = requests.get(url, proxies=proxies)
print('status code:', r.status_code)

# 处理有关每篇文章的信息
submission_ids = r.json()
submission_dicts = []
for sub_id in submission_ids[:10]:
    # 对于每篇文章都执行一个API调用
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
           str(sub_id) + '.json')
    submission_r = requests.get(url, proxies=proxies)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(sub_id),
        'comments': response_dict.get('descendants', 0)
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts,
                          key=itemgetter('comments'), reverse=True)

for s_dict in submission_dicts:
    print(f"title: {s_dict['title']}")
    print(f"discussion link: {s_dict['link']}")
    print(f"comments: {s_dict['comments']}")
