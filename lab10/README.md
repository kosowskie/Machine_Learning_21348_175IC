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
## Wywołania asynchroniczne przy pomocy asynchio
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
