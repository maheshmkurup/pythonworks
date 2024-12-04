from json import load

f=open("C:\\Users\\mahes\\OneDrive\\Desktop\\pythonworks\\datasets\\countries.json",encoding="utf-8")

data=load(f)

#print country names

#print(len(data))


#print country names

all_country_names=[country.get("name") for country in data]

#print(all_country_names)


#print all regions

all_regions=[country.get("region") for country in data]

#print(set(all_regions))


#print region count

region_count={region:all_regions.count(region) for region in all_regions}

#print(region_count)


#print maximum region

max_region_count=max(region_count,key=lambda k: region_count.get(k))

#print(max_region_count,region_count.get(max_region_count))


#print capital of a country

capital=[country.get("capital") for country in data if country.get("name")=="India"]

#print(capital)


#print countries with most number of borders

country_borders={country.get("name"):len(country.get("borders",[])) for country in data}

#print(country_borders)

max_border_country=max(data,key=lambda country:len(country.get("borders",[]))).get("name")

#print(max_border_country)


#print most populated country

max_country_population=max(data,key=lambda country:country.get("population",0)).get("name")

#print(max_country_population)


#names of countries border sharing with india

alpha_three_codes=[country.get("borders")for country in data if country.get("name")=="India"][0]

for code in alpha_three_codes:

    for country in data:

        if country.get("alpha3Code")==code:

            print(country.get("name"))

                 


 






