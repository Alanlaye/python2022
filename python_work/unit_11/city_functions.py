def city_country_names(city,country,population=''):
    if population:
        city_country_name = city.title()+","+country.title()+"-population"+str(population)
    else:
        city_country_name = city.title()+","+country.title() 
    return city_country_name