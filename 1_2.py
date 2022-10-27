import random
import string
import json
import re

link_json = dict()
url = str(input("Введите ссылку для сокращения: "))


def link_shortener(long_url):
    if long_url.find("http://") != 0 and long_url.find("https://") != 0:
        long_url = "http://" + long_url

    if re.match(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', long_url):
        short_url = "http://" + "".join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
                                        for _ in range(random.randrange(5, 8)))
        return short_url


link_json[url] = link_shortener(url)
json_done = json.dumps(link_json)
with open('done.json', 'w') as file:
    file.write(json_done)

