# Importy
```python
from openpyxl import Workbook
from bs4 import BeautifulSoup
import requests
import string
import random
import re
```
# Tworzenie plików Excel'a
```python
wb = Workbook()
wsGielda = wb.active
wsGielda.title = "Giełda"
wsLinki = wb.create_sheet("Linki")
wsFilmweb = wb.create_sheet("Filmweb")
```
# Giełda
## Utworzenie klasy Company
```python
class Company:
    def __init__(self, name, course, percentage, transactions):
        self.name = name
        self.course = course
        self.percentage = percentage
        self.transactions = transactions
    def __str__(self):
        return "Name: "+self.name\
               +"\nCourse: "+ str(self.course)+\
               "\nPercentage: "+str(self.percentage)+\
               "\nNo of Transactions: "+str(self.transactions)+"\n"
```
## Metoda zwracająca text
```python
def get_text():
    str_code = string.ascii_lowercase
    result_str = 'q/?s='
    new_code = ''.join(random.choice(str_code) for j in range(3))
    return result_str + new_code
```
## Metoda zwracająca daną osobę na postawie nazwy
```python
def get_person(text, soup):
    ref = soup.find(text=text).parent.find("span")
    if ref.text == "":
        return 0
    if text == "Transakcje":
        return int(ref.text.replace(" ", ""))

    return float(ref.text.replace(" ", ""))
```
## Metoda znajdująca kurs ze strony przy pomocu zawieranego teekstu dzięki bs4
```python
def find_course(code):
    link = "https://stooq.pl/" + code
    result = requests.get(link)
    result_txt = result.text
    soup = BeautifulSoup(result_txt, "html.parser")
    try:
        course = get_person("Kurs", soup)
        percentage = get_person("Zmiana", soup)
        transactions = get_person("Transakcje", soup)
        name = code.split('=')[1]
        return Company(name, course, percentage, transactions)

    except AttributeError:
        try:
            link = soup.find(id="f16").parent.find('a', href=True)
            if link.text == 'symbol waloru':
                link = get_text()
            else:
                link = link.get('href')

            return find_course(link)

        except AttributeError:
            return find_course(get_text())
```
## Metoda zapisująca dane do poszczególnych wierszy
``` python
def fill_wsGielda(companies):
    i = 1
    for col in wsGielda.iter_cols(min_row=1, max_col=4, max_row=5):
        for cell in col:
            if cell.col_idx == 1:
                cell.value = companies[i].name
            elif cell.col_idx == 2:
                cell.value = companies[i].course
            elif cell.col_idx == 3:
                cell.value = companies[i].percentage
            elif cell.col_idx == 4:
                cell.value = companies[i].transactions
            i += 1
            if i == 5:
                i = 1
```
## Metoda wypisująca dane z wiersza z giełdy
```python
def print_from_gielda():
    for col in wsGielda.iter_cols(min_row=1, max_col=4, max_row=5):
        for cell in col:
            print("Cell: ",cell," Value: ",cell.value)
```
## Metoda wywołująca funkcje
```python
def gielda():
    companies = []
    for i in range(5):
        companies.append(find_course(get_text()))
    print("Created data about companies:")
    for company in companies:
        print(company)
    fill_wsGielda(companies)
    print("Data in the Gielda sheet:")
    print_from_gielda()
gielda()
```
# Kod łączący się ze stroną, znajduje wszystkie linki na stronie, a następnie zapisuje je do arkusza ‘Linki’,
```python
url = "https://www.youtube.com/"
result = requests.get(url)
result_txt = result.text
soup = BeautifulSoup(result_txt, "html.parser")
ref_list = soup.find_all('a', href=True)
link_list = []
for element in ref_list:
   link = element.get("href")
   if url not in link:
       link = "https://www.youtube.com" + link
   link_list.append(link)
i = 0
for row in wsLinki.iter_rows(min_row=1, max_row=len(link_list)):
   for cell in row:
       cell.value = link_list[i]
       i += 1
print("Data in the Links sheet: ")
for row in wsLinki.iter_rows(min_row=1, max_row=len(link_list)):
   for cell in row:
       print("Cell: ",cell," Value: ",cell.value)
```
# Zwracanie z danego filmu na Filmwebie reżysera, datę premiery, boxoffice, ocenę filmu.
```python
url = "https://www.filmweb.pl/film/Srpski+film-2010-497153"
result = requests.get(url)
result_txt = result.text
soup = BeautifulSoup(result_txt, "html.parser")
wsFilmweb['A1'] = soup.find(itemprop="director").text.strip()
wsFilmweb['A2'] = soup.find("span", {"class": "block"}).text.strip()
wsFilmweb['A3'] = soup.find("div", {"class": "filmRating filmRating--hasPanel"}).attrs.get("data-count")
wsFilmweb['A4'] = soup.find("div", {"class": "filmRating filmRating--hasPanel"}).attrs.get("data-rate")
print("Data in the Filmweb sheet")
for row in wsFilmweb.iter_rows(min_row=1, max_row=4):
   for cell in row:
       print("Cell: ",cell," Value: ",cell.value)
```
# Zapisuywanie wyników
```python
wb.save('Kosowski-175ICB1.xlsx')
```
