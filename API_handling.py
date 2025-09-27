import requests

def fetch_api_user():
    url = "https://api.freeapi.app/api/v1/public/randomproducts?page=1&limit=10&inc=category%2Cprice%2Cthumbnail%2Cimages%2Ctitle%2Cid&query=mens-watches"
    response = requests.get(url)
    data = response.json()
    d = {}
    for i,item in enumerate(data["data"]["data"],start=1):
        d.update({f"Product {i}":item["title"]})


    for key,value in d.items():
        print(f"{key} : {value}")


fetch_api_user()
