# w - write
# a - append
# r - read

import json

PATH = 'test.json'


with open(PATH, 'r', encoding='UTF-8') as json_file:
    data = json.load(json_file)

print(data)
print(type(data))
new_contact = input('Введите данные: ')
new_id = max(list(map(int, data))) + 1
data[new_id] = new_contact

with open(PATH, 'w', encoding='UTF-8') as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)
