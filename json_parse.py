import json
import time

with open('test_2.json', 'r', encoding='utf-8') as fr:
    data = json.load(fr)

current_date = str(time.localtime()[0]) + '.' + str(time.localtime()[1]) + '.' + str(time.localtime()[2])
data['date'].insert(0, current_date)
comment = 'huangqimin123'
data['comment'].insert(0, comment)

with open('test_2.json', 'w', encoding='utf-8') as fr:
    json.dump(data, fr, indent=3, ensure_ascii=False)
