#!/usr/bin/env python
# coding=utf-8


'''
@Description:
@Version    :0.1
@CreateTime :2020/03/26 Thursday 21:59:18
@Author     :Le
@LastEditor :
@EditTime   :
'''


import requests
import pygal
from pygal.style import LightColorizedStyle as lcs, LightenStyle as ls


# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
proxies = {
    "http": "http://10.10.1.10:3128",
    "https": "http://10.10.1.10:1080",
    # "https": "https://209.141.46.133:8080"
}
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers, proxies=proxies)
print('status code:', r.status_code)

# 将API响应存储在一个变量中
response_dict = r.json()
print('total repositories:', response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print('Repositories returned:', len(repo_dicts))

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    if repo_dict['description']:
        plot_dict = {
            'value': repo_dict['stargazers_count'],
            'label': repo_dict['description'],
            'xlink': repo_dict['html_url']
        }
        plot_dicts.append(plot_dict)
    else:
        plot_dict = {
            'value': repo_dict['stargazers_count'],
            'label': 'None'
        }
        plot_dicts.append(plot_dict)

# 研究第一个仓库
repo_dict = repo_dicts[0]
print('keys:', len(repo_dict))
for key in sorted(repo_dict.keys()):
    # print(key)
    pass

# 可视化
my_style = ls('#333366', base_style=lcs)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 26
my_config.label_font_size = 16
my_config.major_label_font_size = 25
my_config.truncate_label = 10
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most starred python projects on Github'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')


def information(repo_dict):
    print('selected information about the repository:')
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Created:', repo_dict['created_at'])
    print('Updated:', repo_dict['updated_at'])
    print('Description:', repo_dict['description'])


for r in repo_dicts:
    # information(r)
    pass
