cars=[
    {"id":1,"name":"fronx","price":1200000,"brand":"nexa","colors":["red","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":2,"name":"baleno","price":1100000,"brand":"nexa","colors":["grey","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":3,"name":"3xo","price":900000,"brand":"mahindra","colors":["red","white","black"],"transmissions":["amt","cvt"]},
    {"id":4,"name":"punch","price":700000,"brand":"tata","colors":["red","blue","white","green"],"transmissions":["manuel","cvt"]},
    {"id":5,"name":"nexon","price":1400000,"brand":"tata","colors":["red","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":6,"name":"kiger","price":1000000,"brand":"renault","colors":["blue","white"],"transmissions":["manuel","cvt","dct"]},
    {"id":7,"name":"taigun","price":2300000,"brand":"volkswagon","colors":["red","blue","white"],"transmissions":["manuel","cvt","torque"]},
]

#print total count of vehicles

print(f"total vehicle=>{len(cars)}")


#print available colors of baleno

baleno_colors=[c.get("colors") for c in cars if c.get("name")=="baleno"]

print(baleno_colors[0]) #==. to get output in a single list otherwise output will be inside two list


#print all brands

all_brands={c.get("brand") for c in cars}

print(all_brands)


#print car names available in amt transmission

amt_transmission_cars=[c.get("name") for c in cars if "amt" in c.get("transmissions")]

print(amt_transmission_cars)


#print cars avilable in blue color

blue_color_cars=[c.get("name") for c in cars if "blue" in c.get("colors")]

print(blue_color_cars)


#print all transmission types

all_transmissions={t for c in cars for t in c.get("transmissions")}

print(all_transmissions)


#print all colors

all_colors={co for c in cars for co in c.get("colors")}

print(all_colors)


#most popular color

colors_grp=[co for c in cars for co in c.get("colors")]

popular_color={po:colors_grp.count(po) for po in colors_grp}

print(max(popular_color))


#print costly car

costly_car=max(cars,key=lambda d:d.get("price"))

print(costly_car.get("name"))


#cheapest car

cheapest_car=min(cars,key=lambda d:d.get("price"))

print(cheapest_car.get("name"))


#sort cars with price

sorted_price=sorted(cars,key=lambda d:d.get("price"))  #==> if we want oly price

sorted_list={c.get("name"):c.get("price") for c in sorted_price}  #==> if we want both name and price

print(sorted_list)

sorted_car_name=[c.get("name") for c in sorted_price]  #==> if we want only name

print(sorted_car_name)

sorted_car={c.get("name"):[c.get("price"),c.get("brand")] for c in sorted_price} #==> if we want two values for a single key

print(sorted_car)






 



















