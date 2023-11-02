from django.shortcuts import render
import requests

def weather_home(request):
    if request.method == 'POST':
        city = request.POST.get("city")
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=4e482a857fdf08ae71fa7a53aff40b27"
        response = requests.get(url).json()
        context = {
            "weather": response,
        }
        return render(request, "weather/index.html", context)
    return render(request, "weather/index.html")
