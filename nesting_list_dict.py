travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above
def add_new_country(country_visited, visited_times , citites_visited ):
    new_country={}
    new_country["country"] = country_visited
    new_country["visits"] = visited_times
    new_country["cities"] = citites_visited
    travel_log.append(new_country)

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
