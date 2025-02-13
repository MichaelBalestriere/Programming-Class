import requests
from PIL import Image
from io import BytesIO

api_key = "yhgxz0nUkei4LON6aNoN2FPZdjHm56O4Sr2guB3L"
url = "https://api.nasa.gov/EPIC/api/natural/images"

params = {
    "api_key": api_key
}

response = requests.get(url, params=params)
data = response.json()

if data:
    image_name = data[0]["image"]
    date = data[0]["date"].split(" ")[0].replace("-", "/")
    image_url = f"https://epic.gsfc.nasa.gov/archive/natural/{date}/png/{image_name}.png"
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    img.show()
else:
    print("No photos available")