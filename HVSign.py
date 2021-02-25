# -*- coding: utf8 -*-

import requests, json, time, os, re

s = requests.Session()
cookie = os.environ.get("cookie")

def main(*arg):
    try:
        url = "https://e-hentai.org/news.php"
        headers = {
            'Host': 'e-hentai.org',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Referer': 'https://e-hentai.org/',
            "Cookie": cookie,
            'Upgrade-Insecure-Requests': '1',
            'TE': 'Trailers',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache'
        }
        response = s.get(url, data="", headers=headers)
        text = re.sub('<strong>|</strong>', '', response.text)
        text = re.compile(r'You gain .*Credits!').search(text)
        if text:
            text = text[0]
        else:
            text = 'The Cookie may be entered incorrectly or signed in today'
        return text
    except Exception as e:
        return 'repr(e):'+str(repr(e))

def go(*arg):
    msg = ""
    global cookie
    clist = cookie.split("\n")
    i = 0
    while i < len(clist):
        msg += f"User {i+1} start running\n"
        cookie = clist[i]
        if "event" in cookie:
            cookie = re.sub(r'event=\d+', 'event=1', cookie)
        else:
            cookie += "; event=1"
        msg += main(cookie)
        msg += '\n'
        i += 1
    print(msg)
    return msg

if __name__ == "__main__":
    if cookie:
        go()
    else:
        print('Please add Cookie to Secrets')
