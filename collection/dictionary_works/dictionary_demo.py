product={"id":101,"title":"swift","price":600000,"brand":"maruthi Suzuki"}

print(product["title"])

product["price"]=700000

print(product["price"])

product["manufacturing_date"]="12-01-2024"

print(product)

product["offer"]=20000

print(product)

#add offer as 20000 if offer exists else add offer as 30000

if "offer" in product:

    product["offer"]=20000

else:

    product["offer"]=30000