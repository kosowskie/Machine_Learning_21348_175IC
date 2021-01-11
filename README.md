```python
import json
import requests

import csv
import pandas
```
```python
data = {
    "postId": 1,
    "id": 5,
    "name": "vero eaque aliquid doloribus et culpa",
    "email": "Hayden@althea.biz",
    "body": "harum non quasi et ratione\ntempore iure ex voluptates in ratione\nharum architecto fugit inventore cupiditate\nvoluptates magni quo et"
  }
```
```python
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)
```
```python
json_string = json.dumps(data)

json.dumps(data, indent=4)
```
```python

richest_people = (2, "Jeff Bezos")
encoded_people = json.dumps(richest_people)
decoded_people = json.loads(encoded_people)

print(richest_people == decoded_people)
print(type(richest_people))
print(type(decoded_people))
print(richest_people == tuple(decoded_people))
```
```python
with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
    
data
```
```python
with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
    
data
```
```python
json_string = """
{
  "albumId": 4,
  "id": 161,
  "title": "aliquid aut at sed repudiandae est autem",
  "url": "https://via.placeholder.com/600/739fba",
  "thumbnailUrl": "https://via.placeholder.com/150/739fba"
}
"""

data = json.loads(json_string)
```
```python
response = requests.get("https://jsonplaceholder.typicode.com/photos")
photos = json.loads(response.text)
```
```python
print(photos == response.json())
print(type(photos))
print(photos[:10])
```
```python
photos_by_album={}

#The longest title in album
for photo in photos:
    try:
        if len(photo["title"])> photos_by_album[photo["albumId"]]:
            photos_by_album[photo["albumId"]]=len(photo["title"])
    except KeyError:
            photos_by_album[photo["albumId"]]=len(photo["title"])
            
longest_title = sorted(photos_by_album.items(),
                      key=lambda x:x[1], reverse=True)
print(photos_by_album)
print(longest_title)

album_longest_titile=[]
for title in longest_title:
    if longest_title[0][1]>title[1]:
        break
    album_longest_titile.append(str(title[0]))

title_string = " and ".join(album_longest_titile)
s = "s" if len(album_longest_titile)>1 else ""
print(f'In album{s} {title_string} we have longest title with {longest_title[0][1]} signs')
```
```python
albums = longest_title[:10]

def keep(photo):
    max_counter = False
    for album in albums:
        if album[1] == len(photo["title"]) and photo["albumId"] == album[0]:
            max_counter = True
    return max_counter
```
```python
with open("filtered_data_file.json","w") as data_file:
    filtered_photos = list(filter(keep,photos))
    json.dump(filtered_photos,data_file,indent=2)
```
```python
class Elf:
    def __init__(self, level, ability_scores=None):
        self.level = level
        self.ability_scores = {
            "str": 11, "dex": 12, "con": 10,
            "int": 16, "wis": 14, "cha": 13
        } if ability_scores is None else ability_scores
        self.hp = 10 + self.ability_scores["con"]
```
```python
def decode_complex(dct):
    if "__complex__" in dct:
        return complex(dct["real"], dct["imag"])
    return dct

with open("complex_json.json") as complex_data:
    data=complex_data.read()
    numbers=json.loads(data, object_hook=decode_complex)

print(type(numbers))
numbers
```
```python
with open('bigos_recipe.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t {row[0]} {row[1]}')
            line_count += 1
    print(f'Processed {line_count} lines.')
```
```python
with open('bigos_recipe.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t Ilość: {row["amount"]} Składnik: {row["ingredients"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')
```
```python
with open('bigos_recipe.csv', mode='w') as bigos_recipe:
    employee_writer = csv.writer(bigos_recipe, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['2 łyżki','powideł śliwkowych lub kilka suszonych śliwek'])
    employee_writer.writerow(['1','jabłko (np. reneta lub antonówka) - opcjonalnie'])
 ```
```python
with open('bigos_recipe_2.csv', mode='w') as csv_file:
    fieldnames = ['amount', 'ingredients', 'optional']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'amount': '500 g', 'ingredients': 'miesa wieprzowego', 'optional': 'false'})
    writer.writerow({'amount': '1', 'ingredients': 'jablko (np. reneta lub antonowka)', 'optional': 'true'})
 ```
```python
df = pandas.read_csv('bigos_recipe_3.csv')
print(df)
 ```
```python
df = pandas.read_csv('bigos_recipe_3.csv', index_col='optional')
print(df)
 ```
```python
df = pandas.read_csv('bigos_recipe_3.csv', 
            index_col='amount', 
            header=0,
            names=['amount', 'ingredients','optional'])
print(df)
 ```
```python
df = pandas.read_csv('bigos_recipe_3.csv', 
            index_col='amount', 
            header=0,
            names=['amount', 'ingredients','optional'])
df.to_csv('bigos_recipe_3_modified.csv')
```
