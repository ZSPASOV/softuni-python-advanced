countries = [country for country in input().split(', ')]
capital = [capital for capital in input().split(', ')]
# You can use the zip() method to zip the two lists into tuple pairs
zipped = zip(countries, capital)

countries_and_capitals = {country: capital for (country, capital) in zipped}
for key, value in countries_and_capitals.items():
    print(f'{key} -> {value}')
