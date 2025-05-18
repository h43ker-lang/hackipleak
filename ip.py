import requests

def get_ip_info():
    try:
        response = requests.get("http://ip-api.com/json/")
        data = response.json()

        print(f"IP Address : {data.get('query')}")
        print(f"Country    : {data.get('country')}")
        print(f"Region     : {data.get('regionName')}")
        print(f"City       : {data.get('city')}")
        print(f"ZIP        : {data.get('zip')}")
        print(f"Latitude   : {data.get('lat')}")
        print(f"Longitude  : {data.get('lon')}")
        print(f"ISP        : {data.get('isp')}")
        print(f"Org        : {data.get('org')}")
        print(f"ASN        : {data.get('as')}")
    except Exception as e:
        print(f"[!] Error fetching IP information: {e}")

if __name__ == "__main__":
    get_ip_info()
