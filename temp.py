from weather import Weather, Unit


def weather_in_city(city):

    weather = Weather(unit=Unit.CELSIUS)

    city_weather_info = weather.lookup_by_location(city)
    forecasts = city_weather_info.forecast
    for forecast in forecasts:
        condition = forecast.text
        hightemp = forecast.high
        lowtemp = forecast.low
        break
    print('The weather in ', city, 'is', condition, 'with temperatures trailing from ', lowtemp, ' to ', hightemp)
    return
