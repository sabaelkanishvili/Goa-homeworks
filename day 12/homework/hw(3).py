# პირველი ცვლადი: შედარება და ლოგიკური ოპერატორი (temperature > 30 and not cloudy)
temperature = 35
cloudy = False
result1 = temperature > 30 and not cloudy
print(result1)  #true

# მეორე ცვლადი: შედარების ოპერატორი (age < 18 or age > 60)
age = 25
result2 = age < 18 or age > 60
print(result2)  # False

# მესამე ცვლადი: ლოგიკური ოპერატორი (is_sunny and not is_raining)
is_sunny = True
is_raining = False
result3 = is_sunny and not is_raining
print(result3)  # True, 

# forth ცვლადი: შედარების და ლოგიკური ოპერატორი (speed <= 120 or (speed > 50 and is_windy))
speed = 110
is_windy = True
result4 = speed <= 120 or (speed > 50 and is_windy)
print(result4)  # True 

# მეხუთე ცვლადი: შედარების და ლოგიკური ოპერატორი (temperature == 20 and (humidity > 60 or wind_speed < 10))
temperature = 20
humidity = 70
wind_speed = 5
result5 = temperature == 20 and (humidity > 60 or wind_speed < 10)
print(result5)  # True 