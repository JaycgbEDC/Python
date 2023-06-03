import requests
import pywasm
import time


BASE_URL = "https://spa14.scrape.center"
TOTAL_PAGE = 10


runtime = pywasm.load("./Wasm.wasm")
for i in range(TOTAL_PAGE):
    offset = i * 10
    sign = runtime.exec("encrypt", [offset, int(time.time())])
    url = f"{BASE_URL}/api/movie?limit=10&offset={offset}&sign={sign}"
    response = requests.get(url, verify = False)
    print(response.json())