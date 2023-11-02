from django.shortcuts import render
import requests

def weather_home(request):
    if request.method == 'POST':
        app_id = ""
        city = request.POST.get("city")
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={app_id}"
        response = requests.get(url).json()
        context = {
            "weather": response,
        }
        return render(request, "weather/index.html", context)
    return render(request, "weather/index.html")
