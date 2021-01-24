# Współbieżność w Pythonie part 1

## Importy
```python
import requests
import time
import concurrent.futures
import threading
import asyncio
import aiohttp
import nest_asyncio
nest_asyncio.apply()
import multiprocessing
```
## Standardowe wywołanie, w którym procesor potrzebuje pewnej przerwy zegarowej pomiędzy wywołaniami
![image](https://files.realpython.com/media/IOBound.4810a888b457.png)
```python
sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
```
## Wywołania wykorzystujące wątki
![image](https://files.realpython.com/media/Threading.3eef48da829e.png)
```python
thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
```
```python
thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session
```
## Wywołania asynchroniczne przy pomocy asyncio
![image](https://files.realpython.com/media/Asyncio.31182d3731cf.png)
```python


async def download_site(session, url):
    async with session.get(url) as response:
        print("Read {0} from {1}".format(response.content_length, url))


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")

```
## Wykorzystywanie multiprocessingu
![image](https://files.realpython.com/media/MProc.7cf3be371bbc.png)
```python
import Lab10_multiprocessing as multiprocessing_file

sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
start_time = time.time()
multiprocessing_file.download_all_sites(sites)
duration = time.time() - start_time
print(f"Downloaded {len(sites)} in {duration} seconds")
```
```python
import requests

session = None

def download_site(url, session):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)
```

# Współbieżność w Pythonie part 2

## Importy
```python
import os
from urllib import request
from imgurpython import ImgurClient
import timeit
import time
import requests
import json
import Lab10_multiprocessing_part2 as multiprocessing_file
from concurrent.futures import ThreadPoolExecutor
import multiprocessing
import nest_asyncio
nest_asyncio.apply()
import asyncio
import aiohttp
```
## Pobieranie obrazu ze strony standardową metodą
```python
def download_images():
    response = requests.get("https://picsum.photos/v2/list")
    if response.status_code != 200:
        raise AttributeError('GET /tasks/ {}'.format(response.status_code))
    data = json.loads(response.text)

    pictures=[]
    for s in data:
        pictures.append(s['download_url']+".jpg")
    return pictures

def saveImages(link):
    filename = link.split('/')[6].split('.')[0]
    fileformat = link.split('/')[6].split('.')[1]
    request.urlretrieve(link, "downloads/{}.{}".format(filename, fileformat))

def main():
    images = download_images()
    for image in images:
        saveImages(image)

start_time = time.time()
main()
duration_synch = time.time() - start_time
print(f"Time taken to download 30 images into the downloads folder synchronously: {duration_synch}")
```
## Pobieranie obrazów przy pomocy wątków
```python
def process_images_threading():
    images = download_images()
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(saveImages,images)

start_time = time.time()
process_images_threading()
duration_threading = time.time() - start_time
print(f"Time taken to download 30 images into the downloads folder with multithreading: {duration_threading}")
```
## Pobieranie obrazów przy pomocy multiprocessingu
```python
def process_images_multiprocessing():
    images = download_images()
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    pool.map(multiprocessing_file.multiprocessing_images,images)


start_time = time.time()
process_images_multiprocessing()
duration_multiprocessing = time.time() - start_time
print(f"Time taken to download 30 images into the downloads folder with multiprocessing: {duration_multiprocessing}")
```
```python
from urllib import request


def multiprocessing_images(link):
    filename = link.split('/')[6].split('.')[0]
    fileformat = link.split('/')[6].split('.')[1]
    request.urlretrieve(link, "downloads/{}.{}".format(filename, fileformat))
```
## Pobieranie obrazów przy pomocy Asyncio
```python


async def download_images_asyncio(link, session):
    filename = link.split('/')[6].split('.')[0]
    fileformat = link.split('/')[6].split('.')[1]
    async with session.get(link) as response:
        with open("downloads/{}.{}".format(filename, fileformat), 'wb') as fd:
            async for data in response.content.iter_chunked(1024):
                fd.write(data)

async def main_asyncio():
    images = download_images()

    async with aiohttp.ClientSession() as session:
        tasks=[download_images_asyncio(image,session)for image in images]
        return await asyncio.gather(*tasks)

start_time = time.time()
asyncio.run(main_asyncio())
duration_asyncio = time.time() - start_time
print(f"Time taken to download 30 images into the downloads folder with asyncio: {duration_asyncio}")

```
## Różnice pomiędzy poszczególnymi wywołaniami
#### Standardowa metoda: Time taken to download 30 images into the downloads folder synchronously: 32.752798557281494
#### Metoda z wykorzystaniem wątków: Time taken to download 30 images into the downloads folder with multithreading: 7.226224422454834
#### Metoda z wykorzystaniem multiprocessingu: Time taken to download 30 images into the downloads folder with multiprocessing: 9.249184131622314
#### Metoda z wykorzystaniem Asyncio: Time taken to download 30 images into the downloads folder with asyncio: 3.49655818939209
