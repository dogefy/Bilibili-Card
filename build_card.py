import re
import time
import json
import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55'
}


def get_info(uid):
    info = {}
    url = 'https://api.bilibili.com/x/space/acc/info?mid={}&jsonp=jsonp'.format(uid)
    info_page = requests.get(url, headers=headers)
    info_json = json.loads(info_page.content.decode())['data']
    info['sex'] = info_json['sex']
    info['name'] = info_json['name']
    info['sign'] = info_json['sign']
    info['birthday'] = info_json['birthday']
    info['uid'] = info_json['mid']
    info['face'] = info_json['face']
    if info['birthday'] == '':
        info['birthday'] = 'unknown'
    info['sign'] = re.sub(r'\n', ' ', info['sign'])
    return info


def get_stats(uid):
    stats = {}
    url = 'https://api.bilibili.com/x/relation/stat?vmid={}&jsonp=jsonp'.format(uid)
    stats_page = requests.get(url, headers=headers)
    stats_json = json.loads(stats_page.content.decode())['data']
    stats['fans'] = stats_json['follower']
    stats['followings'] = stats_json['following']
    return stats


if __name__ == '__main__':
    uid = input("Please input uid:")
    uid = int(uid)
    info = get_info(uid)
    stats = get_stats(uid)
    path = 'cards/' + str(uid) + '.svg'
    card = open(path, 'w', encoding='utf-8')
    with open('template/origin_template.svg', 'r', encoding='utf-8') as template:
        temp = template.read()
    marks = re.findall(r'{(.+?)}', temp)
    for i in marks:
        if i == 'fans' or i == 'followings':
            temp = temp.replace('{' + i + '}', str(stats[i]))
        elif i == 'time':
            temp = temp.replace('{' + i + '}', str(time.strftime("%Y.%m.%d", time.localtime())))
        else:
            temp = temp.replace('{' + i + '}', str(info[i]))
    card.write(temp)
