cities = ['mumbai', 'delhi', 'new york']
country = ['india', 'india', 'us']

for k, v in zip(cities, country):
    print(k, v)
d = {city: country for (city, country) in zip(cities, country)}
print(d)
