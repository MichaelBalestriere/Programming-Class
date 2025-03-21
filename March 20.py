import requests

api_key = "e557085670a4fea5b1a3d3b45d671e33"
lat =  40.0290
lon = -75.5717
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=imperial&appid={api_key}"

response = requests.get(url)
data = response.json()

temp = data["main"]["temp"]
question = int(input("Input the temperature at which Ryan will start regretting the long-sleeve t-shirt: "))
print(f"The current temperature is {temp} degrees Fahrenheit")
if temp >= question:
    print("Ryan will be to warm in a long sleeve t-shirt")
else:
    print("Ryan will be fine or to cold in a long sleeve t-shirt")
    
